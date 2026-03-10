---
title: agentshroud-gateway
type: container
tags: [#type/container, #status/critical]
related: ["[[agentshroud-bot]]", "[[docker-compose.yml]]", "[[Architecture Overview]]", "[[lifespan]]", "[[main]]"]
status: active
last_reviewed: 2026-03-09
---

# agentshroud-gateway — Security Proxy Container

## Overview

The gateway is the security brain of AgentShroud. It is the SOLE egress point for all container traffic. Every message, API call, and file transfer passes through it.

## Image Details

| Property | Value |
|----------|-------|
| Base image | `python:3.13-slim` (SHA256-pinned) |
| Build method | Multi-stage (builder + runtime) |
| Dockerfile | `gateway/Dockerfile` |
| Container name | `agentshroud-gateway` |
| Hostname | `gateway` |
| User | Non-root (`nobody` or custom non-root UID) |
| Read-only rootfs | Yes |

## Port Mappings

| Container Port | Host Binding | Protocol | Purpose |
|----------------|-------------|----------|---------|
| 8080 | `127.0.0.1:8080` | HTTP | Main API (Telegram proxy, LLM proxy, management) |
| 8181 | Internal only | HTTP CONNECT | Egress proxy for bot |
| 5353 | Internal only | UDP/TCP DNS | DNS forwarder with blocklist |

## Volume Mounts

| Volume | Mount Point | Mode | Purpose |
|--------|------------|------|---------|
| `../agentshroud.yaml` | `/app/agentshroud.yaml` | RO | Configuration |
| `agentshroud-ssh` | `/var/agentshroud-ssh` | RO | SSH keys for SSHProxy |
| `gateway-data` | `/app/data` | RW | Audit DB, ledger, approvals |
| `../web` | `/app/web` | RO | Dashboard HTML/CSS |
| `../gateway` | `/app/gateway` | RO | Python source (live-mounted) |
| `agentshroud-workspace` | `/data/bot-workspace` | RO | Bot workspace read access |

## Environment Variables

See [[All Environment Variables]] gateway section. Key vars:

| Variable | Value |
|----------|-------|
| [[GATEWAY_AUTH_TOKEN_FILE]] | `/run/secrets/gateway_password` |
| [[PROXY_ALLOWED_NETWORKS]] | `172.11.0.0/16,172.12.0.0/16` |
| `LOG_LEVEL` | `INFO` |
| `PYTHONUNBUFFERED` | `1` |

## Secrets

| Secret | Path | Purpose |
|--------|------|---------|
| `gateway_password` | `/run/secrets/gateway_password` | Auth token |
| `telegram_bot_token` | `/run/secrets/telegram_bot_token` | Telegram API |
| `anthropic_oauth_token` | `/run/secrets/anthropic_oauth_token` | Anthropic (optional) |
| `1password_bot_*` | `/run/secrets/1password_bot_*` | 1Password auth |

## Security Hardening

```yaml
security_opt:
  - no-new-privileges:true
  - seccomp=./seccomp/gateway-seccomp.json
cap_drop:
  - ALL
read_only: true
mem_limit: 1280m
cpus: 1.0
pids_limit: 100
dns: [8.8.8.8, 8.8.4.4]  # Direct resolution (gateway is sole egress point)
```

## Networks

- `agentshroud-internal` (172.10.0.0/16) — internet access
- `agentshroud-isolated` (172.11.0.0/16) — bot ↔ gateway

## Health Check

```bash
python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/status').read()"
```

Interval: 30s, Timeout: 10s, Retries: 3, Start period: 10s

## Log Commands

```bash
# View logs
docker logs agentshroud-gateway --tail 100

# Follow live
docker logs agentshroud-gateway -f

# Check Telegram polling
docker logs agentshroud-gateway | grep getUpdates | tail -5

# Check for errors
docker logs agentshroud-gateway | grep ERROR
```

## Restart Command

```bash
docker compose -f docker/docker-compose.yml restart gateway
```

## Common Failure Modes

| Symptom | Cause | Fix |
|---------|-------|-----|
| Container exits immediately | Bad config YAML | `docker logs agentshroud-gateway` → fix YAML |
| Health check failing | PII init failure (spaCy) | Rebuild image |
| 401 on all bot calls | Wrong/missing gateway password | Check `docker/secrets/gateway_password.txt` |
| DNS resolution failing | Port 5353 conflict | Check for other DNS on 5353 |

See [[Gateway Startup Failure]] for detailed troubleshooting.
