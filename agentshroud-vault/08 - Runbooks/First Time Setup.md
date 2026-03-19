---
title: First Time Setup
type: process
tags: [#type/process, #status/critical]
related: ["[[Restart Procedure]]", "[[Health Checks]]", "[[docker-compose.yml]]", "[[agentshroud.yaml]]"]
status: active
last_reviewed: 2026-03-09
---

# First Time Setup

Complete checklist from zero to running stack.

## Prerequisites

- [ ] Docker (or Colima) installed and running
- [ ] Git repo cloned: `git clone <repo> agentshroud && cd agentshroud`
- [ ] On macOS with VPN: see Colima VPN networking notes in [[Architecture Overview]]

---

## Step 1: Create Secret Files

```bash
# Gateway shared password (generate random)
python3 -c "import secrets; print(secrets.token_hex(32))" > docker/secrets/gateway_password.txt

# Telegram bot token (from @BotFather)
echo "YOUR_BOT_TOKEN_HERE" > docker/secrets/telegram_bot_token_production.txt

# Create empty optional secrets (required by compose for mount to succeed)
echo "" > docker/secrets/anthropic_oauth_token.txt
echo "" > docker/secrets/1password_bot_email.txt
echo "" > docker/secrets/1password_bot_master_password.txt
echo "" > docker/secrets/1password_bot_secret_key.txt

# Verify
ls -la docker/secrets/
```

**Verify:** All 6 secret files exist and are non-empty (except optionals).

**If it fails:** `docker compose up` will fail with "secret not found".

---

## Step 2: Verify agentshroud.yaml

```bash
# Validate YAML syntax
python3 -c "import yaml; yaml.safe_load(open('agentshroud.yaml'))" && echo "YAML OK"

# Check gateway.auth_token is empty (will use Docker secret)
grep "auth_token" agentshroud.yaml
```

**Verify:** YAML parses without error.

---

## Step 3: Build Images

```bash
docker compose -f docker/docker-compose.yml build --no-cache 2>&1 | tee /tmp/build.log
```

Expected final lines:
```
 agentshroud-gateway Built
 agentshroud-bot Built
```

Check for patch confirmation:
```bash
grep "Patched file download URL" /tmp/build.log
# Expected: 4 files patched
```

**If build fails:** Check `/tmp/build.log` for the error. Common issues: network timeout (retry), missing base image (check Docker Hub connectivity).

---

## Step 4: Start the Stack

```bash
docker compose -f docker/docker-compose.yml up -d
```

Wait ~30 seconds for gateway health check, then bot starts.

---

## Step 5: Verify Gateway Health

```bash
# Should return JSON with status: ok
curl http://localhost:8080/status

# Check logs for successful startup
docker logs agentshroud-gateway | grep -E "Gateway ready|ERROR|CRITICAL"
```

**Expected:** `AgentShroud Gateway ready at 127.0.0.1:8080`

**If not healthy:** See [[Gateway Startup Failure]]

---

## Step 6: Verify Bot Started

```bash
# Check container status
docker compose -f docker/docker-compose.yml ps

# Check bot health
curl -sf http://localhost:18790/ && echo "Bot OK"

# Check Telegram polling started
docker logs agentshroud-gateway | grep getUpdates | tail -3
```

**Expected:** `agentshroud-bot` shows `Up (healthy)` or `Up`.

---

## Step 7: Verify Patch Applied

```bash
docker exec agentshroud-bot \
  grep -c "TELEGRAM_API_BASE_URL" \
  /usr/local/lib/node_modules/openclaw/dist/pi-embedded-CtM2Mrrj.js
# Expected: 1 or more
```

---

## Step 8: Test End-to-End

1. Open Telegram, send a message to your bot
2. Bot should respond
3. Send a photo — bot should process it without "Failed to download media"

**Check gateway logs:**
```bash
docker logs agentshroud-gateway --since 2m | grep -E "sendMessage|getUpdates|file/bot"
```

---

## Step 9: (Optional) Configure Home Lab SSH Hosts

If you use the SSH proxy feature, update `agentshroud.yaml` `ssh.hosts` with correct IPs, and populate the `agentshroud-ssh` volume with SSH keys:

```bash
# Copy SSH private key into volume
docker run --rm -v agentshroud_agentshroud-ssh:/target \
  -v ~/.ssh:/source:ro \
  alpine cp /source/id_ed25519 /target/id_ed25519

# Verify
docker run --rm -v agentshroud_agentshroud-ssh:/target alpine ls -la /target
```

---

## Step 10: (Optional) Enable 1Password Integration

Populate the 1Password secret files:
```bash
echo "your@email.com" > docker/secrets/1password_bot_email.txt
echo "your-master-password" > docker/secrets/1password_bot_master_password.txt
echo "A3-XXXXX-..." > docker/secrets/1password_bot_secret_key.txt

# Restart gateway to pick up credentials
docker compose -f docker/docker-compose.yml restart gateway
docker logs agentshroud-gateway | grep "1Password"
```
