---
title: Quick Reference
type: index
tags: [#type/index, #status/critical]
related: ["[[Home]]", "[[Restart Procedure]]", "[[Health Checks]]", "[[Error Index]]"]
status: active
last_reviewed: 2026-03-09
---

# Quick Reference — AgentShroud Cheat Sheet

## Start / Stop / Restart

```bash
# Start stack (from repo root)
docker compose -f docker/docker-compose.yml up -d

# Stop stack
docker compose -f docker/docker-compose.yml down

# Restart everything
docker compose -f docker/docker-compose.yml restart

# Restart only gateway
docker compose -f docker/docker-compose.yml restart gateway

# Restart only bot
docker compose -f docker/docker-compose.yml restart bot

# Full rebuild (no cache)
docker compose -f docker/docker-compose.yml build --no-cache
docker compose -f docker/docker-compose.yml up -d
```

## Health Check Commands

```bash
# Stack status
docker compose -f docker/docker-compose.yml ps

# Gateway health (JSON)
curl http://localhost:8080/status

# Bot health (raw)
curl http://localhost:18790/

# Gateway logs (last 50 lines)
docker logs agentshroud-gateway --tail 50

# Bot logs (last 50 lines)
docker logs agentshroud-bot --tail 50

# Follow gateway logs live
docker logs agentshroud-gateway -f

# Telegram long-polling (should show 200)
docker logs agentshroud-gateway | grep getUpdates

# Verify Telegram messages flowing
docker logs agentshroud-bot | grep "sendMessage ok"
```

## Config File Locations

| File | Path | Description |
|------|------|-------------|
| Main config | `agentshroud.yaml` | Security posture, bots, proxy allowlist |
| Docker compose | `docker/docker-compose.yml` | Container topology |
| Secrets dir | `docker/secrets/` | All Docker secret files |
| Gateway password | `docker/secrets/gateway_password.txt` | Shared auth secret |
| Telegram token | `docker/secrets/telegram_bot_token_production.txt` | Bot token |
| Bot patches | `docker/scripts/patch-telegram-sdk.sh` | Routes file downloads through gateway |
| OpenClaw patches | `docker/bots/openclaw/config/apply-patches.js` | Model, tool, workspace config |

## Log File Locations (inside containers)

| Log | Location | How to Access |
|-----|----------|---------------|
| Gateway app logs | stdout | `docker logs agentshroud-gateway` |
| Alert log | `/tmp/security/alerts/alerts.jsonl` | `docker exec agentshroud-gateway cat /tmp/security/alerts/alerts.jsonl` |
| Audit DB | `/app/data/audit.db` | `docker exec agentshroud-gateway sqlite3 /app/data/audit.db .tables` |
| Collaborator activity | `/app/data/collaborator_activity.jsonl` | `docker exec agentshroud-gateway cat /app/data/collaborator_activity.jsonl` |

## Key Environment Variables

| Variable | Container | Purpose | Note |
|----------|-----------|---------|------|
| [[TELEGRAM_API_BASE_URL]] | bot | Routes Telegram API to gateway | `http://gateway:8080/telegram-api` |
| [[ANTHROPIC_BASE_URL]] | bot | Routes LLM calls to gateway | `http://gateway:8080` |
| [[HTTP_PROXY]] | bot | Routes all HTTP through CONNECT proxy | `http://gateway:8181` |
| [[GATEWAY_AUTH_TOKEN_FILE]] | gateway | Path to gateway password secret | `/run/secrets/gateway_password` |
| [[AGENTSHROUD_MODE]] | gateway | `monitor` disables all blocking | Default: enforce |
| [[PROXY_ALLOWED_NETWORKS]] | gateway | CIDRs that may use CONNECT proxy | `172.11.0.0/16,172.12.0.0/16` |

## Top 5 Emergency Fixes

> [!BUG] 1. "Failed to download media" on photo uploads
> **Cause:** `TELEGRAM_API_BASE_URL` was not set or patch script was not applied
> **Fix:** Rebuild bot image — `docker compose -f docker/docker-compose.yml build bot --no-cache && docker compose -f docker/docker-compose.yml up -d bot`
> **Detail:** See [[Photo Download Failure]]

> [!BUG] 2. Gateway not healthy / won't start
> **Cause:** Missing secret files, bad YAML, can't bind port 8080
> **Check:** `docker logs agentshroud-gateway --tail 100`
> **Fix:** See [[Gateway Startup Failure]]

> [!BUG] 3. Bot starts but has no Telegram connectivity
> **Cause:** `TELEGRAM_BOT_TOKEN_FILE` not found or token invalid
> **Check:** `docker logs agentshroud-bot | grep -i telegram`
> **Fix:** Verify `docker/secrets/telegram_bot_token_production.txt` has valid token, restart bot

> [!BUG] 4. Messages blocked that should be allowed
> **Cause:** Prompt guard or egress filter in enforce mode is over-blocking
> **Quick bypass (dev only):** Set `AGENTSHROUD_MODE=monitor` env var on gateway, restart
> **Detail:** See [[prompt_guard]], [[egress_filter]]

> [!BUG] 5. Bot can't reach Anthropic API
> **Cause:** `ANTHROPIC_BASE_URL=http://gateway:8080` — if gateway is down, bot is blind
> **Check:** `curl http://localhost:8080/status` — must return 200
> **Fix:** Restart gateway: `docker compose -f docker/docker-compose.yml restart gateway`

## Secrets Setup (First Time)

```bash
# Create required secret files
echo "your-gateway-password-here" > docker/secrets/gateway_password.txt
echo "your-telegram-bot-token" > docker/secrets/telegram_bot_token_production.txt
echo "" > docker/secrets/anthropic_oauth_token.txt
echo "" > docker/secrets/1password_bot_email.txt
echo "" > docker/secrets/1password_bot_master_password.txt
echo "" > docker/secrets/1password_bot_secret_key.txt
```

See [[First Time Setup]] for the complete setup procedure.
