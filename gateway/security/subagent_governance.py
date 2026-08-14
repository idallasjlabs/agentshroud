# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Subagent Governance Module — unified governance layer for autonomous AI subagents.

Extends the existing SubagentMonitor, DelegationManager, and AgentIsolation
modules with three critical governance capabilities:

1. Resource Budgets — token and API-call limits per subagent (prevents runaway)
2. Output Trust Scoring — score subagent outputs for safety/quality
3. Privilege Escalation Prevention — hard enforcement that no subagent can
   exceed its parent's permission boundary

Integrates with:
  - SubagentMonitor for spawn/deregister lifecycle and trust inheritance
  - TrustManager for trust score lookups
  - AuditLedger for governance event logging
  - ApprovalQueue for escalation to human when governance thresholds are breached
"""

import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

logger = logging.getLogger("agentshroud.security.subagent_governance")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


class GovernanceAction(str, Enum):
    """Action to take when a governance limit is hit."""

    ALLOW = "allow"  # Log and allow (monitor mode)
    WARN = "warn"  # Allow but flag for review
    DENY = "deny"  # Block the action
    ESCALATE = "escalate"  # Route to ApprovalQueue for human decision


@dataclass
class ResourceBudget:
    """Per-subagent resource limits."""

    max_tokens: int = 100_000  # Total input+output tokens
    max_api_calls: int = 50  # Total LLM API calls
    max_tool_calls: int = 200  # Total tool invocations
    max_egress_bytes: int = 10_485_760  # 10 MB outbound data
    max_runtime_seconds: int = 3600  # 1 hour wall-clock time
    on_exceed: GovernanceAction = GovernanceAction.DENY


@dataclass
class OutputTrustConfig:
    """Configuration for subagent output trust scoring."""

    min_trust_threshold: int = 50  # Minimum score to accept output (0-100)
    pii_check: bool = True  # Check output for PII leakage
    injection_check: bool = True  # Check output for prompt injection
    exfil_check: bool = True  # Check output for data exfiltration patterns
    on_low_trust: GovernanceAction = GovernanceAction.ESCALATE


@dataclass
class PrivilegePolicy:
    """Privilege escalation prevention policy."""

    strict_inheritance: bool = True  # Subagent trust <= parent trust (always)
    depth_penalty: int = 10  # Trust penalty per nesting level
    max_depth: int = 5  # Maximum delegation depth
    deny_tools: list[str] = field(
        default_factory=lambda: [
            "delegate_task",  # Prevent recursive delegation by default
            "memory",  # Subagents can't modify parent's memory
            "send_message",  # Subagents can't message users directly
            "cronjob",  # Subagents can't create scheduled jobs
        ]
    )
    on_escalation: GovernanceAction = GovernanceAction.DENY


@dataclass
class GovernanceConfig:
    """Top-level governance configuration."""

    enabled: bool = True
    mode: str = "enforce"  # "monitor" or "enforce"
    resource_budget: ResourceBudget = field(default_factory=ResourceBudget)
    output_trust: OutputTrustConfig = field(default_factory=OutputTrustConfig)
    privilege_policy: PrivilegePolicy = field(default_factory=PrivilegePolicy)


# ---------------------------------------------------------------------------
# Governance Events
# ---------------------------------------------------------------------------


class GovernanceEventType(str, Enum):
    BUDGET_WARNING = "budget_warning"
    BUDGET_EXCEEDED = "budget_exceeded"
    OUTPUT_LOW_TRUST = "output_low_trust"
    OUTPUT_PII_DETECTED = "output_pii_detected"
    OUTPUT_INJECTION_DETECTED = "output_injection_detected"
    PRIVILEGE_ESCALATION = "privilege_escalation"
    TOOL_DENIED = "tool_denied"
    DEPTH_EXCEEDED = "depth_exceeded"
    GOVERNANCE_OVERRIDE = "governance_override"


@dataclass
class GovernanceEvent:
    timestamp: float
    session_id: str
    agent_id: str
    event_type: GovernanceEventType
    action_taken: GovernanceAction
    details: str = ""
    parent_id: str = ""


# ---------------------------------------------------------------------------
# Resource Tracker
# ---------------------------------------------------------------------------


@dataclass
class ResourceUsage:
    """Tracks cumulative resource consumption for a single subagent."""

    tokens_used: int = 0
    api_calls: int = 0
    tool_calls: int = 0
    egress_bytes: int = 0
    start_time: float = field(default_factory=time.time)

    @property
    def runtime_seconds(self) -> float:
        return time.time() - self.start_time

    def to_dict(self) -> dict:
        return {
            "tokens_used": self.tokens_used,
            "api_calls": self.api_calls,
            "tool_calls": self.tool_calls,
            "egress_bytes": self.egress_bytes,
            "runtime_seconds": round(self.runtime_seconds, 1),
        }


# ---------------------------------------------------------------------------
# Output Trust Scorer
# ---------------------------------------------------------------------------


@dataclass
class OutputScore:
    """Result of scoring a subagent's output."""

    trust_score: int  # 0-100
    pii_detected: bool = False
    injection_detected: bool = False
    exfil_patterns: bool = False
    reasons: list[str] = field(default_factory=list)

    @property
    def acceptable(self) -> bool:
        return not self.pii_detected and not self.injection_detected and not self.exfil_patterns


# ---------------------------------------------------------------------------
# Subagent Governance Module
# ---------------------------------------------------------------------------


class SubagentGovernance:
    """Unified governance layer for subagent lifecycle.

    Wraps SubagentMonitor with resource budgets, output trust scoring,
    and privilege escalation prevention.

    Usage:
        gov = SubagentGovernance(GovernanceConfig())

        # Before spawning a subagent:
        gov.authorize_spawn(session_id, agent_id, parent_id, parent_trust, depth=1)

        # Before each tool call:
        gov.authorize_tool(session_id, agent_id, tool_name)

        # Record resource consumption:
        gov.record_tokens(session_id, agent_id, count=1500)
        gov.record_api_call(session_id, agent_id)
        gov.record_tool_call(session_id, agent_id, tool_name)

        # Score subagent output before returning to parent:
        score = gov.score_output(session_id, agent_id, output_text)

        # Cleanup:
        gov.deregister(session_id, agent_id)
    """

    def __init__(self, config: GovernanceConfig | None = None):
        self.config = config or GovernanceConfig()
        self._usage: dict[str, dict[str, ResourceUsage]] = {}  # session -> agent -> usage
        self._trust: dict[str, dict[str, int]] = {}  # session -> agent -> trust
        self._depth: dict[str, dict[str, int]] = {}  # session -> agent -> depth
        self._denied_tools: dict[str, dict[str, set]] = {}  # session -> agent -> denied tools
        self._events: list[GovernanceEvent] = []

    # -------------------------------------------------------------------
    # Spawn Authorization
    # -------------------------------------------------------------------

    def authorize_spawn(
        self,
        session_id: str,
        agent_id: str,
        parent_id: str,
        parent_trust: int,
        depth: int = 1,
    ) -> tuple[bool, str]:
        """Authorize a subagent spawn. Returns (allowed, reason)."""
        if not self.config.enabled:
            return True, "governance disabled"

        policy = self.config.privilege_policy

        # Check depth limit
        if depth > policy.max_depth:
            event = self._log_event(
                session_id,
                agent_id,
                GovernanceEventType.DEPTH_EXCEEDED,
                policy.on_escalation,
                f"depth={depth}, max={policy.max_depth}",
                parent_id=parent_id,
            )
            if self.config.mode == "enforce":
                return False, f"Delegation depth {depth} exceeds max {policy.max_depth}"

        # Calculate effective trust with depth penalty
        effective_trust = parent_trust - (policy.depth_penalty * depth)
        effective_trust = max(0, effective_trust)

        if policy.strict_inheritance:
            # Look up parent's effective trust (if parent is also a subagent)
            parent_effective = self._trust.get(session_id, {}).get(parent_id, parent_trust)
            effective_trust = min(effective_trust, parent_effective)

        # Initialize tracking
        self._usage.setdefault(session_id, {})[agent_id] = ResourceUsage()
        self._trust.setdefault(session_id, {})[agent_id] = effective_trust
        self._depth.setdefault(session_id, {})[agent_id] = depth
        self._denied_tools.setdefault(session_id, {})[agent_id] = set(policy.deny_tools)

        logger.info(
            "Subagent spawn authorized: session=%s agent=%s parent=%s "
            "trust=%d depth=%d denied_tools=%s",
            session_id,
            agent_id,
            parent_id,
            effective_trust,
            depth,
            policy.deny_tools,
        )
        return True, f"authorized, trust={effective_trust}, depth={depth}"

    # -------------------------------------------------------------------
    # Tool Authorization
    # -------------------------------------------------------------------

    def authorize_tool(
        self,
        session_id: str,
        agent_id: str,
        tool_name: str,
    ) -> tuple[bool, str]:
        """Check if a subagent is allowed to use a specific tool."""
        if not self.config.enabled:
            return True, "governance disabled"

        denied = self._denied_tools.get(session_id, {}).get(agent_id, set())
        if tool_name in denied:
            self._log_event(
                session_id,
                agent_id,
                GovernanceEventType.TOOL_DENIED,
                GovernanceAction.DENY,
                f"tool={tool_name} is in deny list for subagents",
            )
            if self.config.mode == "enforce":
                return False, f"Tool '{tool_name}' denied for subagents"

        # Check resource budget before tool call
        budget_ok, budget_reason = self._check_budget(session_id, agent_id, "tool_calls")
        if not budget_ok:
            return False, budget_reason

        return True, "authorized"

    # -------------------------------------------------------------------
    # Resource Recording
    # -------------------------------------------------------------------

    def record_tokens(self, session_id: str, agent_id: str, count: int) -> tuple[bool, str]:
        """Record token consumption. Returns (within_budget, message)."""
        usage = self._usage.get(session_id, {}).get(agent_id)
        if not usage:
            return True, "no tracking"
        usage.tokens_used += count
        return self._check_budget(session_id, agent_id, "tokens")

    def record_api_call(self, session_id: str, agent_id: str) -> tuple[bool, str]:
        """Record an LLM API call."""
        usage = self._usage.get(session_id, {}).get(agent_id)
        if not usage:
            return True, "no tracking"
        usage.api_calls += 1
        return self._check_budget(session_id, agent_id, "api_calls")

    def record_tool_call(self, session_id: str, agent_id: str, tool_name: str) -> tuple[bool, str]:
        """Record a tool invocation."""
        usage = self._usage.get(session_id, {}).get(agent_id)
        if not usage:
            return True, "no tracking"
        usage.tool_calls += 1
        return self._check_budget(session_id, agent_id, "tool_calls")

    def record_egress(self, session_id: str, agent_id: str, bytes_count: int) -> tuple[bool, str]:
        """Record outbound data volume."""
        usage = self._usage.get(session_id, {}).get(agent_id)
        if not usage:
            return True, "no tracking"
        usage.egress_bytes += bytes_count
        return self._check_budget(session_id, agent_id, "egress")

    # -------------------------------------------------------------------
    # Output Trust Scoring
    # -------------------------------------------------------------------

    def score_output(
        self,
        session_id: str,
        agent_id: str,
        output_text: str,
    ) -> OutputScore:
        """Score a subagent's output for safety and quality.

        In a full deployment, this would call the PII Sanitizer, PromptGuard,
        and EgressFilter modules. This implementation provides the framework
        and basic pattern matching.
        """
        config = self.config.output_trust
        score = 100
        reasons: list[str] = []

        # PII detection (simplified — real impl delegates to PII Sanitizer module)
        pii_detected = False
        if config.pii_check:
            pii_patterns = _check_pii_patterns(output_text)
            if pii_patterns:
                pii_detected = True
                score -= 30
                reasons.append(f"PII patterns detected: {', '.join(pii_patterns)}")

        # Injection detection (simplified — real impl delegates to PromptGuard)
        injection_detected = False
        if config.injection_check:
            injection_patterns = _check_injection_patterns(output_text)
            if injection_patterns:
                injection_detected = True
                score -= 40
                reasons.append(f"Injection patterns detected: {', '.join(injection_patterns)}")

        # Exfiltration pattern detection
        exfil_patterns = False
        if config.exfil_check:
            exfil_matches = _check_exfil_patterns(output_text)
            if exfil_matches:
                exfil_patterns = True
                score -= 25
                reasons.append(f"Exfiltration patterns: {', '.join(exfil_matches)}")

        # Trust penalty from governance context
        agent_trust = self._trust.get(session_id, {}).get(agent_id, 100)
        if agent_trust < 50:
            score -= (50 - agent_trust) // 2
            reasons.append(f"Low agent trust: {agent_trust}")

        score = max(0, min(100, score))

        result = OutputScore(
            trust_score=score,
            pii_detected=pii_detected,
            injection_detected=injection_detected,
            exfil_patterns=exfil_patterns,
            reasons=reasons,
        )

        # Log governance events for flagged outputs
        if pii_detected:
            self._log_event(
                session_id,
                agent_id,
                GovernanceEventType.OUTPUT_PII_DETECTED,
                config.on_low_trust,
                f"PII in output: {', '.join(reasons)}",
            )
        if injection_detected:
            self._log_event(
                session_id,
                agent_id,
                GovernanceEventType.OUTPUT_INJECTION_DETECTED,
                config.on_low_trust,
                f"Injection in output: {', '.join(reasons)}",
            )
        if score < config.min_trust_threshold:
            self._log_event(
                session_id,
                agent_id,
                GovernanceEventType.OUTPUT_LOW_TRUST,
                config.on_low_trust,
                f"Output trust score {score} < threshold {config.min_trust_threshold}",
            )

        return result

    # -------------------------------------------------------------------
    # Lifecycle
    # -------------------------------------------------------------------

    def deregister(self, session_id: str, agent_id: str) -> Optional[ResourceUsage]:
        """Remove a subagent from governance tracking. Returns final usage."""
        usage = self._usage.get(session_id, {}).pop(agent_id, None)
        self._trust.get(session_id, {}).pop(agent_id, None)
        self._depth.get(session_id, {}).pop(agent_id, None)
        self._denied_tools.get(session_id, {}).pop(agent_id, None)
        if usage:
            logger.info(
                "Subagent deregistered: session=%s agent=%s usage=%s",
                session_id,
                agent_id,
                usage.to_dict(),
            )
        return usage

    def get_usage(self, session_id: str, agent_id: str) -> Optional[ResourceUsage]:
        """Get current resource usage for a subagent."""
        return self._usage.get(session_id, {}).get(agent_id)

    def get_governance_events(
        self,
        session_id: str,
        agent_id: Optional[str] = None,
        event_type: Optional[GovernanceEventType] = None,
    ) -> list[GovernanceEvent]:
        """Retrieve governance audit events with optional filters."""
        events = [e for e in self._events if e.session_id == session_id]
        if agent_id:
            events = [e for e in events if e.agent_id == agent_id]
        if event_type:
            events = [e for e in events if e.event_type == event_type]
        return events

    def get_summary(self, session_id: str) -> dict:
        """Get a summary of all subagent governance state for a session."""
        agents = {}
        for agent_id, usage in self._usage.get(session_id, {}).items():
            agents[agent_id] = {
                "usage": usage.to_dict(),
                "trust": self._trust.get(session_id, {}).get(agent_id, 0),
                "depth": self._depth.get(session_id, {}).get(agent_id, 0),
                "denied_tools": sorted(self._denied_tools.get(session_id, {}).get(agent_id, set())),
            }
        violations = [
            e
            for e in self._events
            if e.session_id == session_id
            and e.action_taken in (GovernanceAction.DENY, GovernanceAction.ESCALATE)
        ]
        return {
            "active_agents": len(agents),
            "agents": agents,
            "violations": len(violations),
            "total_events": len([e for e in self._events if e.session_id == session_id]),
        }

    # -------------------------------------------------------------------
    # Internal helpers
    # -------------------------------------------------------------------

    def _check_budget(
        self,
        session_id: str,
        agent_id: str,
        resource_type: str,
    ) -> tuple[bool, str]:
        """Check if a resource budget is exceeded."""
        usage = self._usage.get(session_id, {}).get(agent_id)
        if not usage:
            return True, "no tracking"

        budget = self.config.resource_budget
        checks = {
            "tokens": (usage.tokens_used, budget.max_tokens, "tokens"),
            "api_calls": (usage.api_calls, budget.max_api_calls, "API calls"),
            "tool_calls": (usage.tool_calls, budget.max_tool_calls, "tool calls"),
            "egress": (usage.egress_bytes, budget.max_egress_bytes, "egress bytes"),
            "runtime": (usage.runtime_seconds, budget.max_runtime_seconds, "runtime seconds"),
        }

        if resource_type not in checks:
            return True, "unknown resource type"

        current, limit, label = checks[resource_type]

        # Warning at 80%
        if current >= limit * 0.8 and current < limit:
            self._log_event(
                session_id,
                agent_id,
                GovernanceEventType.BUDGET_WARNING,
                GovernanceAction.WARN,
                f"{label}: {current}/{limit} (80% threshold)",
            )

        # Hard limit
        if current >= limit:
            self._log_event(
                session_id,
                agent_id,
                GovernanceEventType.BUDGET_EXCEEDED,
                budget.on_exceed,
                f"{label}: {current}/{limit} — EXCEEDED",
            )
            if self.config.mode == "enforce" and budget.on_exceed == GovernanceAction.DENY:
                return False, f"Resource budget exceeded: {label} {current}/{limit}"

        return True, f"{label}: {current}/{limit}"

    def _log_event(
        self,
        session_id: str,
        agent_id: str,
        event_type: GovernanceEventType,
        action: GovernanceAction,
        details: str = "",
        parent_id: str = "",
    ) -> GovernanceEvent:
        event = GovernanceEvent(
            timestamp=time.time(),
            session_id=session_id,
            agent_id=agent_id,
            event_type=event_type,
            action_taken=action,
            details=details,
            parent_id=parent_id,
        )
        self._events.append(event)
        logger.info(
            "Governance event: %s %s %s action=%s — %s",
            session_id,
            agent_id,
            event_type.value,
            action.value,
            details,
        )
        return event


# ---------------------------------------------------------------------------
# Pattern detection helpers (simplified — production uses full modules)
# ---------------------------------------------------------------------------

import re

_PII_PATTERNS = {
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "credit_card": re.compile(r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"),
    "api_key": re.compile(r"\b(sk-|AKIA|AIzaSy|ghp_|gho_|github_pat_)[A-Za-z0-9_-]{10,}\b"),
}

_INJECTION_PATTERNS = {
    "system_prompt_override": re.compile(
        r"(ignore previous|forget your|you are now|system prompt|override instructions)",
        re.IGNORECASE,
    ),
    "role_injection": re.compile(
        r'(\{"role"\s*:\s*"system"|\[INST\]|<\|im_start\|>system)',
        re.IGNORECASE,
    ),
}

_EXFIL_PATTERNS = {
    "base64_block": re.compile(r"[A-Za-z0-9+/]{100,}={0,2}"),
    "hex_block": re.compile(r"[0-9a-fA-F]{64,}"),
    "webhook_url": re.compile(
        r"https?://[a-z0-9.-]*(webhook|hook|callback|exfil|receive)[a-z0-9.-]*/",
        re.IGNORECASE,
    ),
}


def _check_pii_patterns(text: str) -> list[str]:
    """Check text for PII patterns. Returns list of pattern names found."""
    return [name for name, pattern in _PII_PATTERNS.items() if pattern.search(text)]


def _check_injection_patterns(text: str) -> list[str]:
    """Check text for prompt injection patterns."""
    return [name for name, pattern in _INJECTION_PATTERNS.items() if pattern.search(text)]


def _check_exfil_patterns(text: str) -> list[str]:
    """Check text for data exfiltration patterns."""
    return [name for name, pattern in _EXFIL_PATTERNS.items() if pattern.search(text)]
