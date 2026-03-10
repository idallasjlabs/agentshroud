---
title: "Error: Bot Isolation Breach"
type: error
tags: [#type/error, #status/critical]
severity: high
related: ["[[agentshroud-bot]]", "[[Architecture Overview]]", "[[egress_filter]]", "[[HTTP_PROXY]]"]
status: active
last_reviewed: 2026-03-09
---

# Error: Bot Isolation Breach

## What It Means

The bot container is making direct internet connections, bypassing the gateway security proxy. This defeats the entire security model.

## Detection

```bash
# From inside the bot container, can it reach the internet directly?
docker exec agentshroud-bot curl -m 5 https://api.telegram.org/bot/getMe
# Expected: connection timeout (bot is isolated)
# Bad: successful response

# Check bot's network interfaces
docker exec agentshroud-bot ip route show
# Expected: no default route to internet
# Only: 172.11.0.0/16 and 172.12.0.0/16
```

## Root Cause

The `agentshroud-isolated` network has `internal: true` — Docker blocks routing to the internet. If the bot CAN reach the internet directly, the network config is wrong.

```yaml
# docker-compose.yml — should be:
agentshroud-isolated:
  driver: bridge
  internal: true  # ← this prevents internet routing
```

## Fix

```bash
# Verify network isolation
docker network inspect agentshroud_agentshroud-isolated | grep -A5 '"Internal"'
# Should show: "Internal": true

# If not isolated, recreate networks:
docker compose -f docker/docker-compose.yml down
docker network rm agentshroud_agentshroud-isolated 2>/dev/null || true
docker compose -f docker/docker-compose.yml up -d
```

## Verify Fix

```bash
# Bot should NOT be able to reach internet
docker exec agentshroud-bot curl -m 3 https://api.telegram.org/ 2>&1
# Should show: timeout or connection refused

# Bot SHOULD reach gateway
docker exec agentshroud-bot curl -m 3 http://gateway:8080/status
# Should show: {"status": "ok", ...}
```
