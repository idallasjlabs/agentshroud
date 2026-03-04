# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.

import asyncio
import json
import logging
import re
import time
import uuid
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set
from urllib.parse import urlparse

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
class EgressRule:
    """Represents an egress allow/deny rule."""
    domain: str
    action: str  # "allow" or "deny"
    mode: ApprovalMode
    created_at: float
    expires_at: Optional[float] = None


class EgressApprovalQueue:
    """
    Thread-safe asyncio queue for managing egress approval requests.
    
    Features:
    - Risk assessment heuristic for incoming requests
    - Persistent allowlist/denylist rules
    - Configurable timeout for pending requests
    - Session vs permanent rules
    """
    
    # Known-safe domains (green risk level)
    SAFE_DOMAINS = {
        "api.openai.com",
        "api.anthropic.com", 
        "github.com",
        "api.github.com",
        "raw.githubusercontent.com",
        "icloud.com",
        "api.icloud.com",
        "googleapis.com",
        "api.google.com",
        "api.slack.com",
        "api.telegram.org",
        "discord.com",
        "api.discord.com",
        "api.twitter.com",
        "api.x.com",
        "pypi.org",
        "files.pythonhosted.org",
        "registry.npmjs.org",
        "registry.npmjs.com",
        "cdnjs.cloudflare.com",
        "unpkg.com",
        "cdn.jsdelivr.net"
    }
    
    # Suspicious TLDs (contribute to red risk level)
    SUSPICIOUS_TLDS = {
        ".tk", ".ml", ".ga", ".cf", ".xyz", ".top", ".click", ".download",
        ".stream", ".science", ".work", ".party", ".webcam", ".win"
    }
    
    def __init__(self, rules_file: str = "/app/data/egress_rules.json", default_timeout: int = 30):
        """
        Initialize the approval queue.
        
        Args:
            rules_file: Path to persistent rules storage
            default_timeout: Default timeout in seconds for pending requests
        """
        self.rules_file = Path(rules_file)
        self.default_timeout = default_timeout
        
        # Thread-safe data structures
        self._lock = asyncio.Lock()
        self._pending_requests: Dict[str, EgressRequest] = {}
        self._once_approved: set = set()  # Track one-time approved request IDs
        self._permanent_rules: Dict[str, EgressRule] = {}
        self._session_rules: Dict[str, EgressRule] = {}
        
        # Ensure rules file directory exists
        self.rules_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Load existing rules
        self._load_rules()
    
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
                    expires_at=rule_data.get("expires_at")
                )
                self._permanent_rules[rule.domain] = rule
                
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
                        "expires_at": rule.expires_at
                    }
                    for rule in self._permanent_rules.values()
                ]
            }
            
            with open(self.rules_file, 'w') as f:
                json.dump(data, f, indent=2)
                
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
            
            logger.info(
                f"Egress approval requested: {domain}:{port} "
                f"(risk={risk_level.value}, agent={agent_id}, tool={tool_name})"
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
            
            logger.info(f"Egress approved: {request.domain}:{request.port} (mode={mode.value})")
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
            
            logger.info(f"Egress denied: {request.domain}:{request.port} (mode={mode.value})")
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
    
    async def get_all_rules(self) -> Dict:
        """Get all rules (permanent and session)."""
        async with self._lock:
            return {
                "permanent_rules": [
                    {
                        "domain": rule.domain,
                        "action": rule.action,
                        "mode": rule.mode.value,
                        "created_at": rule.created_at,
                        "expires_at": rule.expires_at
                    }
                    for rule in self._permanent_rules.values()
                ],
                "session_rules": [
                    {
                        "domain": rule.domain,
                        "action": rule.action,
                        "mode": rule.mode.value,
                        "created_at": rule.created_at,
                        "expires_at": rule.expires_at
                    }
                    for rule in self._session_rules.values()
                ]
            }
    
    async def add_rule(self, domain: str, action: str, mode: ApprovalMode) -> bool:
        """
        Add or modify an egress rule.
        
        Args:
            domain: Target domain
            action: "allow" or "deny"
            mode: Rule mode (permanent or session)
            
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
                created_at=time.time()
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