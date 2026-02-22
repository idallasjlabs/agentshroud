# AgentShroud Prerequisites

**Version**: 1.0.0
**Last Updated**: 2026-02-16
**Status**: Phase 3 - Production Ready

---

## Overview

AgentShroud requires careful setup of **isolated accounts** to maintain the "One Claw Tied Behind Your Back" security model. This document lists all prerequisites and setup steps.

---

## 🎯 Philosophy: Separation of Concerns

**Key Principle**: The bot operates with **separate, dedicated accounts** that are isolated from your primary digital life.

**Why?**
- Your main phone/email/accounts are never exposed to the AI
- If bot is compromised, attacker only gets access to isolated accounts
- You maintain full control and observability
- Easy to revoke access by disabling bot accounts

---

## 📱 Required Accounts & Services

### 1. Phone Number (Separate from Main)

**Required**: Dedicated phone number for bot identity

**Recommended**: Google Voice (Free)

**Your Setup**: ✅ Google Voice number (separate from main cell)

**Purpose**:
- Telegram account registration
- 2FA for bot accounts
- Isolation from your primary phone number

**Setup Steps**:
1. Go to https://voice.google.com
2. Choose a new phone number
3. Save this number for bot identity
4. **DO NOT** link to your primary accounts

**Cost**: Free (Google Voice)

**Alternative Options**:
- Twilio ($1/month per number)
- TextNow (Free with ads)
- Burner app (Paid)

---

### 2. Gmail Account (Dedicated for Bot)

**Required**: Separate Gmail account for bot operations

**Your Setup**: ✅ Separate Gmail account

**Purpose**:
- Bot's email identity
- Receive notifications
- OAuth for services
- 1Password account
- API service registrations

**Setup Steps**:
1. Create new Gmail: https://accounts.google.com/signup
2. Use format like: `yourname.bot@gmail.com` or `agentshroud.bot@gmail.com`
3. Use Google Voice number for 2FA
4. Enable 2-Step Verification
5. Generate App Password for bot use
6. **DO NOT** link to your primary Google account

**Security**:
- ✅ 2FA enabled (using Google Voice number)
- ✅ App password for bot (not main password)
- ✅ No access to your personal Gmail
- ✅ Separate recovery email

**Your Account**: `agentshroud.ai@gmail.com`

---

### 3. Telegram Account (Bot Communication)

**Required**: Dedicated Telegram account for talking to bot

**Your Setup**: ✅ Separate Telegram account (using Google Voice number)

**Purpose**:
- Primary interface for bot communication
- Secure messaging
- Remote bot control

**Setup Steps**:
1. Download Telegram: https://telegram.org/apps
2. Register with Google Voice number (NOT your main phone)
3. Create account
4. Find @BotFather to create bot
5. Get bot token
6. Register bot with OpenClaw

**Security**:
- ✅ Separate from personal Telegram
- ✅ 2FA enabled
- ✅ Session management
- ✅ Device authorization

**Your Bot**: `@agentshroud.ai_bot`

---

### 4. 1Password Account (Credential Management)

**Required**: 1Password account for secure credential storage

**Your Setup**: ✅ Separate 1Password account added to Family plan

**Purpose**:
- Secure credential storage
- No plain-text passwords in chat
- Vault-based access control
- Automatic credential rotation support

**Setup Steps**:
1. Create 1Password account: https://1password.com/sign-up
2. Choose Family plan (or join existing Family plan)
3. Create dedicated vault: "AgentShroud Bot Credentials"
4. **DO NOT** store credentials in default "Shared" vault
5. Share bot vault ONLY with bot account
6. Add bot credentials (Gmail, API keys, etc.)

**Security**:
- ✅ Bot account added to Family plan
- ✅ Dedicated vault (no data in default Shared vault) ✅
- ✅ Read-only access for bot
- ✅ Separate from personal vaults
- ✅ Activity logging enabled

**Your Vaults**:
- Private (your personal vault)
- AgentShroud Bot Credentials (bot's vault) ✅
- Family Shared (no bot access) ✅
- Shared Vault - Do Not Use (empty) ✅

**1Password CLI**: Installed in Docker container
**Bot Account**: `agentshroud.ai@gmail.com`

---

### 5. OpenAI Account (LLM API)

**Required**: OpenAI API key for AI capabilities

**Setup Steps**:
1. Create account: https://platform.openai.com/signup
2. Add payment method (API is paid)
3. Generate API key
4. Set usage limits ($5-50/month recommended)
5. Store key in Docker secrets

**Cost**: Pay-per-use (~$5-20/month typical)

**Your Setup**: ✅ API key configured in Docker secrets

---

### 6. Anthropic Account (Claude API)

**Required**: Anthropic API key for Claude models

**Setup Steps**:
1. Create account: https://console.anthropic.com
2. Add payment method
3. Generate API key
4. Set usage limits
5. Store key in Docker secrets

**Cost**: Pay-per-use (~$5-20/month typical)

**Your Setup**: ✅ API key configured in Docker secrets

---

## 💻 System Requirements

### Hardware

**Minimum**:
- CPU: 2 cores
- RAM: 4GB
- Disk: 10GB free space
- Network: Broadband internet

**Recommended**:
- CPU: 4 cores (M1/M2 Mac or equivalent)
- RAM: 8GB
- Disk: 20GB free space
- Network: Fast, stable connection

**Your System**: Apple Silicon Mac (M1/M2) ✅

---

### Operating System

**Supported**:
- macOS 12+ (Monterey or newer) ✅
- Linux (Ubuntu 22.04+, Debian 12+)
- Windows 11 with WSL2

**Your System**: macOS (Darwin 25.3.0) ✅

---

### Required Software

#### 1. Docker Desktop

**Version**: 4.25.0 or newer

**Installation**:
- macOS: https://www.docker.com/products/docker-desktop
- Linux: https://docs.docker.com/engine/install/
- Windows: https://docs.docker.com/desktop/install/windows-install/

**Verify Installation**:
```bash
docker --version
# Expected: Docker version 24.0.0 or higher

docker compose version
# Expected: Docker Compose version v2.23.0 or higher
```

**Your Setup**: ✅ Docker installed and working

**Configuration**:
- Resources: 4GB RAM, 2 CPUs (minimum)
- Enable BuildKit (modern build system)
- File sharing configured for project directory

---

#### 2. Python 3.11+

**Version**: 3.11, 3.12, or 3.13

**Installation**:
```bash
# macOS (using Homebrew)
brew install python@3.13

# Linux
sudo apt install python3.13

# Verify
python3 --version
# Expected: Python 3.11.x or higher
```

**Your Setup**: Python 3.13 ✅

**Note**: Python 3.14+ not yet supported by some dependencies (spaCy/Presidio)

---

#### 3. Python Packages

**Gateway Dependencies** (gateway/requirements.txt):

```
# Core Framework
fastapi>=0.115.0,<1.0.0
uvicorn[standard]>=0.34.0,<1.0.0
pydantic>=2.10.0,<3.0.0
pydantic-settings>=2.0.0,<3.0.0

# PII Detection (Microsoft Presidio)
presidio-analyzer>=2.2.0,<3.0.0
presidio-anonymizer>=2.2.0,<3.0.0
spacy>=3.8.0,<4.0.0

# Database
aiosqlite>=0.20.0,<1.0.0

# Authentication
python-jose[cryptography]>=3.3.0,<4.0.0

# WebSocket
websockets>=14.0,<15.0

# Configuration
pyyaml>=6.0.0,<7.0.0

# Utilities
python-multipart>=0.0.18
httpx>=0.28.0,<1.0.0

# Testing
pytest>=8.0.0,<9.0.0
pytest-asyncio>=0.24.0,<1.0.0
```

**Installation**:
```bash
# From project root
pip install -r gateway/requirements.txt

# Or using venv (recommended)
python3 -m venv .venv
source .venv/bin/activate
pip install -r gateway/requirements.txt
```

**spaCy Language Model** (Required for PII detection):
```bash
python3 -m spacy download en_core_web_lg
```

---

#### 4. Node.js 22+ (for OpenClaw)

**Version**: 22.x LTS

**Installation**:
```bash
# macOS (using Homebrew)
brew install node@22

# Linux
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify
node --version
# Expected: v22.x.x
```

**Note**: Installed automatically in OpenClaw Docker container

---

#### 5. Git

**Version**: Any recent version

**Installation**:
```bash
# macOS (pre-installed or via Xcode)
xcode-select --install

# Linux
sudo apt install git

# Verify
git --version
```

**Your Setup**: ✅ Git installed (repo is working)

---

#### 6. Tailscale (Optional but Recommended)

**Purpose**: Secure remote access to Control UI

**Installation**:
```bash
# macOS
brew install tailscale

# Linux
curl -fsSL https://tailscale.com/install.sh | sh

# Start Tailscale
sudo tailscale up
```

**Setup**:
1. Create account: https://login.tailscale.com/start
2. Install on your Mac
3. Install on any devices you want to access from
4. All devices get VPN access to each other

**Your Tailscale URL**: `https://marvin.tail240ea8.ts.net`

**Benefits**:
- Access Control UI from anywhere
- Encrypted VPN connection
- No port forwarding needed
- No public internet exposure

---

## 📦 Docker Images & Dependencies

### Base Images

**Gateway Container**:
- Base: `python:3.13-slim`
- Size: ~500MB
- Includes: Python, FastAPI, Presidio

**OpenClaw Container**:
- Base: `node:22-bookworm`
- Size: ~2GB (includes Playwright browsers)
- Includes: Node.js, OpenClaw, 1Password CLI, Playwright

### Additional Tools in Containers

**OpenClaw Container**:
- Bun (JavaScript runtime)
- SSH client
- Git
- OpenSCAP (compliance scanning)
- 1Password CLI v2.32.0
- Playwright (browser automation)

**Gateway Container**:
- OpenSCAP scanner
- Python packages (see requirements.txt)

---

## 🗂️ File Structure

```
agentshroud/
├── docker/
│   ├── docker-compose.yml          # Container orchestration
│   ├── Dockerfile.openclaw         # OpenClaw container definition
│   ├── secrets/                    # Docker secrets (gitignored)
│   │   ├── openai_api_key.txt
│   │   ├── anthropic_api_key.txt
│   │   ├── 1password_bot_email.txt
│   │   ├── 1password_bot_master_password.txt
│   │   └── 1password_bot_secret_key.txt
│   ├── scripts/
│   │   ├── start-openclaw.sh       # Container startup
│   │   ├── get-credential.sh       # Credential retrieval
│   │   ├── 1password-skill.sh      # 1Password integration
│   │   └── bot-access-audit.sh     # Security audit
│   └── scap-content/               # Security scanning profiles
├── gateway/
│   ├── Dockerfile                  # Gateway container definition
│   ├── requirements.txt            # Python dependencies
│   └── ingest_api/                 # Gateway API code
├── agentshroud.yaml                 # Main configuration file
└── README.md
```

---

## 🔐 Security Requirements

### Secrets Management

**Required Secrets** (stored in `docker/secrets/`):

1. `openai_api_key.txt` - OpenAI API key
2. `anthropic_api_key.txt` - Anthropic API key
3. `1password_bot_email.txt` - Bot's 1Password email
4. `1password_bot_master_password.txt` - Bot's 1Password master password
5. `1password_bot_secret_key.txt` - Bot's 1Password Secret Key

**File Permissions**:
```bash
chmod 600 docker/secrets/*.txt
```

**Never Commit**:
- ✅ All secrets files in `.gitignore`
- ✅ No credentials in code
- ✅ No API keys in environment variables (visible in ps)

---

### Network Security

**Firewall Rules**:
- Gateway: localhost only (127.0.0.1:8080)
- Control UI: localhost only (127.0.0.1:18790)
- External access: Tailscale VPN only

**Docker Networks**:
- `agentshroud-internal` (bridge, Gateway ↔ Host)
- `agentshroud-isolated` (bridge, Gateway ↔ OpenClaw, no LAN)

**No Exposed Ports**: All access via localhost or Tailscale

---

## ✅ Setup Checklist

Use this checklist to verify all prerequisites:

### Accounts
- [ ] Google Voice number obtained (separate from main)
- [ ] Gmail account created (bot-dedicated)
- [ ] Telegram account created (using Google Voice)
- [ ] Telegram bot created (@BotFather)
- [ ] 1Password account created (added to Family plan)
- [ ] 1Password vault created ("AgentShroud Bot Credentials")
- [ ] Bot added to Family plan (no access to default Shared vault)
- [ ] OpenAI API key obtained
- [ ] Anthropic API key obtained

### Software
- [ ] Docker Desktop installed (v4.25.0+)
- [ ] Python 3.11+ installed
- [ ] Python packages installed (`pip install -r gateway/requirements.txt`)
- [ ] spaCy model downloaded (`python -m spacy download en_core_web_lg`)
- [ ] Git installed
- [ ] Tailscale installed (optional but recommended)

### Configuration
- [ ] Docker secrets created in `docker/secrets/`
- [ ] File permissions set (`chmod 600 docker/secrets/*.txt`)
- [ ] `agentshroud.yaml` configured
- [ ] Docker containers built (`docker compose build`)
- [ ] Docker containers running (`docker compose up -d`)
- [ ] Containers healthy (`docker compose ps`)

### Verification
- [ ] Gateway accessible: `curl http://localhost:8080/status`
- [ ] Control UI accessible: `http://localhost:18790`
- [ ] 1Password authentication working (check container logs)
- [ ] Bot responds in Telegram
- [ ] Credentials retrievable via console
- [ ] Credentials blocked via Telegram (security test)

---

## 🚀 Quick Start Command

After all prerequisites are met:

```bash
# Clone repo
git clone https://github.com/yourusername/agentshroud.git
cd agentshroud

# Create secrets
mkdir -p docker/secrets
echo "your-openai-key" > docker/secrets/openai_api_key.txt
echo "your-anthropic-key" > docker/secrets/anthropic_api_key.txt
echo "bot@gmail.com" > docker/secrets/1password_bot_email.txt
echo "bot-password" > docker/secrets/1password_bot_master_password.txt
echo "A3-XXXXXX-..." > docker/secrets/1password_bot_secret_key.txt
chmod 600 docker/secrets/*.txt

# Start containers
docker compose -f docker/docker-compose.yml up -d

# Verify
docker compose -f docker/docker-compose.yml ps
curl http://localhost:8080/status
```

---

## 📊 Cost Breakdown

| Item | Cost | Frequency |
|------|------|-----------|
| Google Voice | Free | One-time |
| Gmail | Free | One-time |
| Telegram | Free | One-time |
| 1Password Family Plan | $5/month | Monthly |
| OpenAI API | $5-20/month | Monthly (usage-based) |
| Anthropic API | $5-20/month | Monthly (usage-based) |
| Tailscale | Free (Personal) | Monthly |
| **Total** | **$15-45/month** | **Ongoing** |

**Notes**:
- API costs vary by usage
- 1Password Business plan has more features but costs more
- Tailscale Teams plan available for $6/user/month

---

## 🔄 Maintenance Requirements

### Monthly
- Review 1Password audit logs
- Check API usage/costs
- Update Docker images (`docker compose pull`)
- Run security audit (`./docker/scripts/bot-access-audit.sh`)

### Quarterly
- Rotate 1Password service account token
- Review bot's vault access
- Update dependencies
- Check for security updates

### Annually
- Renew API keys if needed
- Review account access
- Archive old audit logs
- Update documentation

---

## 🆘 Troubleshooting

### Common Issues

**Docker not starting**:
```bash
# Check Docker is running
docker ps

# Restart Docker Desktop
# macOS: Applications → Docker → Restart
```

**Python packages not installing**:
```bash
# Use virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r gateway/requirements.txt
```

**1Password authentication failing**:
```bash
# Check secrets exist
ls -la docker/secrets/1password_*.txt

# Verify content
docker exec openclaw-bot cat /run/secrets/1password_bot_email

# Check container logs
docker logs openclaw-bot 2>&1 | grep -i 1password
```

**Containers not healthy**:
```bash
# Check logs
docker logs agentshroud-gateway
docker logs openclaw-bot

# Restart containers
docker compose -f docker/docker-compose.yml restart
```

---

## 📚 Additional Resources

- [1Password Integration Guide](./docs/1PASSWORD_INTEGRATION.md)
- [1Password Family Plan Security](./docs/1PASSWORD_FAMILY_PLAN_GUIDE.md)
- [Access Methods Explained](./ACCESS-METHODS-EXPLAINED.md)
- [Docker Compose Reference](./docker/docker-compose.yml)
- [Security Policy](./CREDENTIAL-SECURITY-POLICY.md)

---

## ✅ Your Current Setup Status

Based on your configuration:

- ✅ Google Voice number (separate from main cell)
- ✅ Separate Gmail account (agentshroud.ai@gmail.com)
- ✅ Separate Telegram account (@agentshroud.ai_bot)
- ✅ 1Password account (added to Family plan)
- ✅ Dedicated vault (AgentShroud Bot Credentials)
- ✅ No data in default Shared vault
- ✅ Docker installed and working
- ✅ Python 3.13 installed
- ✅ All Python packages installed
- ✅ OpenAI API key configured
- ✅ Anthropic API key configured
- ✅ Containers running and healthy
- ✅ 1Password authentication working
- ✅ Tailscale configured (marvin.tail240ea8.ts.net)

**Status**: COMPLETE - All prerequisites met! ✅

---

## 🎯 You're Not Missing Anything!

Your setup is **complete** and follows security best practices:

✅ Separate accounts for isolation
✅ Secure credential management (1Password)
✅ No credentials in default Shared vault
✅ VPN for remote access (Tailscale)
✅ Docker for containerization
✅ All dependencies installed
✅ Security hardening active

**Ready for production use!** 🚀

---

**Version History**:
- v1.0.0 (2026-02-16): Initial comprehensive prerequisites document

**Next Update**: When new features add requirements (e.g., email skills, SSH capabilities)
