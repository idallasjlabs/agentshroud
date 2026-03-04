---
title: agentshroud-bot
type: container
tags: [container, bot, nodejs, openclaw]
related: [Configuration/docker-compose.yml, Configuration/Dockerfile.bot, Architecture Overview, Containers & Services/agentshroud-gateway]
status: documented
---

# agentshroud-bot

## Summary

The OpenClaw AI agent container. Runs the autonomous agent (Node.js 22 + OpenClaw platform). Has NO direct internet access — all outbound connections route through the gateway. Must wait for `agentshroud-gateway` to be healthy before starting.

## Container Properties

| Property | Value |
|----------|-------|
| Container name | `agentshroud-bot` |
| Hostname | `agentshroud` |
| Image built from | `docker/Dockerfile.agentshroud` |
| Base image | `node:22-bookworm-slim` |
| User | `node` (UID 1000) |
| Restart policy | `unless-stopped` |
| Stop grace period | 15 seconds |
| Depends on | `gateway: service_healthy` |

## Ports

| Exposed Port | Host Binding | Purpose |
|--------------|--------------|---------|
| 18789 | `127.0.0.1:18790` | OpenClaw management UI |

> Note: Internal port 18789, host port 18790 (due to port conflict workaround).

## Network

| Network | Role |
|---------|------|
| `agentshroud-isolated` | Only network — bot is isolated from host |

> The bot has no `agentshroud-internal` network access. It can only reach the gateway.

## Volumes

| Volume | Mount Path | Purpose |
|--------|-----------|---------|
| `agentshroud-config` | `/home/node/.agentshroud` | Config, API keys, memory, settings |
| `agentshroud-workspace` | `/home/node/agentshroud/workspace` | Files agent creates/modifies |
| `agentshroud-ssh` | `/home/node/.ssh` | SSH keypair |
| `agentshroud-browsers` | `/home/node/.cache/ms-playwright` | Playwright browser binaries |
| `../branding` | `/app/branding` | ro — Branding assets |

## Secrets

| Secret | Mount | Used For |
|--------|-------|---------|
| `gateway_password` | `/run/secrets/gateway_password` | Bot → gateway authentication |
| `telegram_bot_token` | `/run/secrets/telegram_bot_token` | Telegram Bot API |

## Key Environment Variables

| Variable | Value | Purpose |
|----------|-------|---------|
| `ANTHROPIC_BASE_URL` | `http://gateway:8080` | Route LLM → gateway |
| `TELEGRAM_API_BASE_URL` | `http://gateway:8080/telegram-api` | Route Telegram → gateway |
| `GATEWAY_OP_PROXY_URL` | `http://gateway:8080` | 1Password proxy via gateway |
| `OPENCLAW_DISABLE_HOST_FILESYSTEM` | `true` | No host filesystem access |
| `OPENCLAW_SANDBOX_MODE` | `strict` | Full sandbox enforcement |
| `OPENCLAW_GATEWAY_BIND` | `lan` | Allow gateway to connect internally |

## Security Hardening

| Measure | Detail |
|---------|--------|
| `no-new-privileges` | No privilege escalation |
| `seccomp` | `./seccomp/agentshroud-seccomp.json` |
| `cap_drop: ALL` | No Linux capabilities |
| `read_only: true` | Read-only root filesystem |
| Credential isolation | Only `gateway_password` and `telegram_bot_token` secrets |

## Resource Limits

| Resource | Limit |
|----------|-------|
| Memory | 4 GB |
| Swap | 4 GB (no additional swap) |
| CPUs | 2.0 |
| PIDs | 512 |

## tmpfs Mounts

| Path | Options |
|------|---------|
| `/tmp` | `noexec,nosuid,size=500m` |
| `/var/tmp` | `noexec,nosuid,size=100m` |
| `/home/node/.npm` | `noexec,nosuid,size=200m` |
| `/home/node/.local` | `noexec,nosuid,size=100m` |
| `/home/node/.config` | `noexec,nosuid,size=100m,uid=1000,gid=1000` |

## Health Check

```
curl -f http://localhost:18789/api/health
interval: 30s | timeout: 10s | start_period: 60s | retries: 3
```

Note: 60s start_period because Playwright and init-openclaw-config.sh take time on first boot.

## Extra Hosts

```yaml
extra_hosts:
  - "host.docker.internal:host-gateway"
```

Allows the bot to reach MCP servers running on the macOS host (e.g., `mac-messages-mcp` on port 8200).

## Logs

```bash
# Live logs
docker logs -f agentshroud-bot

# Startup sequence
docker logs agentshroud-bot 2>&1 | grep "\[startup\]"
```

## Related Notes

- [[Configuration/Dockerfile.bot]] — Image build process
- [[Configuration/docker-compose.yml]] — Full orchestration
- [[Containers & Services/agentshroud-gateway]] — Gateway container (required dependency)
- [[JavaScript/mcp-proxy-wrapper.js|mcp-proxy-wrapper.js]] — MCP intercept in this container
- [[Startup Sequence]] — Detailed boot sequence
