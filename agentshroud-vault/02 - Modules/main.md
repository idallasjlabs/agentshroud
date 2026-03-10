---
title: main.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/ingest_api/main.py
tags: [#type/module, #status/active]
related: ["[[lifespan]]", "[[config]]", "[[pipeline]]", "[[telegram_proxy]]", "[[router]]", "[[agentshroud-gateway]]"]
status: active
last_reviewed: 2026-03-09
---

# main.py — FastAPI Application Entry Point

## Purpose

The top-level FastAPI application. Wires together all route handlers, registers middleware, and mounts sub-routers. The entry point for every HTTP request to the gateway.

## Responsibilities

- Create the `FastAPI` app instance with `lifespan=lifespan`
- Register all route groups (health, forward, approval, dashboard, version, management)
- Handle direct API routes: Telegram proxy, LLM proxy, MCP proxy, SSH proxy, op-proxy, iMessage
- Enforce IP allowlist on proxy endpoints (`_PROXY_ALLOWED_NETWORKS`)
- Handle `X-AgentShroud-System: 1` header (bypass content filter for system notifications)
- Validate `op://` references against `_ALLOWED_OP_PATHS` allowlist

## Key Route Groups

| Router | Mount | Description |
|--------|-------|-------------|
| `health_router` | `/` | `/status`, `/health` |
| `forward_router` | `/` | `/forward` — message forwarding |
| `approval_router` | `/` | `/approve`, `/approval-queue` |
| `dashboard_router` | `/` | Dashboard endpoints |
| `version_router` | `/` | `/version` |
| `management_api_router` | `/api` | REST management API |
| `management_dashboard_router` | `/dashboard` | Web dashboard |
| `dashboard_api_router` | `/` | Dashboard WebSocket + log stream |

## Critical Inline Routes

### `POST /telegram-api/bot{token}/{method}`
Intercepts all Telegram Bot API calls from the bot.
- Checks `X-AgentShroud-System: 1` → `is_system=True` skips outbound filtering
- Extracts `path_prefix` from the path (`""` for regular methods, `"file/"` for file downloads)
- Calls `app_state.llm_proxy.telegram_proxy.proxy_request()`

### `GET /telegram-api/bot{token}/{method}`
Same as above for GET requests (e.g., `getUpdates` long-poll override).

### `POST /v1/{path:path}` — LLM Proxy
Routes Anthropic API calls through `app_state.llm_proxy.handle_request()`.
- IP allowlist enforced: only `_PROXY_ALLOWED_NETWORKS` (172.11.0.0/16, 172.12.0.0/16, 127.0.0.0/8)
- Returns streaming SSE response for `/v1/messages`

### `POST /credentials/op-proxy` — 1Password Proxy
Fetches secrets from 1Password on behalf of bot.
- Validates `op://` reference against `_ALLOWED_OP_PATHS`
- Rejects path traversal (`..` in reference)
- Requires gateway auth token
- Calls `op read <reference>` as subprocess

### `POST /mcp/{server_id}/{tool_name}` — MCP Proxy
Routes Model Context Protocol tool calls.
- IP allowlist enforced
- Delegates to `app_state.mcp_proxy`

### `POST /ssh/{host_id}/exec` — SSH Proxy
Executes commands on approved SSH hosts.
- IP allowlist enforced
- Delegates to `app_state.ssh_proxy`

## IP Allowlist Logic

```python
_PROXY_ALLOWED_NETWORKS = [
    ipaddress.ip_network("172.11.0.0/16"),  # agentshroud-isolated
    ipaddress.ip_network("127.0.0.0/8"),    # loopback (always)
    # + PROXY_ALLOWED_NETWORKS env var (e.g., 172.12.0.0/16 for console network)
]
```

Only requests from these networks may access `/v1/`, `/mcp/`, `/credentials/`, `/ssh/`. Requests from other IPs get `403 Forbidden`.

## op:// Reference Allowlist

```python
_ALLOWED_OP_PATHS = [
    "op://Agent Shroud Bot Credentials/*/*",
]
```

The bot can only fetch secrets from the `Agent Shroud Bot Credentials` vault. Any other `op://` reference is rejected with 403.

## Environment Variables Used

- [[PROXY_ALLOWED_NETWORKS]] — additional CIDRs beyond default
- `GATEWAY_AUTH_TOKEN_FILE` — path to shared secret file

## Config Files Read

- [[agentshroud.yaml]] (via [[config]] `load_config()`)

## Known Issues

> [!WARNING] UNCERTAIN
> The `X-AgentShroud-System` header bypass is only effective if the header is set correctly in `start.sh`. If the bot container's startup script is modified, system notifications may be filtered.
