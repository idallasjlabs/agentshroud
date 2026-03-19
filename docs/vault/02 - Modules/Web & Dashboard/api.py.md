---
title: api.py
type: module
file_path: gateway/web/api.py
tags: [web, api, management, rest]
related: [Gateway Core/main.py, Architecture Overview, Runbooks/Health Checks]
status: documented
---

# api.py

**Location:** `gateway/web/api.py`
**Lines:** ~754
**Router prefix:** `/api`

## Purpose

Management REST API for the AgentShroud gateway. Provides endpoints for container management, config updates, kill switch, ledger queries, audit export, and WebSocket dashboard streaming. All endpoints require Bearer token authentication.

## Responsibilities

- Container start/stop/restart via runtime engine abstraction
- Kill switch activation (freeze, shutdown, disconnect)
- Configuration read/update at runtime
- Runtime environment detection (Docker, Podman, macOS)
- Security comparison across runtime engines
- WebSocket streaming for dashboard

## Security

All endpoints protected by `require_auth` dependency (Bearer token validation). Service names validated against a hardcoded allowlist (`VALID_SERVICES`) to prevent command injection.

**Allowed service names:**
- `agentshroud-gateway`
- `agentshroud-openclaw`
- `falco`
- `wazuh-agent`
- `clamav`

**Valid kill switch modes:** `freeze`, `shutdown`, `disconnect`

## Key Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/runtime` | Detect runtime (Docker/Podman/macOS) |
| GET | `/api/security` | Security feature comparison |
| POST | `/api/services/{name}/start` | Start a service |
| POST | `/api/services/{name}/stop` | Stop a service |
| POST | `/api/services/{name}/restart` | Restart a service |
| GET | `/api/config` | Read current runtime config |
| PUT | `/api/config` | Update runtime config |
| POST | `/api/kill-switch` | Activate kill switch |
| GET | `/api/ledger` | Query audit ledger |
| GET | `/api/health` | Component health status |
| WS | `/api/ws` | WebSocket dashboard stream |

## Pydantic Models

| Model | Purpose |
|-------|---------|
| `ServiceAction` | `timeout: int = 30` |
| `KillSwitchAction` | `confirm: bool = False` |
| `ConfigUpdate` | `config: dict` |
| `UpdateRequest` | Config update request |

## Runtime Engine Integration

Delegates container operations to the appropriate engine:
- `detect_runtime()` — identifies Docker vs Podman vs macOS
- `get_engine()` — returns the correct engine implementation
- `RuntimeConfig` — maps to current runtime settings

## Related Notes

- [[Gateway Core/main.py|main.py]] — Mounts this router at `/api`
- [[Runtime/engine.py|engine.py]] — Abstract container engine
- [[Runbooks/Kill Switch Procedure]] — Kill switch usage
- [[Architecture Overview]] — System context
