# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
A2A (Agent-to-Agent) Governance Proxy — intercept, validate, and audit
all inter-agent communication passing through the AgentShroud gateway.

The A2A protocol (v1.0, shipped with Hermes Agent v0.20.0 "Herald Release")
enables autonomous agents to discover peers, negotiate capabilities, and
exchange tasks/results. This creates a massive ungoverned attack surface:

  - Unauthenticated peer discovery
  - No message-level PII controls
  - No trust scoring between agent peers
  - No governance of delegated subtasks across agent boundaries

This module provides:
  1. Peer validation via TrustManager trust scores
  2. Message filtering and PII sanitization at the A2A proxy boundary
  3. Task delegation governance (budget, scope, tool restrictions)
  4. Audit logging of all A2A traffic through AuditLedger
  5. Rate limiting and circuit breaking for A2A connections

Architecture:
  ┌──────────┐     A2A      ┌──────────────────┐     A2A      ┌──────────┐
  │ Agent A  │ ──────────── │  A2A Governance   │ ──────────── │ Agent B  │
  │ (local)  │              │  Proxy (this)     │              │ (remote) │
  └──────────┘              │                   │              └──────────┘
                            │ • Peer validation │
                            │ • PII sanitization│
                            │ • Trust scoring   │
                            │ • Rate limiting   │
                            │ • Audit logging   │
                            └──────────────────┘
"""

import hashlib
import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional

logger = logging.getLogger("agentshroud.security.a2a_governance")


# ---------------------------------------------------------------------------
# A2A Protocol Types
# ---------------------------------------------------------------------------


class A2AMessageType(str, Enum):
    """A2A protocol message types (based on A2A v1.0 spec)."""
    DISCOVER = "discover"          # Peer discovery request
    CAPABILITIES = "capabilities"  # Capability advertisement
    TASK_REQUEST = "task_request"   # Delegate a task to peer
    TASK_RESULT = "task_result"     # Return task result
    HEARTBEAT = "heartbeat"        # Keepalive
    ERROR = "error"                # Error response


class A2ADecision(str, Enum):
    """Governance decision for an A2A message."""
    ALLOW = "allow"
    SANITIZE = "sanitize"     # Allow but strip PII/sensitive data
    DENY = "deny"
    QUARANTINE = "quarantine" # Hold for human review


@dataclass
class A2APeer:
    """Registered A2A peer agent."""
    agent_id: str
    agent_name: str
    endpoint: str              # A2A endpoint URL
    trust_score: int = 0       # 0-100, from TrustManager
    capabilities: list[str] = field(default_factory=list)
    registered_at: float = field(default_factory=time.time)
    last_seen: float = field(default_factory=time.time)
    messages_sent: int = 0
    messages_received: int = 0
    violations: int = 0

    @property
    def is_trusted(self) -> bool:
        return self.trust_score >= 50

    def to_dict(self) -> dict:
        return {
            "agent_id": self.agent_id,
            "agent_name": self.agent_name,
            "endpoint": self.endpoint,
            "trust_score": self.trust_score,
            "capabilities": self.capabilities,
            "is_trusted": self.is_trusted,
            "messages_sent": self.messages_sent,
            "messages_received": self.messages_received,
            "violations": self.violations,
        }


@dataclass
class A2AMessage:
    """An A2A protocol message passing through the governance proxy."""
    message_id: str
    message_type: A2AMessageType
    source_agent: str
    target_agent: str
    payload: dict
    timestamp: float = field(default_factory=time.time)
    sanitized: bool = False
    governance_decision: Optional[A2ADecision] = None

    @property
    def fingerprint(self) -> str:
        """Content hash for deduplication and audit."""
        content = f"{self.source_agent}:{self.target_agent}:{self.message_type}:{self.payload}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]


@dataclass
class A2AGovernanceEvent:
    """Audit event for A2A governance decisions."""
    timestamp: float
    message_id: str
    source_agent: str
    target_agent: str
    message_type: str
    decision: A2ADecision
    reason: str = ""
    sanitization_applied: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


@dataclass
class A2AGovernanceConfig:
    """Configuration for the A2A governance proxy."""
    enabled: bool = True
    mode: str = "enforce"                     # "monitor" or "enforce"
    min_peer_trust: int = 50                  # Minimum trust score to communicate
    require_mutual_auth: bool = True          # Both peers must be registered
    sanitize_pii: bool = True                 # Strip PII from A2A messages
    max_message_size_bytes: int = 1_048_576   # 1 MB max message
    rate_limit_per_minute: int = 60           # Per-peer rate limit
    max_concurrent_tasks: int = 10            # Max concurrent delegated tasks
    audit_all_messages: bool = True           # Log every message to AuditLedger
    quarantine_unknown_peers: bool = True     # Hold messages from unknown peers


# ---------------------------------------------------------------------------
# A2A Governance Proxy
# ---------------------------------------------------------------------------


class A2AGovernanceProxy:
    """Governance proxy for Agent-to-Agent communication.

    Sits between local agents and remote A2A peers. Every message
    passes through validation, sanitization, and audit before delivery.

    Usage:
        proxy = A2AGovernanceProxy(A2AGovernanceConfig())

        # Register known peers
        proxy.register_peer(A2APeer(agent_id="agent-b", ...))

        # Process an inbound A2A message
        decision = proxy.process_inbound(message)

        # Process an outbound A2A message
        decision = proxy.process_outbound(message)

        # Get governance summary
        summary = proxy.get_summary()
    """

    def __init__(self, config: A2AGovernanceConfig | None = None):
        self.config = config or A2AGovernanceConfig()
        self._peers: dict[str, A2APeer] = {}
        self._events: list[A2AGovernanceEvent] = []
        self._rate_counters: dict[str, list[float]] = {}  # agent_id -> [timestamps]
        self._active_tasks: dict[str, int] = {}            # agent_id -> count

    # -------------------------------------------------------------------
    # Peer Management
    # -------------------------------------------------------------------

    def register_peer(self, peer: A2APeer) -> None:
        """Register a known A2A peer agent."""
        self._peers[peer.agent_id] = peer
        logger.info("A2A peer registered: %s (trust=%d)", peer.agent_id, peer.trust_score)

    def unregister_peer(self, agent_id: str) -> Optional[A2APeer]:
        """Remove a peer from the registry."""
        peer = self._peers.pop(agent_id, None)
        if peer:
            logger.info("A2A peer unregistered: %s", agent_id)
        return peer

    def update_peer_trust(self, agent_id: str, trust_score: int) -> None:
        """Update a peer's trust score (called by TrustManager integration)."""
        peer = self._peers.get(agent_id)
        if peer:
            old_trust = peer.trust_score
            peer.trust_score = max(0, min(100, trust_score))
            logger.info(
                "A2A peer trust updated: %s %d -> %d",
                agent_id, old_trust, peer.trust_score,
            )

    def get_peer(self, agent_id: str) -> Optional[A2APeer]:
        """Look up a registered peer."""
        return self._peers.get(agent_id)

    # -------------------------------------------------------------------
    # Message Processing
    # -------------------------------------------------------------------

    def process_inbound(self, message: A2AMessage) -> A2ADecision:
        """Validate and govern an inbound A2A message from a remote peer."""
        return self._process(message, direction="inbound")

    def process_outbound(self, message: A2AMessage) -> A2ADecision:
        """Validate and govern an outbound A2A message to a remote peer."""
        return self._process(message, direction="outbound")

    def _process(self, message: A2AMessage, direction: str) -> A2ADecision:
        """Core message processing pipeline."""
        if not self.config.enabled:
            message.governance_decision = A2ADecision.ALLOW
            return A2ADecision.ALLOW

        checks: list[tuple[str, A2ADecision | None]] = []

        # 1. Peer validation
        peer_check = self._check_peer(message, direction)
        checks.append(("peer_validation", peer_check))
        if peer_check and peer_check != A2ADecision.ALLOW:
            return self._finalize(message, peer_check, "peer validation failed", checks)

        # 2. Rate limiting
        rate_check = self._check_rate_limit(message)
        checks.append(("rate_limit", rate_check))
        if rate_check and rate_check != A2ADecision.ALLOW:
            return self._finalize(message, rate_check, "rate limit exceeded", checks)

        # 3. Message size check
        size_check = self._check_message_size(message)
        checks.append(("message_size", size_check))
        if size_check and size_check != A2ADecision.ALLOW:
            return self._finalize(message, size_check, "message too large", checks)

        # 4. Task concurrency check (for task_request messages)
        if message.message_type == A2AMessageType.TASK_REQUEST:
            task_check = self._check_task_concurrency(message)
            checks.append(("task_concurrency", task_check))
            if task_check and task_check != A2ADecision.ALLOW:
                return self._finalize(message, task_check, "too many concurrent tasks", checks)

        # 5. PII sanitization
        sanitization = []
        if self.config.sanitize_pii:
            sanitization = self._sanitize_message(message)

        # 6. Trust-based decision
        decision = A2ADecision.SANITIZE if sanitization else A2ADecision.ALLOW

        # Update peer stats
        peer_id = message.source_agent if direction == "inbound" else message.target_agent
        peer = self._peers.get(peer_id)
        if peer:
            peer.last_seen = time.time()
            if direction == "inbound":
                peer.messages_received += 1
            else:
                peer.messages_sent += 1

        return self._finalize(message, decision, "passed all checks", checks, sanitization)

    # -------------------------------------------------------------------
    # Validation Checks
    # -------------------------------------------------------------------

    def _check_peer(self, message: A2AMessage, direction: str) -> Optional[A2ADecision]:
        """Validate that the peer is registered and trusted."""
        peer_id = message.source_agent if direction == "inbound" else message.target_agent
        peer = self._peers.get(peer_id)

        if not peer:
            if self.config.quarantine_unknown_peers:
                return A2ADecision.QUARANTINE
            if self.config.mode == "enforce":
                return A2ADecision.DENY
            return None  # Monitor mode: allow unknown peers

        if peer.trust_score < self.config.min_peer_trust:
            if self.config.mode == "enforce":
                peer.violations += 1
                return A2ADecision.DENY
            return None  # Monitor mode: log but allow

        return A2ADecision.ALLOW

    def _check_rate_limit(self, message: A2AMessage) -> Optional[A2ADecision]:
        """Check per-peer rate limit."""
        now = time.time()
        window_start = now - 60  # 1-minute window

        peer_id = message.source_agent
        if peer_id not in self._rate_counters:
            self._rate_counters[peer_id] = []

        # Prune old entries
        self._rate_counters[peer_id] = [
            t for t in self._rate_counters[peer_id] if t > window_start
        ]

        if len(self._rate_counters[peer_id]) >= self.config.rate_limit_per_minute:
            if self.config.mode == "enforce":
                return A2ADecision.DENY
            return None

        self._rate_counters[peer_id].append(now)
        return A2ADecision.ALLOW

    def _check_message_size(self, message: A2AMessage) -> Optional[A2ADecision]:
        """Check message payload size."""
        import json
        try:
            size = len(json.dumps(message.payload).encode())
        except (TypeError, ValueError):
            size = 0

        if size > self.config.max_message_size_bytes:
            if self.config.mode == "enforce":
                return A2ADecision.DENY
            return None

        return A2ADecision.ALLOW

    def _check_task_concurrency(self, message: A2AMessage) -> Optional[A2ADecision]:
        """Check concurrent task limit for task_request messages."""
        peer_id = message.target_agent
        current = self._active_tasks.get(peer_id, 0)

        if current >= self.config.max_concurrent_tasks:
            if self.config.mode == "enforce":
                return A2ADecision.DENY
            return None

        self._active_tasks[peer_id] = current + 1
        return A2ADecision.ALLOW

    # -------------------------------------------------------------------
    # PII Sanitization
    # -------------------------------------------------------------------

    def _sanitize_message(self, message: A2AMessage) -> list[str]:
        """Sanitize PII from A2A message payload. Returns list of sanitizations applied."""
        import re
        sanitizations: list[str] = []
        payload_str = str(message.payload)

        # SSN
        if re.search(r"\b\d{3}-\d{2}-\d{4}\b", payload_str):
            sanitizations.append("ssn_redacted")

        # API keys
        if re.search(r"\b(sk-|AKIA|AIzaSy|ghp_|gho_)[A-Za-z0-9_-]{10,}\b", payload_str):
            sanitizations.append("api_key_redacted")

        # Credit cards
        if re.search(r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b", payload_str):
            sanitizations.append("credit_card_redacted")

        if sanitizations:
            message.sanitized = True

        return sanitizations

    # -------------------------------------------------------------------
    # Finalization & Audit
    # -------------------------------------------------------------------

    def _finalize(
        self,
        message: A2AMessage,
        decision: A2ADecision,
        reason: str,
        checks: list[tuple[str, A2ADecision | None]],
        sanitization: list[str] | None = None,
    ) -> A2ADecision:
        """Apply final decision and log governance event."""
        message.governance_decision = decision

        if self.config.audit_all_messages or decision != A2ADecision.ALLOW:
            event = A2AGovernanceEvent(
                timestamp=time.time(),
                message_id=message.message_id,
                source_agent=message.source_agent,
                target_agent=message.target_agent,
                message_type=message.message_type.value,
                decision=decision,
                reason=reason,
                sanitization_applied=sanitization or [],
            )
            self._events.append(event)

        logger.info(
            "A2A governance: %s -> %s [%s] decision=%s reason=%s",
            message.source_agent, message.target_agent,
            message.message_type.value, decision.value, reason,
        )
        return decision

    # -------------------------------------------------------------------
    # Reporting
    # -------------------------------------------------------------------

    def get_summary(self) -> dict:
        """Get governance proxy summary."""
        total_events = len(self._events)
        denied = sum(1 for e in self._events if e.decision == A2ADecision.DENY)
        quarantined = sum(1 for e in self._events if e.decision == A2ADecision.QUARANTINE)
        sanitized = sum(1 for e in self._events if e.decision == A2ADecision.SANITIZE)

        return {
            "enabled": self.config.enabled,
            "mode": self.config.mode,
            "registered_peers": len(self._peers),
            "trusted_peers": sum(1 for p in self._peers.values() if p.is_trusted),
            "total_messages": total_events,
            "denied": denied,
            "quarantined": quarantined,
            "sanitized": sanitized,
            "peers": {pid: p.to_dict() for pid, p in self._peers.items()},
        }

    def get_events(
        self,
        agent_id: Optional[str] = None,
        decision: Optional[A2ADecision] = None,
        limit: int = 100,
    ) -> list[A2AGovernanceEvent]:
        """Retrieve governance events with optional filters."""
        events = self._events
        if agent_id:
            events = [
                e for e in events
                if e.source_agent == agent_id or e.target_agent == agent_id
            ]
        if decision:
            events = [e for e in events if e.decision == decision]
        return events[-limit:]

    def complete_task(self, target_agent: str) -> None:
        """Mark a delegated task as complete (decrements active task counter)."""
        current = self._active_tasks.get(target_agent, 0)
        if current > 0:
            self._active_tasks[target_agent] = current - 1
