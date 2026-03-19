---
title: docker-compose.yml
type: config
file_path: /Users/ijefferson.admin/Development/agentshroud/docker/docker-compose.yml
tags: [#type/config, #status/critical]
related: ["[[agentshroud-gateway]]", "[[agentshroud-bot]]", "[[Architecture Overview]]", "[[First Time Setup]]"]
status: active
last_reviewed: 2026-03-09
---

# docker-compose.yml — Container Topology

Located at `docker/docker-compose.yml`. Run from repo root:

```bash
docker compose -f docker/docker-compose.yml up -d
```

## Services

### `gateway`

| Property | Value |
|----------|-------|
| Image | `agentshroud-gateway:latest` |
| Dockerfile | `gateway/Dockerfile` |
| Container | `agentshroud-gateway` |
| Hostname | `gateway` |
| Port | `127.0.0.1:8080→8080` |
| Networks | `agentshroud-internal` + `agentshroud-isolated` |
| Memory limit | 1280 MB |
| CPU limit | 1.0 |
| PIDs limit | 100 |
| Restart | `unless-stopped` |
| Read-only rootfs | `yes` |
| Capabilities | ALL dropped |
| Seccomp | `./seccomp/gateway-seccomp.json` |
| DNS | 8.8.8.8, 8.8.4.4 (direct resolution) |

**Health check:**
```yaml
test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/status').read()"]
interval: 30s
timeout: 10s
retries: 3
start_period: 10s
```

### `bot`

| Property | Value |
|----------|-------|
| Image | `agentshroud-bot:latest` |
| Dockerfile | `docker/bots/openclaw/Dockerfile` |
| Container | `agentshroud-bot` |
| Hostname | `agentshroud` (matches `bots.openclaw.hostname`) |
| Port | `127.0.0.1:18790→18789` |
| Networks | `agentshroud-isolated` + `agentshroud-console` |
| Memory limit | 4 GB |
| CPU limit | 2.0 |
| PIDs limit | 512 |
| Restart | `unless-stopped` |
| Read-only rootfs | `yes` |
| tmpfs | `/tmp` (500MB), `/var/tmp` (100MB), `~/.npm` (200MB), `~/.local` (100MB), `~/.config` (100MB) |
| Depends on | `gateway: service_healthy` |

**Key env vars:**
```yaml
TELEGRAM_API_BASE_URL: http://gateway:8080/telegram-api
ANTHROPIC_BASE_URL: http://gateway:8080
HTTP_PROXY: http://gateway:8181
HTTPS_PROXY: http://gateway:8181
```

## Networks

| Network | Subnet | Internet | Purpose |
|---------|--------|----------|---------|
| `agentshroud-internal` | `172.10.0.0/16` | Yes | Gateway egress |
| `agentshroud-isolated` | `172.11.0.0/16` | No (`internal: true`) | Bot ↔ Gateway only |
| `agentshroud-console` | `172.12.0.0/16` | No masquerade | Bot UI access |

## Volumes

| Volume | Mounted To | Purpose |
|--------|-----------|---------|
| `gateway-data` | `/app/data` | Audit DB, ledger, approvals, drift |
| `agentshroud-config` | `/home/node/.agentshroud` | OpenClaw config, apply-patches output |
| `agentshroud-workspace` | `/home/node/agentshroud/workspace` (bot) + `/data/bot-workspace` (gateway, RO) | Agent workspace |
| `agentshroud-ssh` | `/var/agentshroud-ssh` (gateway, RO) + `/home/node/.ssh` (bot) | SSH keys |
| `agentshroud-browsers` | `/home/node/.cache/ms-playwright` | Playwright browser cache |

## Secrets

All secrets are Docker secret files from `docker/secrets/`:

| Secret | File | Used By |
|--------|------|---------|
| `gateway_password` | `gateway_password.txt` | Gateway auth token + bot auth |
| `telegram_bot_token` | `telegram_bot_token_production.txt` | Gateway Telegram proxy |
| `anthropic_oauth_token` | `anthropic_oauth_token.txt` | Gateway LLM proxy (optional) |
| `1password_bot_email` | `1password_bot_email.txt` | Gateway 1Password auth |
| `1password_bot_master_password` | `1password_bot_master_password.txt` | Gateway 1Password auth |
| `1password_bot_secret_key` | `1password_bot_secret_key.txt` | Gateway 1Password auth |

> [!DANGER] The `docker/secrets/` directory contains plaintext credentials. Never commit these files. `docker/.gitignore` should exclude them — verify with `git status docker/secrets/`.

## extra_hosts

Both containers have static host entries:
```yaml
extra_hosts:
  - "host.docker.internal:host-gateway"
  - "marvin:192.168.7.137"
  - "trillian:192.168.7.97"
  - "raspberrypi:192.168.7.25"
```

> [!WARNING] `marvin`, `trillian`, `raspberrypi` IP addresses are hardcoded. Update if home lab IPs change.
