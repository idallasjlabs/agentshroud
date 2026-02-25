# Deployment Runbook — AgentShroud

> Last updated: 2026-02-18

## Prerequisites

- SSH access to Pi: `ssh agentshroud-bot@<your-tailscale-hostname>`
- conda env `agentshroud` with Python 3.11
- Docker and Docker Compose installed
- GitHub access via `gh` CLI
- 1Password CLI (`op`) for secrets

## Standard Deployment

### 1. Pull Latest Code

```bash
cd ~/Development/agentshroud
git checkout main
git pull origin main
```

### 2. Run Tests

```bash
~/miniforge3/envs/agentshroud/bin/python -m pytest gateway/tests/ -v
# ALL tests must pass before deploying
```

### 3. Update Dependencies (if changed)

```bash
~/miniforge3/envs/agentshroud/bin/pip install -r requirements.txt
```

### 4. Build Containers

```bash
docker compose build --no-cache
```

### 5. Deploy

```bash
# Stop existing services
docker compose down

# Start updated services
docker compose up -d

# Verify health
docker compose ps
docker logs agentshroud-gateway --tail 20
```

### 6. Verify

```bash
# Health check
curl -s http://localhost:8080/health | python3 -m json.tool

# Tailscale serves still working
./scripts/tailscale-check.sh

# Send a test message via Telegram to confirm bot responds
```

---

## Rolling Back

```bash
# Find the previous working commit
git log --oneline -10

# Revert to it
git checkout <commit-hash>

# Rebuild and redeploy
docker compose build --no-cache
docker compose down && docker compose up -d
```

---

## First-Time Setup

See [Raspberry Pi Setup Guide](../deploy/raspberry-pi.md) for initial installation.

### Quick Summary

1. Clone repo
2. Create conda env: `conda create -n agentshroud python=3.13`
3. Install deps: `pip install -r requirements.txt`
4. Configure secrets via 1Password + Docker Secrets
5. `docker compose up -d`
6. Set up Tailscale serves: `sudo ./scripts/tailscale-serve.sh start`

---

## Environment Variables

| Variable | Description | Source |
|----------|-------------|--------|
| `TELEGRAM_BOT_TOKEN` | Bot API token | Docker Secret |
| `ALLOWED_USERS` | Comma-separated Telegram user IDs | Config file |
| `LLM_API_KEY` | LLM provider API key | Docker Secret |
| `LOG_LEVEL` | Logging verbosity (INFO/DEBUG) | Environment |

---

## Version Tagging

After a successful deployment:
```bash
git tag -a v0.X.0 -m "Release v0.X.0: brief description"
git push origin v0.X.0
```
