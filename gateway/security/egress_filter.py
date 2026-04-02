# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Egress Filtering — block unauthorized outbound traffic.

Domain/IP allowlist with default-deny policy. Configurable per-agent
with logging of all egress attempts. Supports enforce and monitor modes.
"""


import asyncio
import ipaddress
import logging
import time
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from urllib.parse import urlparse

from .egress_config import EgressFilterConfig, get_egress_config

logger = logging.getLogger(__name__)


class EgressAction(str, Enum):
    ALLOW = "allow"
    DENY = "deny"


@dataclass
class EgressAttempt:
    timestamp: float
    agent_id: str
    destination: str
    port: Optional[int]
    action: EgressAction
    rule: str
    details: str = ""


@dataclass
class EgressPolicy:
    """Egress policy for an agent or global default."""

    allowed_domains: list[str] = field(default_factory=list)
    allowed_ips: list[str] = field(default_factory=list)  # CIDR or single IP
    allowed_ports: list[int] = field(default_factory=lambda: [80, 443, 465, 587, 993])
    deny_all: bool = True  # Default deny

    def matches_domain(self, domain: str) -> bool:
        """Check if domain matches any allowed domain (supports wildcards).

        Wildcards only match one subdomain level to prevent overly broad rules.
        e.g., *.github.com matches foo.github.com but NOT foo.bar.github.com.
        """
        domain = domain.lower().rstrip(".")
        for allowed in self.allowed_domains:
            allowed = allowed.lower().rstrip(".")
            if allowed.startswith("*."):
                base = allowed[2:]  # "github.com"
                if domain == base:
                    return True
                # Only match one level deep: "sub.github.com" yes, "a.b.github.com" no
                if domain.endswith("." + base):
                    prefix = domain[: -(len(base) + 1)]
                    if "." not in prefix:  # Only one subdomain level
                        return True
            elif domain == allowed:
                return True
        return False

    def matches_ip(self, ip: str) -> bool:
        """Check if IP matches any allowed IP/CIDR."""
        try:
            addr = ipaddress.ip_address(ip)
        except ValueError:
            return False
        for allowed in self.allowed_ips:
            try:
                network = ipaddress.ip_network(allowed, strict=False)
                if addr in network:
                    return True
            except ValueError:
                if ip == allowed:
                    return True
        return False

    def matches_port(self, port: Optional[int]) -> bool:
        """Check if port is allowed."""
        if not self.allowed_ports:  # Empty = all ports allowed
            return True
        if port is None:
            return True  # No port specified, allow
        return port in self.allowed_ports


class EgressFilter:
    """Filter outbound connections based on allowlists with enforce/monitor modes."""

    def __init__(
        self,
        config: Optional[EgressFilterConfig] = None,
        default_policy: Optional[EgressPolicy] = None,
        audit_store=None,
    ):
        self.config = config or get_egress_config()
        self.default_policy = default_policy or EgressPolicy()
        self._agent_policies: dict[str, EgressPolicy] = {}
        self._log: list[EgressAttempt] = []
        self._max_log_size = 10000
        self._audit_store = audit_store  # Optional AuditStore for persistence
        self._notifier = None  # Optional EgressTelegramNotifier
        self._approval_queue = None  # Optional EgressApprovalQueue
        self._event_bus = None
        self._pending_notifications: list[dict] = []
        # Time-limited interactive approvals: domain → expiry unix timestamp.
        # Populated by grant_timed_approval() when owner selects 1h/4h/24h.
        self._timed_approvals: dict[str, float] = {}

    def set_notifier(self, notifier) -> None:
        """Set the Telegram notifier for egress approval requests."""
        self._notifier = notifier

    def set_approval_queue(self, approval_queue) -> None:
        """Set interactive egress approval queue."""
        self._approval_queue = approval_queue

    def set_event_bus(self, event_bus) -> None:
        """Set optional event bus for real-time egress telemetry."""
        self._event_bus = event_bus

    def grant_timed_approval(self, domain: str, expires_at_iso: str) -> None:
        """Record a time-limited interactive approval for a domain.

        Called by the Telegram callback handler when the owner selects 1h/4h/24h.
        Cleans up stale entries to prevent unbounded growth.
        """
        from datetime import datetime, timezone

        try:
            expiry = datetime.fromisoformat(expires_at_iso.replace("Z", "+00:00")).timestamp()
        except (ValueError, AttributeError):
            return
        self._timed_approvals[domain.lower().strip()] = expiry
        # Purge expired entries
        now = time.time()
        self._timed_approvals = {d: e for d, e in self._timed_approvals.items() if e > now}
        logger.info("Timed egress approval granted: %s expires %s", domain, expires_at_iso)

    def set_agent_policy(self, agent_id: str, policy: EgressPolicy) -> None:
        """Set a per-agent egress policy."""
        self._agent_policies[agent_id] = policy

    def get_policy(self, agent_id: str) -> EgressPolicy:
        """Get effective policy for an agent."""
        return self._agent_policies.get(agent_id, self.default_policy)

    def check(self, agent_id: str, destination: str, port: Optional[int] = None) -> EgressAttempt:
        """
        Check if an outbound connection is allowed.

        Args:
            agent_id: The agent making the request.
            destination: Domain name, IP, or URL.
            port: Optional port number.

        Returns:
            EgressAttempt with allow/deny decision.
        """
        policy = self.get_policy(agent_id)

        # Parse URL if provided
        parsed_dest = destination
        if "://" in destination:
            parsed = urlparse(destination)
            parsed_dest = parsed.hostname or destination
            if port is None and parsed.port:
                port = parsed.port
            elif port is None:
                port = 443 if parsed.scheme == "https" else 80
        elif ":" in destination and not self._is_ipv6(destination):
            # Handle host:port format (not IPv6)
            try:
                host_part, port_part = destination.rsplit(":", 1)
                parsed_dest = host_part
                if port is None:
                    port = int(port_part)
            except (ValueError, IndexError):
                # If parsing fails, treat as hostname
                parsed_dest = destination

        # Block private/loopback IPs unless explicitly in allowlist
        if self._is_private_ip(parsed_dest) and not policy.matches_ip(parsed_dest):
            return self._record(
                agent_id,
                destination,
                port,
                EgressAction.DENY,
                f"private/loopback IP '{parsed_dest}' blocked (SSRF protection)",
            )

        # Check port first
        if not policy.matches_port(port):
            action = EgressAction.DENY if self.config.mode == "enforce" else EgressAction.ALLOW
            return self._record(
                agent_id,
                destination,
                port,
                action,
                f"port {port} not allowed ({'blocked' if action == EgressAction.DENY else 'monitored'})",
            )

        # Check denylist first (overrides allowlist in strict mode)
        if self.config.is_denylisted(parsed_dest):
            action = EgressAction.DENY if self.config.mode == "enforce" else EgressAction.ALLOW
            return self._record(
                agent_id,
                destination,
                port,
                action,
                f"domain '{parsed_dest}' in denylist ({'blocked' if action == EgressAction.DENY else 'monitored'})",
            )

        # Check time-limited interactive approvals (owner-granted 1h/4h/24h)
        _now = time.time()
        _timed_expiry = self._timed_approvals.get(parsed_dest.lower() if parsed_dest else "")
        if _timed_expiry is not None:
            if _timed_expiry > _now:
                return self._record(
                    agent_id,
                    destination,
                    port,
                    EgressAction.ALLOW,
                    f"domain '{parsed_dest}' has active timed approval",
                )
            else:
                self._timed_approvals.pop(parsed_dest.lower(), None)

        # Check config-based allowlist
        effective_allowlist = self.config.get_effective_allowlist(agent_id)
        if self._matches_allowlist_domain(parsed_dest, effective_allowlist):
            return self._record(
                agent_id,
                destination,
                port,
                EgressAction.ALLOW,
                f"domain '{parsed_dest}' in config allowlist",
            )

        # Check policy-based domain allowlist (legacy)
        if policy.matches_domain(parsed_dest):
            return self._record(
                agent_id,
                destination,
                port,
                EgressAction.ALLOW,
                f"domain '{parsed_dest}' in policy allowlist",
            )

        # Check config-based IP allowlist
        if parsed_dest and self._matches_ip_list(parsed_dest, self.config.allowed_ips):
            return self._record(
                agent_id,
                destination,
                port,
                EgressAction.ALLOW,
                f"IP '{parsed_dest}' in config allowlist",
            )

        # Check policy-based IP allowlist (legacy)
        if policy.matches_ip(parsed_dest):
            return self._record(
                agent_id,
                destination,
                port,
                EgressAction.ALLOW,
                f"IP '{parsed_dest}' in policy allowlist",
            )

        # Default behavior based on mode
        if self.config.mode == "enforce":
            # In enforce mode, unknown domains are blocked
            return self._record(
                agent_id,
                destination,
                port,
                EgressAction.DENY,
                f"enforce mode: '{parsed_dest}' not in allowlist - BLOCKED",
            )
        else:
            # In monitor mode, unknown domains are allowed but logged
            return self._record(
                agent_id,
                destination,
                port,
                EgressAction.ALLOW,
                f"monitor mode: '{parsed_dest}' not in allowlist - logged only",
            )

    async def check_async(
        self, agent_id: str, destination: str, port: Optional[int] = None, tool_name: str = "egress"
    ) -> EgressAttempt:
        """Async egress check with interactive approval for unknown domains."""
        attempt = self.check(agent_id, destination, port)
        needs_interactive_approval = (
            self._approval_queue is not None
            and self.config.mode == "enforce"
            and (
                attempt.action == EgressAction.DENY
                or (
                    getattr(self.config, "approval_required_for_all", False)
                    and attempt.action == EgressAction.ALLOW
                )
            )
        )
        if needs_interactive_approval:
            parsed = urlparse(destination) if "://" in destination else None
            domain = (parsed.hostname if parsed else destination).split(":")[0]
            resolved_port = port
            if parsed and resolved_port is None:
                resolved_port = parsed.port or (443 if parsed.scheme == "https" else 80)
            if resolved_port is None:
                resolved_port = 443

            wait_task = asyncio.create_task(
                self._approval_queue.request_approval(
                    domain=domain,
                    port=resolved_port,
                    agent_id=agent_id,
                    tool_name=tool_name,
                )
            )
            await asyncio.sleep(0)
            if self._notifier:
                try:
                    pending = await self._approval_queue.get_pending_requests()
                    match = next(
                        (
                            p
                            for p in pending
                            if p["domain"] == domain
                            and p["agent_id"] == agent_id
                            and p["tool_name"] == tool_name
                        ),
                        None,
                    )
                    if match:
                        await self._notifier.notify_pending(
                            request_id=match["request_id"],
                            domain=match["domain"],
                            port=match["port"],
                            risk_level=match["risk_level"],
                            agent_id=match["agent_id"],
                            tool_name=match["tool_name"],
                        )
                        if self._event_bus is not None:
                            from gateway.ingest_api.event_bus import make_event

                            await self._event_bus.emit(
                                make_event(
                                    "egress_approval_pending",
                                    f"Egress approval pending: {match['domain']}:{match['port']}",
                                    {
                                        "request_id": match["request_id"],
                                        "domain": match["domain"],
                                        "port": match["port"],
                                        "agent_id": match["agent_id"],
                                        "tool_name": match["tool_name"],
                                        "risk_level": match["risk_level"],
                                    },
                                    "warning",
                                )
                            )
                except Exception as exc:
                    logger.error("Egress approval notification error: %s", exc)

            approval_result = await wait_task
            if approval_result.value == "approved":
                return self._record(
                    agent_id,
                    destination,
                    port,
                    EgressAction.ALLOW,
                    f"interactive egress approval granted for '{domain}'",
                )
            return self._record(
                agent_id,
                destination,
                port,
                EgressAction.DENY,
                f"interactive egress approval denied/timeout for '{domain}'",
            )
        return attempt

    def _matches_allowlist_domain(self, domain: str, allowlist: set[str]) -> bool:
        """Check if domain matches any domain in the allowlist (supports wildcards)."""
        domain = domain.lower().rstrip(".")
        for allowed in allowlist:
            allowed = allowed.lower().rstrip(".")
            if allowed.startswith("*."):
                base = allowed[2:]  # "github.com"
                if domain == base:
                    return True
                # Only match one level deep: "sub.github.com" yes, "a.b.github.com" no
                if domain.endswith("." + base):
                    prefix = domain[: -(len(base) + 1)]
                    if "." not in prefix:  # Only one subdomain level
                        return True
            elif domain == allowed:
                return True
        return False

    def _matches_ip_list(self, ip_str: str, ip_list: list[str]) -> bool:
        """Check if IP matches any IP/CIDR in the list."""
        try:
            addr = ipaddress.ip_address(ip_str)
        except ValueError:
            return False
        for allowed in ip_list:
            try:
                network = ipaddress.ip_network(allowed, strict=False)
                if addr in network:
                    return True
            except ValueError:
                if ip_str == allowed:
                    return True
        return False

    @staticmethod
    def _is_ipv6(host: str) -> bool:
        """Check if host looks like an IPv6 address."""
        return "::" in host or (host.count(":") > 2)

    @staticmethod
    def _is_private_ip(host: str) -> bool:
        """Check if host is a private, loopback, link-local, or reserved IP.

        Covers: RFC 1918, loopback (v4+v6), link-local, IPv6 ULA,
        IPv4-mapped IPv6, and localhost hostnames.
        """
        try:
            addr = ipaddress.ip_address(host)
            # Check IPv4-mapped IPv6 addresses (e.g., ::ffff:127.0.0.1)
            if isinstance(addr, ipaddress.IPv6Address) and addr.ipv4_mapped:
                mapped = addr.ipv4_mapped
                return (
                    mapped.is_private
                    or mapped.is_loopback
                    or mapped.is_link_local
                    or mapped.is_reserved
                )
            return addr.is_private or addr.is_loopback or addr.is_link_local or addr.is_reserved
        except ValueError:
            # Not an IP address (it's a domain) — check for localhost variants
            normalized = host.lower().rstrip(".")
            return normalized in ("localhost", "ip6-localhost", "ip6-loopback")

    def _record(
        self,
        agent_id: str,
        dest: str,
        port: Optional[int],
        action: EgressAction,
        rule: str,
    ) -> EgressAttempt:
        # Add helpful error message for enforce mode blocks
        details = ""
        if action == EgressAction.DENY and self.config.mode == "enforce":
            details = (
                f"AgentShroud blocked this request in enforce mode. "
                f"Domain '{dest}' is not in the allowlist. "
                f"Contact your administrator to add trusted domains."
            )

        attempt = EgressAttempt(
            timestamp=time.time(),
            agent_id=agent_id,
            destination=dest,
            port=port,
            action=action,
            rule=rule,
            details=details,
        )
        self._log.append(attempt)
        if len(self._log) > self._max_log_size:
            self._log = self._log[-self._max_log_size // 2 :]

        # Persist to SQLite audit store if configured (fire-and-forget)
        if self._audit_store is not None:
            import asyncio

            try:
                loop = asyncio.get_running_loop()
                loop.create_task(
                    self._audit_store.log_event(
                        event_type="egress_filter",
                        severity="HIGH" if action == EgressAction.DENY else "INFO",
                        details={
                            "agent_id": agent_id,
                            "destination": dest,
                            "port": port,
                            "action": action.value,
                            "rule": rule,
                        },
                        source_module="egress_filter",
                    )
                )
            except RuntimeError:
                pass  # No running event loop

        # Feed automatic decisions into the approval queue's decision log so the
        # SOC egress history page shows both interactive and filter-driven decisions.
        if self._approval_queue is not None and hasattr(
            self._approval_queue, "log_external_decision"
        ):
            try:
                self._approval_queue.log_external_decision(
                    domain=dest,
                    decision=action.value,
                    agent_id=agent_id,
                    reason=rule,
                )
            except Exception:
                pass

        if action == EgressAction.DENY:
            logger.warning(
                f"EGRESS DENIED: agent={agent_id} dest={dest} port={port} "
                f"mode={self.config.mode} rule={rule}"
            )
            # Queue notification for async delivery
            if self._notifier:
                self._pending_notifications.append(
                    {
                        "domain": dest,
                        "agent_id": agent_id,
                        "port": port,
                        "timestamp": time.time(),
                    }
                )
        else:
            logger.info(
                f"EGRESS ALLOWED: agent={agent_id} dest={dest} port={port} "
                f"mode={self.config.mode}"
            )

        if self._event_bus is not None:
            try:
                import asyncio

                from gateway.ingest_api.event_bus import make_event

                loop = asyncio.get_running_loop()
                loop.create_task(
                    self._event_bus.emit(
                        make_event(
                            "egress_attempt",
                            f"Egress {action.value}: {dest}",
                            {
                                "agent_id": agent_id,
                                "destination": dest,
                                "port": port,
                                "rule": rule,
                                "mode": self.config.mode,
                            },
                            "warning" if action == EgressAction.DENY else "info",
                        )
                    )
                )
            except RuntimeError:
                pass

        return attempt

    async def flush_notifications(self) -> int:
        """Send pending egress notifications via Telegram. Called from request handler.

        Returns:
            Number of notifications successfully sent.
        """
        sent = 0
        while self._pending_notifications:
            notif = self._pending_notifications.pop(0)
            try:
                try:
                    await self._notifier.notify_pending(
                        request_id=notif.get("request_id", f"legacy-{int(time.time())}"),
                        domain=notif["domain"],
                        port=notif.get("port", 443),
                        risk_level=notif.get("risk_level", "unknown"),
                        agent_id=notif["agent_id"],
                        tool_name=notif.get("tool_name", "egress"),
                    )
                except TypeError:
                    # Backward-compatible notifier contract
                    await self._notifier.notify_pending(
                        notif["domain"],
                        notif["agent_id"],
                    )
                sent += 1
            except Exception as e:
                logger.error("Egress notification failed: %s", e)
        return sent

    def get_log(self, agent_id: Optional[str] = None, limit: int = 100) -> list[EgressAttempt]:
        """Get egress attempt log, optionally filtered by agent."""
        if agent_id:
            filtered = [a for a in self._log if a.agent_id == agent_id]
        else:
            filtered = self._log
        return filtered[-limit:]

    def get_stats(self, agent_id: Optional[str] = None) -> dict:
        """Get summary statistics of egress attempts."""
        log = self.get_log(agent_id, limit=self._max_log_size)
        allowed = sum(1 for a in log if a.action == EgressAction.ALLOW)
        denied = sum(1 for a in log if a.action == EgressAction.DENY)
        pending = 0
        emergency = {"enabled": False, "reason": ""}
        if self._approval_queue is not None:
            pending = len(getattr(self._approval_queue, "_pending_requests", {}))
            emergency = {
                "enabled": bool(getattr(self._approval_queue, "_emergency_block_all", False)),
                "reason": str(getattr(self._approval_queue, "_emergency_reason", "")),
            }
        return {
            "total": len(log),
            "allowed": allowed,
            "denied": denied,
            "pending": pending,
            "emergency": emergency,
            "top_denied_destinations": self.get_top_destinations(limit=5, denied_only=True),
        }

    def get_top_destinations(self, limit: int = 5, denied_only: bool = False) -> list[dict]:
        """Return top destination domains by volume."""
        attempts = self._log
        if denied_only:
            attempts = [a for a in attempts if a.action == EgressAction.DENY]
        counter: Counter[str] = Counter()
        for a in attempts:
            destination = a.destination
            if "://" in destination:
                parsed = urlparse(destination)
                destination = parsed.hostname or destination
            counter[destination] += 1
        return [
            {"destination": dest, "count": count}
            for dest, count in counter.most_common(max(1, limit))
        ]
