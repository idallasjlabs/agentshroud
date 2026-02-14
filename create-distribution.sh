#!/bin/bash

###############################################################################
# Distribution Package Creator
# Project: One Claw Tied Behind Your Back
#
# Creates a shareable tarball for deploying OpenClaw on friends' Macs
###############################################################################

DIST_NAME="one-claw-tied-behind-your-back-v1.0"
DIST_DIR="/tmp/$DIST_NAME"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${BLUE}"
echo "Creating distribution package: $DIST_NAME"
echo -e "${NC}"
echo ""

# Clean up any existing distribution
rm -rf "$DIST_DIR"
rm -f "/tmp/$DIST_NAME.tar.gz"

# Create distribution directory
mkdir -p "$DIST_DIR"

# Copy deployment scripts and Docker files
echo "Copying deployment scripts and Docker files..."
cp "$SCRIPT_DIR/deploy-openclaw.sh" "$DIST_DIR/"
cp "$SCRIPT_DIR/setup-accounts.sh" "$DIST_DIR/"
cp "$SCRIPT_DIR/Dockerfile.secure" "$DIST_DIR/"
cp "$SCRIPT_DIR/docker-compose.secure.yml" "$DIST_DIR/"
cp "$SCRIPT_DIR/SECURITY.md" "$DIST_DIR/"

# Create README
echo "Creating README..."
cat > "$DIST_DIR/README.md" <<'EOF'
# One Claw Tied Behind Your Back

Secure OpenClaw deployment for macOS with network isolation.

> "The best way to secure your AI assistant is to give it only what it needs—and nothing more."

## What is This?

This is a complete deployment package for running [OpenClaw](https://github.com/openclaw/openclaw), an open-source personal AI assistant, in a secure, isolated environment on macOS. The deployment prioritizes security while maintaining full functionality for messaging, email, calendar, and automation tasks.

## Quick Start

```bash
# 1. Extract the package
tar -xzf one-claw-tied-behind-your-back-v1.0.tar.gz
cd one-claw-tied-behind-your-back-v1.0

# 2. Run the deployment script
./deploy-openclaw.sh

# 3. Follow the prompts to complete setup
```

## What This Deployment Does

### Security Features

- **Network Isolation**: Container can only access the internet, not your local network
- **Sandboxed Execution**: All AI tool use runs in a restricted environment
- **Non-Root Container**: Runs as unprivileged user (UID 1000)
- **Read-Only Filesystem**: Container root filesystem is immutable
- **Audit Logging**: All actions are logged for review
- **Minimal Capabilities**: Linux capabilities dropped to minimum required
- **Resource Limits**: CPU and memory limits prevent resource exhaustion

### Features

- **Multi-Platform Messaging**: Telegram, iMessage (via BlueBubbles), Slack, Discord, and more
- **Email Integration**: Gmail with real-time push notifications
- **Calendar Management**: Google Calendar integration, syncs with Fantastical
- **Task Management**: Google Tasks, optional Todoist integration
- **Browser Control**: Automated web browsing for tasks like Amazon purchases
- **Voice Control**: Optional wake-word detection and voice responses
- **66 Built-in Skills**: Calendar, weather, reminders, translations, and more
- **Extensible**: Install community skills from ClavHub.ai

## Requirements

### System Requirements

- **Operating System**: macOS 12 (Monterey) or later
- **CPU**: Intel or Apple Silicon (M1/M2/M3)
- **RAM**: 8GB minimum, 16GB recommended
- **Disk Space**: 10GB free space minimum
- **Internet**: Broadband connection required

### Software Requirements

- **Docker**: Docker Desktop or OrbStack (OrbStack recommended for better performance)
- **Node.js**: Version 22 or later
- **Homebrew**: macOS package manager

### Optional But Recommended

- **Application Firewall**: Little Snitch ($45) or Lulu (free)
- **Password Manager**: 1Password, Bitwarden, or similar for API keys
- **BlueBubbles**: For iMessage integration (free)

## Installation Guide

### Step 1: Prerequisites

Install required software:

```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js 22
brew install node@22

# Install OrbStack (recommended) or Docker Desktop
brew install --cask orbstack
# OR
brew install --cask docker

# Install optional tools
brew install jq  # JSON processor
brew install --cask lulu  # Free firewall (or purchase Little Snitch)
```

### Step 2: Run Deployment Script

```bash
./deploy-openclaw.sh
```

This script will:
1. Check that all prerequisites are installed
2. Create the directory structure at `~/.oneclaw-secure/`
3. Generate secure authentication tokens
4. Create OpenClaw configuration with sandbox enabled
5. Set up Docker Compose with security hardening
6. Create macOS bridge service for iMessage
7. Configure firewall rules
8. Create management scripts (start, stop, status, logs, backup)
9. Pull the latest OpenClaw Docker image

The script takes about 5-10 minutes to complete.

### Step 3: Add API Keys

Before starting OpenClaw, you need at least one AI provider API key:

```bash
# Edit the secrets file
nano ~/.oneclaw-secure/secrets/.env
```

Required: Add ONE of the following:
- `ANTHROPIC_API_KEY` (Claude - recommended)
- `OPENAI_API_KEY` (GPT-4)
- `GEMINI_API_KEY` (Google)

**Where to get API keys:**
- Anthropic (Claude): https://console.anthropic.com/
- OpenAI: https://platform.openai.com/api-keys
- Google (Gemini): https://aistudio.google.com/app/apikey

### Step 4: Create Service Accounts

Run the account setup wizard:

```bash
./setup-accounts.sh
```

This wizard will guide you through creating accounts for:
- Gmail (therealidallasj@gmail.com)
- Apple ID (therealidallasj@icloud.com)
- Telegram bot (@therealidallasj)
- PayPal (for automated purchases)
- Optional: Todoist, Slack

The wizard opens web pages and waits for you to complete each step.

### Step 5: Start OpenClaw

```bash
cd ~/.oneclaw-secure
./start.sh
```

Wait for the health check to confirm the gateway is ready.

### Step 6: Access OpenClaw

Open WebChat UI in your browser:
```
http://localhost:18790
```

Or chat via Telegram with your bot: @therealidallasj

## Management

### Start Services

```bash
cd ~/.oneclaw-secure
./start.sh
```

### Stop Services

```bash
cd ~/.oneclaw-secure
./stop.sh
```

### Check Status

```bash
cd ~/.oneclaw-secure
./status.sh
```

### View Logs

```bash
cd ~/.oneclaw-secure
./logs.sh
```

### Create Backup

```bash
cd ~/.oneclaw-secure
./backup.sh
```

Backups are saved to: `~/openclaw-backups/`

### Restore from Backup

```bash
cd ~/.oneclaw-secure
./stop.sh
tar -xzf ~/openclaw-backups/openclaw_backup_YYYYMMDD_HHMMSS.tar.gz -C ~/.oneclaw-secure
./start.sh
```

## Configuration

### OpenClaw Configuration

Main configuration: `~/.oneclaw-secure/config/oneclaw.json`

Key settings:
- AI model selection
- Sandbox mode (enabled by default)
- Channel configurations (Telegram, iMessage, etc.)
- Security policies
- Skill settings

### Environment Variables

Secrets and API keys: `~/.oneclaw-secure/secrets/.env`

**Never commit this file to git or share it publicly!**

### Docker Compose

Container configuration: `~/.oneclaw-secure/docker-compose.yml`

Includes:
- Security hardening options
- Network isolation settings
- Resource limits
- Volume mounts
- Health checks

## Network Isolation

This deployment implements multi-layer network security:

### Layer 1: Docker Network
- Custom bridge network isolates container from default Docker network
- Ports exposed only to localhost (127.0.0.1)

### Layer 2: Container Firewall
- iptables rules block private IP ranges (RFC1918)
- Blocks: 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8
- Allows: Internet access

### Layer 3: Host Firewall
- Little Snitch or Lulu monitors com.docker.vpnkit process
- Blocks LAN access, allows internet

### Layer 4: Application Security
- Sandbox mode restricts tool execution
- Pairing required for new contacts
- Audit logging tracks all actions

## iMessage Integration

iMessage integration uses [BlueBubbles](https://bluebubbles.app/), which requires:

1. Mac running 24/7 with Messages.app signed in
2. BlueBubbles server installed and configured
3. macOS bridge service relaying webhooks

### BlueBubbles Setup

```bash
# Install BlueBubbles
brew install --cask bluebubbles

# Configure
# 1. Open BlueBubbles.app
# 2. Enable Web API
# 3. Set password (matches BLUEBUBBLES_PASSWORD in .env)
# 4. Configure webhook: http://localhost:8765/bluebubbles-webhook
# 5. Enable Private API features for full functionality
```

### Keep Mac Awake

To prevent Messages.app from going idle:

```bash
# Prevent sleep while plugged in
sudo pmset -c sleep 0
sudo pmset -c displaysleep 10

# OR use caffeinate to prevent sleep
caffeinate -i -s &
```

## Service Integrations

### Gmail

Set up real-time email notifications:

```bash
openclaw webhooks gmail setup --account therealidallasj@gmail.com
```

This configures Google Cloud Pub/Sub for push notifications.

### Google Calendar

Install and configure the calendar skill:

```bash
openclaw skills install @openclaw/calendar
openclaw skills configure calendar
```

Fantastical will automatically sync with your Google Calendar.

### Telegram

After creating your bot via @BotFather:

1. Start a chat with your bot: @therealidallasj
2. Send: `/pair` to pair your account
3. Bot will respond and begin accepting commands

### PayPal/Amazon

No official integration exists yet. Workarounds:

1. **Browser Automation**: OpenClaw can control Chrome to make purchases
2. **Approval Workflow**: Bot asks for permission before purchasing
3. **Spending Limits**: Set PayPal monthly limit to $40

## Troubleshooting

### Container Won't Start

```bash
# Check Docker is running
docker ps

# View container logs
cd ~/.oneclaw-secure
./logs.sh

# Restart services
./stop.sh && ./start.sh
```

### Gateway Not Responding

```bash
# Check health endpoint
curl http://localhost:18789/health

# Check if port is in use
lsof -i :18789

# Verify environment variables
cat ~/.oneclaw-secure/secrets/.env | grep ANTHROPIC_API_KEY
```

### iMessage Not Working

```bash
# Check BlueBubbles is running
curl http://localhost:3000/api/v1/ping

# Check bridge is running
curl http://localhost:8765/health

# Restart bridge
launchctl unload ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist
launchctl load ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist
```

### Network Isolation Not Working

```bash
# Test from inside container
docker exec oneclaw_gateway curl -I https://google.com  # Should work
docker exec oneclaw_gateway curl --connect-timeout 5 http://192.168.1.1  # Should fail

# Verify container security
docker inspect oneclaw_gateway | jq '.[0].HostConfig.CapDrop'
docker inspect oneclaw_gateway | jq '.[0].HostConfig.ReadonlyRootfs'
```

### High Memory Usage

```bash
# Check resource usage
docker stats oneclaw_gateway

# Adjust memory limit in docker-compose.yml
nano ~/.oneclaw-secure/docker-compose.yml
# Change: mem_limit: 4g

# Restart
cd ~/.oneclaw-secure && ./stop.sh && ./start.sh
```

## Security Best Practices

1. **API Keys**:
   - Never commit .env files to git
   - Use API keys with least privilege
   - Rotate keys periodically
   - Monitor API usage for anomalies

2. **Updates**:
   - Keep OpenClaw updated: `docker pull openclaw/openclaw:latest`
   - Update Node.js and dependencies regularly
   - Review OpenClaw security advisories

3. **Backups**:
   - Run `./backup.sh` weekly
   - Store backups off-site (encrypted)
   - Test restore procedure occasionally

4. **Monitoring**:
   - Check logs daily: `./logs.sh`
   - Review audit log: `~/.oneclaw-secure/workspace/logs/audit.log`
   - Set up automated alerts with `monitor.sh`

5. **Firewall**:
   - Configure Little Snitch or Lulu rules
   - Block com.docker.vpnkit from LAN
   - Monitor for unexpected connections

6. **Pairing**:
   - Only pair trusted contacts
   - Review paired accounts regularly
   - Revoke pairing if suspicious activity

## Cost Estimates

### API Usage (Monthly)

- **Claude API**: $15-30 (moderate use)
- **OpenAI** (optional): $10-20
- **Total**: ~$25-50/month

### Infrastructure

- **OrbStack**: Free
- **Docker Desktop**: Free for personal use
- **Little Snitch**: $45 one-time (or free Lulu)
- **Gmail, Calendar, Telegram**: Free
- **BlueBubbles**: Free

### Ongoing

- **Electricity**: ~$2-5/month (Mac running 24/7)
- **Internet**: Included in existing plan

## Limitations

### Known Limitations

1. **macOS Only**: Deployment script designed for macOS
2. **iMessage Requires Mac**: BlueBubbles needs Messages.app
3. **No Official PayPal Integration**: Requires browser automation
4. **Single-User**: Not designed for multi-user scenarios
5. **Local Network Blocked**: Cannot access NAS, printers, etc.
6. **Container Performance**: 10-20% slower than native on macOS

### Workarounds

- **LAN Access**: Add firewall whitelist rules for specific IPs
- **Multi-User**: Deploy separate instances per user
- **PayPal**: Use approval workflow for purchases
- **Performance**: Use OrbStack instead of Docker Desktop

## FAQ

**Q: Is this really secure?**
A: Yes, with multiple layers of isolation. However, no system is 100% secure. The network isolation prevents LAN access, sandbox mode restricts tool execution, and audit logging provides accountability.

**Q: Can I use my existing Gmail account?**
A: Yes, but we recommend creating a dedicated account (therealidallasj@gmail.com) to separate personal and assistant activities.

**Q: Do I need to keep my Mac running 24/7?**
A: Only if you want iMessage integration via BlueBubbles. Telegram, email, and other integrations work without it.

**Q: Can I install this on Linux or Windows?**
A: The deployment script is macOS-specific, but you can adapt it for Linux. Windows requires WSL2.

**Q: How do I share this with friends?**
A: Share the `one-claw-tied-behind-your-back-v1.0.tar.gz` file. They extract it and run `./deploy-openclaw.sh`.

**Q: What if I don't want network isolation?**
A: You can modify the Docker Compose file and firewall rules, but this is not recommended for security.

**Q: Can the AI access my files?**
A: Only files in the workspace directory (`~/.oneclaw-secure/workspace/`). The container has no access to your home directory or other files.

**Q: How do I uninstall?**
A: Run:
```bash
cd ~/.oneclaw-secure
./stop.sh
launchctl unload ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist
docker rmi openclaw/openclaw:latest
rm -rf ~/.oneclaw-secure
```

## Resources

### Documentation

- **OpenClaw Docs**: https://docs.oneclaw.ai
- **GitHub**: https://github.com/openclaw/openclaw
- **BlueBubbles Docs**: https://docs.bluebubbles.app
- **Docker Security**: https://docs.docker.com/engine/security/

### Community

- **OpenClaw Discord**: https://discord.gg/openclaw
- **GitHub Issues**: https://github.com/openclaw/openclaw/issues
- **Reddit**: r/openclaw

### Getting Help

1. Check the troubleshooting section above
2. Search OpenClaw documentation
3. Review GitHub issues for similar problems
4. Ask in OpenClaw Discord
5. Create a GitHub issue with logs and configuration

## Credits

- **OpenClaw**: Peter Steinberger and contributors
- **BlueBubbles**: BlueBubbles team
- **Deployment Package**: Isaiah Jefferson

## License

MIT License - See OpenClaw repository for full license.

## Acknowledgments

This deployment package ("One Claw Tied Behind Your Back") builds upon the excellent work of the OpenClaw team and community. Special thanks to all contributors who make open-source AI assistants possible.

---

**Project**: One Claw Tied Behind Your Back
**Version**: 1.0
**Last Updated**: February 2026
**Maintainer**: Isaiah Jefferson
EOF

# Create quick start guide
echo "Creating quick start guide..."
cat > "$DIST_DIR/QUICKSTART.txt" <<'EOF'
╔════════════════════════════════════════════════════════════╗
║  One Claw Tied Behind Your Back - Quick Start             ║
╚════════════════════════════════════════════════════════════╝

Step 1: Install Prerequisites
─────────────────────────────────────────────────────────────
brew install node@22
brew install --cask orbstack  # or docker
brew install jq  # optional but recommended

Step 2: Run Deployment Script
─────────────────────────────────────────────────────────────
cd one-claw-tied-behind-your-back-v1.0
./deploy-openclaw.sh

Step 3: Add API Key
─────────────────────────────────────────────────────────────
nano ~/.oneclaw-secure/secrets/.env
# Add your ANTHROPIC_API_KEY or OPENAI_API_KEY

Step 4: Create Service Accounts
─────────────────────────────────────────────────────────────
./setup-accounts.sh
# Follow the wizard to create Gmail, Apple ID, Telegram bot

Step 5: Start OpenClaw
─────────────────────────────────────────────────────────────
cd ~/.oneclaw-secure
./start.sh

Step 6: Access WebChat
─────────────────────────────────────────────────────────────
Open browser: http://localhost:18790

╔════════════════════════════════════════════════════════════╗
║  That's it! Your secure OpenClaw deployment is running.   ║
╚════════════════════════════════════════════════════════════╝

Management Commands:
  cd ~/.oneclaw-secure
  ./start.sh   - Start services
  ./stop.sh    - Stop services
  ./status.sh  - Check status
  ./logs.sh    - View logs
  ./backup.sh  - Create backup

Documentation: See README.md for detailed information
Help: https://docs.oneclaw.ai
EOF

# Create LICENSE file
echo "Creating LICENSE..."
cat > "$DIST_DIR/LICENSE" <<'EOF'
MIT License

Copyright (c) 2026 Isaiah Jefferson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

# Make scripts executable
chmod +x "$DIST_DIR"/*.sh

# Create tarball
echo "Creating tarball..."
cd /tmp
tar -czf "$DIST_NAME.tar.gz" "$DIST_NAME"

# Calculate size
SIZE=$(du -h "/tmp/$DIST_NAME.tar.gz" | cut -f1)

# Cleanup
rm -rf "$DIST_DIR"

echo ""
echo -e "${GREEN}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Distribution Package Created Successfully!                ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""
echo "Package: /tmp/$DIST_NAME.tar.gz"
echo "Size: $SIZE"
echo ""
echo "Contents:"
echo "  - deploy-openclaw.sh (main deployment script)"
echo "  - setup-accounts.sh (account creation wizard)"
echo "  - README.md (comprehensive documentation)"
echo "  - QUICKSTART.txt (quick start guide)"
echo "  - LICENSE (MIT license)"
echo ""
echo "Share this package with friends:"
echo "  1. Send them: /tmp/$DIST_NAME.tar.gz"
echo "  2. They extract: tar -xzf $DIST_NAME.tar.gz"
echo "  3. They run: cd $DIST_NAME && ./deploy-openclaw.sh"
echo ""
echo "Upload to GitHub Releases, Dropbox, or share directly via AirDrop."
echo ""
