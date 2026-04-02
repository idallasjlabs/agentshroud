# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""MCP Proxy Configuration — YAML-based MCP server registry."""


import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

logger = logging.getLogger("agentshroud.proxy.mcp_config")


class MCPTransport(str, Enum):
    STDIO = "stdio"
    HTTP_SSE = "http_sse"


class PermissionLevel(str, Enum):
    READ = "read"
    WRITE = "write"
    EXECUTE = "execute"
    ADMIN = "admin"

    @classmethod
    def level_value(cls, level: "PermissionLevel") -> int:
        return {cls.READ: 0, cls.WRITE: 1, cls.EXECUTE: 2, cls.ADMIN: 3}[level]

    def __ge__(self, other):
        if not isinstance(other, PermissionLevel):
            return NotImplemented
        return PermissionLevel.level_value(self) >= PermissionLevel.level_value(other)

    def __gt__(self, other):
        if not isinstance(other, PermissionLevel):
            return NotImplemented
        return PermissionLevel.level_value(self) > PermissionLevel.level_value(other)

    def __le__(self, other):
        if not isinstance(other, PermissionLevel):
            return NotImplemented
        return PermissionLevel.level_value(self) <= PermissionLevel.level_value(other)

    def __lt__(self, other):
        if not isinstance(other, PermissionLevel):
            return NotImplemented
        return PermissionLevel.level_value(self) < PermissionLevel.level_value(other)


@dataclass
class MCPToolConfig:
    """Configuration for a specific MCP tool."""

    name: str
    permission_level: PermissionLevel = PermissionLevel.READ
    rate_limit: int = 0  # 0 = unlimited, N = max calls per minute
    sensitive: bool = False
    description: str = ""


@dataclass
class MCPServerConfig:
    """Configuration for an MCP server."""

    name: str
    transport: MCPTransport = MCPTransport.STDIO
    command: str = ""  # For stdio transport
    args: list[str] = field(default_factory=list)
    url: str = ""  # For HTTP/SSE transport
    env: dict[str, str] = field(default_factory=dict)
    timeout_seconds: int = 30
    max_retries: int = 3
    min_trust_level: int = 0
    tools: dict[str, MCPToolConfig] = field(default_factory=dict)
    allowed_agents: list[str] = field(default_factory=list)  # empty = all allowed
    denied_agents: list[str] = field(default_factory=list)
    enabled: bool = True


@dataclass
class MCPProxyConfig:
    """Top-level MCP proxy configuration."""

    enabled: bool = True
    servers: dict[str, MCPServerConfig] = field(default_factory=dict)
    default_timeout_seconds: int = 30
    default_max_retries: int = 3
    global_rate_limit: int = 0  # 0 = unlimited
    audit_enabled: bool = True
    pii_scan_enabled: bool = True
    injection_scan_enabled: bool = True

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "MCPProxyConfig":
        """Parse config from a dictionary (e.g. loaded from YAML)."""
        servers = {}
        for name, sdata in data.get("servers", {}).items():
            tools = {}
            for tname, tdata in sdata.get("tools", {}).items():
                tools[tname] = MCPToolConfig(
                    name=tname,
                    permission_level=PermissionLevel(tdata.get("permission_level", "read")),
                    rate_limit=tdata.get("rate_limit", 0),
                    sensitive=tdata.get("sensitive", False),
                    description=tdata.get("description", ""),
                )
            servers[name] = MCPServerConfig(
                name=name,
                transport=MCPTransport(sdata.get("transport", "stdio")),
                command=sdata.get("command", ""),
                args=sdata.get("args", []),
                url=sdata.get("url", ""),
                env=sdata.get("env", {}),
                timeout_seconds=sdata.get(
                    "timeout_seconds", data.get("default_timeout_seconds", 30)
                ),
                max_retries=sdata.get("max_retries", data.get("default_max_retries", 3)),
                min_trust_level=sdata.get("min_trust_level", 0),
                tools=tools,
                allowed_agents=sdata.get("allowed_agents", []),
                denied_agents=sdata.get("denied_agents", []),
                enabled=sdata.get("enabled", True),
            )
        return cls(
            enabled=data.get("enabled", True),
            servers=servers,
            default_timeout_seconds=data.get("default_timeout_seconds", 30),
            default_max_retries=data.get("default_max_retries", 3),
            global_rate_limit=data.get("global_rate_limit", 0),
            audit_enabled=data.get("audit_enabled", True),
            pii_scan_enabled=data.get("pii_scan_enabled", True),
            injection_scan_enabled=data.get("injection_scan_enabled", True),
        )
