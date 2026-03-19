---
title: GATEWAY_OP_PROXY_URL
type: env-var
tags: [1password, credentials, proxy]
related: [OP_SERVICE_ACCOUNT_TOKEN, Configuration/All Environment Variables, Gateway Core/main.py]
status: documented
---

# GATEWAY_OP_PROXY_URL

## Description

URL the bot uses to make 1Password credential requests through the gateway's op-proxy endpoint. When set, `op-wrapper.sh` routes all `op read` commands to `POST $GATEWAY_OP_PROXY_URL/credentials/op-proxy` instead of calling 1Password directly.

## Value

```
http://gateway:8080
```

Requests go to `http://gateway:8080/credentials/op-proxy`.

## Usage Flow

```
Bot (op-wrapper.sh)
  → POST http://gateway:8080/credentials/op-proxy
  → {"reference": "op://Agent Shroud Bot Credentials/..."}
Gateway (main.py)
  → Validates reference against _ALLOWED_OP_PATHS allowlist
  → Calls 1Password CLI using OP_SERVICE_ACCOUNT_TOKEN
  → Returns secret value
```

## Security

- Only `op://Agent Shroud Bot Credentials/*/*` patterns are allowed
- Path traversal (`..`) in references is rejected
- The bot never has direct 1Password access — all credential retrieval is mediated by the gateway

## Set In

`docker/docker-compose.yml`:
```yaml
environment:
  - GATEWAY_OP_PROXY_URL=http://gateway:8080
```

## Related Notes

- [[OP_SERVICE_ACCOUNT_TOKEN]] — The service account token the gateway uses
- [[Gateway Core/main.py|main.py]] — The `/credentials/op-proxy` endpoint
- [[Configuration/All Environment Variables]] — All env vars
