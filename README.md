# One Claw Tied Behind Your Back

Maximum-security OpenClaw deployment for macOS - completely self-contained.

## 🔒 Security-First Design

**Source code never touches your host.** Everything runs in an isolated Docker container with:
- ✅ **No host dependencies** - All data in current directory
- ✅ **Internet-only access** - Cannot access your LAN or VPN connections
- ✅ **Zero-trust build** - Source cloned and built inside container
- ✅ **Read-only filesystem** - Container root is immutable
- ✅ **Non-root execution** - Runs as unprivileged user (UID 1000)
- ✅ **Isaiah's personality** - Pre-loaded with your professional identity

---

## ⚡ Quick Start

### 1. Deploy (First Time)

```bash
./deploy-local.sh
```

This will:
- Build OpenClaw in a secure container (10-20 minutes)
- Load Isaiah's personality from `workspace/` files
- Create self-contained deployment in `openclaw-container/`
- Never install anything on your host system

### 2. Add API Key

```bash
nano openclaw-container/secrets/.env
```

Add one of these:
```bash
# Anthropic Claude (Recommended)
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Or OpenAI
OPENAI_API_KEY=sk-your-key-here
```

**Get keys:**
- Anthropic: https://console.anthropic.com/
- OpenAI: https://platform.openai.com/api-keys

### 3. Start

```bash
cd openclaw-container
docker-compose up -d
```

### 4. Access

- **WebChat**: http://localhost:18790
- **Gateway API**: http://localhost:18789

---

## 📂 What's in This Directory

```
one-claw-tied-behind-your-back/
├── openclaw-container/          # ← All container data (self-contained)
│   ├── workspace/
│   │   ├── IDENTITY             # Isaiah's persona
│   │   ├── SOUL.md              # Values & decision-making
│   │   └── USER.md              # Professional background
│   ├── config/
│   │   └── openclaw.json        # OpenClaw configuration
│   ├── secrets/
│   │   └── .env                 # API keys (chmod 600)
│   ├── logs/
│   │   └── audit.log            # Security audit log
│   └── docker-compose.yml       # Container orchestration
│
├── Dockerfile.secure            # Multi-stage secure build
├── deploy-local.sh              # Deployment script
├── SECURITY.md                  # Security architecture
├── QUICK-REFERENCE.md           # Command cheat sheet
└── README.md                    # This file
```

**No files in your home directory. No system services. Everything in one place.**

---

## 🎭 Isaiah's Personality

Your bot represents you using these files in `openclaw-container/workspace/`:

| File | Purpose |
|------|---------|
| `IDENTITY` | Core persona, name, tone, communication style |
| `SOUL.md` | Values, decision-making, long-term goals |
| `USER.md` | Professional background, team, technical environment |

These files are read by the AI on startup. Edit them to customize how your bot represents you.

---

## 📋 Daily Commands

All commands run from the container directory:

```bash
cd openclaw-container

# Start
docker-compose up -d

# Stop
docker-compose down

# View logs
docker-compose logs -f

# Check status
docker ps | grep openclaw

# Restart
docker-compose restart
```

---

## 🔒 Verify Security

### Test Network Isolation

```bash
# Should work (internet):
docker exec openclaw_isaiah curl -I https://google.com

# Should FAIL (LAN blocked - use your router IP):
docker exec openclaw_isaiah curl --connect-timeout 5 http://192.168.1.1

# Should FAIL (cannot access host):
docker exec openclaw_isaiah curl --connect-timeout 5 http://host.docker.internal
```

### Check Container Hardening

```bash
# Non-root user:
docker exec openclaw_isaiah whoami
# Output: node

# Read-only root:
docker inspect openclaw_isaiah | jq '.[0].HostConfig.ReadonlyRootfs'
# Output: true

# Capabilities dropped:
docker inspect openclaw_isaiah | jq '.[0].HostConfig.CapDrop'
# Output: ["ALL"]
```

---

## 🔄 Updates

### Update OpenClaw

```bash
cd openclaw-container
docker-compose down
docker build --no-cache -t openclaw-secure:latest -f ../Dockerfile.secure ..
docker-compose up -d
```

### Update Personality Files

```bash
nano openclaw-container/workspace/IDENTITY
nano openclaw-container/workspace/SOUL.md
nano openclaw-container/workspace/USER.md

cd openclaw-container
docker-compose restart
```

---

## 📦 Backup & Restore

### Backup

```bash
tar -czf openclaw-backup-$(date +%Y%m%d).tar.gz openclaw-container/
```

### Restore

```bash
tar -xzf openclaw-backup-YYYYMMDD.tar.gz
cd openclaw-container
docker-compose up -d
```

---

## 🚨 Troubleshooting

### Container Won't Start

```bash
cd openclaw-container
docker-compose logs

# Check API key is set
grep ANTHROPIC_API_KEY secrets/.env
```

### Gateway Not Responding

```bash
# Check if running
docker ps | grep openclaw

# Check health
curl http://localhost:18789/health

# View recent logs
docker-compose logs --tail=50
```

### Network Issues

```bash
# Verify Docker network
docker network inspect openclaw-container_openclaw_isolated

# Check DNS resolution
docker exec openclaw_isaiah nslookup google.com
```

### Reset Everything

```bash
cd openclaw-container
docker-compose down
docker rmi openclaw-secure:latest
cd ..
./deploy-local.sh
```

---

## 🆘 Getting Help

1. **Security Architecture**: See `SECURITY.md`
2. **Command Reference**: See `QUICK-REFERENCE.md`
3. **OpenClaw Docs**: https://docs.openclaw.ai
4. **GitHub Issues**: https://github.com/openclaw/openclaw/issues

---

## 📤 Share with Others

To share this deployment setup:

```bash
# Create distribution package (updates to create-distribution.sh needed)
./create-distribution.sh
```

Or simply zip the entire directory:

```bash
cd ..
zip -r one-claw-tied-behind-your-back.zip one-claw-tied-behind-your-back/ \
  -x "*/openclaw-container/secrets/*" \
  -x "*/openclaw-container/logs/*" \
  -x "*/openclaw-container/workspace/*"
```

---

## 💰 Cost Estimate

**API Usage** (monthly):
- Claude Opus 4.6: ~$15-30 (moderate use)
- **Total: ~$15-30/month** (everything else is free)

**Infrastructure:**
- Docker: Free
- Gmail, Telegram: Free
- No cloud hosting needed

---

## ✅ What Makes This Secure

### 1. Self-Contained
- All files in one directory
- No system-wide installation
- No background services on host
- Easy to backup, move, or delete

### 2. Maximum Container Isolation
- Non-root user (UID 1000)
- Read-only root filesystem
- All Linux capabilities dropped
- Process ID isolation
- IPC namespace isolation
- Resource limits (4GB RAM, 2 CPUs)

### 3. Network Security
- Custom Docker network (172.30.0.0/24)
- Ports bound to localhost only
- DNS: Cloudflare (1.1.1.1) + Google (8.8.8.8)
- Inter-container communication disabled
- No access to Docker host network

### 4. Zero-Trust Build
- Source code cloned INSIDE container
- Build tools NEVER on your Mac
- Multi-stage build discards all build artifacts
- Final image: runtime only (2.5GB)

### 5. Audit & Monitoring
- All actions logged to `logs/audit.log`
- 90-day retention
- JSON format for parsing
- Container health checks every 30s

---

## 🎯 Your Bot's Identity

When running, your OpenClaw bot:
- ✅ Knows it represents Isaiah Jefferson
- ✅ Understands your role at Fluence Energy
- ✅ Speaks with your communication style (direct, technically precise)
- ✅ References your team, tech stack, and domain expertise
- ✅ Follows your values (security-first, team-oriented, cost-conscious)
- ✅ Never exposes credentials or internal details

All from the three files in `openclaw-container/workspace/`.

---

**Project**: One Claw Tied Behind Your Back
**Security Level**: Maximum
**Host Impact**: Zero
**Isaiah's Personality**: Loaded

**Status**: 🟢 Ready to Deploy