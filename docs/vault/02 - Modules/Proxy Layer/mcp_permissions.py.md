---
title: mcp_permissions.py
type: module
file_path: gateway/proxy/mcp_permissions.py
tags: [proxy, mcp, permissions, trust-levels, rate-limiting, access-control]
related: [[mcp_proxy.py]], [[mcp_config.py]], [[mcp_audit.py]]
status: documented
---

# mcp_permissions.py

## Purpose
Implements per-tool and per-server permission enforcement for MCP tool calls. Uses a default-allow philosophy where tools pass unless trust level is clearly insufficient for a known-dangerous operation or the agent/server is explicitly blocked.

## Responsibilities
- Map agent trust levels (0–3) to maximum allowed `PermissionLevel` ceilings
- Infer required permission level for any tool by pattern-matching its name
- Enforce explicit agent allowlists and denylists per MCP server
- Enforce per-tool and global rate limits using a sliding-window counter
- Run all checks in sequence via `check_all()` — server access, tool permission, rate limit
- Evict stale rate limit entries to prevent unbounded memory growth

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `PermissionCheck` | Dataclass | Result of a permission check: allowed flag, reason, required level, trust level, rate-limited flag |
| `RateLimitEntry` | Dataclass | Sliding-window counter state for a specific agent+server+tool combination |
| `MCPPermissionManager` | Class | Manages all MCP permission logic; default-allow with escalation for dangerous ops |
| `TRUST_PERMISSION_MAP` | Dict | Maps trust level int (0–3) to `PermissionLevel` ceiling (READ/WRITE/EXECUTE/ADMIN) |
| `SENSITIVE_TOOL_PATTERNS` | List | Glob patterns matching tools that require EXECUTE level (*shell*, *exec*, *delete*, etc.) |
| `READ_ONLY_PATTERNS` | List | Glob patterns matching tools inferred as READ level (*get*, *list*, *search*, etc.) |

## Function Details

### MCPPermissionManager.set_trust_level(agent_id, level)
**Purpose:** Assign a trust level to a named agent; clamped to [0, 3].
**Parameters:** `agent_id` (str), `level` (int).

### MCPPermissionManager.get_trust_level(agent_id)
**Purpose:** Return an agent's trust level, defaulting to 1 (WRITE) for unknown agents.
**Returns:** int (0–3).

### MCPPermissionManager.infer_permission_level(tool_name, server_config)
**Purpose:** Determine the permission ceiling a tool requires. Checks explicit config first, then pattern-matches against sensitive and read-only globs, defaulting to WRITE.
**Returns:** `PermissionLevel`.

### MCPPermissionManager.check_agent_server_access(agent_id, server_name)
**Purpose:** Verify an agent can access a server at all — checks enabled flag, denylist, allowlist, and minimum trust level.
**Returns:** `PermissionCheck`.

### MCPPermissionManager.check_tool_permission(agent_id, server_name, tool_name)
**Purpose:** Compare the tool's required permission level against the agent's trust ceiling.
**Returns:** `PermissionCheck`. Blocks only when required level exceeds the ceiling.

### MCPPermissionManager.check_rate_limit(agent_id, server_name, tool_name)
**Purpose:** Enforce sliding-window rate limits. Uses per-tool config when available, falls back to global rate limit.
**Parameters:** `agent_id` (str), `server_name` (str), `tool_name` (str).
**Returns:** `PermissionCheck` with `rate_limited=True` when limit exceeded.

### MCPPermissionManager.check_all(agent_id, server_name, tool_name)
**Purpose:** Run server access → tool permission → rate limit in order, returning the first failure or final success.
**Returns:** `PermissionCheck`.

## Trust Level Reference

| Trust Level | Max Allowed Permission | Typical Use |
|-------------|----------------------|-------------|
| 0 | READ | Read-only untrusted agents |
| 1 | WRITE | Default for unknown agents |
| 2 | EXECUTE | Trusted agents with shell access |
| 3 | ADMIN | Fully privileged admin agents |

## Configuration / Environment Variables
- `MCPProxyConfig.global_rate_limit` — global cap on calls per minute across all tools (0 = unlimited)
- Per-tool rate limits configured in `MCPServerConfig.tools[tool_name].rate_limit`
- `MAX_RATE_LIMIT_ENTRIES` = 10,000 — prevents unbounded rate limit map growth

## Related
- [[mcp_proxy.py]]
- [[mcp_config.py]]
- [[mcp_audit.py]]
