# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""MCP Permissions — per-tool permission system with sensible defaults.

Design: default-allow with escalation for dangerous operations.
Trust levels map to permission ceilings, not floors.
"""


import fnmatch
import json
import logging
import os
import re
import time
from dataclasses import dataclass
from typing import Optional

from gateway.security.rbac_config import RBACConfig

from .mcp_config import MCPProxyConfig, MCPServerConfig, PermissionLevel

logger = logging.getLogger("agentshroud.proxy.mcp_permissions")

# Trust level → maximum permission allowed
TRUST_PERMISSION_MAP: dict[int, PermissionLevel] = {
    0: PermissionLevel.READ,
    1: PermissionLevel.WRITE,
    2: PermissionLevel.EXECUTE,
    3: PermissionLevel.ADMIN,
}

# Tools that are inherently sensitive (pattern-matched)
SENSITIVE_TOOL_PATTERNS: list[str] = [
    "*shell*",
    "*exec*",
    "*command*",
    "*rm_*",
    "*delete*",
    "*sudo*",
    "*admin*",
    "*drop_*",
    "*truncate*",
]

# Tools that are inherently read-only (pattern-matched)
READ_ONLY_PATTERNS: list[str] = [
    "*get*",
    "*list*",
    "*read*",
    "*search*",
    "*query*",
    "*describe*",
    "*show*",
    "*info*",
    "*status*",
    "*health*",
    "*fetch*",
    "*find*",
    "*count*",
    "*browse*",
]

# Admin-private tool patterns. Non-owner users cannot invoke these.
PRIVATE_TOOL_PATTERNS: list[str] = [
    "*gmail*",
    "*icloud*",
    "*homeassistant*",
    "*home_assistant*",
    "*financial*",
    "*bank*",
    "*wallet*",
    "*contacts*",
    "*calendar*",
    "*messages*",
    "*mail*",
    "*smtp*",
    "*imap*",
    "*memory_search*",
    "*memory.search*",
    "*memory-search*",
    "*memory_get*",
    "*memory.get*",
    "*memory-get*",
    "*memory_write*",
    "*memory.write*",
    "*memory-write*",
    "*memory_update*",
    "*memory.update*",
    "*memory-update*",
    "*memory_delete*",
    "*memory.delete*",
    "*memory-delete*",
    "*memory_list*",
    "*memory.list*",
    "*memory-list*",
    "memory_*",
    "memory.*",
    "memory-*",
]

# Redaction patterns for admin-private content that must never leak to
# non-owner sessions, even through "shared" tool results.
PRIVATE_DATA_PATTERNS: list[str] = [
    r"\b(?:gmail|google\s*mail)\b",
    r"\b(?:icloud|apple\s*id)\b",
    r"\b(?:home\s*assistant|homeassistant)\b",
    r"\b(?:bank\s*account|routing\s*number|account\s*number)\b",
    r"\b(?:financial\s*data|wallet|credit\s*limit)\b",
    r"\bMEMORY\.md\b",
    r"#\s*Session\s+Memory\s+for\s+User\b",
    r"/home/node/\.openclaw/workspace/(?:memory|MEMORY\.md)\b",
    r"/home/node/\.openclaw/workspace/memory/",
    r"/home/node/\.agentshroud/workspace/(?:memory|MEMORY\.md)\b",
    r"/home/node/\.agentshroud/workspace/memory/",
    r"/app/data/sessions/",
    r"/home/node/agentshroud/gateway-data/sessions/",
    r"/app/data/contributors/",
    r"/data/bot-workspace/memory/contributors/",
    r"/home/node/\.openclaw/workspace/memory/contributors/",
    r"/home/node/agentshroud/gateway-data/contributors/",
    r"/home/node/agentshroud/gateway-data/collaborator_activity\.jsonl\b",
    r"/app/data/collaborator_activity\.jsonl\b",
]


@dataclass
class PermissionCheck:
    """Result of a permission check."""

    allowed: bool
    reason: str = ""
    required_level: Optional[PermissionLevel] = None
    agent_trust_level: int = 0
    rate_limited: bool = False
    logged_only: bool = False  # True = allowed but flagged for audit


@dataclass
class RateLimitEntry:
    """Track rate limit state for a tool+agent combo."""

    count: int = 0
    window_start: float = 0.0
    window_seconds: float = 60.0


@dataclass
class PrivateAccessAttempt:
    """Audit signal for blocked admin-private tool access attempts."""

    timestamp: float
    agent_id: str
    server_name: str
    tool_name: str
    matched_pattern: str
    reason: str


@dataclass
class PrivateRedactionEvent:
    """Audit signal when admin-private data is redacted from tool results."""

    timestamp: float
    agent_id: str
    server_name: str
    tool_name: str
    redaction_count: int


class MCPPermissionManager:
    """Manages permissions for MCP tool calls.

    Default-allow philosophy: tools work unless there is a specific reason to block.
    """

    MAX_RATE_LIMIT_ENTRIES = 10000  # Prevent unbounded growth

    def __init__(self, config: Optional[MCPProxyConfig] = None):
        self.config = config or MCPProxyConfig()
        self._rate_limits: dict[str, RateLimitEntry] = {}
        self._trust_levels: dict[str, int] = {}  # agent_id → trust level
        self._owner_user_id = RBACConfig().owner_user_id
        self._private_tool_patterns = list(PRIVATE_TOOL_PATTERNS)
        self._private_data_patterns = list(PRIVATE_DATA_PATTERNS)
        self._compiled_private_data_patterns: list[tuple[str, re.Pattern[str]]] = []
        self._private_access_attempts: list[PrivateAccessAttempt] = []
        self._private_redaction_events: list[PrivateRedactionEvent] = []
        self._max_private_access_attempts = 2000
        self._privacy_policy_status: dict[str, object] = {
            "path": os.environ.get(
                "AGENTSHROUD_PRIVACY_POLICY_FILE", "/app/data/privacy_policy.json"
            ),
            "loaded": False,
            "loaded_at": None,
            "error": "",
        }
        self._load_privacy_policy()
        self._recompile_private_data_patterns()

    def _recompile_private_data_patterns(self) -> None:
        """Compile private data patterns once for efficient repeated use."""
        compiled: list[tuple[str, re.Pattern[str]]] = []
        for pattern in self._private_data_patterns:
            try:
                compiled.append((pattern, re.compile(pattern, re.IGNORECASE)))
            except re.error:
                pass
        self._compiled_private_data_patterns = compiled

    def _load_privacy_policy(self) -> None:
        """Load optional admin-private tool patterns from policy file."""
        policy_path = str(self._privacy_policy_status["path"])
        if not os.path.exists(policy_path):
            self._privacy_policy_status.update(
                {"loaded": False, "loaded_at": None, "error": "policy file not found"}
            )
            return
        try:
            with open(policy_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            custom_patterns = data.get("admin_private_tool_patterns", [])
            if isinstance(custom_patterns, list):
                self._private_tool_patterns = [
                    str(p).lower() for p in custom_patterns if str(p).strip()
                ]
                logger.info(
                    "Loaded %d admin-private tool patterns from privacy policy",
                    len(self._private_tool_patterns),
                )
            private_data_patterns = data.get("admin_private_data_patterns", [])
            if isinstance(private_data_patterns, list) and private_data_patterns:
                self._private_data_patterns = [
                    str(p) for p in private_data_patterns if str(p).strip()
                ]
                logger.info(
                    "Loaded %d admin-private data patterns from privacy policy",
                    len(self._private_data_patterns),
                )
                self._recompile_private_data_patterns()
            self._privacy_policy_status.update(
                {"loaded": True, "loaded_at": time.time(), "error": ""}
            )
        except Exception as exc:
            logger.warning("Failed to load privacy policy from %s: %s", policy_path, exc)
            self._privacy_policy_status.update(
                {"loaded": False, "loaded_at": None, "error": str(exc)}
            )

    def _record_private_access_attempt(
        self,
        agent_id: str,
        server_name: str,
        tool_name: str,
        matched_pattern: str,
        reason: str,
    ) -> None:
        """Record blocked private-tool access attempts for SOC/audit views."""
        self._private_access_attempts.append(
            PrivateAccessAttempt(
                timestamp=time.time(),
                agent_id=agent_id,
                server_name=server_name,
                tool_name=tool_name,
                matched_pattern=matched_pattern,
                reason=reason,
            )
        )
        if len(self._private_access_attempts) > self._max_private_access_attempts:
            self._private_access_attempts = self._private_access_attempts[
                -self._max_private_access_attempts :
            ]

    def get_private_access_events(self, limit: int = 100) -> list[dict]:
        """Return recent blocked private-tool attempts for auditing."""
        if limit <= 0:
            return []
        return [
            {
                "timestamp": e.timestamp,
                "agent_id": e.agent_id,
                "server_name": e.server_name,
                "tool_name": e.tool_name,
                "matched_pattern": e.matched_pattern,
                "reason": e.reason,
            }
            for e in self._private_access_attempts[-limit:]
        ]

    def get_private_access_summary(self, limit: int = 500) -> dict:
        """Aggregate recent private-tool violations for SOC reporting."""
        events = self.get_private_access_events(limit=limit)
        by_agent: dict[str, int] = {}
        by_tool: dict[str, int] = {}
        for evt in events:
            by_agent[evt["agent_id"]] = by_agent.get(evt["agent_id"], 0) + 1
            by_tool[evt["tool_name"]] = by_tool.get(evt["tool_name"], 0) + 1
        return {
            "total": len(events),
            "by_agent": by_agent,
            "by_tool": by_tool,
        }

    def record_private_data_redaction(
        self,
        agent_id: str,
        server_name: str,
        tool_name: str,
        redaction_count: int = 1,
    ) -> None:
        """Record admin-private data redaction event for compliance audit."""
        self._private_redaction_events.append(
            PrivateRedactionEvent(
                timestamp=time.time(),
                agent_id=agent_id,
                server_name=server_name,
                tool_name=tool_name,
                redaction_count=max(1, int(redaction_count or 1)),
            )
        )
        if len(self._private_redaction_events) > self._max_private_access_attempts:
            self._private_redaction_events = self._private_redaction_events[
                -self._max_private_access_attempts :
            ]

    def get_private_redaction_events(self, limit: int = 100) -> list[dict]:
        """Return recent private-data redaction events."""
        if limit <= 0:
            return []
        return [
            {
                "timestamp": e.timestamp,
                "agent_id": e.agent_id,
                "server_name": e.server_name,
                "tool_name": e.tool_name,
                "redaction_count": e.redaction_count,
            }
            for e in self._private_redaction_events[-limit:]
        ]

    def get_private_redaction_summary(self, limit: int = 500) -> dict:
        """Aggregate recent private-data redaction events."""
        events = self.get_private_redaction_events(limit=limit)
        by_agent: dict[str, int] = {}
        by_tool: dict[str, int] = {}
        total_redactions = 0
        for evt in events:
            by_agent[evt["agent_id"]] = by_agent.get(evt["agent_id"], 0) + 1
            by_tool[evt["tool_name"]] = by_tool.get(evt["tool_name"], 0) + 1
            total_redactions += int(evt.get("redaction_count", 0) or 0)
        return {
            "events": len(events),
            "total_redactions": total_redactions,
            "by_agent": by_agent,
            "by_tool": by_tool,
        }

    def get_private_data_patterns(self) -> list[str]:
        """Return configured admin-private data redaction patterns."""
        return list(self._private_data_patterns)

    def get_privacy_policy_status(self) -> dict[str, object]:
        """Return privacy policy file load status for dashboard/audit APIs."""
        return dict(self._privacy_policy_status)

    def set_trust_level(self, agent_id: str, level: int) -> None:
        """Set trust level for an agent."""
        self._trust_levels[agent_id] = max(0, min(3, level))

    def get_trust_level(self, agent_id: str) -> int:
        """Get trust level, defaulting to 1 (write) for unknown agents."""
        return self._trust_levels.get(agent_id, 1)

    def infer_permission_level(
        self, tool_name: str, server_config: Optional[MCPServerConfig] = None
    ) -> PermissionLevel:
        """Infer the permission level needed for a tool based on its name.

        Checks explicit config first, then falls back to pattern matching.
        """
        # Check explicit tool config first
        if server_config and tool_name in server_config.tools:
            return server_config.tools[tool_name].permission_level

        # Pattern match against known sensitive tools
        lower_name = tool_name.lower()
        for pattern in SENSITIVE_TOOL_PATTERNS:
            if fnmatch.fnmatch(lower_name, pattern):
                return PermissionLevel.EXECUTE

        # Pattern match against known read-only tools
        for pattern in READ_ONLY_PATTERNS:
            if fnmatch.fnmatch(lower_name, pattern):
                return PermissionLevel.READ

        # Default: WRITE level (generous but not unrestricted)
        return PermissionLevel.WRITE

    def check_agent_server_access(self, agent_id: str, server_name: str) -> PermissionCheck:
        """Check if an agent can access a server at all."""
        server_config = self.config.servers.get(server_name)
        if not server_config:
            # Unknown server — allow but log
            return PermissionCheck(
                allowed=True, reason="Unknown server, default allow", logged_only=True
            )

        if not server_config.enabled:
            return PermissionCheck(allowed=False, reason=f"Server {server_name} is disabled")

        # Check denylist first
        if server_config.denied_agents and agent_id in server_config.denied_agents:
            return PermissionCheck(
                allowed=False,
                reason=f"Agent {agent_id} denied for server {server_name}",
            )

        # Check allowlist (empty = all allowed)
        if server_config.allowed_agents and agent_id not in server_config.allowed_agents:
            return PermissionCheck(
                allowed=False,
                reason=f"Agent {agent_id} not in allowlist for {server_name}",
            )

        # Check minimum trust level
        trust_level = self.get_trust_level(agent_id)
        if trust_level < server_config.min_trust_level:
            return PermissionCheck(
                allowed=False,
                reason=f"Trust level {trust_level} < required {server_config.min_trust_level}",
                agent_trust_level=trust_level,
            )

        return PermissionCheck(allowed=True, agent_trust_level=trust_level)

    def check_tool_permission(
        self,
        agent_id: str,
        server_name: str,
        tool_name: str,
    ) -> PermissionCheck:
        """Check if an agent can call a specific tool.

        Default-allow: only blocks if trust level is clearly insufficient
        for a known-dangerous operation.
        """
        trust_level = self.get_trust_level(agent_id)
        lower_name = tool_name.lower()

        # Hard data-isolation boundary: admin-private tools are owner-only.
        if str(agent_id) != str(self._owner_user_id):
            for pattern in self._private_tool_patterns:
                if fnmatch.fnmatch(lower_name, pattern):
                    reason = (
                        f"Tool {tool_name} is admin-private and unavailable "
                        f"to non-owner agent {agent_id}"
                    )
                    self._record_private_access_attempt(
                        agent_id=agent_id,
                        server_name=server_name,
                        tool_name=tool_name,
                        matched_pattern=pattern,
                        reason=reason,
                    )
                    return PermissionCheck(
                        allowed=False,
                        reason=reason,
                        agent_trust_level=trust_level,
                    )

        server_config = self.config.servers.get(server_name)
        required = self.infer_permission_level(tool_name, server_config)
        max_allowed = TRUST_PERMISSION_MAP.get(trust_level, PermissionLevel.READ)

        if required > max_allowed:
            return PermissionCheck(
                allowed=False,
                reason=f"Tool {tool_name} requires {required.value}, agent trust level {trust_level} allows up to {max_allowed.value}",
                required_level=required,
                agent_trust_level=trust_level,
            )

        return PermissionCheck(
            allowed=True,
            required_level=required,
            agent_trust_level=trust_level,
        )

    def check_tool_parameters(
        self,
        agent_id: str,
        server_name: str,
        tool_name: str,
        parameters: object | None,
    ) -> PermissionCheck:
        """Block non-owner tool calls that reference admin-private data paths/content."""
        if str(agent_id) == str(self._owner_user_id):
            return PermissionCheck(allowed=True, agent_trust_level=self.get_trust_level(agent_id))
        if parameters is None:
            return PermissionCheck(allowed=True, agent_trust_level=self.get_trust_level(agent_id))

        compiled_patterns = self._compiled_private_data_patterns
        if not compiled_patterns:
            return PermissionCheck(allowed=True, agent_trust_level=self.get_trust_level(agent_id))

        matched_pattern: str | None = None
        matched_value: str | None = None

        def _walk(value: object) -> None:
            nonlocal matched_pattern, matched_value
            if matched_pattern is not None:
                return
            if isinstance(value, dict):
                for v in value.values():
                    _walk(v)
                return
            if isinstance(value, (list, tuple, set)):
                for item in value:
                    _walk(item)
                return
            if not isinstance(value, str):
                return
            for pattern, cre in compiled_patterns:
                if cre.search(value):
                    matched_pattern = pattern
                    matched_value = value
                    return

        _walk(parameters)
        if matched_pattern is None:
            return PermissionCheck(allowed=True, agent_trust_level=self.get_trust_level(agent_id))

        reason = (
            f"Tool {tool_name} parameters reference admin-private data and are "
            f"unavailable to non-owner agent {agent_id}"
        )
        self._record_private_access_attempt(
            agent_id=agent_id,
            server_name=server_name,
            tool_name=tool_name,
            matched_pattern=matched_pattern,
            reason=reason,
        )
        logger.warning(
            "Blocked admin-private parameter access: agent=%s server=%s tool=%s pattern=%s sample=%s",
            agent_id,
            server_name,
            tool_name,
            matched_pattern,
            (matched_value or "")[:120],
        )
        return PermissionCheck(
            allowed=False,
            reason=reason,
            agent_trust_level=self.get_trust_level(agent_id),
        )

    def check_rate_limit(
        self,
        agent_id: str,
        server_name: str,
        tool_name: str,
    ) -> PermissionCheck:
        """Check and update rate limits for a tool call.

        Returns allowed=True and increments counter, or allowed=False if limited.
        """
        # Get configured rate limit
        limit = 0  # 0 = unlimited
        server_config = self.config.servers.get(server_name)
        if server_config and tool_name in server_config.tools:
            limit = server_config.tools[tool_name].rate_limit

        # Also check global rate limit
        global_limit = self.config.global_rate_limit

        if limit == 0 and global_limit == 0:
            return PermissionCheck(allowed=True)

        effective_limit = limit if limit > 0 else global_limit
        key = f"{agent_id}:{server_name}:{tool_name}"
        now = time.time()

        if key not in self._rate_limits:
            # Evict stale entries if over limit
            if len(self._rate_limits) >= self.MAX_RATE_LIMIT_ENTRIES:
                stale = [
                    k
                    for k, v in self._rate_limits.items()
                    if now - v.window_start > v.window_seconds * 2
                ]
                for k in stale:
                    del self._rate_limits[k]
            self._rate_limits[key] = RateLimitEntry(count=1, window_start=now)
            return PermissionCheck(allowed=True)

        entry = self._rate_limits[key]

        # Reset window if expired
        if now - entry.window_start >= entry.window_seconds:
            entry.count = 1
            entry.window_start = now
            return PermissionCheck(allowed=True)

        if entry.count >= effective_limit:
            return PermissionCheck(
                allowed=False,
                reason=f"Rate limit exceeded: {entry.count}/{effective_limit} per minute for {tool_name}",
                rate_limited=True,
            )

        entry.count += 1
        return PermissionCheck(allowed=True)

    def check_all(
        self,
        agent_id: str,
        server_name: str,
        tool_name: str,
        parameters: object | None = None,
    ) -> PermissionCheck:
        """Run all permission checks in order. Returns first failure or final success."""
        # 1. Server access
        result = self.check_agent_server_access(agent_id, server_name)
        if not result.allowed:
            return result

        # 2. Tool permission
        result = self.check_tool_permission(agent_id, server_name, tool_name)
        if not result.allowed:
            return result

        # 3. Tool parameters
        result = self.check_tool_parameters(agent_id, server_name, tool_name, parameters)
        if not result.allowed:
            return result

        # 4. Rate limit
        result = self.check_rate_limit(agent_id, server_name, tool_name)
        return result
