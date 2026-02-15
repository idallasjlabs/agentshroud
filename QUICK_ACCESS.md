# OpenClaw Quick Access Guide

**Status**: ⚠️ **PAIRING REQUIRED** - Follow steps below to complete setup

---

## 🔐 FIRST TIME SETUP: Pair Control UI with Gateway

### Step 1: Open Control UI
Go to: **http://localhost:18790**

### Step 2: Enter Token in Settings
1. Click the **Settings** icon (⚙️) in the UI
2. Find the **"Gateway Token"** or **"Token"** field
3. Paste this token:
   ```
   b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05
   ```
4. Click **"Save"** or **"Connect"**

### Step 3: Verify Connection
The UI should show **"Connected"** status. You're ready to use OpenClaw!

**Full pairing guide**: [PAIRING_INSTRUCTIONS.md](PAIRING_INSTRUCTIONS.md)

---

## 🔐 After Pairing: Regular Access

### **Control UI URL**:
```
http://localhost:18790
```
(Your browser will remember the token after first pairing)

### **Security Token** (if needed again):
```
b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05
```

**⚠️ Keep this token secure** - it grants full control of your OpenClaw instance

---

## 🚀 Quick Commands

### Open OpenClaw UI (Auto-login)
```bash
open "http://localhost:18790/#token=b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05"
```

### Check System Status
```bash
cd /Users/ijefferson.admin/Development/oneclaw
docker compose -f docker/docker-compose.yml ps
```

### View Logs
```bash
# OpenClaw logs
docker logs openclaw-bot -f

# Gateway logs
docker logs secureclaw-gateway -f
```

### Restart Containers
```bash
docker compose -f docker/docker-compose.yml restart
```

### Stop System
```bash
docker compose -f docker/docker-compose.yml down
```

### Start System
```bash
docker compose -f docker/docker-compose.yml up -d
```

---

## 📱 Add Telegram Channel

```bash
# Step 1: Create bot with @BotFather on Telegram
# Step 2: Get your bot token from BotFather
# Step 3: Run this command:

docker compose -f docker/docker-compose.yml exec openclaw openclaw channels add \
  --channel telegram \
  --token "YOUR_TELEGRAM_BOT_TOKEN"

# Step 4: Message your bot on Telegram from any device
```

See [TELEGRAM_SETUP.md](TELEGRAM_SETUP.md) for full details.

---

## 🔑 Configure OpenAI API Key

### Option A: Through Web UI (Recommended)
1. Open Control UI: http://localhost:18790/#token=b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05
2. Go to **Settings → Providers**
3. Click **Add Provider**
4. Select **OpenAI**
5. Paste your API key from: `docker/secrets/openai_api_key.txt`

### Option B: Via Command Line
```bash
OPENAI_KEY=$(cat docker/secrets/openai_api_key.txt)
docker compose -f docker/docker-compose.yml exec openclaw openclaw providers add \
  --provider openai \
  --api-key "$OPENAI_KEY"
```

---

## 🛡️ Security Configuration

### Current Security Settings

✅ **Authentication**: Token-based (32-byte cryptographic random)
✅ **Network Binding**: Localhost only (127.0.0.1)
✅ **Container Isolation**: No host filesystem access
✅ **Network Isolation**: Cannot access LAN (192.168.x.x)
✅ **Container Hardening**: Capabilities dropped, non-root user
✅ **Resource Limits**: Memory/CPU/PID limits enforced

### Access Control

The system requires a secure token for all access:

- **Control UI**: Token required (in URL or manual entry)
- **API Access**: Token required in Authorization header
- **Gateway**: Separate token (auto-generated on startup)

### Token Storage

```bash
# View current token
docker compose -f docker/docker-compose.yml exec openclaw \
  printenv OPENCLAW_GATEWAY_TOKEN

# Regenerate token (requires container restart)
# 1. Edit docker/docker-compose.yml
# 2. Replace OPENCLAW_GATEWAY_TOKEN value
# 3. Restart: docker compose -f docker/docker-compose.yml restart openclaw
```

---

## 🔍 Troubleshooting

### "unauthorized: gateway token missing" Error

**Fix**: Use the authenticated URL with token:
```
http://localhost:18790/#token=b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05
```

### Container Not Healthy

```bash
# Check status
docker compose -f docker/docker-compose.yml ps

# View logs
docker logs openclaw-bot --tail 50

# Restart
docker compose -f docker/docker-compose.yml restart openclaw
```

### Cannot Access UI

```bash
# Verify port mapping
docker port openclaw-bot
# Should show: 18789/tcp -> 127.0.0.1:18790

# Test locally
curl http://localhost:18790/api/health
```

### Forgot Token

```bash
# Get token from container
docker compose -f docker/docker-compose.yml exec openclaw \
  printenv OPENCLAW_GATEWAY_TOKEN
```

---

## 📊 System Health Check

Run this to verify everything is working:

```bash
cd /Users/ijefferson.admin/Development/oneclaw

echo "=== Container Status ==="
docker compose -f docker/docker-compose.yml ps

echo -e "\n=== Gateway Health ==="
curl -s http://localhost:8080/status | grep -E "(status|healthy)"

echo -e "\n=== OpenClaw Connectivity ==="
docker exec openclaw-bot curl -s https://api.openai.com | head -3

echo -e "\n=== Security Token ==="
docker compose -f docker/docker-compose.yml exec openclaw \
  printenv OPENCLAW_GATEWAY_TOKEN

echo -e "\n✅ All systems operational!"
```

---

## 📚 Full Documentation

- **Deployment Status**: [DEPLOYMENT_STATUS.md](DEPLOYMENT_STATUS.md)
- **OpenClaw Setup**: [OPENCLAW_SETUP.md](OPENCLAW_SETUP.md)
- **Telegram Setup**: [TELEGRAM_SETUP.md](TELEGRAM_SETUP.md)
- **Security Architecture**: [SECURITY_ARCHITECTURE.md](SECURITY_ARCHITECTURE.md)

---

## 💾 Save This Information

**Important**: Save this access token in your password manager or secure notes:

```
OpenClaw Control UI Token:
b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05

Control UI URL:
http://localhost:18790/#token=b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05
```

If you lose this token, you can retrieve it with:
```bash
docker compose -f docker/docker-compose.yml exec openclaw \
  printenv OPENCLAW_GATEWAY_TOKEN
```

---

**Last Updated**: 2026-02-15
**System Version**: 0.2.0
