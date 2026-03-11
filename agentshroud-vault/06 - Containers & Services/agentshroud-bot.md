---
title: agentshroud-bot
type: container
tags: [#type/container, #status/critical]
related: ["[[agentshroud-gateway]]", "[[docker-compose.yml]]", "[[patch-telegram-sdk.sh]]", "[[apply-patches.js]]", "[[TELEGRAM_API_BASE_URL]]"]
status: active
last_reviewed: 2026-03-09
---

# agentshroud-bot — OpenClaw Agent Container

## Overview

The AI agent container. Runs OpenClaw (a Claude-powered autonomous agent with Telegram integration). Fully network-isolated — no direct internet, all egress through the gateway.

## Image Details

| Property | Value |
|----------|-------|
| Base image | `node:22-bookworm-slim` (SHA256-pinned) |
| Dockerfile | `docker/bots/openclaw/Dockerfile` |
| Container name | `agentshroud-bot` |
| Hostname | `agentshroud` (matches `bots.openclaw.hostname`) |
| Runtime | Node.js 22 + OpenClaw `2026.3.2` |
| User | `node` (UID 1000) |
| Read-only rootfs | Yes |

## Port Mappings

| Container Port | Host Binding | Protocol | Purpose |
|----------------|-------------|----------|---------|
| 18789 | `127.0.0.1:18790` | HTTP | OpenClaw API (health, chat, webhook, UI) |

## Volume Mounts

| Volume | Mount Point | Mode | Purpose |
|--------|------------|------|---------|
| `agentshroud-config` | `/home/node/.agentshroud` | RW | OpenClaw config, workspace |
| `agentshroud-workspace` | `/home/node/agentshroud/workspace` | RW | Agent workspace files |
| `agentshroud-ssh` | `/home/node/.ssh` | RW | SSH keys for SSH targets |
| `agentshroud-browsers` | `/home/node/.cache/ms-playwright` | RW | Playwright browser cache |
| `../branding` | `/app/branding` | RO | Bot branding files |
| `../memory-backups` | `/app/memory-backups` | RW | Memory backup for persistence |

## tmpfs Mounts (Ephemeral)

| Path | Size | Flags |
|------|------|-------|
| `/tmp` | 500MB | noexec,nosuid |
| `/var/tmp` | 100MB | noexec,nosuid |
| `/home/node/.npm` | 200MB | noexec,nosuid |
| `/home/node/.local` | 100MB | noexec,nosuid |
| `/home/node/.config` | 100MB | noexec,nosuid |
| `/home/node/.ssh-tmp` | 10MB | nosuid |

## Environment Variables

See [[All Environment Variables]] bot section. Critical:

| Variable | Value |
|----------|-------|
| [[TELEGRAM_API_BASE_URL]] | `http://gateway:8080/telegram-api` |
| [[ANTHROPIC_BASE_URL]] | `http://gateway:8080` |
| [[HTTP_PROXY]] | `http://gateway:8181` |
| [[HTTPS_PROXY]] | `http://gateway:8181` |
| `NO_PROXY` | `gateway,localhost,127.0.0.1` |

## Build-Time Patches Applied

During `docker build`:

1. `patch-anthropic-sdk.sh` — routes Anthropic SDK to `ANTHROPIC_BASE_URL`
2. `patch-telegram-sdk.sh` — routes grammY and OpenClaw dist file downloads to `TELEGRAM_API_BASE_URL`
3. Playwright install with Chromium
4. 1Password CLI install

See [[patch-telegram-sdk.sh]] for detail on the critical file download patch.

## Runtime Patches Applied (at container start)

`apply-patches.js` runs before OpenClaw starts:
- Sets model, maxTokens, denied tools
- Sets collaborator workspace to writable path (`.agentshroud/collaborator-workspace`)
- Migration: updates stale configs with old workspace path

See [[apply-patches.js]] for detail.

## Network

- `agentshroud-isolated` (172.11.0.0/16) — bot ↔ gateway only, no internet
- `agentshroud-console` (172.12.0.0/16) — UI access

## Security Hardening

```yaml
security_opt:
  - no-new-privileges:true
  - seccomp=./seccomp/agentshroud-seccomp.json
cap_drop:
  - ALL
read_only: true
mem_limit: 4g
cpus: 2.0
pids_limit: 512
```

## Health Check

```bash
curl -sf http://localhost:18789/ -o /dev/null || exit 1
```

Interval: 30s, Timeout: 10s, Retries: 3, Start period: 60s (OpenClaw takes time to start)

## Depends On

`gateway: service_healthy` — bot does not start until gateway passes health check.

## Log Commands

```bash
# View logs
docker logs agentshroud-bot --tail 100

# Telegram messages flowing?
docker logs agentshroud-bot | grep "sendMessage ok"

# Startup complete?
docker logs agentshroud-bot | grep -i "ready\|startup\|telegram"
```

## Restart Command

```bash
docker compose -f docker/docker-compose.yml restart bot
```

## Common Failure Modes

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Failed to download media" | File download URL not patched | Rebuild bot image |
| Bot healthy but no Telegram | Token invalid/missing | Check `docker/secrets/telegram_bot_token_production.txt` |
| `ENOENT mkdir collaborator-workspace` | Old apply-patches.js | Rebuild bot image |
| Memory errors | `mem_limit: 4g` exceeded | Check `docker stats agentshroud-bot` |

See [[Photo Download Failure]] for the most common issue.
