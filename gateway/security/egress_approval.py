# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744

import asyncio
import json
import logging
import re
import time
import uuid
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set
from urllib.parse import urlparse

from .egress_config import PERMANENT_EGRESS_DOMAINS

logger = logging.getLogger(__name__)


class ApprovalResult(Enum):
    """Result of an approval request."""
    APPROVED = "approved"
    DENIED = "denied" 
    TIMEOUT = "timeout"


class RiskLevel(Enum):
    """Risk assessment levels for egress requests."""
    GREEN = "green"    # Known-safe domains
    YELLOW = "yellow"  # Unknown domain, standard ports
    RED = "red"        # High-risk (IP, non-standard ports, suspicious TLDs)


class ApprovalMode(Enum):
    """Approval modes for rules."""
    PERMANENT = "permanent"
    SESSION = "session" 
    ONCE = "once"


@dataclass
class EgressRequest:
    """Represents a pending egress approval request."""
    request_id: str
    domain: str
    port: int
    agent_id: str
    tool_name: str
    timestamp: float
    risk_level: RiskLevel
    timeout_at: float


@dataclass
class EgressScope:
    """Defines who an egress rule applies to.

    kind values:
      "all"   — applies to every user/agent (default, backward-compatible)
      "user"  — applies only to user_ids listed
      "group" — applies only to members of group_ids listed
    """
    kind: str = "all"  # "all" | "user" | "group"
    user_ids: List[str] = field(default_factory=list)
    group_ids: List[str] = field(default_factory=list)

    def matches(self, user_id: Optional[str], group_ids: Optional[List[str]], is_owner: bool = False) -> bool:
        """Return True if this scope applies to the given user context."""
        if is_owner or self.kind == "all":
            return True
        if self.kind == "user" and user_id and user_id in self.user_ids:
            return True
        if self.kind == "group" and group_ids:
            return any(gid in self.group_ids for gid in group_ids)
        return False

    def to_dict(self) -> dict:
        return {"kind": self.kind, "user_ids": self.user_ids, "group_ids": self.group_ids}

    @classmethod
    def from_dict(cls, d: dict) -> "EgressScope":
        return cls(
            kind=d.get("kind", "all"),
            user_ids=d.get("user_ids", []),
            group_ids=d.get("group_ids", []),
        )


@dataclass
class EgressRule:
    """Represents an egress allow/deny rule."""
    domain: str
    action: str  # "allow" or "deny"
    mode: ApprovalMode
    created_at: float
    expires_at: Optional[float] = None
    scope: EgressScope = field(default_factory=EgressScope)


class EgressApprovalQueue:
    """
    Thread-safe asyncio queue for managing egress approval requests.
    
    Features:
    - Risk assessment heuristic for incoming requests
    - Persistent allowlist/denylist rules
    - Configurable timeout for pending requests
    - Session vs permanent rules
    """
    
    # Known-safe domains (green risk level) — derived from canonical PERMANENT_EGRESS_DOMAINS.
    # Wildcards (*.foo.com) are stored as their base domain (foo.com) so the subdomain
    # walk in _assess_risk can match them via domain.endswith(".foo.com").
    SAFE_DOMAINS: set[str] = {
        d[2:] if d.startswith("*.") else d
        for d in PERMANENT_EGRESS_DOMAINS
    } | {
        # Additional known-safe domains not in the egress allowlist
        "github.com",
        "api.github.com",
        "raw.githubusercontent.com",
        "discord.com",
        "api.discord.com",
        "api.twitter.com",
        "api.x.com",
        "registry.npmjs.com",
    }
    
    # Suspicious TLDs (contribute to red risk level)
    SUSPICIOUS_TLDS = {
        ".tk", ".ml", ".ga", ".cf", ".xyz", ".top", ".click", ".download",
        ".stream", ".science", ".work", ".party", ".webcam", ".win"
    }
    
    def __init__(
        self,
        rules_file: str = "/tmp/agentshroud/egress_rules.json",
        default_timeout: int = 300,
    ):
        """
        Initialize the approval queue.

        Args:
            rules_file: Path to persistent rules storage
            default_timeout: Default timeout in seconds for pending requests (default 5 min)
        """
        self.rules_file = Path(rules_file)
        self.default_timeout = default_timeout
        
        # Thread-safe data structures
        self._lock = asyncio.Lock()
        self._pending_requests: Dict[str, EgressRequest] = {}
        self._once_approved: set = set()  # Track one-time approved request IDs
        self._permanent_rules: Dict[str, EgressRule] = {}
        self._session_rules: Dict[str, EgressRule] = {}
        # Maps request_id -> domain; persisted so old inline keyboard buttons
        # still resolve their domain after a gateway restart.
        self._request_domain_map: Dict[str, str] = {}
        self._emergency_block_all: bool = False
        self._emergency_reason: str = ""
        self._event_bus = None
        # Decision audit log — capped at 500 entries (CC-40)
        self._decision_log: List[Dict] = []
        # Throttle for EgressFilter auto-decisions: domain → last-logged unix timestamp.
        # Prevents the decision log being flooded with repetitive allow entries for
        # pre-approved domains (only first occurrence per domain per hour is logged).
        self._external_decision_throttle: Dict[str, float] = {}
        
        # Ensure rules file directory exists
        try:
            self.rules_file.parent.mkdir(parents=True, exist_ok=True)
        except Exception:
            # Fallback for restricted environments/tests where /app is unwritable
            self.rules_file = Path("/tmp/agentshroud/egress_rules.json")
            self.rules_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Load existing rules
        self._load_rules()

    def set_event_bus(self, event_bus) -> None:
        """Set optional event bus for approval telemetry."""
        self._event_bus = event_bus

    async def preload_permanent_rules(self, domains: List[str]) -> int:
        """Pre-approve known service domains at startup without interactive prompts.

        Creates in-memory PERMANENT allow rules for each domain that has no
        existing rule. Domains with persisted deny rules (SOC overrides) are
        intentionally skipped, preserving SOC control across restarts.

        Rules are NOT written to disk — they are re-injected on every startup
        from the canonical PERMANENT_EGRESS_DOMAINS list, while persisted deny
        overrides always win because _check_existing_rule is consulted first.

        Returns:
            Number of domains newly pre-approved.
        """
        added = 0
        async with self._lock:
            for raw_domain in domains:
                # Normalize wildcards: *.foo.com → foo.com for rule storage
                domain = raw_domain[2:] if raw_domain.startswith("*.") else raw_domain
                if self._check_existing_rule(domain):
                    continue  # Existing rule (allow or deny) takes precedence
                rule = EgressRule(
                    domain=domain,
                    action="allow",
                    mode=ApprovalMode.PERMANENT,
                    created_at=time.time(),
                )
                rule.source = "preloaded"  # tag so UI can categorize (CC-09)
                self._permanent_rules[domain] = rule
                added += 1
        if added:
            logger.info("EgressApprovalQueue: pre-approved %d known service domain(s)", added)
        return added

    def _assess_risk(self, domain: str, port: int) -> RiskLevel:
        """
        Assess risk level for a domain/port combination.
        
        Returns:
            RiskLevel.GREEN: Known-safe domains
            RiskLevel.YELLOW: Unknown domain, standard ports (80/443)
            RiskLevel.RED: IP addresses, non-standard ports, suspicious TLDs
        """
        # Check if it's an IP address
        ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
        if ip_pattern.match(domain):
            return RiskLevel.RED
        
        # Check for suspicious TLDs
        for tld in self.SUSPICIOUS_TLDS:
            if domain.endswith(tld):
                return RiskLevel.RED
        
        # Check for non-standard ports
        if port not in (80, 443, 8080, 8443):
            return RiskLevel.RED
        
        # Check if it's a known-safe domain
        if domain in self.SAFE_DOMAINS:
            return RiskLevel.GREEN
        
        # Check if subdomain of known-safe domain
        for safe_domain in self.SAFE_DOMAINS:
            if domain.endswith(f".{safe_domain}"):
                return RiskLevel.GREEN
        
        # Default to yellow for unknown domains on standard ports
        return RiskLevel.YELLOW

    def assess_risk(self, domain: str, port: int) -> str:
        """Public risk assessment helper for management/API surfaces."""
        return self._assess_risk(domain, port).value
    
    def _load_rules(self):
        """Load rules from persistent storage."""
        if not self.rules_file.exists():
            return
        
        try:
            with open(self.rules_file, 'r') as f:
                content = f.read().strip()
                if not content:  # Empty file
                    return
                data = json.loads(content)
            
            for rule_data in data.get("permanent_rules", []):
                rule = EgressRule(
                    domain=rule_data["domain"],
                    action=rule_data["action"],
                    mode=ApprovalMode(rule_data.get("mode", "permanent")),
                    created_at=rule_data["created_at"],
                    expires_at=rule_data.get("expires_at"),
                    scope=EgressScope.from_dict(rule_data.get("scope", {})),
                )
                self._permanent_rules[rule.domain] = rule

            # Restore request_domain_map so old inline keyboard buttons still work
            # after a gateway restart (buttons carry request_id but not domain).
            self._request_domain_map = dict(data.get("request_domain_map", {}))

        except Exception as e:
            logger.error(f"Failed to load egress rules: {e}")
    
    def _save_rules(self):
        """Save rules to persistent storage."""
        try:
            data = {
                "permanent_rules": [
                    {
                        "domain": rule.domain,
                        "action": rule.action,
                        "mode": rule.mode.value,
                        "created_at": rule.created_at,
                        "expires_at": rule.expires_at,
                        "scope": getattr(rule, "scope", EgressScope()).to_dict(),
                    }
                    for rule in self._permanent_rules.values()
                ],
                # Persist so old inline keyboard buttons resolve domain after restart.
                # Capped at 500 entries to avoid unbounded growth.
                "request_domain_map": dict(
                    list(self._request_domain_map.items())[-500:]
                ),
            }
            
            with open(self.rules_file, 'w') as f:
                json.dump(data, f, indent=2)

            # Cap in-memory map to match the on-disk cap
            if len(self._request_domain_map) > 500:
                self._request_domain_map = dict(
                    list(self._request_domain_map.items())[-500:]
                )

        except Exception as e:
            logger.error(f"Failed to save egress rules: {e}")
    
    def _check_existing_rule(self, domain: str) -> Optional[EgressRule]:
        """Check if domain matches an existing rule."""
        # Check exact domain match first
        if domain in self._permanent_rules:
            return self._permanent_rules[domain]
        if domain in self._session_rules:
            return self._session_rules[domain]
        
        # Check for wildcard/parent domain matches
        parts = domain.split('.')
        for i in range(1, len(parts)):
            parent_domain = '.'.join(parts[i:])
            if parent_domain in self._permanent_rules:
                return self._permanent_rules[parent_domain]
            if parent_domain in self._session_rules:
                return self._session_rules[parent_domain]
        
        return None
    
    async def request_approval(
        self, 
        domain: str, 
        port: int, 
        agent_id: str, 
        tool_name: str,
        timeout: Optional[int] = None
    ) -> ApprovalResult:
        """
        Request approval for egress to a domain/port.
        
        Args:
            domain: Target domain
            port: Target port
            agent_id: ID of requesting agent
            tool_name: Name of tool making request
            timeout: Custom timeout in seconds
            
        Returns:
            ApprovalResult indicating if request was approved, denied, or timed out
        """
        async with self._lock:
            if self._emergency_block_all:
                logger.warning(
                    "Egress denied by emergency block-all: %s:%s (%s)",
                    domain, port, self._emergency_reason or "no reason",
                )
                if self._event_bus is not None:
                    from gateway.ingest_api.event_bus import make_event
                    await self._event_bus.emit(
                        make_event(
                            "egress_approval_denied",
                            f"Egress denied by emergency block-all: {domain}:{port}",
                            {"domain": domain, "port": port, "agent_id": agent_id},
                            "critical",
                        )
                    )
                return ApprovalResult.DENIED

            # Check existing rules first
            existing_rule = self._check_existing_rule(domain)
            if existing_rule:
                if existing_rule.action == "allow":
                    logger.info(f"Egress approved by existing rule: {domain}:{port}")
                    return ApprovalResult.APPROVED
                else:
                    logger.info(f"Egress denied by existing rule: {domain}:{port}")
                    return ApprovalResult.DENIED
            
            # Create new pending request
            request_id = str(uuid.uuid4())
            risk_level = self._assess_risk(domain, port)
            request_timeout = timeout or self.default_timeout
            
            request = EgressRequest(
                request_id=request_id,
                domain=domain,
                port=port,
                agent_id=agent_id,
                tool_name=tool_name,
                timestamp=time.time(),
                risk_level=risk_level,
                timeout_at=time.time() + request_timeout
            )
            
            self._pending_requests[request_id] = request
            self._request_domain_map[request_id] = domain

            logger.info(
                f"Egress approval requested: {domain}:{port} "
                f"(risk={risk_level.value}, agent={agent_id}, tool={tool_name})"
            )
            if self._event_bus is not None:
                from gateway.ingest_api.event_bus import make_event
                await self._event_bus.emit(
                    make_event(
                        "egress_approval_requested",
                        f"Egress approval requested: {domain}:{port}",
                        {
                            "request_id": request_id,
                            "domain": domain,
                            "port": port,
                            "agent_id": agent_id,
                            "tool_name": tool_name,
                            "risk_level": risk_level.value,
                        },
                        "warning",
                    )
                )
        
        # Wait for approval or timeout
        try:
            while time.time() < request.timeout_at:
                async with self._lock:
                    if request_id not in self._pending_requests:
                        # Request was processed - check if once-approved
                        if request_id in self._once_approved:
                            self._once_approved.discard(request_id)
                            return ApprovalResult.APPROVED
                        rule = self._check_existing_rule(domain)
                        if rule and rule.action == "allow":
                            return ApprovalResult.APPROVED
                        else:
                            return ApprovalResult.DENIED
                
                await asyncio.sleep(0.1)  # Check every 100ms
            
            # Timeout reached
            async with self._lock:
                self._pending_requests.pop(request_id, None)
            
            logger.warning(f"Egress approval timeout: {domain}:{port}")
            return ApprovalResult.TIMEOUT
            
        except Exception as e:
            logger.error(f"Error in approval request: {e}")
            async with self._lock:
                self._pending_requests.pop(request_id, None)
            return ApprovalResult.DENIED
    
    async def approve(self, request_id: str, mode: ApprovalMode = ApprovalMode.ONCE) -> bool:
        """
        Approve a pending egress request.
        
        Args:
            request_id: ID of request to approve
            mode: Approval mode (permanent, session, or once)
            
        Returns:
            True if request was found and approved, False otherwise
        """
        async with self._lock:
            request = self._pending_requests.get(request_id)
            if not request:
                return False
            
            if mode == ApprovalMode.ONCE:
                # Remove from pending, mark as once-approved
                self._once_approved.add(request_id)
                self._pending_requests.pop(request_id)
            else:
                # Create a rule for future requests
                rule = EgressRule(
                    domain=request.domain,
                    action="allow",
                    mode=mode,
                    created_at=time.time()
                )
                
                if mode == ApprovalMode.PERMANENT:
                    self._permanent_rules[request.domain] = rule
                    self._save_rules()
                else:  # SESSION
                    self._session_rules[request.domain] = rule
                
                # Remove from pending
                self._pending_requests.pop(request_id)
            
            self._append_decision(request, "approved", mode.value, "")
            logger.info(f"Egress approved: {request.domain}:{request.port} (mode={mode.value})")
            if self._event_bus is not None:
                from gateway.ingest_api.event_bus import make_event
                await self._event_bus.emit(
                    make_event(
                        "egress_approval_decision",
                        f"Egress approved: {request.domain}:{request.port}",
                        {
                            "request_id": request_id,
                            "domain": request.domain,
                            "port": request.port,
                            "mode": mode.value,
                            "decision": "approved",
                        },
                        "info",
                    )
                )
            return True
    
    async def deny(self, request_id: str, mode: ApprovalMode = ApprovalMode.ONCE) -> bool:
        """
        Deny a pending egress request.
        
        Args:
            request_id: ID of request to deny
            mode: Denial mode (permanent, session, or once)
            
        Returns:
            True if request was found and denied, False otherwise
        """
        async with self._lock:
            request = self._pending_requests.get(request_id)
            if not request:
                return False
            
            if mode == ApprovalMode.ONCE:
                # Remove from pending, deny this one request
                self._pending_requests.pop(request_id)
            else:
                # Create a deny rule for future requests
                rule = EgressRule(
                    domain=request.domain,
                    action="deny",
                    mode=mode,
                    created_at=time.time()
                )
                
                if mode == ApprovalMode.PERMANENT:
                    self._permanent_rules[request.domain] = rule
                    self._save_rules()
                else:  # SESSION
                    self._session_rules[request.domain] = rule
                
                # Remove from pending
                self._pending_requests.pop(request_id)
            
            self._append_decision(request, "denied", mode.value, "")
            logger.info(f"Egress denied: {request.domain}:{request.port} (mode={mode.value})")
            if self._event_bus is not None:
                from gateway.ingest_api.event_bus import make_event
                await self._event_bus.emit(
                    make_event(
                        "egress_approval_decision",
                        f"Egress denied: {request.domain}:{request.port}",
                        {
                            "request_id": request_id,
                            "domain": request.domain,
                            "port": request.port,
                            "mode": mode.value,
                            "decision": "denied",
                        },
                        "warning",
                    )
                )
            return True
    
    async def get_pending_requests(self) -> List[Dict]:
        """Get list of pending approval requests."""
        async with self._lock:
            return [
                {
                    "request_id": req.request_id,
                    "domain": req.domain,
                    "port": req.port,
                    "agent_id": req.agent_id,
                    "tool_name": req.tool_name,
                    "timestamp": req.timestamp,
                    "risk_level": req.risk_level.value,
                    "timeout_at": req.timeout_at
                }
                for req in self._pending_requests.values()
            ]
    
    def _rule_to_dict(self, rule: "EgressRule") -> dict:
        d = {
            "domain": rule.domain,
            "action": rule.action,
            "mode": rule.mode.value,
            "created_at": rule.created_at,
            "expires_at": rule.expires_at,
            "scope": getattr(rule, "scope", EgressScope()).to_dict(),
        }
        src = getattr(rule, "source", "user")
        if src:
            d["source"] = src
        return d

    async def get_all_rules(self) -> Dict:
        """Get all rules (permanent and session) with scope information."""
        async with self._lock:
            return {
                "permanent_rules": [self._rule_to_dict(r) for r in self._permanent_rules.values()],
                "session_rules": [self._rule_to_dict(r) for r in self._session_rules.values()],
            }

    def get_rules_for_user(
        self, user_id: Optional[str], group_ids: Optional[List[str]] = None, is_owner: bool = False
    ) -> List["EgressRule"]:
        """Return all rules whose scope matches the given user context (synchronous, lock-free read)."""
        group_ids = group_ids or []
        matching = []
        for rule in list(self._permanent_rules.values()) + list(self._session_rules.values()):
            scope = getattr(rule, "scope", EgressScope())
            if scope.matches(user_id, group_ids, is_owner=is_owner):
                matching.append(rule)
        return matching
    
    def _append_decision(self, request: "EgressRequest", decision: str, mode: str, decided_by: str) -> None:
        """Append an entry to the capped decision audit log (CC-40)."""
        entry = {
            "id": str(uuid.uuid4())[:8],
            "domain": request.domain,
            "port": request.port,
            "agent_id": request.agent_id,
            "decision": decision,
            "mode": mode,
            "decided_by": decided_by,
            "decided_at": time.time(),
        }
        self._decision_log.insert(0, entry)
        if len(self._decision_log) > 500:
            self._decision_log = self._decision_log[:500]

    def log_external_decision(
        self, domain: str, decision: str, agent_id: str, reason: str = ""
    ) -> None:
        """Log an automatic allow/deny from EgressFilter.check() (non-interactive).

        Throttled to one entry per domain per hour so pre-approved permanent domains
        do not flood the decision log on every request.
        """
        now = time.time()
        last = self._external_decision_throttle.get(domain, 0.0)
        if now - last < 3600:
            return
        self._external_decision_throttle[domain] = now
        entry = {
            "id": str(uuid.uuid4())[:8],
            "domain": domain,
            "port": None,
            "agent_id": agent_id,
            "decision": decision,
            "mode": "auto",
            "decided_by": "egress_filter",
            "decided_at": now,
            "reason": reason,
        }
        self._decision_log.insert(0, entry)
        if len(self._decision_log) > 500:
            self._decision_log = self._decision_log[:500]

    async def get_decision_log(self, limit: int = 100) -> List[Dict]:
        """Return recent approval/denial decisions (CC-40)."""
        async with self._lock:
            return self._decision_log[:limit]

    async def revoke_decision(self, entry_id: str) -> bool:
        """Revoke an active rule associated with a decision log entry (CC-40)."""
        async with self._lock:
            for entry in self._decision_log:
                if entry["id"] == entry_id:
                    domain = entry["domain"]
                    removed = domain in self._permanent_rules or domain in self._session_rules
                    self._permanent_rules.pop(domain, None)
                    self._session_rules.pop(domain, None)
                    if removed:
                        self._save_rules()
                    return removed
        return False

    async def add_rule(
        self, domain: str, action: str, mode: ApprovalMode, scope: Optional["EgressScope"] = None
    ) -> bool:
        """
        Add or modify an egress rule.

        Args:
            domain: Target domain
            action: "allow" or "deny"
            mode: Rule mode (permanent or session)
            scope: Optional EgressScope (default: all users)

        Returns:
            True if rule was added successfully
        """
        if action not in ("allow", "deny"):
            return False

        async with self._lock:
            rule = EgressRule(
                domain=domain,
                action=action,
                mode=mode,
                created_at=time.time(),
                scope=scope or EgressScope(),
            )
            
            if mode == ApprovalMode.PERMANENT:
                self._permanent_rules[domain] = rule
                self._save_rules()
            else:  # SESSION
                self._session_rules[domain] = rule
            
            logger.info(f"Egress rule added: {domain} -> {action} (mode={mode.value})")
            return True
    
    async def remove_rule(self, domain: str) -> bool:
        """
        Remove an egress rule.
        
        Args:
            domain: Domain to remove rule for
            
        Returns:
            True if rule was found and removed
        """
        async with self._lock:
            removed = False
            
            if domain in self._permanent_rules:
                del self._permanent_rules[domain]
                self._save_rules()
                removed = True
            
            if domain in self._session_rules:
                del self._session_rules[domain]
                removed = True
            
            if removed:
                logger.info(f"Egress rule removed: {domain}")
            
            return removed

    async def set_emergency_block_all(self, enabled: bool, reason: str = "") -> None:
        """Enable/disable emergency global egress deny."""
        async with self._lock:
            self._emergency_block_all = enabled
            self._emergency_reason = reason or ""

    async def get_emergency_status(self) -> Dict[str, str | bool]:
        """Get emergency block-all state."""
        async with self._lock:
            return {
                "enabled": self._emergency_block_all,
                "reason": self._emergency_reason,
            }
    
    async def cleanup_expired(self):
        """Remove expired session rules and timed-out requests."""
        current_time = time.time()
        
        async with self._lock:
            # Clean up timed-out pending requests
            expired_requests = [
                req_id for req_id, req in self._pending_requests.items()
                if req.timeout_at < current_time
            ]
            
            for req_id in expired_requests:
                self._pending_requests.pop(req_id)
            
            if expired_requests:
                logger.info(f"Cleaned up {len(expired_requests)} expired pending requests")
            
            # Clean up expired rules (if we add expiration support later)
            expired_permanent = [
                domain for domain, rule in self._permanent_rules.items()
                if rule.expires_at and rule.expires_at < current_time
            ]
            
            expired_session = [
                domain for domain, rule in self._session_rules.items() 
                if rule.expires_at and rule.expires_at < current_time
            ]
            
            for domain in expired_permanent:
                del self._permanent_rules[domain]
            
            for domain in expired_session:
                del self._session_rules[domain]
            
            if expired_permanent or expired_session:
                logger.info(f"Cleaned up {len(expired_permanent + expired_session)} expired rules")
                if expired_permanent:
                    self._save_rules()
