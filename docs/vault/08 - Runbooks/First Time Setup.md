---
title: First Time Setup
type: runbook
tags: [setup, deployment, runbook]
related: [Startup Sequence, Quick Reference, Configuration/agentshroud.yaml, Configuration/docker-compose.yml]
status: documented
---

# First Time Setup

## Prerequisites

- Docker Desktop (macOS) or Docker Engine + Docker Compose (Linux)
- 1Password with the "Agent Shroud Bot Credentials" vault
- Tailscale configured on the host machine (for iOS Shortcuts access)
- Git repository cloned to local machine

---

## Step 1: Create Secret Files

```bash
cd agentshroud/docker/secrets/

# 1. Generate gateway auth token
python3 -c "import secrets; print(secrets.token_hex(32))" > gateway_password.txt

# 2. Create 1Password service account token
# (Generate in 1Password: Settings → Developer → Service Accounts)
# Grant READ access to "Agent Shroud Bot Credentials" vault only
echo "ops_YOUR_SERVICE_ACCOUNT_TOKEN" > 1password_service_account

# 3. Add Telegram bot token
# (Create bot via @BotFather on Telegram)
echo "YOUR_BOT_TOKEN" > telegram_bot_token_production.txt

# Verify files exist
ls -la docker/secrets/
```

Required secret files:
- `gateway_password.txt` — shared secret between gateway and bot
- `1password_service_account` — 1Password service account token (no extension)
- `telegram_bot_token_production.txt` — Telegram bot token

---

## Step 2: Configure agentshroud.yaml

Review and update key settings:

```bash
# Edit the config file
vim agentshroud.yaml
```

**Required changes:**
```yaml
# Leave auth_token empty — will be loaded from secret file
gateway:
  auth_token: ""

# Update iOS Shortcuts endpoint (your Tailscale hostname)
shortcuts:
  endpoint: "http://YOUR-HOSTNAME.tail240ea8.ts.net:8080"

# Verify SSH hosts match your actual Tailscale hostnames
ssh:
  hosts:
    pi:
      host: "raspberrypi.tail240ea8.ts.net"
    marvin:
      host: "marvin.tail240ea8.ts.net"
```

---

## Step 3: Configure 1Password Items

In 1Password, create the following items in the "Agent Shroud Bot Credentials" vault:

| Item | Field | Content |
|------|-------|---------|
| AgentShroud - Anthropic Claude OAuth Token | `claude oath token` | Claude OAuth token |
| (Brave Search item) | `brave search api key` | Brave Search API key |
| (iCloud item) | `agentshroud app-specific password` | iCloud app-specific password |

The exact 1Password item IDs and paths are referenced in `docker/scripts/start-agentshroud.sh`.

---

## Step 4: Build Container Images

```bash
cd agentshroud

# Build gateway image (downloads spaCy model, ClamAV, 1Password CLI)
docker compose -f docker/docker-compose.yml build agentshroud-gateway

# Build bot image (installs OpenClaw, Playwright, patches SDKs)
docker compose -f docker/docker-compose.yml build agentshroud-bot
```

> **Note:** First build takes 10-20 minutes (Playwright downloads Chromium ~400MB, spaCy downloads ~12MB).

---

## Step 5: Start Containers

```bash
cd agentshroud

# Start all services
docker compose -f docker/docker-compose.yml up -d

# Watch startup logs
docker compose -f docker/docker-compose.yml logs -f
```

Expected startup sequence:
1. Gateway starts → loads config → initializes spaCy → health check passes (~30s)
2. Bot starts → loads secrets from 1Password → patches OpenClaw config → starts agent (~60s)
3. Telegram notification received: `🛡️ AgentShroud online`

---

## Step 6: Verify Setup

```bash
# Check container status
docker compose -f docker/docker-compose.yml ps

# Test gateway health
curl -s http://localhost:8080/status | jq .

# Test gateway auth
curl -s -H "Authorization: Bearer $(cat docker/secrets/gateway_password.txt)" \
  http://localhost:8080/health | jq .

# Access management dashboard
open http://localhost:18790
```

---

## Step 7: Configure iOS Shortcuts (Optional)

1. Open the iOS Shortcuts app
2. Import the AgentShroud shortcuts from `examples/` or create new ones
3. Set the gateway URL to your Tailscale hostname:
   ```
   http://YOUR-HOSTNAME.tail240ea8.ts.net:8080
   ```
4. Set the auth token to the value from `docker/secrets/gateway_password.txt`

---

## Step 8: Verify Security Posture

```bash
# Run security verification
./docker/scripts/verify-security.sh

# Check security mode (should be 'enforce')
docker exec agentshroud-gateway env | grep AGENTSHROUD_MODE
# Should return nothing (or "enforce")
```

---

## Troubleshooting First Setup

| Issue | Fix |
|-------|-----|
| Containers start and stop immediately | Check docker logs; verify secret files exist |
| Gateway health check fails | Check if port 8080 is in use; check YAML syntax |
| Bot never healthy | Wait for gateway health check; check logs |
| 1Password secrets not loading | Verify service account token; check vault permissions |
| Telegram notification not sent | Verify bot token; check Telegram API access |

---

## Related Notes

- [[Startup Sequence]] — What happens during startup
- [[Quick Reference]] — Daily operations cheat sheet
- [[Configuration/agentshroud.yaml]] — Full config reference
- [[Runbooks/Restart Procedure]] — After setup, restarting
