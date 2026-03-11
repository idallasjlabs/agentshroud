# AgentShroud Deployment & Troubleshooting Runbook

## Infrastructure

| Host | Role | Arch | SSH | Compose Override |
|------|------|------|-----|-----------------|
| **Marvin** | Dev/Test (Mac Studio) | aarch64 | `ssh marvin` | `docker-compose.agentshroud-bot.marvin.yml` |
| **Trillian** | Dev/Test (Intel Mac) | x86_64 | `ssh trillian` | `docker-compose.agentshroud-bot.trillian.yml` |
| **Raspberry Pi** | Dev/Test/Prod | aarch64 | `ssh raspberrypi` | `docker-compose.agentshroud-bot.raspberrypi.yml` |

All three run Docker via Colima under the `agentshroud-bot` user.
Gateway source is mounted RO from the repo (`../gateway:/app/gateway:ro`).

---

## Deploy Latest Code (Any Host)

```bash
# 1. Pull latest
ssh <host> "cd ~/Development/agentshroud && git pull origin feat/v0.8.0-enforcement-hardening"

# 2. Rebuild and start
ssh <host> "cd ~/Development/agentshroud && docker compose -f docker/docker-compose.yml -f docker/docker-compose.agentshroud-bot.<host>.yml up -d --build"

# 3. Verify
ssh <host> "docker ps"
ssh <host> "docker logs agentshroud-gateway --tail=10"  # or agentshroud-dev-gateway on Marvin
```

Replace `<host>` with `marvin`, `trillian`, or `raspberrypi`.

**Container names:**
- Marvin: `agentshroud-dev-gateway`, `agentshroud-dev-bot`
- Trillian: `agentshroud-gateway` (+ bot if configured)
- Pi: `agentshroud-gateway`, `agentshroud-bot`

---

## Quick Restart (No Rebuild)

If you only changed Python files (gateway source is mounted RO):

```bash
ssh <host> "docker restart agentshroud-gateway"  # or agentshroud-dev-gateway on Marvin
```

Python reimports on startup — no build needed for source-only changes.

⚠️ **Rebuild required if:** Dockerfile changed, new pip dependencies, new system packages.

---

## Troubleshooting

### Docker says "Cannot connect to Docker daemon"

Colima isn't running. Start it:
```bash
ssh <host> "colima start"
```

If it fails with "disk in use":
```bash
ssh <host> "colima stop --force && colima start"
```

### "Fatal glibc error: Cannot allocate TLS block"

Container image is corrupted or incompatible. Full rebuild needed:
```bash
ssh <host> "docker stop agentshroud-gateway && docker rm agentshroud-gateway"
ssh <host> "cd ~/Development/agentshroud && docker compose -f docker/docker-compose.yml -f docker/docker-compose.agentshroud-bot.<host>.yml up -d --build"
```

### Container starts but unhealthy

Check logs:
```bash
ssh <host> "docker logs agentshroud-gateway --tail=50"
```

Common causes:
- **1Password session expired:** `op-proxy: 1Password session not available` — not critical, credential injection won't work until session refreshed
- **Import error:** Python syntax/import issue — check the specific error, fix in repo, restart
- **Port in use:** Another process on 8080 — `ssh <host> "lsof -i :8080"`

### Colima won't start

```bash
# Check status
ssh <host> "colima list"

# Force stop and restart
ssh <host> "colima stop --force && colima start"

# Nuclear option — delete and recreate (LOSES ALL CONTAINERS)
ssh <host> "colima delete && colima start"
```

### Tests failing after deploy

```bash
ssh <host> "cd ~/Development/agentshroud && python3 -m pytest gateway/tests/ -q --tb=short --ignore=gateway/tests/test_op_proxy.py"
```

---

## Deploy to Production

Production runs on the Pi. When ready to deploy:

```bash
# 1. Merge to main
ssh marvin "cd ~/Development/agentshroud && git checkout main && git merge feat/v0.8.0-enforcement-hardening && git push origin main"

# 2. Deploy on Pi
ssh raspberrypi "cd ~/Development/agentshroud && git checkout main && git pull origin main"
ssh raspberrypi "cd ~/Development/agentshroud && docker compose -f docker/docker-compose.yml -f docker/docker-compose.agentshroud-bot.raspberrypi.yml up -d --build"

# 3. Verify
ssh raspberrypi "docker ps"
ssh raspberrypi "docker logs agentshroud-gateway --tail=20"
```

---

## Run Tests on Any Host

```bash
ssh <host> "cd ~/Development/agentshroud && python3 -m pytest gateway/tests/ -q --tb=short --ignore=gateway/tests/test_op_proxy.py"
```

Full verbose:
```bash
ssh <host> "cd ~/Development/agentshroud && python3 -m pytest gateway/tests/ -v --tb=long"
```

Single test file:
```bash
ssh <host> "cd ~/Development/agentshroud && python3 -m pytest gateway/tests/test_telegram_proxy_outbound.py -v"
```

---

## Check Gateway Health

```bash
# From the host
ssh <host> "curl -s http://localhost:8080/status"

# Container health
ssh <host> "docker inspect agentshroud-gateway --format '{{.State.Health.Status}}'"
```

---

## Architecture Notes

- Gateway source mounted at `/app/gateway:ro` — changes to `~/Development/agentshroud/gateway/` are live in container after restart
- Bot container connects to gateway at `http://gateway:8080/telegram-api/` — all Telegram traffic proxied
- Gateway runs on port 8080 inside container, mapped to 8080 (Pi/Trillian) or 9080 (Marvin)
- DNS managed by gateway's DNSBlocklist (187K+ blocked domains)
- HTTP CONNECT proxy on port 8181 for agent outbound traffic
