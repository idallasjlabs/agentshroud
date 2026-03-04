---
type: reference
created: 2026-03-03
tags: [operations, cheatsheet, runbook]
related: [System Overview, Runbooks/Health Checks, Runbooks/Kill Switch Procedure]
---

# Quick Reference — AgentShroud

## Start / Stop

```bash
# Start (standard)
cd /path/to/agentshroud
docker compose -f docker/docker-compose.yml up -d

# Start with secrets from 1Password
./docker/scripts/start-agentshroud.sh

# Stop gracefully
docker compose -f docker/docker-compose.yml down

# Restart gateway only
docker compose -f docker/docker-compose.yml restart agentshroud-gateway

# Restart bot only
docker compose -f docker/docker-compose.yml restart agentshroud-bot
```

---

## Health Checks

```bash
# Gateway health endpoint
curl -s http://localhost:8080/health | jq .

# Gateway status with auth
curl -s -H "Authorization: Bearer $GATEWAY_AUTH_TOKEN" \
  http://localhost:8080/status | jq .

# Full health report
curl -s -H "Authorization: Bearer $GATEWAY_AUTH_TOKEN" \
  http://localhost:8080/health/report | jq .

# Container health
docker compose -f docker/docker-compose.yml ps

# Using built-in health script
./docker/scripts/health-check.sh
```

**Expected healthy response:**
```json
{
  "status": "healthy",
  "components": {
    "pii_sanitizer": "ok",
    "prompt_guard": "ok",
    "egress_filter": "ok",
    "ledger": "ok"
  }
}
```

---

## Logs

```bash
# All containers
docker compose -f docker/docker-compose.yml logs -f

# Gateway only
docker compose -f docker/docker-compose.yml logs -f agentshroud-gateway

# Bot only
docker compose -f docker/docker-compose.yml logs -f agentshroud-bot

# Tail last 100 lines
docker compose -f docker/docker-compose.yml logs --tail=100 agentshroud-gateway
```

---

## Key Ports

| Port | Service | Protocol |
|------|---------|----------|
| 8080 | Gateway API | HTTP |
| 8181 | HTTP CONNECT proxy | HTTP |
| 18789 | OpenClaw agent | HTTP |
| 18790 | Management dashboard | HTTP |
| 3000 | Dashboard (alternate) | HTTP |

---

## Environment Variables (required)

| Variable | Purpose |
|----------|---------|
| `GATEWAY_AUTH_TOKEN` | Shared secret for gateway authentication |
| `ANTHROPIC_BASE_URL` | Redirect LLM calls through gateway (e.g., `http://gateway:8080/v1`) |
| `TELEGRAM_BOT_TOKEN` | Telegram bot credentials |
| `TELEGRAM_API_BASE_URL` | Telegram API routed through gateway |
| `OP_SERVICE_ACCOUNT_TOKEN` | 1Password service account (gateway-side) |
| `OPENCLAW_GATEWAY_PASSWORD` | Bot → gateway authentication |
| `AGENTSHROUD_CONFIG` | Path to `agentshroud.yaml` (optional, defaults to CWD) |
| `AGENTSHROUD_MODE` | `enforce` (default) or `monitor` (log-only) |

---

## Kill Switch

```bash
# Immediate emergency shutdown
./docker/scripts/killswitch.sh

# Via API
curl -X POST -H "Authorization: Bearer $GATEWAY_AUTH_TOKEN" \
  http://localhost:8080/admin/kill-switch

# Via dashboard
# Navigate to http://localhost:18790 → Kill Switch button
```

**Kill switch actions (configured in `agentshroud.yaml`):**
- `freeze` — Pause all agent actions, keep containers running
- `shutdown` — Stop all containers
- `disconnect` — Drop network connections only

---

## Common Issues

| Symptom | Quick Fix |
|---------|-----------|
| Gateway returns 401 | Check `GATEWAY_AUTH_TOKEN` matches config |
| PII false positives blocking requests | Set `pii_min_confidence: 0.95` in `agentshroud.yaml` |
| Bot can't reach gateway | Verify `ANTHROPIC_BASE_URL=http://gateway:8080/v1` in bot env |
| Egress blocked unexpectedly | Add domain to `proxy.allowed_domains` in `agentshroud.yaml` |
| Approval queue backlog | Access dashboard at `:18790` to approve/deny pending items |
| Startup fails, no auth token | Set `GATEWAY_AUTH_TOKEN` env var or `auth_token` in `agentshroud.yaml` |

See [[Errors & Troubleshooting/Troubleshooting Matrix]] for full diagnosis guide.

---

## Configuration Files

| File | Purpose |
|------|---------|
| `agentshroud.yaml` | Master configuration |
| `docker/docker-compose.yml` | Container definitions |
| `docker/docker-compose.secure.yml` | Hardened production config |
| `docker/docker-compose.sidecar.yml` | Proxy-only minimal deployment |

---

## Security Mode Toggle

```bash
# Switch to monitor mode (log but don't block — development only)
export AGENTSHROUD_MODE=monitor
docker compose restart agentshroud-gateway

# Return to enforce mode (production default)
unset AGENTSHROUD_MODE
docker compose restart agentshroud-gateway
```

> **Warning:** `monitor` mode disables all enforcement. Never use in production.

---

## Related Notes

- [[Runbooks/First Time Setup]] — Full deployment guide
- [[Runbooks/Restart Procedure]] — Safe restart steps
- [[Runbooks/Crash Recovery]] — Post-crash recovery
- [[Errors & Troubleshooting/Troubleshooting Matrix]] — Full diagnostic matrix
- [[Configuration/All Environment Variables]] — Complete env var reference
