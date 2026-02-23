# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""MCP Audit — tool-call-specific audit trail integrated with hash chain.

Every MCP tool call and response is logged with full parameters (PII redacted),
included in the existing cryptographic hash chain, and queryable for reports.
"""


import hashlib
import logging
import time
import uuid
from dataclasses import dataclass
from typing import Any, Optional

logger = logging.getLogger("agentshroud.proxy.mcp_audit")


@dataclass
class MCPAuditEntry:
    """A single MCP tool call audit entry."""

    id: str
    timestamp: float
    direction: str  # "tool_call" or "tool_result"
    agent_id: str
    server_name: str
    tool_name: str
    # For tool_call
    parameters: Optional[dict[str, Any]] = None
    # For tool_result
    result_summary: str = ""
    success: bool = True
    error_message: str = ""
    # Timing
    duration_ms: float = 0.0
    # Security
    findings_count: int = 0
    threat_level: str = "none"
    blocked: bool = False
    block_reason: str = ""
    pii_redacted: bool = False
    # Hash chain
    content_hash: str = ""
    previous_hash: str = ""
    chain_hash: str = ""


class MCPAuditTrail:
    """Audit trail for MCP tool calls, integrated with SHA-256 hash chain."""

    GENESIS_HASH = "0" * 64

    MAX_PENDING_CALLS = 1000  # Prevent unbounded growth

    def __init__(self):
        self._entries: list[MCPAuditEntry] = []
        self._last_hash: str = self.GENESIS_HASH
        self._call_start_times: dict[str, float] = {}

    def _compute_chain_hash(
        self, content: str, direction: str, timestamp: float
    ) -> tuple[str, str]:
        """Compute hash chain values. Returns (content_hash, chain_hash)."""
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        chain_input = f"{self._last_hash}:{content_hash}:{direction}:{timestamp}"
        chain_hash = hashlib.sha256(chain_input.encode()).hexdigest()
        return content_hash, chain_hash

    def start_call(self, call_id: str) -> None:
        """Record the start time of a tool call for duration tracking."""
        # Evict stale entries (>5 min old) if we hit the limit
        if len(self._call_start_times) >= self.MAX_PENDING_CALLS:
            now = time.time()
            stale = [k for k, v in self._call_start_times.items() if now - v > 300]
            for k in stale:
                del self._call_start_times[k]
            # If still over limit after eviction, drop oldest
            if len(self._call_start_times) >= self.MAX_PENDING_CALLS:
                oldest = min(self._call_start_times, key=self._call_start_times.get)
                del self._call_start_times[oldest]
        self._call_start_times[call_id] = time.time()

    def log_tool_call(
        self,
        agent_id: str,
        server_name: str,
        tool_name: str,
        parameters: dict[str, Any],
        findings_count: int = 0,
        threat_level: str = "none",
        blocked: bool = False,
        block_reason: str = "",
        pii_redacted: bool = False,
        call_id: Optional[str] = None,
    ) -> MCPAuditEntry:
        """Log an outgoing MCP tool call."""
        entry_id = call_id or str(uuid.uuid4())
        now = time.time()

        # Build content string for hashing (deterministic)
        content = f"tool_call:{server_name}:{tool_name}:{agent_id}:{now}"
        content_hash, chain_hash = self._compute_chain_hash(content, "tool_call", now)

        entry = MCPAuditEntry(
            id=entry_id,
            timestamp=now,
            direction="tool_call",
            agent_id=agent_id,
            server_name=server_name,
            tool_name=tool_name,
            parameters=parameters,
            findings_count=findings_count,
            threat_level=threat_level,
            blocked=blocked,
            block_reason=block_reason,
            pii_redacted=pii_redacted,
            content_hash=content_hash,
            previous_hash=self._last_hash,
            chain_hash=chain_hash,
        )

        self._entries.append(entry)
        self._last_hash = chain_hash
        self.start_call(entry_id)

        logger.info(
            "MCP audit: %s %s/%s by %s [%s] %s",
            "BLOCKED" if blocked else "ALLOWED",
            server_name,
            tool_name,
            agent_id,
            threat_level,
            block_reason or "ok",
        )
        return entry

    def log_tool_result(
        self,
        call_id: str,
        agent_id: str,
        server_name: str,
        tool_name: str,
        success: bool = True,
        error_message: str = "",
        result_summary: str = "",
        findings_count: int = 0,
        threat_level: str = "none",
        pii_redacted: bool = False,
    ) -> MCPAuditEntry:
        """Log an incoming MCP tool result."""
        now = time.time()
        duration_ms = 0.0
        if call_id in self._call_start_times:
            duration_ms = (now - self._call_start_times.pop(call_id)) * 1000

        content = f"tool_result:{server_name}:{tool_name}:{agent_id}:{now}"
        content_hash, chain_hash = self._compute_chain_hash(content, "tool_result", now)

        entry = MCPAuditEntry(
            id=str(uuid.uuid4()),
            timestamp=now,
            direction="tool_result",
            agent_id=agent_id,
            server_name=server_name,
            tool_name=tool_name,
            success=success,
            error_message=error_message,
            result_summary=result_summary[:500],  # Truncate long results
            duration_ms=duration_ms,
            findings_count=findings_count,
            threat_level=threat_level,
            pii_redacted=pii_redacted,
            content_hash=content_hash,
            previous_hash=self._last_hash,
            chain_hash=chain_hash,
        )

        self._entries.append(entry)
        self._last_hash = chain_hash

        logger.info(
            "MCP audit result: %s %s/%s [%.1fms] %s",
            "OK" if success else "ERROR",
            server_name,
            tool_name,
            duration_ms,
            error_message or "success",
        )
        return entry

    def verify_chain(self) -> tuple[bool, str]:
        """Verify integrity of the MCP audit hash chain."""
        if not self._entries:
            return True, "Empty chain"

        prev_hash = self.GENESIS_HASH
        for i, entry in enumerate(self._entries):
            if entry.previous_hash != prev_hash:
                return False, f"Entry {i} ({entry.id}): previous_hash mismatch"

            content = f"{entry.direction}:{entry.server_name}:{entry.tool_name}:{entry.agent_id}:{entry.timestamp}"
            expected_content_hash = hashlib.sha256(content.encode()).hexdigest()
            if entry.content_hash != expected_content_hash:
                return False, f"Entry {i} ({entry.id}): content_hash mismatch"

            chain_input = f"{entry.previous_hash}:{entry.content_hash}:{entry.direction}:{entry.timestamp}"
            expected_chain_hash = hashlib.sha256(chain_input.encode()).hexdigest()
            if entry.chain_hash != expected_chain_hash:
                return False, f"Entry {i} ({entry.id}): chain_hash mismatch (tampered)"

            prev_hash = entry.chain_hash

        return True, f"Chain valid ({len(self._entries)} entries)"

    @property
    def entries(self) -> list[MCPAuditEntry]:
        return list(self._entries)

    @property
    def last_hash(self) -> str:
        return self._last_hash

    def __len__(self) -> int:
        return len(self._entries)

    def get_entries_for_agent(self, agent_id: str) -> list[MCPAuditEntry]:
        return [e for e in self._entries if e.agent_id == agent_id]

    def get_entries_for_server(self, server_name: str) -> list[MCPAuditEntry]:
        return [e for e in self._entries if e.server_name == server_name]

    def get_entries_for_tool(self, tool_name: str) -> list[MCPAuditEntry]:
        return [e for e in self._entries if e.tool_name == tool_name]

    def get_blocked_entries(self) -> list[MCPAuditEntry]:
        return [e for e in self._entries if e.blocked]

    def get_failed_entries(self) -> list[MCPAuditEntry]:
        return [
            e for e in self._entries if not e.success and e.direction == "tool_result"
        ]

    def generate_report(self) -> dict[str, Any]:
        """Generate an MCP audit report summary."""
        tool_calls = [e for e in self._entries if e.direction == "tool_call"]
        tool_results = [e for e in self._entries if e.direction == "tool_result"]
        blocked = self.get_blocked_entries()

        # Tool usage stats
        tool_usage: dict[str, int] = {}
        for e in tool_calls:
            key = f"{e.server_name}/{e.tool_name}"
            tool_usage[key] = tool_usage.get(key, 0) + 1

        # Average duration
        durations = [e.duration_ms for e in tool_results if e.duration_ms > 0]
        avg_duration = sum(durations) / len(durations) if durations else 0

        valid, msg = self.verify_chain()

        return {
            "total_entries": len(self._entries),
            "tool_calls": len(tool_calls),
            "tool_results": len(tool_results),
            "blocked": len(blocked),
            "failed": len(self.get_failed_entries()),
            "tool_usage": tool_usage,
            "avg_duration_ms": round(avg_duration, 1),
            "chain_valid": valid,
            "chain_message": msg,
            "pii_redactions": sum(1 for e in self._entries if e.pii_redacted),
            "unique_agents": len(set(e.agent_id for e in self._entries)),
            "unique_servers": len(set(e.server_name for e in self._entries)),
        }
