# API Keys Setup Guide

**System**: OpenClaw + AgentShroud Gateway
**Bot**: @agentshroud.ai_bot
**Last Updated**: 2026-02-15

---

## Overview

OpenClaw supports multiple AI providers. This guide will help you set up both OpenAI and Anthropic API keys.

---

## Step 1: Save API Keys to Secret Files

### Create the Anthropic API Key File

Once you have your Anthropic API key, save it:

```bash
cd /Users/ijefferson.admin/Development/agentshroud

# Create the secret file
echo "YOUR_ANTHROPIC_API_KEY_HERE" > docker/secrets/anthropic_api_key.txt

# Secure the file
chmod 600 docker/secrets/anthropic_api_key.txt
```

Replace `YOUR_ANTHROPIC_API_KEY_HERE` with your actual Anthropic API key.

### Verify OpenAI Key Exists

The OpenAI key should already be set up:

```bash
cat docker/secrets/openai_api_key.txt
```

If it's missing, create it:

```bash
echo "YOUR_OPENAI_API_KEY_HERE" > docker/secrets/openai_api_key.txt
chmod 600 docker/secrets/openai_api_key.txt
```

---

## Step 2: Restart OpenClaw Container

The container needs to be restarted to mount the new Anthropic API key secret:

```bash
cd /Users/ijefferson.admin/Development/agentshroud

docker compose -f docker/docker-compose.yml restart openclaw
```

Wait for the container to become healthy:

```bash
# Check status (wait for "healthy")
docker compose -f docker/docker-compose.yml ps

# Should show:
# openclaw-bot    Up X minutes (healthy)
```

---

## Step 3: Configure API Keys in OpenClaw

### Option A: Via Control UI (Recommended)

1. **Connect to Control UI**:
   - Go to http://localhost:18790
   - Enter gateway password: `b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05`
   - Click "Connect"

2. **Add OpenAI Provider**:
   - Go to **Settings** → **Providers**
   - Click **Add Provider**
   - Select **OpenAI**
   - Paste your OpenAI API key
   - Click **Save**

3. **Add Anthropic Provider**:
   - Click **Add Provider** again
   - Select **Anthropic**
   - Paste your Anthropic API key
   - Click **Save**

### Option B: Via Command Line

```bash
cd /Users/ijefferson.admin/Development/agentshroud

# Add OpenAI authentication
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw models auth add --provider openai --api-key "$(cat docker/secrets/openai_api_key.txt)"

# Add Anthropic authentication
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw models auth add --provider anthropic --api-key "$(cat docker/secrets/anthropic_api_key.txt)"
```

---

## Step 4: Set Default Model

Choose which model you want as your primary:

### Option 1: Use Anthropic Claude (Recommended)

```bash
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw models set anthropic/claude-opus-4-6
```

### Option 2: Use OpenAI GPT-4

```bash
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw models set openai/gpt-4o
```

---

## Step 5: Verify Configuration

Check that both providers are authenticated:

```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw models status
```

**Expected output**:

```
Active model
✓ anthropic/claude-opus-4-6  (or whichever you set as default)

Configured
✓ anthropic - All models available
✓ openai - All models available
```

Both should show checkmarks, not "Missing auth".

---

## Step 6: Add Telegram Bot

Now add your @agentshroud.ai_bot to OpenClaw:

1. **Get the token from @BotFather**:
   - Open Telegram as @agentshroud.ai (you)
   - Message **@BotFather**
   - Send: `/mybots`
   - Select: `@agentshroud.ai_bot`
   - Click: **API Token**
   - Copy the full token

2. **Update the channel** (only if needed):

```bash
# Remove old channel
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw channels remove telegram

# Add with new token
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw channels add --channel telegram --token "YOUR_BOT_TOKEN_HERE"

# Approve pairing
docker compose -f docker/docker-compose.yml exec openclaw openclaw pairing list
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw pairing approve telegram PAIRING_ID_HERE
```

---

## Step 7: Test the Bot

### Test via Telegram

1. Open Telegram as **@agentshroud.ai** (you)
2. Search for and message **@agentshroud.ai_bot** (your bot)
3. Send: "Hello! Can you hear me?"
4. Wait for AI response

**Expected**: You should receive an AI-powered response from Claude or GPT-4o (depending on your default model)

### Test via Control UI

1. Go to http://localhost:18790
2. Open the chat interface
3. Send a test message
4. Verify you get a response

---

## Troubleshooting

### "Missing auth" for a provider

```bash
# Re-add the authentication
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw models auth add --provider PROVIDER_NAME --api-key "YOUR_KEY_HERE"

# Verify
docker compose -f docker/docker-compose.yml exec openclaw openclaw models status
```

### Bot not responding on Telegram

```bash
# Check OpenClaw logs
docker logs openclaw-bot --tail 50

# Check if channel is enabled
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels list

# Check if pairing is approved
docker compose -f docker/docker-compose.yml exec openclaw openclaw pairing list
```

### Container won't start after adding Anthropic secret

```bash
# Check if the secret file exists
ls -la docker/secrets/anthropic_api_key.txt

# View container logs
docker logs openclaw-bot

# If secret file is missing or has wrong permissions:
chmod 600 docker/secrets/anthropic_api_key.txt
docker compose -f docker/docker-compose.yml restart openclaw
```

---

## Security Notes

- ✅ API keys are stored in `docker/secrets/` which is in `.gitignore`
- ✅ Secret files have `600` permissions (owner read/write only)
- ✅ Keys are mounted as Docker secrets (read-only in container)
- ✅ Keys are never exposed in environment variables or logs
- ⚠️ **Never commit secret files to git**
- ⚠️ **Never share API keys publicly**

---

## Quick Reference

### View Configured Providers

```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw models status
```

### Change Default Model

```bash
# To Claude
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw models set anthropic/claude-opus-4-6

# To GPT-4o
docker compose -f docker/docker-compose.yml exec openclaw \
  openclaw models set openai/gpt-4o
```

### List Available Models

```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw models list
```

### Check Telegram Channel Status

```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels list
```

---

## Summary Checklist

- [ ] Save Anthropic API key to `docker/secrets/anthropic_api_key.txt`
- [ ] Verify OpenAI key exists in `docker/secrets/openai_api_key.txt`
- [ ] Restart OpenClaw container
- [ ] Add both providers via Control UI or CLI
- [ ] Set default model
- [ ] Verify both providers show as configured
- [ ] Get bot token from @BotFather for @agentshroud.ai_bot
- [ ] Add Telegram channel with token
- [ ] Approve Telegram pairing
- [ ] Test bot via Telegram
- [ ] Test bot via Control UI

---

**Next**: Once setup is complete, you can message @agentshroud.ai_bot from any device (Mac, iPhone, iPad, Apple Watch) and get AI responses!
