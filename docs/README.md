# SecureClaw Documentation

**Last Updated:** 2026-02-16

---

## 📚 Documentation Structure

### [setup/](./setup/) - Setup & Configuration Guides
Complete guides for setting up SecureClaw and all integrated services.

**Key Documents:**
- [OpenClaw Setup](./setup/OPENCLAW_SETUP.md) - Main OpenClaw bot installation
- [OpenClaw SSH Setup](./setup/OPENCLAW_SSH_SETUP.md) - SSH key configuration for remote access
- [Bot Development Team RPI Setup](./setup/BOT_DEVELOPMENT_TEAM_RPI_SETUP.md) - Raspberry Pi 4 setup for autonomous development
- [1Password Integration](./setup/1PASSWORD_INTEGRATION.md) - 1Password CLI integration
- [1Password Bot Usage](./setup/1PASSWORD_BOT_USAGE.md) - Using 1Password from the bot
- [Telegram Setup](./setup/TELEGRAM_SETUP.md) - Telegram bot configuration
- [Device Pairing](./setup/DEVICE_PAIRING.md) - Control UI device pairing
- [Tailscale Setup](./setup/TAILSCALE_SETUP.md) - Tailscale VPN configuration

**Service Integrations:**
- [Apple Services Setup](./setup/APPLE-SERVICES-SETUP.md)
- [Google Services Setup](./setup/GOOGLE-SERVICES-SETUP.md)
- [Google Calendar Quick Setup](./setup/GOOGLE-CALENDAR-QUICK-SETUP.md)
- [iCloud Services Setup](./setup/ICLOUD-SERVICES-SETUP.md)
- [Gmail/Telegram Setup](./setup/TELEGRAM_GMAIL_SETUP.md)

---

### [security/](./security/) - Security Documentation
Security architecture, policies, and verification procedures.

**Key Documents:**
- [Security Architecture](./security/SECURITY_ARCHITECTURE.md) - Overall security design
- [Security Scripts Reference](./security/SECURITY_SCRIPTS_REFERENCE.md) - verify-security.sh, scan.sh, killswitch.sh
- [Security Verification](./security/SECURITY_VERIFICATION.md) - Validation procedures
- [Verification Results](./security/VERIFICATION_RESULTS.md) - Latest security audit results
- [Credential Security Policy](./security/CREDENTIAL-SECURITY-POLICY.md) - How credentials are protected
- [Development Workflow (Read-Only)](./security/DEVELOPMENT_WORKFLOW_READ_ONLY.md) - Read-only filesystem workflow

**Security Value & Implementation:**
- [Security Value Proposition](./security/SECURITY_VALUE_PROPOSITION_REVISED.md)
- [Security Implementation Verification](./security/SECURITY-IMPLEMENTATION-VERIFICATION.md)
- [Security Policy Final](./security/SECURITY-POLICY-FINAL.md)
- [Credential Protection Implemented](./security/CREDENTIAL-PROTECTION-IMPLEMENTED.md)

---

### [architecture/](./architecture/) - Architecture & Planning
System design, implementation plans, and architectural decisions.

**Key Documents:**
- [Phase 3A/3B Implementation](./architecture/PHASE_3A_3B_IMPLEMENTATION.md) - Security hardening implementation
- [Phase 3 Requirements](./architecture/PHASE3_REQUIREMENTS.md) - Phase 3 planning
- [Distributed OpenClaw Node Architecture](./architecture/DISTRIBUTED_OPENCLAW_NODE_ARCHITECTURE.md) - Future: Pi as OpenClaw node
- [Identity Architecture](./architecture/IDENTITY.md) - Identity and authentication design
- [Workspace Decision](./architecture/WORKSPACE_DECISION.md) - Workspace isolation approach
- [Workspace Usage](./architecture/WORKSPACE_USAGE.md) - How workspaces work
- [OpenClaw Write Requirements](./architecture/OPENCLAW_WRITE_REQUIREMENTS.md) - Write access requirements

---

### [reference/](./reference/) - Reference Guides
Quick reference guides, commands, and how-to documentation.

**Key Documents:**
- [Quick Reference](./reference/QUICK_REFERENCE.md) - Common commands and workflows
- [Tailscale Commands](./reference/TAILSCALE_COMMANDS.md) - Tailscale CLI reference
- [Browser Fetch Skill](./reference/BROWSER_FETCH_SKILL.md) - Using the browser-fetch skill
- [1Password Security Test Guide](./reference/1PASSWORD-SECURITY-TEST-GUIDE.md) - Testing 1Password integration
- [Prerequisites](./reference/PREREQUISITES.md) - System prerequisites
- [Publish to ClawHub](./reference/PUBLISH-TO-CLAWHUB.md) - Publishing skills

---

## 🚀 Quick Start

### For New Users

1. **Prerequisites**: [reference/PREREQUISITES.md](./reference/PREREQUISITES.md)
2. **OpenClaw Setup**: [setup/OPENCLAW_SETUP.md](./setup/OPENCLAW_SETUP.md)
3. **Telegram Setup**: [setup/TELEGRAM_SETUP.md](./setup/TELEGRAM_SETUP.md)
4. **Device Pairing**: [setup/DEVICE_PAIRING.md](./setup/DEVICE_PAIRING.md)
5. **Quick Reference**: [reference/QUICK_REFERENCE.md](./reference/QUICK_REFERENCE.md)

### For Developers

1. **Architecture Overview**: [architecture/IDENTITY.md](./architecture/IDENTITY.md)
2. **Security Architecture**: [security/SECURITY_ARCHITECTURE.md](./security/SECURITY_ARCHITECTURE.md)
3. **Phase 3A/3B Implementation**: [architecture/PHASE_3A_3B_IMPLEMENTATION.md](./architecture/PHASE_3A_3B_IMPLEMENTATION.md)
4. **Raspberry Pi Setup**: [setup/BOT_DEVELOPMENT_TEAM_RPI_SETUP.md](./setup/BOT_DEVELOPMENT_TEAM_RPI_SETUP.md)

---

## 📋 Current Status

### ✅ Phase 1: Foundation (Complete)
- OpenClaw container running
- Telegram integration active
- Control UI accessible

### ✅ Phase 2: Gateway & Integration (Complete)
- SecureClaw Gateway operational (FastAPI, 89% coverage)
- PII sanitization active
- Audit ledger recording all activity
- 1Password integration working

### ✅ Phase 3A/3B: Security Hardening (Complete)
- Seccomp profiles enabled
- NET_RAW capability removed
- Gateway password moved to Docker secrets
- mDNS/Bonjour disabled
- Security verification script (13 checks)
- OpenSCAP compliance scanner
- Kill switch (freeze/shutdown/disconnect modes)

### ✅ SSH Capability (Complete)
- Bot can SSH to Raspberry Pi and other authorized hosts
- SSH key generated: `/home/node/.ssh/id_ed25519`
- Config: `/home/node/.ssh/config`

### ⏳ Phase 4: SSH Capability (In Progress)
- SSH proxy module
- Approval integration
- Command allowlist

### 📋 Phase 5: Live Action Dashboard (Planned)
- Real-time activity feed
- Security alerting
- React frontend

### 📋 Phase 6: Tailscale + Documentation (Planned)
- Tailscale serve script
- IEC 62443 compliance matrix
- Container security policy

---

## 🔐 Security Features

### Active Protections
- ✅ Non-root containers
- ✅ Read-only gateway filesystem
- ✅ Seccomp profiles (syscall filtering)
- ✅ Capability dropping (ALL dropped)
- ✅ Localhost-only binding
- ✅ Docker secrets for credentials
- ✅ PII sanitization
- ✅ Audit ledger
- ✅ Approval queue

### Security Tools
- `docker/scripts/verify-security.sh` - 13-check validation
- `docker/scripts/scan.sh` - OpenSCAP compliance scanning
- `docker/scripts/killswitch.sh` - Emergency shutdown

**See:** [security/SECURITY_SCRIPTS_REFERENCE.md](./security/SECURITY_SCRIPTS_REFERENCE.md)

---

## 🎯 Use Cases

### Personal AI Assistant
- Telegram-based interaction (@therealidallasj_bot)
- 1Password credential management
- Gmail/Calendar integration
- iCloud integration

### Secure Development
- SSH to development servers
- Git operations on remote machines
- Docker commands via SSH
- Autonomous code deployment

### Bot Development Team (Future)
- Raspberry Pi as autonomous development server
- Distributed OpenClaw node architecture
- Automated testing and CI/CD
- Self-healing deployments

---

## 📞 Getting Help

### Documentation Issues
- Check [session-notes/](../session-notes/) for latest session summaries
- Check [archive/](../archive/) for historical documentation

### System Issues
- Run security verification: `./docker/scripts/verify-security.sh`
- Check container logs: `docker logs openclaw-bot`
- Check gateway logs: `docker logs secureclaw-gateway`

### Service Status
- OpenClaw: http://localhost:18790
- Gateway: http://localhost:8080
- Telegram: @therealidallasj_bot

---

## 🗂️ Archive

Old status files and completion summaries are archived in [archive/](../archive/).

These files are kept for historical reference but are no longer actively maintained:
- Phase completion summaries
- Service integration success logs
- Old configuration snapshots
- Historical troubleshooting guides

---

## 📝 Contributing

When adding new documentation:

1. **Setup guides** → `setup/`
2. **Security docs** → `security/`
3. **Architecture/Planning** → `architecture/`
4. **Reference/How-to** → `reference/`
5. **Session notes** → `../session-notes/`

### Naming Conventions
- Use UPPER_SNAKE_CASE for consistency
- Be descriptive: `OPENCLAW_SSH_SETUP.md` not `SSH.md`
- Date session notes: `SESSION_SUMMARY_2026-02-16.md`

---

**Documentation maintained by:** Claude Sonnet 4.5 + @therealidallasj_bot
**Last major update:** Phase 3A/3B Security Completion (2026-02-16)
