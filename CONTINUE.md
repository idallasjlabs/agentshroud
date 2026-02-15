# SecureClaw / OneClaw - Session Continue File

**Date**: 2026-02-15
**Project**: SecureClaw - "One Claw Tied Behind Your Back"
**Status**: Phase 3 Partially Complete, Ready for Full Security Implementation

---

## ✅ What's Working Now

### Infrastructure
- ✅ Gateway (FastAPI): Healthy, 89% test coverage, 87 tests passing
- ✅ OpenClaw Container: Healthy, running Node.js 22 with OpenClaw
- ✅ Docker Compose: Both containers operational
- ✅ API Keys: Loading correctly via startup script
  - OpenAI: sk-proj-Op8I...VYIA
  - Anthropic: sk-ant-api03-20XC...uQAA
- ✅ Telegram Bot: @therealidallasj_bot running (dmPolicy: open)
- ✅ Control UI: http://localhost:18790 (accessible)
- ✅ Gateway: http://localhost:8080 (accessible)

### Security (Partial)
- ✅ Both containers: non-root execution (node user, secureclaw user)
- ✅ Both containers: cap_drop: ALL, no-new-privileges
- ✅ Both containers: localhost-only binding (127.0.0.1)
- ✅ Gateway: read_only: true filesystem
- ✅ Docker Secrets: API keys mounted securely
- ✅ PII Sanitizer: Active in gateway
- ✅ Audit Ledger: SQLite-based, SHA-256 hashed
- ✅ Approval Queue: Functional with WebSocket

---

## ⏳ Pending Setup (User Action Required)

### 1. Gmail Integration
**Status**: Waiting for user to complete browser setup

**Steps to complete**:
1. Enable IMAP: Gmail → Settings → Forwarding and POP/IMAP → Enable IMAP
2. Create app password: https://myaccount.google.com/apppasswords
3. Run this command with your email and app password:
```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels add \
  --channel gmail \
  --email "YOUR_EMAIL@gmail.com" \
  --password "YOUR_16_CHAR_APP_PASSWORD"
```

**Test Gmail**:
- Message @therealidallasj_bot on Telegram: "Send an email to YOUR_EMAIL@gmail.com with subject 'Test' and message 'Hello'"

### 2. Tailscale Remote Access
**Status**: Command ready, waiting for execution

**Run this command**:
```bash
sudo tailscale serve --bg --https=18790 http://localhost:18790
sudo tailscale serve --bg --https=443 http://localhost:8080
```

**Access from anywhere on Tailnet**:
- Dashboard: https://marvin.tail240ea8.ts.net
- Control UI: https://marvin.tail240ea8.ts.net:18790

### 3. Test Telegram
**Status**: Bot ready, waiting for user to test

- Open Telegram (Mac/iPhone/iPad/Apple Watch)
- Search: @therealidallasj_bot
- Send: "Hello, are you working?"
- Expected: AI response from Claude Opus 4.6

---

## 🔴 Security Gaps (Phase 3A - Must Fix Before Production)

| Item | Status | Risk Level | Action Needed |
|------|--------|-----------|---------------|
| Seccomp profiles | ❌ DISABLED | HIGH | Re-enable after profiling syscalls |
| OpenClaw read-only | ❌ read_only: false | HIGH | Change to true, add tmpfs |
| NET_RAW capability | ❌ Present | MEDIUM | Remove from docker-compose.yml |
| mDNS broadcasting | ❌ Active | MEDIUM | Add OPENCLAW_DISABLE_BONJOUR=1 |
| Gateway password | ❌ Hardcoded | MEDIUM | Move to Docker secrets |
| Security verification | ❌ No script | N/A | Create verify-security.sh |
| OpenSCAP scanning | ❌ No script | N/A | Create scan.sh |
| Telegram security | ⚠️ dmPolicy: open | HIGH | Change to allowlist mode |

---

## 📋 Implementation Roadmap

### PHASE 3A: Security Completion (1-2 days) ← START HERE
- Re-enable seccomp profiles
- Make OpenClaw read-only
- Remove NET_RAW
- Disable mDNS
- Move secrets to Docker secrets
- Create verify-security.sh (13 checks)
- Create scan.sh (OpenSCAP)
- Secure Telegram (allowlist mode)

### PHASE 3B: Kill Switch (1 day)
- killswitch.sh script (freeze/shutdown/disconnect)
- API endpoint: POST /killswitch
- Configuration integration

### PHASE 4: SSH Capability (2-3 days)
- Trusted hosts configuration
- SSH proxy module
- Command allowlist/denylist
- Approval queue integration
- Full audit trail

### PHASE 5: Live Dashboard (3-4 days)
- Real-time WebSocket activity feed
- Security alerting
- React frontend
- Action replay

### PHASE 6-8: Advanced Features (5-10 days)
- Tailscale integration
- IEC 62443 compliance
- Import/Export
- Hardening skills
- iOS/macOS Shortcuts

**Total to MVP**: 15-20 days

---

## 🎯 Next Session Quick Start

Choose one path:

### PATH A: Complete Setup (30 minutes)
1. Set up Gmail (follow steps above)
2. Enable Tailscale remote access
3. Test Telegram bot
4. Verify everything works end-to-end

### PATH B: Implement Security (2-3 hours)
1. Profile syscalls with strace
2. Update seccomp profiles
3. Make OpenClaw read-only
4. Create verification scripts
5. Run security scan

### PATH C: Build Kill Switch (1 hour)
1. Create killswitch.sh
2. Test all three modes
3. Add API endpoint

---

## 🔧 Quick Commands

### System Check
```bash
# Full system test
./docker/scripts/test-system.sh

# Container status
docker compose -f docker/docker-compose.yml ps

# Security status (after Phase 3A)
./docker/scripts/verify-security.sh
```

### Telegram
```bash
# Channel status
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels list

# Pairing status
docker compose -f docker/docker-compose.yml exec openclaw openclaw pairing list telegram
```

### Logs
```bash
# All logs
./docker/scripts/logs.sh

# OpenClaw only
./docker/scripts/logs.sh openclaw 100

# Gateway only
./docker/scripts/logs.sh gateway 50
```

---

## 📁 Key File Locations

**Configuration**:
- /Users/ijefferson.admin/Development/oneclaw/secureclaw.yaml
- /Users/ijefferson.admin/Development/oneclaw/docker/docker-compose.yml

**Secrets** (⚠️ NEVER commit to git):
- docker/secrets/openai_api_key.txt
- docker/secrets/anthropic_api_key.txt
- docker/secrets/gateway_password.txt (to be created)

**Scripts**:
- docker/scripts/ (all management scripts)
- docker/scripts/start-openclaw.sh (startup with API keys)

**Documentation**:
- /Users/ijefferson.admin/.claude/plans/snuggly-wobbling-fox.md (implementation plan)
- /Users/ijefferson.admin/Development/oneclaw/CONTINUE.md (this file)
- /Users/ijefferson.admin/Development/oneclaw/TAILSCALE_COMMANDS.md (remote access)

---

## 🚨 Critical Reminders

### "One Claw Tied Behind Your Back"
- You control what the agent sees (not the agent)
- No direct filesystem access
- No LAN access
- All data flows through gateway
- Full audit trail
- Kill switch available

### Security First
- Never use dmPolicy: open in production
- Always verify containers are healthy
- Test Telegram/Gmail regularly
- Run security scans after changes
- Backup before major modifications

### OpenClaw Vulnerabilities (from trust.openclaw.ai)
- Prompt injection → Need PromptGuard
- Tool abuse → Approval queue active
- Supply chain → Need skill scanner
- Data exfiltration → Need egress filtering

---

**Last Updated**: 2026-02-15
**Current Phase**: Phase 3 (Partially Complete)
**Next Milestone**: Complete Phase 3A security gaps
**Project Goal**: Enable safe, controlled use of OpenClaw's full capabilities
