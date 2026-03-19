---
title: volumes
type: infrastructure
tags: [storage, docker, persistence]
related: [Configuration/docker-compose.yml, Containers & Services/agentshroud-gateway, Containers & Services/agentshroud-bot]
status: documented
---

# Docker Volumes

## Volume Inventory

| Volume | Driver | Mounted In | Path | Purpose |
|--------|--------|-----------|------|---------|
| `gateway-data` | local | gateway | `/app/data` | SQLite audit ledger |
| `agentshroud-config` | local | bot | `/home/node/.agentshroud` | OpenClaw config, API keys, memory |
| `agentshroud-workspace` | local | gateway (ro), bot | `/data/bot-workspace`, `/home/node/agentshroud/workspace` | Agent work files |
| `agentshroud-ssh` | local | gateway (ro), bot | `/var/agentshroud-ssh`, `/home/node/.ssh` | SSH keypair |
| `agentshroud-browsers` | local | bot | `/home/node/.cache/ms-playwright` | Playwright browser binaries |

## Volume Details

### gateway-data

- **Contains:** SQLite database (`ledger.db`) — audit trail of all requests
- **Retention:** 90 days (auto-cleanup configured)
- **Backup:** Back up this volume to preserve audit history
- **Recovery:** Volume persists across container restarts; WAL mode is crash-safe

### agentshroud-config

- **Contains:** OpenClaw configuration, saved memories, API key cache, model settings
- **Symlinked:** `~/.openclaw → ~/.agentshroud` for OpenClaw CLI compatibility
- **Persistence:** Bot state (conversations, memories) lives here

### agentshroud-workspace

- **Contains:** Files the agent creates, reads, or modifies during tasks
- **Dual mount:** Gateway reads it (ro) to serve workspace files to iOS Shortcuts; bot writes it
- **Security:** No host directory mount — isolated Docker volume

### agentshroud-ssh

- **Contains:** `id_ed25519` SSH keypair generated on first bot startup
- **Cross-mount:** Gateway reads keys to authenticate SSH sessions; bot uses same keys
- **Note:** Keys are generated inside the bot container on first run, not pre-provisioned

### agentshroud-browsers

- **Contains:** Chromium browser binaries downloaded by Playwright
- **Size:** ~400-600 MB
- **Purpose:** Avoid re-downloading browsers on every container restart

## Inspecting Volumes

```bash
# List all volumes
docker volume ls | grep agentshroud

# Inspect a specific volume
docker volume inspect agentshroud_gateway-data

# View ledger file location
docker volume inspect agentshroud_gateway-data --format '{{.Mountpoint}}'
```

## Backup

```bash
# Backup gateway data (audit ledger)
docker run --rm \
  -v agentshroud_gateway-data:/data \
  -v $(pwd)/backup:/backup \
  alpine tar czf /backup/gateway-data-$(date +%Y%m%d).tar.gz /data

# Backup bot config
docker run --rm \
  -v agentshroud_agentshroud-config:/data \
  -v $(pwd)/backup:/backup \
  alpine tar czf /backup/bot-config-$(date +%Y%m%d).tar.gz /data
```

## Cleanup Warning

```bash
# WARNING: This destroys ALL data including audit history and bot memory
docker compose -f docker/docker-compose.yml down -v
```

## Related Notes

- [[Configuration/docker-compose.yml]] — Volume definitions
- [[Gateway Core/ledger.py|ledger.py]] — Uses gateway-data
- [[Containers & Services/agentshroud-gateway]] — Gateway volume mounts
- [[Containers & Services/agentshroud-bot]] — Bot volume mounts
