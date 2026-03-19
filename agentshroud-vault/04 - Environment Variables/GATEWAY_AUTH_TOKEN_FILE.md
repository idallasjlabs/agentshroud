---
title: GATEWAY_AUTH_TOKEN_FILE
type: env-var
tags: [#type/env-var, #status/critical]
required: true
default: "none"
related: ["[[agentshroud-gateway]]", "[[agentshroud-bot]]", "[[docker-compose.yml]]", "[[config]]"]
status: active
last_reviewed: 2026-03-09
---

# GATEWAY_AUTH_TOKEN_FILE

## What It Controls

The file path to the gateway's shared authentication secret. The gateway reads this file at startup and uses the token to authenticate all API requests from the bot.

## Expected Format

Filesystem path to a file containing a hex token:
```
/run/secrets/gateway_password
```

The file content should be a 32-byte hex string (64 characters):
```
a1b2c3d4e5f6...
```

Generate with:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))" > docker/secrets/gateway_password.txt
```

## Effect If Missing

The gateway generates a random token at startup (logs it), but the bot won't know this token. All authenticated API calls from the bot will fail with 401.

## Effect If Wrong Value

`401 Unauthorized` on all bot → gateway API calls. The bot cannot reach the LLM, Telegram proxy, or MCP tools.

## Where It Is Set

`docker/docker-compose.yml` gateway service:
```yaml
environment:
  - GATEWAY_AUTH_TOKEN_FILE=/run/secrets/gateway_password
secrets:
  - gateway_password  # mounts docker/secrets/gateway_password.txt at /run/secrets/gateway_password
```

## Auth Token Resolution Order (in config.py)

1. File at `$GATEWAY_AUTH_TOKEN_FILE`
2. `gateway.auth_token` in `agentshroud.yaml`
3. Auto-generated random token (logged to stdout, warning issued)

> [!DANGER] Critical — the bot and gateway must share the same token. Ensure `docker/secrets/gateway_password.txt` is populated before first start.

## Used In

- [[config]] — `load_config()` reads the token file
- [[agentshroud-gateway]] — validates incoming requests against this token
- [[agentshroud-bot]] — sends token with all gateway API requests
