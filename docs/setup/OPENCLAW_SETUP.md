# OpenClaw Setup Guide - agentshroud.ai Bot

**Version**: 0.2.0
**Date**: 2026-02-15
**Status**: Real OpenClaw Platform Integrated

---

## What Changed

We've replaced the custom Python chat service with the **real OpenClaw platform** from https://openclaw.ai

**Old Architecture** (v0.1.0):
- Custom FastAPI Python service
- Single `/chat` endpoint
- OpenAI API only
- Limited features

**New Architecture** (v0.2.0):
- Real OpenClaw CLI and Gateway
- Full agents, skills, MCP server support
- Multiple LLM providers (OpenAI, Anthropic, etc.)
- SSH capability for remote work
- Control UI for configuration

---

## Communication Channels

OpenClaw supports multiple ways to interact with your bot:

- **Telegram** (Recommended for mobile) - See [TELEGRAM_SETUP.md](TELEGRAM_SETUP.md)
  - Works on Mac, iPhone, iPad, Apple Watch
  - Real-time notifications
  - Syncs across all devices

- **Web UI** - http://localhost:18790 (currently 18790, change to 18789 after Docker Desktop restart)
  - Full control interface
  - Configuration and settings
  - Chat history

- **AgentShroud Gateway** - Port 8080
  - iOS Shortcuts integration
  - Email forwarding
  - Custom web interface

---

## Quick Start

### 1. Build and Start OpenClaw

```bash
cd /Users/ijefferson.admin/Development/agentshroud

# Stop old containers
docker compose -f docker/docker-compose.yml down

# Remove old volumes (optional - clean slate)
docker volume rm agentshroud_openclaw-data 2>/dev/null || true

# Build and start with new OpenClaw
docker compose -f docker/docker-compose.yml up -d --build

# Wait for containers to be healthy (60-90 seconds for first build)
sleep 90

# Check status
docker compose -f docker/docker-compose.yml ps
```

Both containers should show `(healthy)`:
- `agentshroud-gateway` - Your audit/PII layer
- `openclaw-bot` - Real OpenClaw platform

### 2. Access OpenClaw Control UI

OpenClaw has its own web-based Control UI for configuration.

**Open in browser:**
```
http://localhost:18789
```

**Get the gateway token:**
```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw dashboard --no-open
```

This will display the dashboard URL with token. Copy the token and paste it into the Control UI (Settings → Token).

---

## Initial Configuration

### Step 1: Add Your OpenAI API Key

Since we already have the OpenAI key as a Docker secret, OpenClaw can access it via environment variable.

**Option A: Through UI (Recommended)**
1. Go to http://localhost:18789
2. Navigate to Settings → Providers
3. Add OpenAI provider
4. Paste your API key from `docker/secrets/openai_api_key.txt`

**Option B: Via CLI**
```bash
# Read the key from the secret
OPENAI_KEY=$(cat docker/secrets/openai_api_key.txt)

# Configure in OpenClaw
docker compose -f docker/docker-compose.yml exec openclaw openclaw providers add \
  --provider openai \
  --api-key "$OPENAI_KEY"
```

### Step 2: Configure Bot Identity

Set up agentshroud.ai as the bot's identity:

```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw config set \
  --key "bot.name" \
  --value "agentshroud.ai"

docker compose -f docker/docker-compose.yml exec openclaw openclaw config set \
  --key "bot.email" \
  --value "agentshroud.ai@gmail.com"
```

### Step 3: Load Persona (Optional)

Your IDENTITY, SOUL, and USER files are mounted at `/home/node/persona/` inside the container.

You can reference them in OpenClaw's system prompt or load them as context:

```bash
# View available persona files
docker compose -f docker/docker-compose.yml exec openclaw ls -l /home/node/persona/

# Set custom system prompt (combine persona files)
docker compose -f docker/docker-compose.yml exec openclaw openclaw config set \
  --key "agents.defaults.systemPrompt" \
  --value "$(cat tobeornottobe/IDENTITY tobeornottobe/SOUL.md tobeornottobe/USER)"
```

### Step 4: Set Up Channels (Optional)

OpenClaw supports multiple communication channels.

**Telegram Bot:**
```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels add \
  --channel telegram \
  --token "YOUR_TELEGRAM_BOT_TOKEN"
```

**Discord Bot:**
```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels add \
  --channel discord \
  --token "YOUR_DISCORD_BOT_TOKEN"
```

**WhatsApp (QR code login):**
```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels login
# Scan QR code with WhatsApp app
```

### Step 5: Configure SSH Access (For Bot to Work on Remote Systems)

Generate SSH keys for the bot:

```bash
# Generate SSH key pair inside container
docker compose -f docker/docker-compose.yml exec -u node openclaw ssh-keygen -t ed25519 -f /home/node/.ssh/id_ed25519 -N "" -C "agentshroud.ai@bot"

# Get the public key to add to target systems
docker compose -f docker/docker-compose.yml exec openclaw cat /home/node/.ssh/id_ed25519.pub
```

Copy this public key to the `~/.ssh/authorized_keys` file on any system you want the bot to access via SSH.

**Test SSH access:**
```bash
docker compose -f docker/docker-compose.yml exec openclaw ssh -o StrictHostKeyChecking=no user@target-host
```

---

## Using OpenClaw

### Through Control UI (Port 18789)

**Direct access:**
```
http://localhost:18789
```

- Configure providers (OpenAI, Anthropic, etc.)
- Set up agents and skills
- View chat history and logs
- Manage MCP servers
- Configure channels

### Through AgentShroud Gateway (Port 8080)

**Your existing web chat still works** and now talks to real OpenClaw:

```bash
# Get Gateway auth token
TOKEN=$(docker logs agentshroud-gateway 2>&1 | grep "Generated new token" -A3 | tail -2 | xargs)

# Open web chat
open "http://localhost:8080/?token=$TOKEN"
```

Messages go through:
1. Your browser/shortcut → AgentShroud Gateway (PII sanitization, audit)
2. Gateway → OpenClaw Gateway (port 18789)
3. OpenClaw processes with full agents/skills
4. Response back through the chain

### Via CLI

Run OpenClaw commands directly:

```bash
# Check OpenClaw status
docker compose -f docker/docker-compose.yml exec openclaw openclaw status

# Run health check
docker compose -f docker/docker-compose.yml exec openclaw openclaw doctor

# List configured providers
docker compose -f docker/docker-compose.yml exec openclaw openclaw providers list

# List agents
docker compose -f docker/docker-compose.yml exec openclaw openclaw agents list

# View logs
docker compose -f docker/docker-compose.yml logs -f openclaw
```

---

## OpenClaw Features Now Available

### ✅ Agents
OpenClaw has specialized agents for different tasks:
- **Code agents**: Write, review, test code
- **Research agents**: Search, analyze, summarize
- **Task agents**: Plan and execute multi-step workflows

### ✅ Skills
Pre-built capabilities:
- Git operations (commit, PR, merge)
- File operations (read, write, search)
- Web browsing and scraping
- API integrations
- Custom skills (you can add your own)

### ✅ MCP Servers
Model Context Protocol servers for extended capabilities:
- GitHub integration (issues, PRs, repos)
- Atlassian (Jira, Confluence)
- Filesystem access
- Database queries
- Custom MCP servers

### ✅ Multi-LLM Support
Switch between providers:
- OpenAI (GPT-4, GPT-4 Turbo)
- Anthropic (Claude Opus, Sonnet)
- Local models (Ollama, LM Studio)
- Azure OpenAI
- Custom endpoints

---

## Architecture Overview

```
┌────────────────────────────────────────────┐
│ You (Shortcuts, Web, Email, Telegram)     │
└────────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────┐
│ AgentShroud Gateway (Port 8080)             │
│ - PII Sanitization                         │
│ - Audit Ledger                             │
│ - Approval Queue                           │
└────────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────┐
│ OpenClaw Gateway (Port 18789)              │
│ - Control UI                               │
│ - Channel Management                       │
│ - Agent Orchestration                      │
└────────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────┐
│ OpenClaw Bot Engine                        │
│ - Agents (code, research, task)            │
│ - Skills (git, files, web)                 │
│ - MCP Servers (GitHub, Jira, etc.)         │
│ - LLM Providers (OpenAI, Anthropic)        │
│ - SSH Client (remote work)                 │
│ - Workspace (/home/node/openclaw/workspace)│
└────────────────────────────────────────────┘
```

---

## Data Locations

### Inside Container

**Configuration:**
- `/home/node/.openclaw/` - OpenClaw config, API keys, memory
- `/home/node/.openclaw/config.json` - Main configuration file

**Workspace:**
- `/home/node/openclaw/workspace/` - Bot's working files
- Files the agent creates will be saved here

**SSH:**
- `/home/node/.ssh/` - Bot's SSH keys

**Persona:**
- `/home/node/persona/` - Your IDENTITY, SOUL, USER files (read-only)

### On Host (Docker Volumes)

```bash
# List volumes
docker volume ls | grep openclaw

# Inspect volume location
docker volume inspect agentshroud_openclaw-config
docker volume inspect agentshroud_openclaw-workspace
docker volume inspect agentshroud_openclaw-ssh

# Backup volumes
docker run --rm -v agentshroud_openclaw-config:/data -v $(pwd):/backup \
  alpine tar czf /backup/openclaw-config-backup.tar.gz /data

# Restore volumes
docker run --rm -v agentshroud_openclaw-config:/data -v $(pwd):/backup \
  alpine tar xzf /backup/openclaw-config-backup.tar.gz -C /
```

---

## Troubleshooting

### OpenClaw Won't Start

```bash
# Check logs
docker compose -f docker/docker-compose.yml logs openclaw

# Common issues:
# 1. Node.js version mismatch - verify base image is node:22-bookworm
# 2. npm install failed - check network connectivity
# 3. Permissions - ensure /home/node owned by node user
```

### Control UI Not Accessible

```bash
# Check if port 18789 is bound
docker compose -f docker/docker-compose.yml ps
# Should show: 127.0.0.1:18789->18789/tcp

# Test locally
curl http://localhost:18789/api/health

# Get token again
docker compose -f docker/docker-compose.yml exec openclaw openclaw dashboard --no-open
```

### Gateway Can't Reach OpenClaw

```bash
# Test from Gateway container
docker exec agentshroud-gateway curl http://openclaw:18789/api/health

# Check network
docker network inspect agentshroud_agentshroud-internal

# Verify both containers on same network
docker compose -f docker/docker-compose.yml ps
```

### SSH Not Working

```bash
# Verify SSH client installed
docker compose -f docker/docker-compose.yml exec openclaw ssh -V

# Check key permissions
docker compose -f docker/docker-compose.yml exec openclaw ls -la /home/node/.ssh/

# Test SSH with verbose output
docker compose -f docker/docker-compose.yml exec openclaw ssh -vvv user@host
```

---

## Security Notes

### Current Security Posture

**Container Hardening:**
- ✅ Non-root execution (node user, UID 1000)
- ✅ Capability dropping (CAP_DROP: ALL)
- ✅ no-new-privileges enabled
- ✅ Resource limits (4GB memory, 2 CPUs, 512 PIDs)
- ⚠️ Read-only filesystem disabled (OpenClaw needs write access for config/workspace)
- ⚠️ Custom seccomp disabled (threading issue, using Docker default)

**Network Security:**
- ✅ OpenClaw Gateway bound to localhost only (127.0.0.1:18789)
- ✅ Internal Docker network (agentshroud-internal)
- ✅ AgentShroud Gateway as audit/PII layer
- ⚠️ Internet access enabled (OpenClaw needs to reach LLM APIs)

**Secrets Management:**
- ✅ Docker Secrets for API keys (not environment variables)
- ✅ SSH keys in dedicated volume
- ✅ Configuration in persistent volumes (not in image)

### Recommendations

1. **Add approval queue** for sensitive operations (git push, SSH commands)
2. **Monitor OpenClaw logs** for unexpected activity
3. **Limit SSH access** to specific hosts/users
4. **Use separate bot accounts** for all services (GitHub, email, etc.)
5. **Regular backups** of openclaw-config and openclaw-workspace volumes

---

## Next Steps

1. ✅ **Configure your first provider** (OpenAI already available)
2. ✅ **Test chat through Control UI** (http://localhost:18789)
3. ✅ **Test chat through Gateway** (http://localhost:8080)
4. ⬜ **Add Telegram/Discord channels** for bot communication
5. ⬜ **Configure SSH keys** for remote system access
6. ⬜ **Set up MCP servers** (GitHub, Jira, custom)
7. ⬜ **Create custom skills** for your workflows
8. ⬜ **Configure approval queue** in Gateway for sensitive actions

---

**Questions or issues?** Check the official OpenClaw docs: https://docs.openclaw.ai

**AgentShroud Gateway docs**: See `CONTINUE.md` for Gateway features and troubleshooting.
