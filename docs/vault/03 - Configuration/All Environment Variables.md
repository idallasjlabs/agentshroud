---
title: All Environment Variables
type: reference
tags: [environment, configuration, operations]
related: [Configuration/agentshroud.yaml, Containers & Services/agentshroud-gateway, Containers & Services/agentshroud-bot]
status: documented
---

# All Environment Variables

## Summary

AgentShroud uses Docker secrets (files mounted at `/run/secrets/`) for credentials and environment variables for runtime configuration. This note catalogs all variables across both containers.

---

## Gateway Container (`agentshroud-gateway`)

### Required

| Variable | Source | Purpose |
|----------|--------|---------|
| `GATEWAY_AUTH_TOKEN_FILE` | `docker-compose.yml` | Path to Docker secret file containing the gateway auth token |
| `OP_SERVICE_ACCOUNT_TOKEN_FILE` | `docker-compose.yml` | Path to 1Password service account token secret file |

### Optional / Runtime

| Variable | Default | Purpose |
|----------|---------|---------|
| `AGENTSHROUD_CONFIG` | None (searches CWD) | Explicit path to `agentshroud.yaml` |
| `AGENTSHROUD_MODE` | `enforce` | `monitor` = log only, no blocking (dev/debug only) |
| `LOG_LEVEL` | `INFO` | Gateway log verbosity: DEBUG, INFO, WARNING, ERROR |
| `PYTHONUNBUFFERED` | `1` | Stream logs immediately |
| `PYTHONDONTWRITEBYTECODE` | `1` | No .pyc files (read-only rootfs) |
| `XDG_CONFIG_HOME` | `/tmp` | op CLI config location (tmpfs) |
| `PYTHONPATH` | `/app` | Module resolution |

### Derived (set at runtime by `config.py`)

| Variable | Source |
|----------|--------|
| `GATEWAY_AUTH_TOKEN` | Read from `$GATEWAY_AUTH_TOKEN_FILE` or auto-generated |

---

## Bot Container (`agentshroud-bot`)

### Required Secrets (as Docker secret files)

| Secret File | Variable Exported | Purpose |
|-------------|-------------------|---------|
| `/run/secrets/gateway_password` | `OPENCLAW_GATEWAY_PASSWORD` + `GATEWAY_AUTH_TOKEN` | Bot → gateway authentication |
| `/run/secrets/telegram_bot_token` | `TELEGRAM_BOT_TOKEN` | Telegram bot API credentials |

### Set in `docker-compose.yml`

| Variable | Value | Purpose |
|----------|-------|---------|
| `NODE_ENV` | `production` | Node.js environment |
| `OPENCLAW_GATEWAY_BIND` | `lan` | Allow gateway connections from the network |
| `OPENCLAW_GATEWAY_PASSWORD_FILE` | `/run/secrets/gateway_password` | Credential file path |
| `TELEGRAM_BOT_TOKEN_FILE` | `/run/secrets/telegram_bot_token` | Credential file path |
| `GATEWAY_OP_PROXY_URL` | `http://gateway:8080` | Gateway op-proxy endpoint for 1Password |
| `ANTHROPIC_BASE_URL` | `http://gateway:8080` | Route all LLM API calls through gateway |
| `TELEGRAM_API_BASE_URL` | `http://gateway:8080/telegram-api` | Route Telegram API through gateway |
| `OPENCLAW_BOT_NAME` | `agentshroud_bot` | Bot display name |
| `OPENCLAW_BOT_EMAIL` | `agentshroud.ai@icloud.com` | Bot email identity |
| `OPENCLAW_DISABLE_HOST_FILESYSTEM` | `true` | Disable host filesystem access |
| `OPENCLAW_SANDBOX_MODE` | `strict` | OpenClaw sandbox enforcement |
| `OPENCLAW_DISABLE_BONJOUR` | `1` | Disable mDNS/Bonjour discovery |

### Loaded at Startup via 1Password op-proxy

These are set by `start-agentshroud.sh` during startup (with retry logic):

| Variable | 1Password Reference | Purpose |
|----------|--------------------|----|
| `ANTHROPIC_OAUTH_TOKEN` | `op://Agent Shroud Bot Credentials/AgentShroud - Anthropic Claude OAuth Token/claude oath token` | Claude OAuth token |
| `BRAVE_API_KEY` | `op://Agent Shroud Bot Credentials/<item-id>/brave search api key` | Brave Search API |
| `ICLOUD_APP_PASSWORD` | `op://Agent Shroud Bot Credentials/<item-id>/agentshroud app-specific password` | iCloud email (background) |

---

## Environment Variable Index

See individual env var notes:

- [[Environment Variables/GATEWAY_AUTH_TOKEN]]
- [[Environment Variables/OP_SERVICE_ACCOUNT_TOKEN]]
- [[Environment Variables/ANTHROPIC_BASE_URL]]
- [[Environment Variables/TELEGRAM_API_BASE_URL]]
- [[Environment Variables/TELEGRAM_BOT_TOKEN]]
- [[Environment Variables/OPENCLAW_GATEWAY_PASSWORD]]
- [[Environment Variables/GATEWAY_URL]]
- [[Environment Variables/AGENTSHROUD_CONFIG]]
- [[Environment Variables/AGENTSHROUD_MODE]]
- [[Environment Variables/LOG_LEVEL]]
- [[Environment Variables/GATEWAY_OP_PROXY_URL]]
- [[Environment Variables/OPENCLAW_DISABLE_HOST_FILESYSTEM]]
- [[Environment Variables/OPENCLAW_SANDBOX_MODE]]
- [[Environment Variables/HTTP_PROXY]]

---

## Security Notes

- **Never** put secrets in environment variables directly; use Docker secrets files
- The only credentials that go in `docker-compose.yml` environment are file paths (`*_FILE` variables)
- `AGENTSHROUD_MODE=monitor` disables all security enforcement — only for debugging, never in production
- `ANTHROPIC_BASE_URL` pointing to the gateway is critical for LLM call interception

---

## Related Notes

- [[Configuration/agentshroud.yaml]] — Config file (overrides some defaults)
- [[Configuration/docker-compose.yml]] — Where these variables are set
- [[Startup Sequence]] — How secrets are loaded at boot
- [[Runbooks/First Time Setup]] — Required secrets to create before first run
