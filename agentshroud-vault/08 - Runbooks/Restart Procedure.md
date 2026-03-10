---
title: Restart Procedure
type: process
tags: [#type/process, #status/critical]
related: ["[[Health Checks]]", "[[Crash Recovery]]", "[[agentshroud-gateway]]", "[[agentshroud-bot]]"]
status: active
last_reviewed: 2026-03-09
---

# Restart Procedure

## When to Use Which Restart Type

| Scenario | Restart Type | Command |
|----------|-------------|---------|
| Config change in `agentshroud.yaml` | Gateway restart | `docker compose restart gateway` |
| Secret file changed | Gateway restart | `docker compose restart gateway` |
| Gateway is crashed/unhealthy | Gateway restart | `docker compose restart gateway` |
| Bot is crashed/unhealthy | Bot restart | `docker compose restart bot` |
| Bot image rebuilt | Bot recreate | `docker compose up -d bot` |
| Gateway image rebuilt | Gateway recreate | `docker compose up -d gateway` |
| Both images rebuilt | Full recreate | `docker compose up -d` |
| Network config changed | Full down/up | `docker compose down && docker compose up -d` |
| After `docker compose down` | Full start | `docker compose up -d` |

## Safe Restart — Gateway Only

```bash
cd /Users/ijefferson.admin/Development/agentshroud  # repo root

# Restart gateway (15s grace period, then killed)
docker compose -f docker/docker-compose.yml restart gateway

# Wait for healthy
sleep 15

# Verify
curl http://localhost:8080/status
docker logs agentshroud-gateway | tail -20
```

Expected time: 15–30 seconds

> [!WARNING] Restarting the gateway will cause the bot to lose connectivity temporarily. The bot's `ANTHROPIC_BASE_URL` points to the gateway — any in-flight LLM calls will fail. OpenClaw typically retries automatically.

## Safe Restart — Bot Only

```bash
docker compose -f docker/docker-compose.yml restart bot

# Wait for bot to start (60s start_period)
sleep 60

# Verify
curl -sf http://localhost:18790/ && echo "Bot OK"
docker logs agentshroud-bot | tail -20
```

Expected time: 60–90 seconds (OpenClaw startup takes ~60s)

## Full Stack Restart

```bash
docker compose -f docker/docker-compose.yml restart

# Verify sequence:
# 1. Gateway restarts first
curl http://localhost:8080/status  # wait for this

# 2. Bot restarts
sleep 60
curl -sf http://localhost:18790/ && echo "Bot OK"
```

## Rolling Restart vs Full Restart

**Rolling (one at a time):** Lower disruption — restart gateway, wait for healthy, restart bot. Users may see brief delays but the stack never fully stops.

**Full restart (`docker compose down && up`):** Required when network configuration changes. Destroys and recreates all containers. Use for: subnet changes, volume changes, security config changes.

## What to Verify After Any Restart

```bash
# 1. Gateway healthy
curl http://localhost:8080/status

# 2. Bot healthy
docker compose -f docker/docker-compose.yml ps

# 3. Telegram long-poll active
docker logs agentshroud-gateway | grep getUpdates | tail -3

# 4. No startup errors
docker logs agentshroud-gateway | grep -E "CRITICAL|ERROR" | tail -10

# 5. Audit chain intact
docker logs agentshroud-gateway | grep AuditChain | tail -3
```

## If Restart Takes Too Long

Normal timing:
- Gateway: healthy in 10–30 seconds
- Bot: healthy in 60–90 seconds

If gateway takes >60 seconds → likely startup failure. Check logs:
```bash
docker logs agentshroud-gateway --tail 50
```

If bot takes >2 minutes → likely OpenClaw config issue. Check logs:
```bash
docker logs agentshroud-bot --tail 50
```
