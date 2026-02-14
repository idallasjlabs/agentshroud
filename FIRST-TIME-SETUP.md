# First Time Setup Guide - OneClaw

Complete step-by-step setup for beginners. Follow in order.

## Overview

You'll create fresh accounts for OneClaw to keep it separate from your personal accounts. This takes about 30 minutes.

---

## Step 1: Create Dedicated Gmail Account

**Why?** Keep OneClaw's activities separate from your personal email for better security and organization.

### Instructions

1. **Go to Gmail signup**: https://accounts.google.com/signup

2. **Choose a username**:
   - Pattern: `yourname-oneclaw@gmail.com`
   - Example: `therealidallasj@gmail.com`
   - Must be available (try variations if taken)

3. **Phone verification** - You have options:

   **Option A: Use existing Google Voice number**
   - If you have Google Voice, you can reuse the number
   - Google allows one number for multiple Gmail accounts

   **Option B: Create new Google Voice number** (Recommended)
   - Go to https://voice.google.com
   - Sign in with your personal Gmail
   - Click "Get a number"
   - Choose area code and number
   - Free for US/Canada users
   - Use this number for OneClaw Gmail verification

   **Option C: Use your phone number**
   - Less ideal (ties OneClaw to your personal number)
   - But works if you don't have Google Voice

4. **Complete signup**:
   - Enter verification code
   - Set strong password (save in password manager)
   - Skip recovery email (or use your personal email)

5. **Enable 2-Factor Authentication** (Recommended):
   - Go to https://myaccount.google.com/security
   - Click "2-Step Verification"
   - Follow setup wizard

6. **Save credentials**:
   ```
   Email: yourname-oneclaw@gmail.com
   Password: [save securely]
   2FA: [app or backup codes]
   ```

✅ **Task completed!** You now have a dedicated Gmail for OneClaw.

---

## Step 2: Create AI API Account

**Why?** OneClaw needs an AI provider to generate responses.

### Option A: OpenAI (What You're Doing)

1. **Go to OpenAI**: https://platform.openai.com/signup

2. **Sign up**:
   - Use your NEW Gmail: `yourname-oneclaw@gmail.com`
   - Click "Continue with Google"
   - Select the OneClaw Gmail account
   - Verify email if prompted

3. **Create API Key**:
   - Go to https://platform.openai.com/api-keys
   - Click "Create new secret key"
   - Name it: `OneClaw`
   - **COPY THE KEY** (starts with `sk-`)
   - **SAVE IT** - you won't see it again!

4. **Add Billing**:
   - Go to https://platform.openai.com/settings/organization/billing
   - Click "Add payment method"
   - Add credit/debit card
   - Add initial credit: $10-20 (recommended)

5. **Set spending limit** (Optional but recommended):
   - Go to https://platform.openai.com/settings/organization/limits
   - Set monthly budget: $30 (prevents runaway costs)

**Cost**: ~$10-20/month for moderate use (pay-as-you-go)

### Option B: Anthropic Claude API (Alternative)

If you prefer Claude instead of OpenAI:

1. **Go to Anthropic**: https://console.anthropic.com/
2. **Sign up** with OneClaw Gmail
3. **Create API key**: Settings → API Keys → Create Key
4. **Add credits**: Billing → Add to balance → $10-20
5. **Save key** (starts with `sk-ant-`)

**Cost**: ~$15-30/month for moderate use

✅ **Task completed!** You have an AI API account and key.

---

## Step 3: Add API Key to OneClaw

Now let's give OneClaw access to the AI.

### Instructions

1. **Open Terminal** (Spotlight → type "Terminal")

2. **Navigate to OneClaw**:
   ```bash
   cd ~/Development/oneclaw
   # Or wherever you put OneClaw
   ```

3. **Edit secrets file**:
   ```bash
   nano oneclaw-container/secrets/.env
   ```

4. **Add your API key**:

   For OpenAI:
   ```bash
   OPENAI_API_KEY=sk-proj-your-actual-key-here
   ```

   For Anthropic:
   ```bash
   ANTHROPIC_API_KEY=sk-ant-api03-your-actual-key-here
   ```

5. **Save the file**:
   - Press `Ctrl+O` (WriteOut)
   - Press `Enter` (confirm)
   - Press `Ctrl+X` (eXit)

6. **Verify it was saved**:
   ```bash
   cat oneclaw-container/secrets/.env
   ```
   Should show your API key.

✅ **Task completed!** API key is configured.

---

## Step 4: Configure AI Model

Tell OneClaw which AI to use.

### For OpenAI Users

1. **Edit config file**:
   ```bash
   nano oneclaw-container/config/config.json
   ```

2. **Find this line** (around line 14):
   ```json
   "model": "anthropic/claude-opus-4-6",
   ```

3. **Change to**:
   ```json
   "model": "openai/gpt-4",
   ```

4. **Save**: `Ctrl+O`, `Enter`, `Ctrl+X`

### For Anthropic Users

No changes needed - the default is already Claude.

✅ **Task completed!** Model configured.

---

## Step 5: Start OneClaw

Time to fire it up!

### Option A: Use the Startup Script (Easiest)

```bash
cd ~/Development/oneclaw
./start-oneclaw.sh
```

This automatically:
- Starts the Docker container
- Starts the web interface
- Opens browser (if you choose)

### Option B: Manual Start

```bash
# Start container
cd ~/Development/oneclaw/oneclaw-container
docker compose up -d

# Wait 30 seconds
sleep 30

# Start web interface
python3 -m http.server 18791 --directory control-ui &

# Open browser
open http://localhost:18791
```

### Verify It's Running

Check container status:
```bash
docker ps | grep oneclaw
```

Should show:
```
oneclaw_isaiah   Up XX seconds (healthy)
```

✅ **Task completed!** OneClaw is running.

---

## Step 6: Connect Control UI to Gateway

The web interface needs to connect to OneClaw's backend.

### Instructions

1. **Open Control UI**:
   - Local: http://localhost:18791
   - Or Tailscale: https://marvin.tail240ea8.ts.net

2. **Look for connection dialog**:
   - May appear automatically
   - Or look for ⚙️ Settings icon
   - Or "Add Gateway" button

3. **Enter connection details**:
   ```
   Gateway URL: ws://127.0.0.1:18789
   Auth Token: [see below]
   ```

4. **Get your auth token**:
   ```bash
   grep OPENCLAW_GATEWAY_TOKEN oneclaw-container/secrets/.env
   ```
   Copy the long hex string (64 characters).

5. **Click "Connect"**

6. **Verify**: Status should change to "Connected" (green)

✅ **Task completed!** Control UI is connected.

---

## Step 7: Test OneClaw

Send your first message!

### Instructions

1. **In the Control UI**, find the message box

2. **Type**:
   ```
   Hello, who are you?
   ```

3. **Press Send** or `Enter`

4. **Wait** 10-30 seconds (first message is slower)

5. **Expected response**:
   - Should mention your name (from IDENTITY file)
   - Should be direct and technical (from SOUL.md)
   - Should work without errors

### If It Doesn't Work

**Check logs**:
```bash
docker compose -f oneclaw-container/docker-compose.yml logs -f
```

**Common issues**:
- "Invalid API key" → Check `secrets/.env`, restart container
- "Insufficient credits" → Add money to OpenAI/Anthropic account
- "Model not found" → Check `config.json` model name

✅ **Task completed!** OneClaw is working!

---

## Optional: Set Up Telegram Bot

Get OneClaw on your phone.

### Instructions

1. **Open Telegram app** (install from App Store if needed)

2. **Search for**: `@BotFather`

3. **Start chat**, send: `/newbot`

4. **Follow prompts**:
   - Bot name: `Isaiah's Assistant` (or whatever you like)
   - Username: `therealidallasj_bot` (must end in `_bot`)
   - Must be unique - try variations if taken

5. **Copy the bot token**:
   ```
   Format: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz
   ```

6. **Add to OneClaw**:
   ```bash
   nano oneclaw-container/secrets/.env
   ```

   Add line:
   ```bash
   TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
   ```

   Save: `Ctrl+O`, `Enter`, `Ctrl+X`

7. **Restart OneClaw**:
   ```bash
   cd oneclaw-container
   docker compose restart
   ```

8. **Test it**:
   - In Telegram, search for your bot: `@therealidallasj_bot`
   - Click "Start"
   - Send: `Hello`
   - OneClaw should respond!

✅ **Optional task completed!** You can now message OneClaw from your phone.

---

## Optional: Enable Remote HTTPS Access

Access OneClaw from anywhere via Tailscale.

### Prerequisites

- Tailscale installed: https://tailscale.com/download
- Tailscale account (free for personal use)

### Instructions

1. **Install Tailscale** (if not already):
   ```bash
   brew install --cask tailscale
   ```

2. **Start Tailscale**:
   - Open Tailscale from Applications
   - Sign in (creates account if needed)

3. **Enable serve**:
   ```bash
   tailscale serve --bg http://127.0.0.1:18791
   ```

4. **Get your URL**:
   ```
   Should show: https://your-mac-name.your-tailnet.ts.net/
   ```

5. **Test it**:
   - Open that URL on your phone (connected to Tailscale)
   - Should see the OneClaw Control UI
   - Works from anywhere!

**What is Tailscale?**
- Private VPN between your devices
- Secure HTTPS access
- Only your devices can connect
- Free for personal use (up to 100 devices)

✅ **Optional task completed!** OneClaw is accessible remotely via HTTPS.

---

## Optional: Gmail Integration

Let OneClaw read and send emails.

### Instructions

1. **Install Gmail skill**:
   ```bash
   docker exec oneclaw_isaiah node openclaw.mjs skills install @openclaw/gmail
   ```

2. **Configure OAuth**:
   ```bash
   docker exec oneclaw_isaiah node openclaw.mjs skills configure gmail
   ```

3. **Browser will open**:
   - Sign in with `yourname-oneclaw@gmail.com`
   - Click "Allow" to grant permissions
   - Close browser when done

4. **Test it**:
   - In Control UI: "Check my recent emails"
   - Should list your inbox

### What Can It Do?

- "Check my emails from today"
- "Send an email to john@example.com saying I'll be late"
- "What's in my inbox?"
- "Forward that email to sarah@example.com"

### Security

- Uses OAuth (secure, no password stored)
- You can revoke access anytime: https://myaccount.google.com/permissions
- Only accesses emails when you ask

✅ **Optional task completed!** Gmail integration working.

---

## Summary of Accounts Created

| Service | Account | Purpose | Cost |
|---------|---------|---------|------|
| Gmail | `yourname-oneclaw@gmail.com` | Dedicated email for OneClaw | Free |
| Google Voice | New or existing number | Phone verification | Free |
| OpenAI | Same Gmail | AI responses | $10-20/month |
| Telegram | `@yourname_bot` | Mobile messaging (optional) | Free |
| Tailscale | Your choice | Remote access (optional) | Free |

---

## Next Steps

1. **Customize personality**:
   - Edit `oneclaw-container/workspace/IDENTITY`
   - Edit `oneclaw-container/workspace/SOUL.md`
   - Edit `oneclaw-container/workspace/USER.md`
   - Restart: `docker compose restart`

2. **Explore features**:
   - Try different commands
   - Set up more integrations
   - Add Telegram bot for mobile

3. **Share with friends**:
   - See README.md "Share with Friends" section
   - They follow this same guide!

---

## Troubleshooting

### "Cannot connect to Docker"
- Start Docker Desktop or OrbStack

### "Container keeps restarting"
- Check API key: `cat oneclaw-container/secrets/.env`
- Check logs: `docker compose logs`

### "Control UI shows disconnected"
- Verify gateway URL: `ws://127.0.0.1:18789`
- Check token in `secrets/.env`

### "API key invalid"
- Verify key is correct
- Check you added credits to account
- Wait a few minutes (sometimes takes time to activate)

---

## Getting Help

- **OneClaw Docs**: https://docs.openclaw.ai
- **This Project**: https://github.com/idallasj/oneclaw
- **OpenClaw GitHub**: https://github.com/openclaw/openclaw

---

**You're all set!** 🎉

Your OneClaw assistant is running and ready to help. Start chatting!
