# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Sub-agent Oversight — track, audit, and optionally restrict sub-agent activity.

Default mode: monitor (observe and audit everything, block nothing).
Enforce mode: hard limits on concurrency and trust-gated tool access.
"""

import logging
import time
from dataclasses import dataclass
from enum import Enum
from typing import Optional

logger = logging.getLogger(__name__)


class SubagentEventType(str, Enum):
    SPAWNED = "spawned"
    TERMINATED = "terminated"
    KILLED = "killed"
    TOOL_USED = "tool_used"
    TRUST_VIOLATION = "trust_violation"
    LIMIT_EXCEEDED = "limit_exceeded"


@dataclass
class SubagentEvent:
    timestamp: float
    session_id: str
    agent_id: str
    event_type: SubagentEventType
    details: str = ""


@dataclass
class SubagentInfo:
    agent_id: str
    parent_id: str
    session_id: str
    parent_trust: int
    effective_trust: int
    spawn_time: float


@dataclass
class ToolCheckResult:
    allowed: bool
    flagged: bool
    reason: str = ""


@dataclass
class SubagentMonitorConfig:
    mode: str = "monitor"  # "monitor" or "enforce"
    max_concurrent_per_session: int = 20
    inherit_trust: bool = True


class SubagentMonitor:
    def __init__(self, config: SubagentMonitorConfig):
        self.config = config
        self._active: dict[str, dict[str, SubagentInfo]] = (
            {}
        )  # session -> {agent_id: info}
        self._events: list[SubagentEvent] = []

    def register_spawn(
        self, session_id: str, agent_id: str, parent_id: str, parent_trust: int
    ) -> SubagentInfo:
        if session_id not in self._active:
            self._active[session_id] = {}

        current = len(self._active[session_id])
        if current >= self.config.max_concurrent_per_session:
            self._log_event(
                session_id,
                agent_id,
                SubagentEventType.LIMIT_EXCEEDED,
                f"concurrent={current+1}, limit={self.config.max_concurrent_per_session}",
            )
            if self.config.mode == "enforce":
                raise RuntimeError(
                    f"Concurrent sub-agent limit reached ({self.config.max_concurrent_per_session})"
                )

        effective_trust = parent_trust if self.config.inherit_trust else parent_trust
        # Check if parent is itself a sub-agent — inherit minimum
        if parent_id in self._active.get(session_id, {}):
            parent_info = self._active[session_id][parent_id]
            effective_trust = min(parent_trust, parent_info.effective_trust)

        info = SubagentInfo(
            agent_id=agent_id,
            parent_id=parent_id,
            session_id=session_id,
            parent_trust=parent_trust,
            effective_trust=effective_trust,
            spawn_time=time.time(),
        )
        self._active[session_id][agent_id] = info
        self._log_event(
            session_id,
            agent_id,
            SubagentEventType.SPAWNED,
            f"parent={parent_id}, trust={effective_trust}",
        )
        return info

    def deregister(self, session_id: str, agent_id: str):
        if session_id in self._active:
            self._active[session_id].pop(agent_id, None)
        self._log_event(session_id, agent_id, SubagentEventType.TERMINATED)

    def get_active(self, session_id: str) -> list[SubagentInfo]:
        return list(self._active.get(session_id, {}).values())

    def check_tool_usage(
        self, session_id: str, agent_id: str, tool_name: str, required_trust: int = 0
    ) -> ToolCheckResult:
        info = self._active.get(session_id, {}).get(agent_id)
        flagged = False
        reason = ""

        if info and info.effective_trust < required_trust:
            flagged = True
            reason = f"trust {info.effective_trust} < required {required_trust} for {tool_name}"
            self._log_event(
                session_id, agent_id, SubagentEventType.TRUST_VIOLATION, reason
            )

        self._log_event(
            session_id,
            agent_id,
            SubagentEventType.TOOL_USED,
            f"tool={tool_name}, required_trust={required_trust}",
        )

        if self.config.mode == "enforce" and flagged:
            return ToolCheckResult(allowed=False, flagged=True, reason=reason)

        return ToolCheckResult(allowed=True, flagged=flagged, reason=reason)

    def kill_all(self, session_id: str) -> int:
        agents = self._active.get(session_id, {})
        count = len(agents)
        for agent_id in list(agents.keys()):
            self._log_event(session_id, agent_id, SubagentEventType.KILLED, "kill_all")
        self._active[session_id] = {}
        return count

    def kill_agent(self, session_id: str, agent_id: str):
        if session_id in self._active:
            self._active[session_id].pop(agent_id, None)
        self._log_event(session_id, agent_id, SubagentEventType.KILLED, "kill_agent")

    def get_audit_log(
        self, session_id: str, agent_id: Optional[str] = None
    ) -> list[SubagentEvent]:
        events = [e for e in self._events if e.session_id == session_id]
        if agent_id:
            events = [e for e in events if e.agent_id == agent_id]
        return events

    def get_flagged_events(self, session_id: str) -> list[SubagentEvent]:
        flagged_types = {
            SubagentEventType.TRUST_VIOLATION,
            SubagentEventType.LIMIT_EXCEEDED,
        }
        return [
            e
            for e in self._events
            if e.session_id == session_id and e.event_type in flagged_types
        ]

    def _log_event(
        self,
        session_id: str,
        agent_id: str,
        event_type: SubagentEventType,
        details: str = "",
    ):
        event = SubagentEvent(
            timestamp=time.time(),
            session_id=session_id,
            agent_id=agent_id,
            event_type=event_type,
            details=details,
        )
        self._events.append(event)
        logger.info(
            "Subagent event: %s %s %s — %s", session_id, agent_id, event_type, details
        )
