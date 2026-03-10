---
title: All Environment Variables
type: index
tags: [#type/index, #type/env-var]
related: ["[[agentshroud-gateway]]", "[[agentshroud-bot]]", "[[docker-compose.yml]]"]
status: active
last_reviewed: 2026-03-09
---

# All Environment Variables

## Gateway Container

| Variable | Required | Default | Description | Note |
|----------|----------|---------|-------------|------|
| [[GATEWAY_AUTH_TOKEN_FILE]] | Yes | — | Path to gateway password secret | `/run/secrets/gateway_password` |
| [[AGENTSHROUD_MODE]] | No | `enforce` | `monitor` disables all blocking globally | Dev/debug only |
| [[PROXY_ALLOWED_NETWORKS]] | No | `172.11.0.0/16` | CIDRs allowed to use CONNECT proxy | Comma-separated |
| `AGENTSHROUD_DATA_DIR` | No | `/app/data` | Path to persistent data directory | Must be writable volume |
| `AGENTSHROUD_CONFIG` | No | `/app/agentshroud.yaml` | Explicit config file path | |
| `LOG_LEVEL` | No | `INFO` | Logging verbosity | DEBUG/INFO/WARNING/ERROR |
| `PYTHONUNBUFFERED` | No | `1` | Ensures logs are not buffered | Always set to 1 |
| `PYTHONDONTWRITEBYTECODE` | No | `1` | No .pyc files on read-only rootfs | |
| `OP_SERVICE_ACCOUNT_TOKEN_FILE` | No | — | 1Password service account (unused — personal auth used instead) | |

## Bot Container

| Variable | Required | Default | Description | Note |
|----------|----------|---------|-------------|------|
| [[TELEGRAM_API_BASE_URL]] | Yes | — | Routes Telegram API to gateway | `http://gateway:8080/telegram-api` |
| [[ANTHROPIC_BASE_URL]] | Yes | — | Routes LLM calls to gateway | `http://gateway:8080` |
| [[HTTP_PROXY]] | Yes | — | Routes HTTP through CONNECT proxy | `http://gateway:8181` |
| [[HTTPS_PROXY]] | Yes | — | Routes HTTPS through CONNECT proxy | `http://gateway:8181` |
| `NO_PROXY` | No | — | Bypasses proxy for these hosts | `gateway,localhost,127.0.0.1` |
| `OPENCLAW_GATEWAY_PASSWORD_FILE` | Yes | — | Path to gateway password secret | `/run/secrets/gateway_password` |
| `TELEGRAM_BOT_TOKEN_FILE` | Yes | — | Path to Telegram bot token secret | `/run/secrets/telegram_bot_token` |
| `NODE_ENV` | No | `production` | Node.js environment | |
| `OPENCLAW_GATEWAY_BIND` | No | — | Gateway binding mode | `lan` |
| `GATEWAY_OP_PROXY_URL` | No | — | op-proxy URL | `http://gateway:8080` |
| `OPENCLAW_BOT_NAME` | No | — | Bot identifier | `agentshroud_bot` |
| `OPENCLAW_BOT_EMAIL` | No | — | Bot email for channels | |
| `OPENCLAW_DISABLE_HOST_FILESYSTEM` | No | — | Disable host FS access | `true` |
| `OPENCLAW_SANDBOX_MODE` | No | — | Sandbox strictness | `strict` |
| `OPENCLAW_DISABLE_BONJOUR` | No | — | Disable mDNS discovery | `1` |

## Docker Secrets (Available as Files in `/run/secrets/`)

| Secret Name | File | Container | Purpose |
|-------------|------|-----------|---------|
| `gateway_password` | `docker/secrets/gateway_password.txt` | Both | Shared auth token |
| `telegram_bot_token` | `docker/secrets/telegram_bot_token_production.txt` | Both | Telegram Bot API token |
| `anthropic_oauth_token` | `docker/secrets/anthropic_oauth_token.txt` | Both | Anthropic OAuth (optional) |
| `1password_bot_email` | `docker/secrets/1password_bot_email.txt` | Gateway | 1Password personal email |
| `1password_bot_master_password` | `docker/secrets/1password_bot_master_password.txt` | Gateway | 1Password master password |
| `1password_bot_secret_key` | `docker/secrets/1password_bot_secret_key.txt` | Gateway | 1Password secret key |

> [!DANGER] Docker secrets are mounted from `docker/secrets/*.txt` files on the host. These are plaintext. Ensure this directory is not committed to git and is not world-readable.
