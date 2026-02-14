# OpenClaw Setup & Usage Guide
**One Claw Tied Behind Your Back**

A complete beginner-friendly guide to setting up and using your secure, self-contained OpenClaw AI assistant.

---

## What Is This?

OpenClaw is your personal AI assistant that runs in a secure container on your Mac. It can:
- Respond to messages from multiple platforms (Telegram, iMessage, etc.)
- Access your Gmail, Calendar, and other services
- Execute tasks and automation on your behalf
- Represent you with your personality (loaded from IDENTITY, SOUL, USER files)

**Security**: The container ONLY has internet access - it cannot access your Mac, local network, or VPN.

---

## Step 1: Add Your API Key

OpenClaw needs an AI provider to work. You mentioned you have a Claude Max subscription - let's use that.

### Option A: Use Claude API (Anthropic)

**What you need**: Anthropic API key (separate from Claude.ai subscription)
- Visit: https://console.anthropic.com/
- Sign in with your Anthropic account
- Go to "API Keys" → "Create Key"
- Copy the key (starts with `sk-ant-`)

**Add to OpenClaw**:
```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container
nano secrets/.env
```

Add this line:
```bash
ANTHROPIC_API_KEY=sk-ant-api03-your-actual-key-here
```

Press `Ctrl+O` to save, `Enter` to confirm, `Ctrl+X` to exit.

**Important**: Claude Max subscription (claude.ai) is separate from Claude API. The API is pay-as-you-go (~$15-30/month for moderate use). If you want to use your existing Max subscription without API costs, see "Option B" below.

### Option B: Use OpenAI Instead (If You Don't Want Claude API)

If you prefer to avoid Claude API costs:
```bash
OPENAI_API_KEY=sk-your-openai-key
```

Then update `openclaw-container/config/openclaw.json`:
```json
"model": "openai/gpt-4"
```

---

## Step 2: Start OpenClaw

```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container
docker-compose up -d
```

**What this does**:
- `docker-compose up` - Starts the container
- `-d` - Runs in background (detached mode)

**Wait 10-15 seconds** for OpenClaw to fully start.

Check if it's running:
```bash
docker ps | grep openclaw
```

You should see:
```
openclaw_isaiah   Up X seconds   127.0.0.1:18789->18789/tcp, 127.0.0.1:18790->18790/tcp
```

---

## Step 3: Access OpenClaw

### Option 1: WebChat (Recommended for Testing)

Open your browser:
```bash
open http://localhost:18790
```

You'll see the OpenClaw WebChat interface. Type a message to test:
- "Who are you?" (Should respond as Isaiah's assistant using your personality)
- "What's on my calendar?" (Will prompt for Google Calendar setup)

### Option 2: Command Line Interface

```bash
docker exec -it openclaw_isaiah npx openclaw chat
```

This opens an interactive chat session. Type messages and press Enter.

Exit with `Ctrl+C`.

---

## Step 4: View Logs (Troubleshooting)

If something isn't working, check the logs:

```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container
docker-compose logs -f
```

**What to look for**:
- ✅ `OpenClaw gateway started on port 18789`
- ✅ `WebChat UI available at http://localhost:18790`
- ❌ `Error: Invalid API key` - Check your `.env` file
- ❌ `Connection refused` - Container may not be running

Press `Ctrl+C` to stop viewing logs.

---

## Step 5: Verify Network Isolation (Security Check)

Test that the container can ONLY access the internet:

### Should Work (Internet):
```bash
docker exec openclaw_isaiah curl -I https://google.com
```
Expected: `HTTP/2 200` (Success)

### Should Fail (LAN Blocked):
```bash
# Replace 192.168.1.1 with YOUR router's IP
docker exec openclaw_isaiah curl --connect-timeout 5 http://192.168.1.1
```
Expected: `Connection timed out` or `No route to host`

### Should Fail (Host Blocked):
```bash
docker exec openclaw_isaiah curl --connect-timeout 5 http://host.docker.internal:22
```
Expected: Connection failure

**If any LAN/host tests succeed, STOP and review security configuration.**

---

## Step 6: Set Up Service Integrations

Now that OpenClaw is running, let's connect it to your services.

### Create Service Accounts (Username: therealidallasj)

You'll need new accounts for security isolation:

#### 6.1: Gmail (Email, Calendar, Tasks)
1. Visit: https://accounts.google.com/signup
2. Create account: `therealidallasj@gmail.com`
3. Enable 2FA (required for security)
4. Keep credentials safe (you'll need them for OAuth)

#### 6.2: Telegram (Recommended - Primary Chat Interface)
1. Download Telegram: https://telegram.org/
2. Create account with your phone number
3. Talk to @BotFather in Telegram
4. Send: `/newbot`
5. Name: `Isaiah's Assistant` (or similar)
6. Username: `therealidallasj` (must be unique, try variations if taken)
7. Copy the token (format: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

**Add to OpenClaw**:
```bash
nano /Users/ijefferson.admin/Development/openclaw/openclaw-container/secrets/.env
```
Add:
```bash
TELEGRAM_BOT_TOKEN=your-bot-token-here
```

**Restart OpenClaw**:
```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container
docker-compose restart
```

**Test**: Open Telegram, search for your bot (@therealidallasj), send "Hello"

#### 6.3: Google Calendar Integration
```bash
docker exec -it openclaw_isaiah npx openclaw skills install @openclaw/calendar
docker exec -it openclaw_isaiah npx openclaw skills configure calendar
```

Follow the OAuth prompts - they'll open a browser for you to authorize access.

#### 6.4: PayPal ($40 Budget)
PayPal doesn't have an official OpenClaw skill yet. Options:
- **Manual**: You approve purchases via Telegram before OpenClaw executes
- **Browser Automation**: OpenClaw can control a browser to complete purchases (requires setup)

For now, we'll use manual approval (safer).

---

## Step 7: Daily Usage

### Interacting with OpenClaw

**Via Telegram** (Recommended):
- Open Telegram → Find your bot (@therealidallasj)
- Send messages like normal conversation
- Examples:
  - "What's on my calendar today?"
  - "Send an email to john@example.com saying I'll be 10 minutes late"
  - "Remind me to call Mom at 3pm"

**Via WebChat**:
- Browser: http://localhost:18790
- Good for testing and one-off queries

**Via CLI**:
```bash
docker exec -it openclaw_isaiah npx openclaw chat --message "What's the weather?"
```

### Management Commands

**Start OpenClaw**:
```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container && docker-compose up -d
```

**Stop OpenClaw**:
```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container && docker-compose down
```

**Restart OpenClaw** (after config changes):
```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container && docker-compose restart
```

**Check Status**:
```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container && bash status.sh
```

**View Logs**:
```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container && docker-compose logs -f
```

---

## Step 8: Your Personality

OpenClaw represents you using these files:
- `workspace/IDENTITY` - Your core identity, communication style
- `workspace/SOUL.md` - Your values, decision-making approach
- `workspace/USER.md` - Your professional background, context

The AI reads these files on startup. To update:
1. Edit files in `openclaw-container/workspace/`
2. Restart OpenClaw: `docker-compose restart`

**Example - Update your preferred username**:
```bash
nano /Users/ijefferson.admin/Development/openclaw/openclaw-container/workspace/IDENTITY
```
Edit the "Name" line, save, then restart.

---

## Step 9: Advanced Configuration

### Enable More Skills

List available skills:
```bash
docker exec -it openclaw_isaiah npx openclaw skills list --available
```

Install a skill:
```bash
docker exec -it openclaw_isaiah npx openclaw skills install @openclaw/todoist
```

Configure it:
```bash
docker exec -it openclaw_isaiah npx openclaw skills configure todoist
```

### Adjust Resource Limits

Edit `docker-compose.yml`:
```yaml
mem_limit: 4g   # Increase to 8g if you have RAM
cpus: 2         # Increase to 4 for faster responses
```

Restart: `docker-compose up -d --force-recreate`

### Enable Auto-Start on Boot

Create a LaunchAgent to auto-start OpenClaw when you log in:
```bash
cat > ~/Library/LaunchAgents/com.openclaw.isaiah.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.openclaw.isaiah</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/docker-compose</string>
        <string>-f</string>
        <string>/Users/ijefferson.admin/Development/openclaw/openclaw-container/docker-compose.yml</string>
        <string>up</string>
        <string>-d</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
    <key>StandardOutPath</key>
    <string>/Users/ijefferson.admin/Development/openclaw/openclaw-container/logs/launchd.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/ijefferson.admin/Development/openclaw/openclaw-container/logs/launchd.err</string>
</dict>
</plist>
EOF

launchctl load ~/Library/LaunchAgents/com.openclaw.isaiah.plist
```

---

## Troubleshooting

### Container Won't Start

**Check Docker is running**:
```bash
docker ps
```
If error: "Cannot connect to Docker daemon", start Docker Desktop or OrbStack.

**Check logs**:
```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container
docker-compose logs
```

**Common issues**:
- Port already in use: `lsof -i :18789` (kill the process using it)
- Out of memory: Increase Docker memory limit in preferences
- Invalid API key: Double-check `secrets/.env`

### WebChat Not Loading

**Test the gateway**:
```bash
curl http://localhost:18789/health
```

Expected: `{"status":"ok"}`

If connection refused:
```bash
docker-compose ps  # Check if container is running
docker-compose logs | grep error  # Look for errors
```

### Bot Not Responding on Telegram

**Check token is correct**:
```bash
grep TELEGRAM_BOT_TOKEN /Users/ijefferson.admin/Development/openclaw/openclaw-container/secrets/.env
```

**Check Telegram channel is enabled**:
```bash
docker exec -it openclaw_isaiah npx openclaw channels list
```

Should show `telegram: enabled`

**Restart after adding token**:
```bash
docker-compose restart
```

### "Permission Denied" Errors

**Fix permissions**:
```bash
cd /Users/ijefferson.admin/Development/openclaw/openclaw-container
chmod 600 secrets/.env
chmod -R 755 logs workspace config
```

### Cannot Access LAN (Isolation Working as Intended)

This is **expected behavior** for security. The container can ONLY access the internet.

If you need to access a specific local service (e.g., Home Assistant), you would need to:
1. Expose that service to the internet (via Cloudflare Tunnel, Tailscale, etc.)
2. Access it via public URL instead of LAN IP

**Do NOT disable network isolation** - it defeats the security model.

---

## Backup & Recovery

### Backup Your Configuration

```bash
cd /Users/ijefferson.admin/Development/openclaw
tar -czf openclaw-backup-$(date +%Y%m%d).tar.gz openclaw-container/
```

**What's backed up**:
- Configuration (`config/`)
- Secrets (`secrets/.env`)
- Personality files (`workspace/`)
- Logs (`logs/`)

**Restore**:
```bash
tar -xzf openclaw-backup-20260214.tar.gz
cd openclaw-container
docker-compose up -d
```

### Secure Backup Storage

**Never commit secrets to Git**:
```bash
cat openclaw-container/.gitignore
```
Should include `secrets/` and `logs/`.

**Encrypted backup** (recommended):
```bash
tar -czf - openclaw-container/ | openssl enc -aes-256-cbc -out openclaw-backup-encrypted.tar.gz.enc
```

Decrypt:
```bash
openssl enc -aes-256-cbc -d -in openclaw-backup-encrypted.tar.gz.enc | tar -xzf -
```

---

## Sharing with Friends

To share this setup:

1. **Clean your directory** (remove secrets):
```bash
cd /Users/ijefferson.admin/Development/openclaw
cp -r openclaw-container openclaw-distribution
cd openclaw-distribution
rm secrets/.env
echo "ANTHROPIC_API_KEY=" > secrets/.env
echo "TELEGRAM_BOT_TOKEN=" >> secrets/.env
rm -rf logs/*
```

2. **Create tarball**:
```bash
cd /Users/ijefferson.admin/Development/openclaw
tar -czf one-claw-tied-behind-your-back.tar.gz deploy-local.sh Dockerfile.secure README.md SECURITY-AUDIT.md SETUP-GUIDE.md openclaw-distribution/
```

3. **Share**: Send `one-claw-tied-behind-your-back.tar.gz` to friends

**They extract and run**:
```bash
tar -xzf one-claw-tied-behind-your-back.tar.gz
cd one-claw-tied-behind-your-back
./deploy-local.sh
```

---

## Next Steps

1. ✅ **You are here** - OpenClaw is deployed and running
2. 🔑 Add your API key (Anthropic or OpenAI)
3. 🚀 Start the container: `docker-compose up -d`
4. 💬 Test via WebChat: http://localhost:18790
5. 📱 Set up Telegram bot for mobile access
6. 📧 Connect Gmail and Calendar (OAuth setup)
7. 🎯 Start using your AI assistant!

---

## Quick Reference

| Task | Command |
|------|---------|
| Start | `cd openclaw-container && docker-compose up -d` |
| Stop | `cd openclaw-container && docker-compose down` |
| Restart | `cd openclaw-container && docker-compose restart` |
| Logs | `cd openclaw-container && docker-compose logs -f` |
| Status | `cd openclaw-container && bash status.sh` |
| WebChat | `open http://localhost:18790` |
| CLI Chat | `docker exec -it openclaw_isaiah npx openclaw chat` |
| Add Skill | `docker exec -it openclaw_isaiah npx openclaw skills install @openclaw/SKILLNAME` |
| Security Test | `docker exec openclaw_isaiah curl --connect-timeout 5 http://192.168.1.1` (should fail) |

---

## Getting Help

**Logs first**: Always check logs when something doesn't work:
```bash
docker-compose logs | tail -100
```

**OpenClaw Documentation**: https://github.com/openclaw/openclaw

**Common Issues**: See "Troubleshooting" section above

**Security Questions**: See `SECURITY-AUDIT.md` for comprehensive security analysis

---

**Project**: One Claw Tied Behind Your Back
**Security**: Internet-only, self-contained, no LAN/VPN access
**Personality**: Isaiah Dallas Jefferson, Jr. (Chief Innovation Engineer, Fluence Energy)
