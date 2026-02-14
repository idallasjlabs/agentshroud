# OneClaw - Your Secure Personal AI Assistant

A simple, secure way to run your own AI assistant on your Mac. Everything stays on your computer in one folder.

## What You Get

- 🤖 **Personal AI assistant** that knows you and speaks for you
- 🔒 **100% private** - runs on your Mac, internet-only access (can't see your home network)
- 📁 **Self-contained** - everything in one folder, nothing installed system-wide
- 🌐 **Optional remote access** - securely access from phone/tablet via Tailscale

---

## Prerequisites (What You Need Installed)

✅ **Docker** or **OrbStack** (for running the container)
- Install Docker Desktop: https://www.docker.com/products/docker-desktop/
- OR install OrbStack (faster, lighter): https://orbstack.dev/

✅ **Python 3** (already on Mac)
- Check: Open Terminal and type `python3 --version`

✅ **(Optional) Tailscale** (for remote HTTPS access)
- Only needed if you want to access OneClaw from your phone/tablet
- Install: https://tailscale.com/download

---

## Quick Setup (15 Minutes)

### Step 1: Get an API Key

OneClaw needs an AI provider. Choose one:

**Option A: Claude API** (Recommended)
1. Go to https://console.anthropic.com/
2. Click "Get API keys" → "Create Key"
3. Copy the key (starts with `sk-ant-`)
4. Add $10-20 credit in "Billing" section
5. Cost: ~$15-30/month for moderate use

**Option B: OpenAI**
1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with `sk-`)
4. Add $10-20 credit
5. Cost: ~$10-20/month for moderate use

### Step 2: Add Your API Key

Open Terminal and run:

```bash
nano oneclaw-container/secrets/.env
```

Add this line (replace with your actual key):
```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Save: Press `Ctrl+O`, then `Enter`, then `Ctrl+X`

### Step 3: Start OneClaw

```bash
cd oneclaw-container
docker compose up -d
```

Wait 30 seconds for it to start.

### Step 4: Access the Web Interface

#### Option A: Local Access (Easiest)

Run this command to start the web interface:
```bash
python3 -m http.server 18791 --directory control-ui &
```

Then open in your browser:
```
http://localhost:18791
```

#### Option B: Remote Access via Tailscale (Optional)

**Only do this if you want to access OneClaw from your phone or other devices.**

1. Install Tailscale: https://tailscale.com/download
2. Run this command:
   ```bash
   tailscale serve --bg http://127.0.0.1:18791
   ```
3. You'll get a URL like: `https://your-mac-name.your-tailnet.ts.net`
4. Open that URL on any device connected to your Tailscale network

**What is Tailscale?**
- Creates a private network between your devices
- Gives you secure HTTPS access from anywhere
- Only devices you authorize can connect
- Free for personal use

---

## Daily Usage

### Start OneClaw

```bash
# Start the container
cd oneclaw-container
docker compose up -d

# Start the web interface (local access)
python3 -m http.server 18791 --directory control-ui &

# OR start Tailscale (remote access)
tailscale serve --bg http://127.0.0.1:18791
```

Then open: http://localhost:18791 (local) or https://your-mac.tailnet.ts.net (remote)

### Stop OneClaw

```bash
cd oneclaw-container
docker compose down

# Stop web interface
kill $(lsof -ti:18791)

# OR stop Tailscale
tailscale serve --https=443 off
```

### View Logs (If Something's Wrong)

```bash
cd oneclaw-container
docker compose logs -f
```

Press `Ctrl+C` to stop viewing logs.

---

## What's in This Folder

```
oneclaw/
├── oneclaw-container/          # Everything OneClaw needs
│   ├── workspace/              # Your personality files
│   │   ├── IDENTITY           # Who you are, how you talk
│   │   ├── SOUL.md            # Your values and goals
│   │   └── USER.md            # Your background and context
│   ├── config/
│   │   └── config.json        # OneClaw settings
│   ├── secrets/
│   │   └── .env               # API keys (KEEP PRIVATE!)
│   ├── control-ui/            # Web interface files
│   └── docker-compose.yml     # Container configuration
│
├── Dockerfile.secure          # How OneClaw is built
└── README.md                  # This file
```

**Everything is self-contained** - no files scattered across your Mac!

---

## Customize Your AI's Personality

Your AI assistant reads these three files to understand how to represent you:

1. **IDENTITY** - Your name, role, communication style
2. **SOUL.md** - Your values, how you make decisions
3. **USER.md** - Your professional background, team, tech environment

To update:
```bash
nano oneclaw-container/workspace/IDENTITY
nano oneclaw-container/workspace/SOUL.md
nano oneclaw-container/workspace/USER.md
```

After editing, restart:
```bash
cd oneclaw-container
docker compose restart
```

---

## Troubleshooting

### "Cannot connect to Docker"

**Problem**: Docker isn't running

**Fix**: Start Docker Desktop or OrbStack from your Applications folder

### "Container keeps restarting"

**Problem**: Missing or invalid API key

**Fix**:
```bash
# Check your API key
cat oneclaw-container/secrets/.env

# Should show: ANTHROPIC_API_KEY=sk-ant-...
# If not, add it and restart
cd oneclaw-container
docker compose restart
```

### "Cannot access localhost:18791"

**Problem**: Web server isn't running

**Fix**:
```bash
# Start the web server
python3 -m http.server 18791 --directory oneclaw-container/control-ui &

# Check it's running
curl http://localhost:18791
```

### "How do I reset everything?"

```bash
cd oneclaw-container
docker compose down
docker rmi oneclaw-secure:latest
cd ..
./deploy-local.sh
```

---

## Security Features

### What OneClaw CAN Access
- ✅ Internet (for AI API calls)
- ✅ Files in `oneclaw-container/workspace/` (your personality)
- ✅ Its own logs and configuration

### What OneClaw CANNOT Access
- ❌ Your home folder
- ❌ Other files on your Mac
- ❌ Your local network (router, printers, NAS, etc.)
- ❌ Your VPN or Tailscale network
- ❌ Other Docker containers

### How It's Secured
1. **Runs in a container** - isolated from your Mac
2. **Non-root user** - can't modify system files
3. **Network isolation** - internet-only access
4. **Localhost binding** - web interface only accessible from your Mac (unless Tailscale enabled)
5. **All capabilities dropped** - minimal permissions

To verify security:
```bash
# Should work (internet):
docker exec oneclaw_isaiah curl -I https://google.com

# Should FAIL (your router - use your actual router IP):
docker exec oneclaw_isaiah curl --connect-timeout 5 http://192.168.1.1
```

---

## Backup Your Setup

### Create Backup

```bash
# Backup everything
tar -czf oneclaw-backup-$(date +%Y%m%d).tar.gz oneclaw-container/

# Backup without secrets (for sharing)
tar -czf oneclaw-backup-$(date +%Y%m%d).tar.gz \
  --exclude='oneclaw-container/secrets/.env' \
  --exclude='oneclaw-container/logs/*' \
  oneclaw-container/
```

### Restore Backup

```bash
tar -xzf oneclaw-backup-20260214.tar.gz
cd oneclaw-container
docker compose up -d
```

---

## Share with Friends

To share OneClaw with others:

1. **Remove your secrets**:
   ```bash
   rm oneclaw-container/secrets/.env
   echo "ANTHROPIC_API_KEY=" > oneclaw-container/secrets/.env
   ```

2. **Customize personality files** (optional):
   - Edit `workspace/IDENTITY`, `SOUL.md`, `USER.md` to be generic
   - Or delete them so your friend can add their own

3. **Zip everything**:
   ```bash
   cd ..
   zip -r oneclaw-for-friend.zip oneclaw/ \
     -x "*/logs/*"
   ```

4. **Send them**:
   - The zip file
   - This README
   - Tell them to follow "Quick Setup" above

---

## Cost Breakdown

### Monthly Costs
- **Claude API**: $15-30 (pay-as-you-go, ~$3 per million tokens)
- **OpenAI API**: $10-20 (similar usage)
- **Docker/OrbStack**: Free
- **Tailscale**: Free (personal use)
- **Everything else**: Free

**Total: $15-30/month** for a private AI assistant

### One-Time Costs
- None! Everything is free or pay-as-you-go

---

## Common Questions

**Q: Will this slow down my Mac?**
A: No. OneClaw uses 2 CPU cores max and 4GB RAM. Your Mac has plenty to spare.

**Q: Can I run this on Windows or Linux?**
A: Not yet - this setup is macOS-specific. A Linux version would work with minor changes.

**Q: Is my data private?**
A: Yes. OneClaw runs locally. Only API calls go to Claude/OpenAI (encrypted). No telemetry.

**Q: Can I use my existing Claude Pro subscription?**
A: No. Claude Pro (claude.ai) is separate from Claude API. You need API credits.

**Q: What if I want to stop using it?**
A: Just delete the `oneclaw` folder. Nothing is installed system-wide.

**Q: Can I use this without Tailscale?**
A: Yes! Tailscale is completely optional. Use `http://localhost:18791` for local-only access.

---

## Next Steps After Setup

1. **Test the web interface** - Open http://localhost:18791 and send a test message
2. **Customize your personality** - Edit `workspace/IDENTITY`, `SOUL.md`, `USER.md`
3. **Set up channels** (optional):
   - Telegram bot (for mobile messaging)
   - Gmail integration (for email)
   - Calendar sync
4. **Enable Tailscale** (optional) - For remote access from phone/tablet

---

## Getting Help

- **OneClaw Documentation**: https://docs.openclaw.ai
- **GitHub Issues**: https://github.com/openclaw/openclaw/issues
- **This Project**: https://github.com/idallasj/oneclaw

---

## What Makes This Special

Unlike ChatGPT or Claude.ai:
- ✅ **Runs locally** on your Mac (more private)
- ✅ **Customizable personality** - it knows YOU
- ✅ **Multiple integrations** - Telegram, Gmail, Calendar, etc.
- ✅ **Programmable** - add your own skills and automations
- ✅ **Self-contained** - one folder, easy to backup/move
- ✅ **Optional remote access** - via Tailscale (secure)

---

**Project**: OneClaw
**Security**: Maximum (containerized, isolated, internet-only)
**Privacy**: 100% (runs on your Mac)
**Cost**: ~$15-30/month (API usage only)
**Difficulty**: Easy (just follow this guide!)

**Ready?** Start with "Quick Setup" above! ⬆️
