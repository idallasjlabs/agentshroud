"""
Egress Filtering — block unauthorized outbound traffic.

Domain/IP allowlist with default-deny policy. Configurable per-agent
with logging of all egress attempts.
"""

import ipaddress
import logging
import re
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from urllib.parse import urlparse

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
    allowed_ports: list[int] = field(default_factory=lambda: [80, 443])
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
    """Filter outbound connections based on allowlists."""

    def __init__(self, default_policy: Optional[EgressPolicy] = None):
        self.default_policy = default_policy or EgressPolicy()
        self._agent_policies: dict[str, EgressPolicy] = {}
        self._log: list[EgressAttempt] = []
        self._max_log_size = 10000

    def set_agent_policy(self, agent_id: str, policy: EgressPolicy) -> None:
        """Set a per-agent egress policy."""
        self._agent_policies[agent_id] = policy

    def get_policy(self, agent_id: str) -> EgressPolicy:
        """Get effective policy for an agent."""
        return self._agent_policies.get(agent_id, self.default_policy)

    def check(
        self, agent_id: str, destination: str, port: Optional[int] = None
    ) -> EgressAttempt:
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

        # Block private/loopback IPs unless explicitly in allowlist
        if self._is_private_ip(parsed_dest) and not policy.matches_ip(parsed_dest):
            return self._record(
                agent_id, destination, port, EgressAction.DENY,
                f"private/loopback IP '{parsed_dest}' blocked (SSRF protection)"
            )

        # Check port first
        if not policy.matches_port(port):
            return self._record(
                agent_id, destination, port, EgressAction.DENY,
                f"port {port} not allowed"
            )

        # Check domain
        if policy.matches_domain(parsed_dest):
            return self._record(
                agent_id, destination, port, EgressAction.ALLOW,
                f"domain '{parsed_dest}' in allowlist"
            )

        # Check IP
        if policy.matches_ip(parsed_dest):
            return self._record(
                agent_id, destination, port, EgressAction.ALLOW,
                f"IP '{parsed_dest}' in allowlist"
            )

        # Default deny
        if policy.deny_all:
            return self._record(
                agent_id, destination, port, EgressAction.DENY,
                f"default deny: '{parsed_dest}' not in allowlist"
            )

        return self._record(
            agent_id, destination, port, EgressAction.ALLOW,
            "default allow (deny_all=False)"
        )

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
                return mapped.is_private or mapped.is_loopback or mapped.is_link_local or mapped.is_reserved
            return addr.is_private or addr.is_loopback or addr.is_link_local or addr.is_reserved
        except ValueError:
            # Not an IP address (it's a domain) — check for localhost variants
            normalized = host.lower().rstrip(".")
            return normalized in ("localhost", "ip6-localhost", "ip6-loopback")

    def _record(
        self, agent_id: str, dest: str, port: Optional[int],
        action: EgressAction, rule: str
    ) -> EgressAttempt:
        attempt = EgressAttempt(
            timestamp=time.time(),
            agent_id=agent_id,
            destination=dest,
            port=port,
            action=action,
            rule=rule,
        )
        self._log.append(attempt)
        if len(self._log) > self._max_log_size:
            self._log = self._log[-self._max_log_size // 2:]

        if action == EgressAction.DENY:
            logger.warning(f"EGRESS DENIED: agent={agent_id} dest={dest} port={port} rule={rule}")
        else:
            logger.info(f"EGRESS ALLOWED: agent={agent_id} dest={dest} port={port}")

        return attempt

    def get_log(
        self, agent_id: Optional[str] = None, limit: int = 100
    ) -> list[EgressAttempt]:
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
        return {"total": len(log), "allowed": allowed, "denied": denied}
