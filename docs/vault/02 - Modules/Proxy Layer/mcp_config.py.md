---
title: mcp_config.py
type: module
file_path: gateway/proxy/mcp_config.py
tags: [proxy, mcp, configuration, permissions, transport, yaml]
related: [[mcp_proxy.py]], [[mcp_permissions.py]], [[mcp_audit.py]]
status: documented
---

# mcp_config.py

## Purpose
Defines the YAML-loadable configuration model for the MCP proxy: transport type, per-server settings, per-tool permission levels and rate limits, and global security flags. `PermissionLevel` is an ordered enum with full comparison operators.

## Responsibilities
- Model MCP server registry entries with transport, command/URL, auth env, and agent access controls
- Model per-tool permission levels and rate limit thresholds
- Provide a `from_dict()` factory to parse config from a loaded YAML dictionary
- Define the ordered `PermissionLevel` enum used throughout the MCP permission system
- Define `MCPTransport` enum for stdio vs HTTP/SSE transport selection

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `MCPTransport` | Enum | STDIO or HTTP_SSE transport type |
| `PermissionLevel` | Enum | READ, WRITE, EXECUTE, ADMIN with ordered comparison operators |
| `MCPToolConfig` | Dataclass | Per-tool settings: name, permission_level, rate_limit, sensitive flag, description |
| `MCPServerConfig` | Dataclass | Per-server settings: transport, command, args, URL, env, timeout, trust level, agent lists, tools map |
| `MCPProxyConfig` | Dataclass | Top-level config: enabled flag, servers dict, global rate limit, audit/PII/injection scan flags |

## Function Details

### MCPProxyConfig.from_dict(data)
**Purpose:** Parse a config dictionary (e.g. loaded from YAML) into the full `MCPProxyConfig` object graph, including nested `MCPServerConfig` and `MCPToolConfig` instances.
**Parameters:** `data` (dict) — raw config dictionary.
**Returns:** `MCPProxyConfig`.

### PermissionLevel comparison operators
**Purpose:** Allow direct comparison of permission levels using standard Python operators (`>`, `>=`, `<`, `<=`).
**Example:** `PermissionLevel.EXECUTE > PermissionLevel.WRITE` → True.

## PermissionLevel Ordering

| Level | Ordinal | Meaning |
|-------|---------|---------|
| READ | 0 | Read-only operations |
| WRITE | 1 | Create/update operations |
| EXECUTE | 2 | Shell execution, destructive commands |
| ADMIN | 3 | Full administrative access |

## MCPServerConfig Fields

| Field | Default | Description |
|-------|---------|-------------|
| `transport` | STDIO | How to communicate with the server |
| `command` | "" | Binary to launch for stdio transport |
| `args` | [] | Arguments for stdio command |
| `url` | "" | Endpoint for HTTP/SSE transport |
| `env` | {} | Extra environment variables to inject |
| `timeout_seconds` | 30 | Per-request timeout |
| `max_retries` | 3 | Retry attempts on transient failure |
| `min_trust_level` | 0 | Minimum agent trust to access this server |
| `allowed_agents` | [] | Empty = all agents; populated = allowlist |
| `denied_agents` | [] | Explicit blocklist |
| `enabled` | True | Quick disable without removing config |

## MCPProxyConfig Fields

| Field | Default | Description |
|-------|---------|-------------|
| `enabled` | True | Master kill switch for MCP proxying |
| `global_rate_limit` | 0 | Calls per minute across all tools (0 = unlimited) |
| `audit_enabled` | True | Enable audit trail |
| `pii_scan_enabled` | True | Scan params and results for PII |
| `injection_scan_enabled` | True | Scan params for prompt injection |

## Configuration / Environment Variables
- Config loaded from YAML via `MCPProxyConfig.from_dict(yaml.safe_load(...))`
- No direct environment variables; typically loaded by the gateway main configuration loader

## Related
- [[mcp_proxy.py]]
- [[mcp_permissions.py]]
- [[mcp_audit.py]]
