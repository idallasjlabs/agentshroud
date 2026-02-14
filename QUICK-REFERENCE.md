# Quick Reference Guide
## One Claw Tied Behind Your Back

## 🚀 Quick Start (First Time)

```bash
# 1. Test environment (optional)
./test-environment.sh

# 2. Deploy (builds in container - takes 5-15 min)
./deploy-openclaw.sh

# 3. Add API key
nano ~/.oneclaw-secure/secrets/.env
# Add: ANTHROPIC_API_KEY=sk-ant-...

# 4. Create accounts
./setup-accounts.sh

# 5. Start
cd ~/.oneclaw-secure && ./start.sh

# 6. Access
open http://localhost:18790
```

## 🔒 Security Highlights

### Zero-Trust Build Process

```
❌ OLD WAY: git clone on host → build on host → docker
✅ OUR WAY: docker build → clone in container → build in container
```

**What this means:**
- OpenClaw source code NEVER on your Mac
- Build tools NEVER installed on your Mac
- Only final runtime image exists
- Minimal attack surface

### Multi-Layer Network Isolation

1. **Docker Network**: Custom bridge, localhost-only ports
2. **Container Firewall**: Blocks RFC1918 private IPs
3. **Host Firewall**: Little Snitch blocks `com.docker.vpnkit` → LAN
4. **App Security**: Sandbox mode, pairing required, audit logs

### Container Hardening

- ✅ Non-root user (UID 1000)
- ✅ Read-only root filesystem
- ✅ Capabilities dropped (all → minimal)
- ✅ no-new-privileges security option
- ✅ Resource limits (4GB RAM, 2 CPUs)

## 📋 Daily Commands

```bash
cd ~/.oneclaw-secure

# Start services
./start.sh

# Stop services
./stop.sh

# Check status
./status.sh

# View logs (live)
./logs.sh

# Create backup
./backup.sh
```

## 🔍 Verification

### Test Network Isolation

```bash
# Should work (internet)
docker exec oneclaw_gateway curl -I https://google.com

# Should fail (LAN blocked)
docker exec oneclaw_gateway curl --connect-timeout 5 http://192.168.1.1
```

### Check Security Settings

```bash
# Verify non-root
docker exec oneclaw_gateway whoami
# Output: node

# Verify read-only root
docker inspect oneclaw_gateway | jq '.[0].HostConfig.ReadonlyRootfs'
# Output: true

# Verify capabilities dropped
docker inspect oneclaw_gateway | jq '.[0].HostConfig.CapDrop'
# Output: ["ALL"]
```

### Run Security Audit

```bash
docker exec oneclaw_gateway openclaw security audit --fix
```

## 📊 Monitoring

### Manual Checks

```bash
# Gateway health
curl http://localhost:18789/health

# Bridge health
curl http://localhost:8765/health

# Resource usage
docker stats oneclaw_gateway

# Audit log
tail -50 ~/.oneclaw-secure/workspace/logs/audit.log
```

### Automated Monitoring

```bash
# Add to crontab
crontab -e

# Add this line:
*/5 * * * * ~/.oneclaw-secure/monitor.sh
```

Auto-restarts on 3 consecutive failures, sends macOS notifications.

## 🔄 Updates

### Update OpenClaw

```bash
cd ~/.oneclaw-secure

# Stop services
./stop.sh

# Rebuild (pulls latest OpenClaw in container)
docker build -t oneclaw-secure:latest -f Dockerfile .

# Start services
./start.sh
```

### Update Dependencies (Docker, Node, etc.)

```bash
# Update Homebrew packages
brew upgrade

# Update Docker Desktop/OrbStack
brew upgrade --cask orbstack  # or docker

# Rebuild OpenClaw image (picks up new Node.js)
cd ~/.oneclaw-secure
docker build --no-cache -t oneclaw-secure:latest -f Dockerfile .
```

## 📦 Backup & Restore

### Create Backup

```bash
cd ~/.oneclaw-secure
./backup.sh
```

Saves to: `~/openclaw-backups/openclaw_backup_YYYYMMDD_HHMMSS.tar.gz`

### Restore Backup

```bash
cd ~/.oneclaw-secure
./stop.sh

# Extract backup
tar -xzf ~/openclaw-backups/openclaw_backup_YYYYMMDD_HHMMSS.tar.gz -C ~/.oneclaw-secure

./start.sh
```

## 🚨 Troubleshooting

### Container Won't Start

```bash
# Check logs
cd ~/.oneclaw-secure && ./logs.sh

# Rebuild image
docker build -t oneclaw-secure:latest -f Dockerfile .

# Restart
./stop.sh && ./start.sh
```

### Gateway Not Responding

```bash
# Check if running
docker ps | grep openclaw

# Check health
curl http://localhost:18789/health

# Check API key
cat ~/.oneclaw-secure/secrets/.env | grep ANTHROPIC_API_KEY

# Restart
cd ~/.oneclaw-secure && ./stop.sh && ./start.sh
```

### iMessage Not Working

```bash
# Check BlueBubbles
curl http://localhost:3000/api/v1/ping

# Check bridge
curl http://localhost:8765/health

# Restart bridge
launchctl unload ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist
launchctl load ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist
```

### Network Isolation Not Working

```bash
# Test from inside container
docker exec oneclaw_gateway curl --connect-timeout 5 http://192.168.1.1
# Should timeout/fail

# Check firewall rules
# Open Little Snitch and verify com.docker.vpnkit rules
```

### High Resource Usage

```bash
# Check current usage
docker stats oneclaw_gateway

# Adjust limits in docker compose.yml
cd ~/.oneclaw-secure
nano docker compose.yml
# Change: mem_limit, cpus

# Restart
./stop.sh && ./start.sh
```

## 📂 File Locations

```
~/.oneclaw-secure/               # Main installation
├── docker compose.yml            # Container config
├── Dockerfile                    # Build instructions
├── config/
│   └── oneclaw.json             # OpenClaw config
├── secrets/
│   └── .env                      # API keys (chmod 600)
├── workspace/
│   └── logs/
│       └── audit.log             # Audit log
├── macos-bridge/
│   └── index.js                  # iMessage bridge
├── start.sh                      # Start script
├── stop.sh                       # Stop script
├── status.sh                     # Status check
├── logs.sh                       # View logs
└── backup.sh                     # Backup script

~/Library/LaunchAgents/
└── com.oneclaw.macos-bridge.plist  # Bridge auto-start

~/openclaw-backups/               # Backup storage
```

## 🆘 Getting Help

1. **Check Logs**: `cd ~/.oneclaw-secure && ./logs.sh`
2. **Read Security Doc**: `less SECURITY.md`
3. **OpenClaw Docs**: https://docs.oneclaw.ai
4. **GitHub Issues**: https://github.com/openclaw/openclaw/issues
5. **Discord**: https://discord.gg/openclaw

## 📤 Sharing with Friends

```bash
cd /Users/ijefferson.admin/Development/openclaw

# Create distribution package
./create-distribution.sh

# Shares: /tmp/one-claw-tied-behind-your-back-v1.0.tar.gz
# Send to friends via AirDrop, email, etc.

# They run:
tar -xzf one-claw-tied-behind-your-back-v1.0.tar.gz
cd one-claw-tied-behind-your-back-v1.0
./deploy-openclaw.sh
```

## ✅ Security Checklist

**Before First Start:**
- [ ] API key added to secrets/.env
- [ ] Application firewall installed (Little Snitch/Lulu)
- [ ] Secrets file is chmod 600
- [ ] Reviewed SECURITY.md

**After First Start:**
- [ ] Tested network isolation
- [ ] Verified non-root container
- [ ] Confirmed read-only root filesystem
- [ ] Set up monitoring cron job
- [ ] Created first backup

**Monthly:**
- [ ] Update OpenClaw
- [ ] Review audit logs
- [ ] Check for security advisories
- [ ] Test backup restore

**Quarterly:**
- [ ] Rotate API keys
- [ ] Review paired accounts
- [ ] Update firewall rules if needed

---

**Remember**: Security is about layers. Every layer adds protection!
