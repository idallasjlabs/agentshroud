"""MCP Permissions — per-tool permission system with sensible defaults.

Design: default-allow with escalation for dangerous operations.
Trust levels map to permission ceilings, not floors.
"""

import fnmatch
import logging
import time
from dataclasses import dataclass
from typing import Optional

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


class MCPPermissionManager:
    """Manages permissions for MCP tool calls.

    Default-allow philosophy: tools work unless there is a specific reason to block.
    """

    MAX_RATE_LIMIT_ENTRIES = 10000  # Prevent unbounded growth

    def __init__(self, config: Optional[MCPProxyConfig] = None):
        self.config = config or MCPProxyConfig()
        self._rate_limits: dict[str, RateLimitEntry] = {}
        self._trust_levels: dict[str, int] = {}  # agent_id → trust level

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

    def check_agent_server_access(
        self, agent_id: str, server_name: str
    ) -> PermissionCheck:
        """Check if an agent can access a server at all."""
        server_config = self.config.servers.get(server_name)
        if not server_config:
            # Unknown server — allow but log
            return PermissionCheck(
                allowed=True, reason="Unknown server, default allow", logged_only=True
            )

        if not server_config.enabled:
            return PermissionCheck(
                allowed=False, reason=f"Server {server_name} is disabled"
            )

        # Check denylist first
        if server_config.denied_agents and agent_id in server_config.denied_agents:
            return PermissionCheck(
                allowed=False,
                reason=f"Agent {agent_id} denied for server {server_name}",
            )

        # Check allowlist (empty = all allowed)
        if (
            server_config.allowed_agents
            and agent_id not in server_config.allowed_agents
        ):
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

        # 3. Rate limit
        result = self.check_rate_limit(agent_id, server_name, tool_name)
        return result
