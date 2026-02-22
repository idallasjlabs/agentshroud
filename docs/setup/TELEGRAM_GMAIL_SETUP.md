# Telegram & Gmail Integration Guide

**Goal**: Get @agentshroud.ai_bot working on Telegram and Gmail for full MVP functionality
**Status**: Telegram configured, Gmail needs setup

---

## Part 1: Test Telegram Bot

### ✅ Current Status
- Bot: **@agentshroud.ai_bot** 
- Status: **Running** (confirmed in logs)
- Token: Configured
- Pairing: Ready

### Test Now

1. **Open Telegram** on any device (Mac, iPhone, iPad, etc.)
2. **Search for**: `@agentshroud.ai_bot`
3. **Send a message**: "Hello! Are you working?"
4. **Wait for response**

**Expected**: AI-powered response from GPT-4o (or Claude if you switch models)

### If Bot Doesn't Respond

Check logs for errors:
```bash
./docker/scripts/logs.sh openclaw 100 | grep telegram
```

Check Telegram status:
```bash
./docker/scripts/telegram.sh status
```

---

## Part 2: Set Up Gmail Integration

OpenClaw supports Gmail integration for sending and receiving emails. Here's how to set it up:

### Prerequisites

1. **Google Account**: Your Gmail account
2. **App Password**: Gmail App Password (not your regular password)
3. **IMAP Enabled**: Gmail IMAP must be enabled

### Step 1: Enable IMAP in Gmail

1. Go to Gmail → Settings (gear icon) → See all settings
2. Click **Forwarding and POP/IMAP** tab
3. Under **IMAP Access**, select **Enable IMAP**
4. Click **Save Changes**

### Step 2: Create Gmail App Password

**Note**: You need 2-Factor Authentication enabled first.

1. Go to https://myaccount.google.com/security
2. Enable **2-Step Verification** (if not already enabled)
3. Go to https://myaccount.google.com/apppasswords
4. Select app: **Mail**
5. Select device: **Other (Custom name)**
6. Enter: `OpenClaw Bot`
7. Click **Generate**
8. **Copy the 16-character password** (no spaces)

### Step 3: Add Gmail to OpenClaw

```bash
# Add Gmail channel
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw channels add --channel gmail \
  --email "your-email@gmail.com" \
  --password "YOUR_APP_PASSWORD_HERE"
```

Replace:
- `your-email@gmail.com` - Your Gmail address
- `YOUR_APP_PASSWORD_HERE` - The 16-character app password from Step 2

### Step 4: Verify Gmail Channel

```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels list
```

You should see:
```
- Gmail default: configured, token=config, enabled
```

### Step 5: Test Gmail

Send a test email:

**Via Control UI**:
1. Go to http://localhost:18790
2. In chat, type: "Send an email to myself at your-email@gmail.com with subject 'Test from OpenClaw' and message 'This is a test'"
3. Check your Gmail inbox

**Via Telegram**:
1. Message @agentshroud.ai_bot on Telegram
2. Say: "Send an email to your-email@gmail.com with subject 'Test' and say hello"
3. Check your Gmail inbox

---

## Part 3: Ensure Functionality Remains

To keep both Telegram and Gmail working permanently:

### 1. Backup Configuration

The configuration is stored in Docker volumes. To back it up:

```bash
# Create backup directory
mkdir -p ~/openclaw-backups

# Backup OpenClaw config
docker cp openclaw-bot:/home/node/.openclaw ~/openclaw-backups/openclaw-config-$(date +%Y%m%d)

# Backup current docker-compose.yml
cp docker/docker-compose.yml ~/openclaw-backups/docker-compose-$(date +%Y%m%d).yml
```

### 2. Regular Health Checks

Add this to your crontab to check health daily:

```bash
# Edit crontab
crontab -e

# Add this line (checks daily at 9 AM)
0 9 * * * ./docker/scripts/check-status.sh > /tmp/openclaw-health.log 2>&1
```

### 3. Auto-Restart on Reboot

Docker Compose is configured with `restart: unless-stopped`, so containers will auto-restart after Mac reboots.

To verify:
```bash
docker compose -f docker/docker-compose.yml ps
```

Both should show `restart: unless-stopped`.

### 4. Monitor Logs

Check logs periodically:
```bash
# View recent logs
./docker/scripts/logs.sh

# Check for errors
./docker/scripts/logs.sh | grep -i error

# Check Telegram activity
./docker/scripts/logs.sh | grep -i telegram

# Check Gmail activity
./docker/scripts/logs.sh | grep -i gmail
```

### 5. Test Regularly

**Weekly Test Checklist**:
- [ ] Message @agentshroud.ai_bot on Telegram
- [ ] Ask bot to send a test email
- [ ] Check both API keys are working
- [ ] Verify containers are healthy

```bash
# Quick weekly test
./docker/scripts/check-status.sh
```

---

## Part 4: Gmail Troubleshooting

### "Invalid credentials" Error

**Cause**: App password wrong or 2FA not enabled

**Fix**:
1. Verify 2-Step Verification is enabled
2. Generate a new app password
3. Re-add Gmail channel with new password

### "IMAP not enabled" Error

**Cause**: IMAP disabled in Gmail settings

**Fix**:
1. Go to Gmail Settings → Forwarding and POP/IMAP
2. Enable IMAP
3. Save changes
4. Restart OpenClaw: `./docker/scripts/restart.sh`

### Gmail Not Receiving Emails from Bot

**Check**:
1. Spam folder
2. OpenClaw logs for sending errors:
   ```bash
   ./docker/scripts/logs.sh | grep -i "gmail\|email\|smtp"
   ```

### Gmail Not Detecting New Emails

**Check**:
1. IMAP is enabled
2. Bot has permissions to read inbox
3. Check logs for IMAP connection errors

---

## Part 5: Telegram Troubleshooting

### Bot Not Responding

**Check pairing**:
```bash
./docker/scripts/telegram.sh status
```

If pairing required, approve it:
```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw pairing list telegram
docker compose -f docker/docker-compose.yml exec openclaw openclaw pairing approve telegram PAIRING_ID
```

### "Bot was blocked by user" Error

You need to start a conversation first:
1. Open Telegram
2. Search @agentshroud.ai_bot
3. Click **START** or **/start**
4. Try messaging again

### Bot Responds Slowly

**Check model**:
```bash
./docker/scripts/check-status.sh | grep "Default"
```

Claude Opus is slower but higher quality. GPT-4o is faster:
```bash
./docker/scripts/set-model.sh openai/gpt-4o
```

---

## Part 6: Complete System Test

Run this complete test to verify everything:

```bash
#!/bin/bash
# Save as: test-complete-system.sh

cd /Users/ijefferson.admin/Development/agentshroud

echo "=== Complete System Test ==="
echo ""

echo "1. Container Health"
docker compose -f docker/docker-compose.yml ps
echo ""

echo "2. API Keys Status"
docker compose -f docker/docker-compose.yml exec openclaw bash -c '
export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key)
export ANTHROPIC_API_KEY=$(cat /run/secrets/anthropic_api_key)
openclaw models status | head -20
'
echo ""

echo "3. Telegram Status"
./docker/scripts/telegram.sh status
echo ""

echo "4. Gmail Status"
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels list | grep -i gmail
echo ""

echo "5. Gateway Health"
curl -s http://localhost:8080/status | jq '.'
echo ""

echo "=== Test Complete ==="
echo ""
echo "Next steps:"
echo "1. Message @agentshroud.ai_bot on Telegram"
echo "2. Ask bot to send a test email"
echo "3. Verify both work"
```

---

## Part 7: Maintaining Functionality

### Monthly Checklist

- [ ] Update OpenClaw: `npm update -g openclaw`
- [ ] Rebuild containers: `./docker/scripts/restart.sh rebuild`
- [ ] Backup configuration (see Part 3, Step 1)
- [ ] Test Telegram bot
- [ ] Test Gmail integration
- [ ] Review logs for errors
- [ ] Check API key balances (OpenAI/Anthropic dashboards)

### When Upgrading macOS

Before upgrading:
```bash
# Backup everything
./docker/scripts/export.sh  # When we add this script later

# Or manually:
docker cp openclaw-bot:/home/node/.openclaw ~/openclaw-backups/
```

After upgrading:
```bash
# Restart Docker Desktop
# Then restart containers
./docker/scripts/restart.sh
```

---

## Summary

### Current Status

✅ **Working**:
- OpenClaw containers healthy
- OpenAI API configured
- Anthropic API configured
- Telegram bot @agentshroud.ai_bot running
- Safari and Chrome connected

⏳ **Needs Setup**:
- Gmail integration (follow Part 2)

### Quick Start Commands

```bash
# Check everything
./docker/scripts/check-status.sh

# Test Telegram
# (Message @agentshroud.ai_bot on Telegram)

# Add Gmail
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw channels add --channel gmail \
  --email "your-email@gmail.com" \
  --password "YOUR_APP_PASSWORD"

# View logs
./docker/scripts/logs.sh

# Restart if needed
./docker/scripts/restart.sh
```

---

## Documentation Created

- `DEVICE_PAIRING.md` - Device pairing explained
- `TELEGRAM_GMAIL_SETUP.md` - This file
- `SYSTEM_STATUS.md` - Complete system status
- `ACCESS_INFO.md` - Access information
- `docker/scripts/devices.sh` - Device management script

---

**Next**: Test @agentshroud.ai_bot on Telegram, then set up Gmail following Part 2!
