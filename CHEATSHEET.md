# AgentShroud Operations Cheat Sheet

> Quick reference for managing the `agentshroud-gateway` and `agentshroud-bot` containers.
> All commands run from `~/Development/agentshroud` on marvin unless noted.

---

## Container Basics

```bash
# Status
docker ps --filter name=agentshroud --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Logs
docker logs agentshroud-gateway --tail 50
docker logs agentshroud-bot --tail 50
docker logs agentshroud-gateway -f          # follow (live tail)

# Restart
docker restart agentshroud-gateway
docker restart agentshroud-bot

# Rebuild (picks up code + compose changes)
docker compose -f docker/docker-compose.yml -p agentshroud up -d --build gateway
docker compose -f docker/docker-compose.yml -p agentshroud up -d --build bot

# Recreate (picks up compose changes only — no image rebuild)
docker compose -f docker/docker-compose.yml -p agentshroud up -d --force-recreate gateway

# Full stack
docker compose -f docker/docker-compose.yml -p agentshroud up -d
docker compose -f docker/docker-compose.yml -p agentshroud down

# asb wrapper (auto-detects host profile)
scripts/asb up
scripts/asb down
scripts/asb rebuild
scripts/asb clean-rebuild
scripts/asb status
scripts/asb logs gateway
```

---

## Colima VM

> Colima is the Docker runtime on macOS. PROD runs as `ijefferson.admin`, DEV as `agentshroud-bot`.
> Both user homes are virtiofs-mounted so each instance stays fully isolated.

```bash
# Status
colima status

# Start (standard flags for this host)
colima start --cpu 8 --memory 10 --disk 60 --network-address

# Stop / restart
colima stop
colima stop && colima start --cpu 8 --memory 10 --disk 60 --network-address

# Verify both user homes are mounted (expect two virtiofs entries)
colima ssh -- mount | grep virtiofs

# SSH into the VM (for deep diagnostics)
colima ssh

# Disk usage inside VM
colima ssh -- df -h /

# Check what paths are visible to Docker (mounts config)
# ~/.colima/default/colima.yaml  →  mounts: section
# Both /Users/ijefferson.admin and /Users/agentshroud-bot must be listed

# If a container can't find a bind-mount path, the host path is not virtiofs-mounted.
# Fix: add the missing path to mounts: in colima.yaml, then restart Colima.
```

---

## Network Diagnostics

```bash
# DNS resolution inside containers
docker exec agentshroud-gateway getent hosts marvin
docker exec agentshroud-gateway getent hosts trillian
docker exec agentshroud-gateway getent hosts raspberrypi
docker exec agentshroud-bot getent hosts marvin

# TCP connectivity
docker exec agentshroud-gateway nc -zv 192.168.7.137 22    # SSH to marvin
docker exec agentshroud-gateway nc -zv 192.168.7.97 22     # SSH to trillian
docker exec agentshroud-gateway nc -zv 192.168.7.25 22     # SSH to raspberrypi

# Internet connectivity
docker exec agentshroud-gateway ping -c1 8.8.8.8
docker exec agentshroud-bot ping -c1 8.8.8.8

# Container network inspect
docker exec agentshroud-gateway ip addr show
docker exec agentshroud-gateway cat /etc/hosts
docker exec agentshroud-bot cat /etc/hosts
```

---

## OpenClaw (Bot) Management

```bash
# Version check
docker exec agentshroud-bot openclaw --version
docker exec agentshroud-bot cat /app/.openclaw-image-version

# Device management
docker exec agentshroud-bot openclaw devices list
docker exec agentshroud-bot openclaw devices approve <device-id>
docker exec agentshroud-bot openclaw devices approve-all

# Channel management
docker exec agentshroud-bot openclaw channels list

# Model status
docker exec agentshroud-bot openclaw models status

# Pairing
docker exec agentshroud-bot openclaw pairing list

# 1-click upgrade (via SOC API — re-applies SDK patches automatically)
curl -s -X POST http://localhost:8080/soc/v1/updates/bot/upgrade \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(cat /run/secrets/gateway_password 2>/dev/null || echo $AGENTSHROUD_TOKEN)" \
  -d '{"confirm": true}'

# Manual upgrade inside container
docker exec agentshroud-bot npm install -g openclaw@latest
# ⚠ Must re-apply SDK patches after manual upgrade:
docker exec agentshroud-bot sh /usr/local/bin/patch-anthropic-sdk.sh
docker exec agentshroud-bot sh /usr/local/bin/patch-telegram-sdk.sh
docker exec agentshroud-bot sh /usr/local/bin/patch-slack-sdk.sh
```

---

## Secrets

```bash
# Read gateway password (copies to clipboard, never displayed)
docker exec agentshroud-gateway cat /run/secrets/gateway_password | pbcopy

# List available secrets (names only)
docker exec agentshroud-gateway ls /run/secrets/
docker exec agentshroud-bot ls /run/secrets/

# Verify a secret exists and has content (length only, no value)
docker exec agentshroud-gateway sh -c 'wc -c < /run/secrets/gateway_password'
docker exec agentshroud-bot sh -c 'wc -c < /run/secrets/telegram_bot_token'

# Peek at first 8 chars (for rotation verification)
docker exec agentshroud-bot sh -c 'head -c 8 /run/secrets/telegram_bot_token'

# Setup/rotate secrets (interactive — run from host)
docker/setup-secrets.sh
docker/setup-secrets.sh store
docker/setup-secrets.sh extract
```

---

## Security Scanners

```bash
# Run scans via SOC API
curl -s -X POST http://localhost:8080/soc/v1/scan/trivy -H "Content-Type: application/json" -d '{"confirm":true}'
curl -s -X POST http://localhost:8080/soc/v1/scan/clamav -H "Content-Type: application/json" -d '{"confirm":true}'
curl -s -X POST http://localhost:8080/soc/v1/scan/all -H "Content-Type: application/json" -d '{"confirm":true}'

# View results
curl -s http://localhost:8080/soc/v1/scan/results | python -m json.tool
curl -s http://localhost:8080/soc/v1/scanners | python -m json.tool
curl -s http://localhost:8080/soc/v1/scorecard | python -m json.tool
curl -s http://localhost:8080/soc/v1/trivy | python -m json.tool
curl -s http://localhost:8080/soc/v1/sbom | python -m json.tool

# Run scan script inside gateway
docker exec agentshroud-gateway security-scan.sh --trivy
docker exec agentshroud-gateway security-scan.sh --clamav
docker exec agentshroud-gateway security-scan.sh --all
```

---

## SOC API — Common Queries

```bash
BASE=http://localhost:8080/soc/v1

# Overview
curl -s $BASE/health | python -m json.tool
curl -s $BASE/security/risk | python -m json.tool
curl -s $BASE/security/risk/summary | python -m json.tool
curl -s $BASE/security/events?limit=20 | python -m json.tool

# Egress
curl -s $BASE/egress/log?limit=10 | python -m json.tool
curl -s $BASE/egress/pending | python -m json.tool
curl -s $BASE/egress/rules | python -m json.tool
curl -s $BASE/egress/history | python -m json.tool

# Approve/deny egress
curl -s -X POST $BASE/egress/<ID>/approve -H "Content-Type: application/json" -d '{"mode":"permanent"}'
curl -s -X POST $BASE/egress/<ID>/deny -H "Content-Type: application/json"

# Emergency block all egress
curl -s -X POST $BASE/egress/emergency-block -H "Content-Type: application/json" -d '{"confirm":true}'

# Services
curl -s $BASE/services | python -m json.tool
curl -s $BASE/services/agentshroud-gateway/logs?tail=30 | python -m json.tool
curl -s -X POST $BASE/services/agentshroud-bot/restart -H "Content-Type: application/json" -d '{"confirm":true}'

# Users & collaborators
curl -s $BASE/users | python -m json.tool
curl -s $BASE/collaborators/activity?limit=20 | python -m json.tool

# Security modules (list / toggle)
curl -s $BASE/security/modules | python -m json.tool
curl -s -X PUT $BASE/security/modules/egress_filter/mode -H "Content-Type: application/json" -d '{"mode":"monitor"}'

# Config
curl -s $BASE/config | python -m json.tool
curl -s -X PUT $BASE/config/log-level -H "Content-Type: application/json" -d '{"level":"DEBUG"}'
```

---

## Web Management UI

```
http://localhost:8080/manage/                    # Dashboard
http://localhost:8080/manage/dashboard/approvals # Approval queue
http://localhost:8080/manage/dashboard/modules   # Security modules
http://localhost:8080/manage/dashboard/ssh       # SSH hosts
http://localhost:8080/manage/dashboard/audit     # Audit log
http://localhost:8080/manage/dashboard/collaborators
http://localhost:8080/manage/dashboard/security
http://localhost:8080/manage/dashboard/killswitch

# Via Tailscale
https://marvin.tail240ea8.ts.net:18790/          # Control UI
```

---

## Upgrades & Rollbacks

```bash
# Check for updates
curl -s http://localhost:8080/soc/v1/updates | python -m json.tool

# Upgrade OpenClaw (in-place, no rebuild needed)
curl -s -X POST http://localhost:8080/soc/v1/updates/bot/upgrade \
  -H "Content-Type: application/json" -d '{"confirm":true}'

# Upgrade gateway (SSH git pull + rebuild)
curl -s -X POST http://localhost:8080/soc/v1/updates/gateway/upgrade \
  -H "Content-Type: application/json" -d '{"confirm":true}'

# Rollback gateway
curl -s -X POST http://localhost:8080/soc/v1/updates/gateway/rollback \
  -H "Content-Type: application/json" -d '{"confirm":true}'

# Manual version manager
scripts/agentshroud-manage.sh check
scripts/agentshroud-manage.sh upgrade
scripts/agentshroud-manage.sh rollback
```

---

## Kill Switch (Emergency)

```bash
# Via script
docker/scripts/killswitch.sh freeze       # Pause (forensics-safe)
docker/scripts/killswitch.sh shutdown      # Graceful stop
docker/scripts/killswitch.sh disconnect    # Nuclear: stop + shred creds

# Via API
curl -s -X POST http://localhost:8080/soc/v1/killswitch/freeze -H "Content-Type: application/json" -d '{"confirm":true}'
curl -s -X POST http://localhost:8080/soc/v1/killswitch/shutdown -H "Content-Type: application/json" -d '{"confirm":true}'

# Recovery
docker compose -f docker/docker-compose.yml -p agentshroud unpause   # after freeze
docker compose -f docker/docker-compose.yml -p agentshroud up -d     # after shutdown
scripts/emergency-rollback.sh                                         # after lockdown
```

---

## Tests

```bash
# From host
python -m pytest gateway/tests/ -q
python -m pytest gateway/tests/ -v --cov=gateway --cov-report=term-missing

# From inside gateway container
docker exec agentshroud-gateway python -m pytest gateway/tests/ -q
```

---

## Telegram Bot Commands (Owner)

| Command | Purpose |
|---------|---------|
| `/pending` | Review pending approval requests |
| `/collabs` | List collaborators |
| `/addcollab <uid>` | Add collaborator |
| `/revoke <uid>` | Revoke collaborator |
| `/approve <id>` | Approve request |
| `/deny <id>` | Deny request |
| `/unlock <uid>` | Unlock suspended user |
| `/locked` | Show lockdown status |
| `/delegate <name> <priv> <duration>` | Delegate privilege |
| `/delegations` | List active delegations |
| `/egress` | View egress status |
| `/egress-allow <domain>` | Allow domain |
| `/status` | Gateway + bot health |
| `/model` | Active AI model |

---

## Key Paths

| What | Path |
|------|------|
| Compose file | `docker/docker-compose.yml` |
| Config | `agentshroud.yaml` (gitignored, mounted `:ro`) |
| SSH keys | volume `agentshroud-ssh` → `/var/agentshroud-ssh/` |
| Bot workspace | volume `agentshroud-workspace` → `/home/node/.agentshroud/workspace/` |
| Bot config | volume `agentshroud-config` → `/home/node/.agentshroud/` |
| Gateway data | volume `gateway-data` → `/app/data/` |
| Security reports | volume `security-reports` → `/var/log/security/` |
| Memory backups | `memory-backups/` (host-side) |
| apply-patches.js | `docker/config/openclaw/apply-patches.js` (baked into image) |

---

## Host IPs (extra_hosts)

| Host | LAN IP | Tailscale IP |
|------|--------|-------------|
| marvin | 192.168.7.137 | 100.90.175.83 |
| trillian | 192.168.7.97 | 100.88.24.16 |
| raspberrypi | 192.168.7.25 | 100.107.248.66 |
| Pi-hole DNS | 192.168.7.45 | — |
