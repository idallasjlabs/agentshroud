# API Reference

## AgentShroud v1.3.0

### Overview

AgentShroud's gateway is a transparent security proxy — most of its "API" is
the intercepted traffic between an AI agent and the systems it talks to
(Telegram, Anthropic, egress domains, SSH targets), not a conventional REST
API consumed by external clients. The endpoints below are the gateway's own
**management/control-plane API**, used by the terminal dashboard, web
control center, and the wrapped bots themselves — not a public integration
surface.

**Base URL**: `http://gateway:8080` (internal Docker network) /
`http://localhost:8080` (host, if published) / your Tailscale hostname if
served externally (e.g. `https://<host>.<tailnet>.ts.net:8080`)
**Authentication**: `Authorization: Bearer <gateway auth token>` — the token
is a 64-char secret provisioned via `docker/setup-secrets.sh`
(`gateway_password` / `GATEWAY_AUTH_TOKEN_FILE`), not a per-user JWT.
**Content Type**: `application/json`
**Note**: there is no `/api/v1` prefix and no port `8443` — this reference
previously described a fictional API that never existed in this codebase;
it's rewritten below against the actual route table.

---

## Authentication

Every protected route depends on `auth_dep` (`gateway/ingest_api/main.py`),
which validates a bearer token against the configured gateway auth token:

```
Authorization: Bearer <gateway_auth_token>
```

Some route groups (the management API, SOC dashboard) implement their own
Bearer check per-endpoint rather than sharing `auth_dep` — same header
format either way. System-internal callers (startup/shutdown notifications)
identify themselves with `X-AgentShroud-System: 1` instead.

---

## Route map (by router)

The gateway mounts several `APIRouter`s onto the FastAPI app
(`gateway/ingest_api/main.py:182-197`). This is the real, current route
table — grep `gateway/ingest_api/main.py`, `gateway/soc/router.py`, and
`gateway/web/api.py` directly for the authoritative, byte-for-byte list;
what follows is organized by area, not exhaustive per-field schemas (the
surface is 100+ routes across these files and changes with the code).

### Health & status
- `GET /manage/health` — aggregated status of every wired security module
  (ClamAV, Trivy, OpenSCAP, drift detector, encrypted store, key vault,
  alert dispatcher, killswitch monitor, Falco, Wazuh, …)
- `GET /manage/killswitch/status`, `POST /manage/killswitch/verify`
- `GET /proxy/status`

### Egress control
- `GET /manage/egress/pending`, `GET /manage/egress/log`,
  `GET /manage/egress/risk`
- `POST /manage/egress/{request_id}/approve`,
  `POST /manage/egress/{request_id}/deny`
- `POST /manage/egress/emergency-block`
- `GET|POST|DELETE /manage/egress/rules`

### Audit / ledger
- `GET /ledger`, `GET /ledger/{entry_id}`, `DELETE /ledger/{entry_id}`
  (SHA-256 hash-chained audit trail — see ADR-005)

### Scanning
- `POST /manage/scan/{trivy|clamav|openscap|cis-benchmark|all}`
- `GET /manage/scanners/summary`, `GET /manage/scanners/history`
- `GET /manage/falco/alerts`, `GET /manage/wazuh/alerts`
- `GET /manage/container-security`, `GET /manage/compliance/soc2`

### Quarantine
- `GET /manage/quarantine/summary`
- `GET|POST /manage/quarantine/blocked-messages[/{id}/release|discard]`
- `GET|POST /manage/quarantine/blocked-outbound[/{id}/release|discard]`

### RBAC
- `GET /manage/rbac/my-permissions`, `GET /manage/rbac/users`,
  `PUT /manage/rbac/users/{target_user_id}`,
  `GET /manage/rbac/users/{user_id}/permissions`

### DNS
- `GET|POST|DELETE /manage/dns/blocked`, `POST /manage/dns/refresh`

### SOC — Shared Command Layer (`/soc/v1/*`, `gateway/soc/router.py`)
The largest single router (~65 routes): killswitch (`freeze`/`shutdown`/
`disconnect`), egress approve/deny/history/rules, RBAC (`users`, `groups`,
`delegation`), security modules + heatmap, SBOM, scanners, CVE registry
(`/agent-cves`), collaborator activity, service lifecycle
(`start`/`stop`/`restart`/`update`/`rebuild`), bot updates
(`/updates/bot/upgrade`, `/updates/gateway/upgrade`,
`/updates/gateway/rollback`, `/updates/hermes/upgrade`), config
integrity, auth (`/auth/login`, `/auth/ws-token`).

### Web control center (`gateway/web/api.py`)
Bot lifecycle (start/stop/restart/killswitch), config import/export,
per-bot updates (upgrade/rollback per `bot_id`), security report, logs,
skills reload, competitive-intel reports.

### Agent-facing proxy endpoints (not control-plane)
- `POST /mcp/proxy`, `POST /mcp/result` — MCP tool-call interception
- `POST /ssh/exec`, `GET /ssh/history`, `GET /ssh/hosts` — the
  `agentshroud-ssh-exec.sh` wrapper target (see
  `docker/scripts/agentshroud-ssh-exec.sh`)
- `POST /credentials/op-proxy` — 1Password credential proxy
- Telegram/Slack/LLM traffic is intercepted transparently, not via a
  documented REST contract — see `docker-compose.yml`'s `*_API_BASE_URL`
  env vars for how each bot is pointed at the gateway.

---

## Example: `GET /manage/health`

Real response shape (`gateway/ingest_api/main.py`, `security_health_report`)
— module keys present depend on which modules are wired for this deployment:

```json
{
  "timestamp": "2026-08-04T12:00:00+00:00",
  "modules": {
    "clamav": { "status": "ready", "binary": true },
    "trivy": { "status": "ready", "binary": true },
    "drift_detector": { "status": "active" },
    "killswitch_monitor": { "status": "active" },
    "falco_monitor": { "status": "listening" },
    "wazuh_client": { "status": "listening" }
  }
}
```

```bash
curl -H "Authorization: Bearer $GATEWAY_AUTH_TOKEN" \
  http://localhost:8080/manage/health
```

## Example: `POST /manage/egress/{request_id}/approve`

```bash
curl -X POST \
  -H "Authorization: Bearer $GATEWAY_AUTH_TOKEN" \
  http://localhost:8080/manage/egress/req-abc123/approve
```

Approves a pending egress request (an agent attempting to reach an
unrecognized domain) — see `gateway/security/egress_filter.py` and
`gateway/proxy/telegram_egress_notify.py` for the approval flow, including
the Telegram inline-button path.

---

## Error responses

FastAPI's default `HTTPException` shape is used throughout:

```json
{ "detail": "Service not initialized" }
```

Specific status codes vary per route (`401` unauthenticated, `403`
forbidden, `404` not found, `409` conflict, `422` validation error) — check
the individual route handler for exact conditions rather than assuming a
single global error schema.

---

## Source of truth

This document is a map, not a contract — the routes themselves, their
request/response Pydantic models, and their exact status codes live in:
- `gateway/ingest_api/main.py` — core routes + router mounting
- `gateway/soc/router.py` — `/soc/v1/*` Shared Command Layer
- `gateway/web/api.py`, `gateway/web/management.py` — web control center
- `gateway/ingest_api/routes/` — health, forward, approval, dashboard,
  version routers

When in doubt, `grep -n '@app\.\|@router\.' <file>` beats this document.
