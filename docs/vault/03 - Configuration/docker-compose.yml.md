---
title: docker-compose.yml
type: config
file_path: docker/docker-compose.yml
tags: [docker, containers, configuration, deployment]
related: [Containers & Services/agentshroud-gateway, Containers & Services/agentshroud-bot, Configuration/Dockerfile.gateway]
status: documented
---

# docker-compose.yml

**Location:** `docker/docker-compose.yml`
**Purpose:** Primary Docker Compose file defining both containers, networks, volumes, and secrets.

## Services

### gateway (agentshroud-gateway)

| Property | Value |
|----------|-------|
| Build context | `..` (repo root) |
| Dockerfile | `gateway/Dockerfile` |
| Container name | `agentshroud-gateway` |
| Hostname | `gateway` |
| Ports | `127.0.0.1:8080:8080` |
| Restart | `unless-stopped` |
| Stop grace | 15 seconds |
| Networks | `agentshroud-internal` + `agentshroud-isolated` |
| Memory limit | 1280 MB |
| CPU limit | 1.0 |
| PID limit | 100 |
| Root filesystem | Read-only |
| Seccomp | `./seccomp/gateway-seccomp.json` |
| Capabilities | ALL dropped |

**Volumes:**
| Host/Volume | Container Path | Mode |
|-------------|---------------|------|
| `../agentshroud.yaml` | `/app/agentshroud.yaml` | ro |
| `agentshroud-ssh` | `/var/agentshroud-ssh` | ro |
| `gateway-data` | `/app/data` | rw |
| `../web` | `/app/web` | ro |
| `agentshroud-workspace` | `/data/bot-workspace` | ro |

**Secrets mounted:**
- `gateway_password` → `/run/secrets/gateway_password`
- `1password_service_account` → `/run/secrets/1password_service_account`

**Environment:**
```yaml
PYTHONUNBUFFERED: "1"
LOG_LEVEL: INFO
PYTHONDONTWRITEBYTECODE: "1"
GATEWAY_AUTH_TOKEN_FILE: /run/secrets/gateway_password
OP_SERVICE_ACCOUNT_TOKEN_FILE: /run/secrets/1password_service_account
```

**Health check:**
```
python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/status').read()"
interval: 30s | timeout: 10s | retries: 3 | start_period: 10s
```

---

### agentshroud (agentshroud-bot)

| Property | Value |
|----------|-------|
| Build context | `..` (repo root) |
| Dockerfile | `docker/Dockerfile.agentshroud` |
| Container name | `agentshroud-bot` |
| Hostname | `agentshroud` |
| Ports | `127.0.0.1:18790:18789` |
| Restart | `unless-stopped` |
| Stop grace | 15 seconds |
| Networks | `agentshroud-isolated` only |
| Memory limit | 4 GB |
| CPU limit | 2.0 |
| PID limit | 512 |
| Root filesystem | Read-only |
| Seccomp | `./seccomp/agentshroud-seccomp.json` |
| Capabilities | ALL dropped |
| Depends on | `gateway: service_healthy` |

**Volumes:**
| Volume | Container Path | Purpose |
|--------|---------------|---------|
| `agentshroud-config` | `/home/node/.agentshroud` | Config, API keys, memory |
| `agentshroud-workspace` | `/home/node/agentshroud/workspace` | Agent work files |
| `agentshroud-ssh` | `/home/node/.ssh` | SSH keys |
| `agentshroud-browsers` | `/home/node/.cache/ms-playwright` | Playwright browsers |
| `../branding` | `/app/branding` | ro |

**Secrets:**
- `gateway_password`
- `telegram_bot_token`

**Key environment variables:**
```yaml
NODE_ENV: production
OPENCLAW_GATEWAY_BIND: lan
ANTHROPIC_BASE_URL: http://gateway:8080
TELEGRAM_API_BASE_URL: http://gateway:8080/telegram-api
GATEWAY_OP_PROXY_URL: http://gateway:8080
OPENCLAW_DISABLE_HOST_FILESYSTEM: "true"
OPENCLAW_SANDBOX_MODE: strict
```

**Health check:**
```
curl -f http://localhost:18789/api/health
interval: 30s | timeout: 10s | retries: 3 | start_period: 60s
```

---

## Networks

| Network | Subnet | Internal | Purpose |
|---------|--------|----------|---------|
| `agentshroud-internal` | 172.20.0.0/16 | false | Gateway ↔ host access |
| `agentshroud-isolated` | 172.21.0.0/16 | false* | Bot ↔ gateway only |

*Note: `internal: false` is a Docker Desktop macOS workaround. Bot isolation is enforced via `HTTP_PROXY` and `ANTHROPIC_BASE_URL` routing.

---

## Volumes

| Volume | Purpose |
|--------|---------|
| `gateway-data` | SQLite ledger database |
| `agentshroud-config` | Bot config, memory, settings |
| `agentshroud-workspace` | Files the agent creates/edits |
| `agentshroud-ssh` | SSH keypair shared between gateway and bot |
| `agentshroud-browsers` | Playwright browser binaries |

---

## Secrets Files

Secret files must exist in `docker/secrets/` before starting:

| Secret Name | File |
|-------------|------|
| `gateway_password` | `docker/secrets/gateway_password.txt` |
| `1password_service_account` | `docker/secrets/1password_service_account` |
| `telegram_bot_token` | `docker/secrets/telegram_bot_token_production.txt` |

---

## Alternate Compose Files

| File | Use Case |
|------|---------|
| `docker-compose.secure.yml` | Hardened production (additional security opts) |
| `docker-compose.sidecar.yml` | Proxy-only minimal deployment |
| `docker-compose.marvin-prod.yml` | Marvin host production |
| `docker-compose.marvin-test.yml` | Marvin host testing |
| `docker-compose.trillian.yml` | Trillian (general purpose) host |
| `docker-compose.pi.yml` | Raspberry Pi deployment |

---

## Related Notes

- [[Containers & Services/agentshroud-gateway]] — Gateway container deep-dive
- [[Containers & Services/agentshroud-bot]] — Bot container deep-dive
- [[Containers & Services/networks]] — Network details
- [[Containers & Services/volumes]] — Volume details
- [[Configuration/Dockerfile.gateway]] — Gateway image build
- [[Configuration/Dockerfile.bot]] — Bot image build
- [[Runbooks/First Time Setup]] — Pre-requisites and setup
