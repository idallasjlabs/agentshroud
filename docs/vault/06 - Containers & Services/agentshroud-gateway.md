---
title: agentshroud-gateway
type: container
tags: [container, gateway, python, fastapi]
related: [Configuration/docker-compose.yml, Configuration/Dockerfile.gateway, Architecture Overview, Startup Sequence]
status: documented
---

# agentshroud-gateway

## Summary

The core security gateway container. All traffic between the OpenClaw bot and the external world passes through this container. Runs the Python 3.13 FastAPI application.

## Container Properties

| Property | Value |
|----------|-------|
| Container name | `agentshroud-gateway` |
| Hostname | `gateway` |
| Image built from | `gateway/Dockerfile` |
| Base image | `python:3.13-slim` |
| User | `agentshroud` (UID 1000) |
| Restart policy | `unless-stopped` |
| Stop grace period | 15 seconds |

## Ports

| Exposed Port | Host Binding | Purpose |
|--------------|--------------|---------|
| 8080 | `127.0.0.1:8080` | Gateway API (authentication required) |
| 8181 | Not exposed externally | HTTP CONNECT proxy (internal) |

## Networks

| Network | Role |
|---------|------|
| `agentshroud-internal` | Accessible from host (localhost:8080) |
| `agentshroud-isolated` | Internal communication with bot container |

## Volumes

| Volume / Bind | Mount Path | Mode | Purpose |
|---------------|-----------|------|---------|
| `../agentshroud.yaml` | `/app/agentshroud.yaml` | ro | Master config |
| `agentshroud-ssh` | `/var/agentshroud-ssh` | ro | SSH keys for SSH proxy |
| `gateway-data` | `/app/data` | rw | SQLite ledger database |
| `../web` | `/app/web` | ro | Web management assets |
| `agentshroud-workspace` | `/data/bot-workspace` | ro | Bot workspace read access |

## Secrets

| Secret | Mount | Used For |
|--------|-------|---------|
| `gateway_password` | `/run/secrets/gateway_password` | Auth token (read by `GATEWAY_AUTH_TOKEN_FILE`) |
| `1password_service_account` | `/run/secrets/1password_service_account` | 1Password CLI auth |

## Environment Variables

| Variable | Value |
|----------|-------|
| `PYTHONUNBUFFERED` | `1` |
| `LOG_LEVEL` | `INFO` |
| `PYTHONDONTWRITEBYTECODE` | `1` |
| `GATEWAY_AUTH_TOKEN_FILE` | `/run/secrets/gateway_password` |
| `OP_SERVICE_ACCOUNT_TOKEN_FILE` | `/run/secrets/1password_service_account` |

## Security Hardening

| Measure | Detail |
|---------|--------|
| `no-new-privileges` | Prevents privilege escalation |
| `seccomp` | `./seccomp/gateway-seccomp.json` profile |
| `cap_drop: ALL` | No Linux capabilities |
| `read_only: true` | Read-only root filesystem |
| tmpfs `/tmp` | `noexec,nosuid,size=100m` |
| tmpfs `/var/tmp` | `noexec,nosuid,size=50m` |

## Resource Limits

| Resource | Limit |
|----------|-------|
| Memory | 1280 MB |
| Swap | 1280 MB (no additional swap) |
| CPUs | 1.0 |
| PIDs | 100 |

## Health Check

```
python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/status').read()"
interval: 30s | timeout: 10s | start_period: 10s | retries: 3
```

## tmpfs Mounts

| Path | Options |
|------|---------|
| `/tmp` | `noexec,nosuid,size=100m` |
| `/var/tmp` | `noexec,nosuid,size=50m` |

## Key Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/status` | GET | Health check (no auth required) |
| `/health` | GET | Detailed health (auth required) |
| `/forward` | POST | Main message forwarding |
| `/admin/*` | Various | Management API |
| `/ws` | WS | WebSocket approval queue / dashboard |
| `/credentials/op-proxy` | POST | 1Password credential proxy |
| `/telegram-api/*` | Various | Telegram API proxy |

## Logs

```bash
# Live logs
docker logs -f agentshroud-gateway

# Tail last 100 lines
docker logs --tail=100 agentshroud-gateway

# Search for errors
docker logs agentshroud-gateway 2>&1 | grep -i error
```

## Related Notes

- [[Configuration/Dockerfile.gateway]] — Image build process
- [[Configuration/docker-compose.yml]] — Full orchestration config
- [[Containers & Services/agentshroud-bot]] — The bot container
- [[Containers & Services/networks]] — Network details
- [[Architecture Overview]] — How this fits in the system
