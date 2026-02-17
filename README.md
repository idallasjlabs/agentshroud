# SecureClaw: A User-Controlled Proxy Layer for OpenClaw

**Version:** 0.2.0
**Status:** Phase 5 Complete — SSH Proxy + Live Dashboard
**Bot:** @therealidallasj_bot (Telegram)

> "One Claw Tied Behind Your Back" — You decide what the agent sees, not the agent.

---

## 🚀 Quick Start

**New users:** See [docs/setup/OPENCLAW_SETUP.md](docs/setup/OPENCLAW_SETUP.md)
**Documentation:** [docs/README.md](docs/README.md)
**Latest work:** [session-notes/CONTINUE.md](session-notes/CONTINUE.md)

---

## Current Status: v0.2.0

| Phase | Status | Description |
|-------|--------|-------------|
| **Phase 1: Foundation** | ✅ Complete | OpenClaw container, Telegram integration, Control UI |
| **Phase 2: Gateway Layer** | ✅ Complete | PII sanitization (89% coverage), audit ledger, approval queue |
| **Phase 3A/3B: Security** | ✅ Complete | Seccomp, secrets management, kill switch, verification tools |
| **Phase 4: SSH Capability** | ✅ Complete | SSH proxy, approval integration, command audit trail |
| **Phase 5: Dashboard** | ✅ Complete | Real-time activity feed, WebSocket events, live dashboard |
| Phase 6: Tailscale + Docs | 📅 Planned | Remote access, IEC 62443 compliance, policies |
| Phase 7: Hardening Skills | 📅 Planned | PromptGuard, egress filtering, drift detection |
| Phase 8: Polish & Publish | 📅 Planned | Documentation, examples, release |

**Latest Achievement:** SSH proxy with approval workflow, live dashboard with real-time WebSocket activity feed, and SQLite-backed approval queue persistence.

---

## What is SecureClaw?

SecureClaw is an open-source security framework that sits between your real digital life and an OpenClaw AI agent. Instead of granting the agent direct access to your email, files, browser, and accounts, SecureClaw creates a **controlled gateway** where you decide what data flows to the AI.

### Core Principles

1. **User Control**: You explicitly forward data; the agent never has direct access
2. **Defense in Depth**: Multiple security layers (network, container, application)
3. **Full Observability**: Complete audit trail of all agent actions
4. **Kill Switch**: Immediate emergency shutdown with credential revocation
5. **Zero Trust**: Agent runs in isolated container with minimal privileges

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    YOUR REAL DIGITAL LIFE                │
│  Gmail · iCloud · Browser · Files · Photos · Contacts   │
│                    (NEVER TOUCHED)                       │
└──────────────┬──────────────────────┬───────────────────┘
               │ You decide what      │
               │ to forward           │
               ▼                      ▼
┌──────────────────────┐  ┌───────────────────────┐
│   Telegram Bot       │  │   Control UI          │
│   @therealidallasj   │  │   localhost:18790     │
└──────────┬───────────┘  └──────────┬────────────┘
           │                         │
           ▼                         ▼
┌──────────────────────────────────────────────────────┐
│              SECURECLAW GATEWAY (FastAPI)             │
│                                                      │
│  ┌─────────────┐  ┌──────────┐  ┌────────────────┐  │
│  │  PII         │  │  Audit   │  │  Approval      │  │
│  │  Sanitizer   │  │  Ledger  │  │  Queue         │  │
│  └──────┬──────┘  └────┬─────┘  └───────┬────────┘  │
│         │              │                │            │
│         ▼              ▼                ▼            │
│  ┌──────────────────────────────────────────────┐    │
│  │    Encrypted Data in Transit & At Rest      │    │
│  └──────────────────┬───────────────────────────┘    │
└─────────────────────┼────────────────────────────────┘
                      │
        ──────── Localhost/Tailscale Only ────────
                      │
┌─────────────────────┼────────────────────────────────┐
│           HARDENED DOCKER CONTAINER                   │
│           (Non-root · Seccomp · Read-only FS)        │
│                     │                                │
│                     ▼                                │
│  ┌──────────────────────────────────────────────┐    │
│  │              OPENCLAW BOT                     │    │
│  │   • Claude Opus 4.6 (Anthropic API)         │    │
│  │   • No LAN access                            │    │
│  │   • No direct credentials                    │    │
│  │   • SSH capability (authorized hosts only)   │    │
│  │   • 1Password integration (vault access)     │    │
│  └──────────────────────────────────────────────┘    │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## Security Features (Phase 3A/3B Complete)

### Container Hardening
- ✅ **Non-root execution**: Both containers run as non-root users
- ✅ **Seccomp profiles**: Syscall filtering (default-deny, explicit allowlist)
- ✅ **Capability dropping**: ALL capabilities dropped, minimal re-add
- ✅ **Read-only filesystem**: Gateway container fully read-only
- ✅ **Network isolation**: No LAN access, localhost-only binding
- ✅ **Resource limits**: CPU, memory, PID limits enforced

### Secrets Management
- ✅ **Docker secrets**: API keys, passwords in encrypted secrets
- ✅ **1Password integration**: Secure credential storage and retrieval
- ✅ **No hardcoded secrets**: All sensitive data externalized

### Monitoring & Response
- ✅ **Audit ledger**: SQLite-based, SHA-256 hashed, 90-day retention
- ✅ **Security verification**: 13 automated checks (`verify-security.sh`)
- ✅ **Compliance scanning**: OpenSCAP integration (`scan.sh`)
- ✅ **Kill switch**: 3 modes (freeze/shutdown/disconnect) with credential revocation

### Data Protection
- ✅ **PII sanitization**: Presidio-based, 89% test coverage
- ✅ **Approval queue**: High-risk actions require user confirmation
- ✅ **Data retention**: Automatic cleanup after 90 days
- ✅ **Encrypted secrets**: TLS for external communication

**Security Score:** 26/26 checks passed (1 expected warning)

---

## Current Capabilities

### Communication
- **Telegram**: @therealidallasj_bot (allowlist: user 8096968754)
- **Control UI**: http://localhost:18790 (browser-based chat)
- **API**: http://localhost:8080 (Gateway REST API)

### Integrations
- **1Password**: Secure credential access via CLI
- **SSH**: Remote command execution on authorized hosts
- **Git**: Repository operations via SSH
- **Docker**: Container management via SSH

### AI Model
- **Claude Opus 4.6** (Anthropic API)
- **Fallback**: OpenAI GPT-4 support

---

## Quick Commands

### Security Verification
```bash
# Run all security checks
./docker/scripts/verify-security.sh

# Run compliance scan
./docker/scripts/scan.sh

# Emergency kill switch
./docker/scripts/killswitch.sh freeze  # Pause for investigation
./docker/scripts/killswitch.sh shutdown  # Graceful stop
./docker/scripts/killswitch.sh disconnect  # Nuclear option
```

### Container Management
```bash
# Start services
docker compose -f docker/docker-compose.yml up -d

# Check status
docker compose -f docker/docker-compose.yml ps

# View logs
docker logs openclaw-bot --tail 50
docker logs secureclaw-gateway --tail 50

# Restart services
docker compose -f docker/docker-compose.yml restart
```

### SSH (New in v0.1.0)
```bash
# SSH from bot to authorized hosts
docker exec -u node openclaw-bot ssh pi-dev "hostname"

# Example: Check disk space on Raspberry Pi
docker exec -u node openclaw-bot ssh raspberrypi "df -h"
```

### 1Password Access
```bash
# List vaults
docker exec -u node openclaw-bot bash -c 'source ~/.ssh/scripts/op-auth.sh && op vault list'

# Get credential
docker exec -u node openclaw-bot bash -c 'source ~/.ssh/scripts/op-auth.sh && op item get "Anthropic API Key" --fields password'
```

---

## Deploy on macOS

1. **Prerequisites**: Docker Desktop, Git
2. **Clone**: `git clone https://github.com/idallasj/oneclaw.git && cd oneclaw`
3. **Create secrets**:
   ```bash
   mkdir -p docker/secrets
   echo "your-openai-key" > docker/secrets/openai_api_key.txt
   echo "your-anthropic-key" > docker/secrets/anthropic_api_key.txt
   python3 -c "import secrets; print(secrets.token_hex(32))" > docker/secrets/gateway_password.txt
   # 1Password secrets (optional):
   echo "email" > docker/secrets/1password_bot_email.txt
   echo "password" > docker/secrets/1password_bot_master_password.txt
   echo "secret-key" > docker/secrets/1password_bot_secret_key.txt
   ```
4. **Configure**: Edit `secureclaw.yaml` — set `gateway.auth_token`
5. **Build & run**:
   ```bash
   cd docker
   docker compose build
   docker compose up -d
   ```
6. **Access**:
   - Gateway API: http://localhost:8080/status
   - Dashboard: http://localhost:8080/dashboard?token=YOUR_AUTH_TOKEN
   - OpenClaw UI: http://localhost:18790

---

## Documentation

### 📖 [Complete Documentation Index](docs/README.md)

**Quick Links:**
- [Setup Guide](docs/setup/OPENCLAW_SETUP.md) - Installation and configuration
- [SSH Setup](docs/setup/OPENCLAW_SSH_SETUP.md) - Remote access configuration
- [Raspberry Pi Setup](docs/setup/BOT_DEVELOPMENT_TEAM_RPI_SETUP.md) - Autonomous development server
- [Security Scripts](docs/security/SECURITY_SCRIPTS_REFERENCE.md) - verify, scan, killswitch
- [Security Architecture](docs/security/SECURITY_ARCHITECTURE.md) - Defense in depth
- [Phase 3A/3B Implementation](docs/architecture/PHASE_3A_3B_IMPLEMENTATION.md) - Latest work

**By Category:**
- [docs/setup/](docs/setup/) - Setup & configuration guides (18 files)
- [docs/security/](docs/security/) - Security documentation (11 files)
- [docs/architecture/](docs/architecture/) - System design & planning (7 files)
- [docs/reference/](docs/reference/) - Quick reference guides (6 files)

---

## Project Structure

```
oneclaw/
├── README.md                   ← You are here
├── docker/
│   ├── docker-compose.yml     ← Main container orchestration
│   ├── Dockerfile.openclaw    ← OpenClaw bot container
│   ├── seccomp/               ← Seccomp security profiles
│   ├── secrets/               ← Docker secrets (gitignored)
│   └── scripts/               ← Management scripts
│       ├── verify-security.sh ← 13-check security validation
│       ├── scan.sh            ← OpenSCAP compliance scanning
│       └── killswitch.sh      ← Emergency shutdown
├── gateway/
│   ├── ingest_api/            ← FastAPI gateway server
│   ├── tests/                 ← 89% test coverage
│   └── Dockerfile             ← Gateway container
├── docs/
│   ├── README.md              ← Documentation index
│   ├── setup/                 ← Setup guides
│   ├── security/              ← Security docs
│   ├── architecture/          ← Design docs
│   └── reference/             ← Quick reference
├── session-notes/             ← Development session logs
└── archive/                   ← Historical documentation
```

---

## Recent Changes (v0.1.0)

### Phase 3A: Security Completion
- ✅ Seccomp profiles re-enabled with ARM64 support
- ✅ NET_RAW capability removed
- ✅ Gateway password moved to Docker secrets
- ✅ mDNS/Bonjour disabled (prevents info disclosure)
- ✅ Read-only filesystem preparation (tmpfs added)
- ✅ Security verification script (13 automated checks)
- ✅ OpenSCAP compliance scanner
- ✅ DM policy verified (allowlist mode)

### Phase 3B: Kill Switch
- ✅ 3-mode emergency shutdown (freeze/shutdown/disconnect)
- ✅ Audit ledger export
- ✅ Credential revocation workflow
- ✅ Incident report generation

### SSH Capability (Phase 4 - In Progress)
- ✅ SSH key generation (Ed25519)
- ✅ SSH config for authorized hosts
- ✅ Raspberry Pi access configured
- ⏳ SSH proxy module (planned)
- ⏳ Approval integration (planned)

### Repository Cleanup
- ✅ 67 markdown files organized into docs/
- ✅ Documentation index created
- ✅ Session notes separated
- ✅ Archive for historical files

**See:** [CHANGELOG.md](CHANGELOG.md) for complete version history

---

## System Requirements

### Runtime
- **Docker**: 24.0+ with Compose v2
- **Storage**: 20GB free (104GB allocated for development)
- **RAM**: 6GB (Gateway: 512MB, OpenClaw: 4GB)
- **Network**: Tailscale (optional, for remote access)

### Development
- **OS**: macOS (Darwin 25.3.0) or Linux
- **Node.js**: 20+ (for OpenClaw)
- **Python**: 3.13+ (for Gateway)
- **Git**: 2.30+

### Optional
- **Raspberry Pi 4**: 8GB RAM (for autonomous development server)
- **1Password**: Family plan (for credential management)
- **OpenSCAP**: For compliance scanning

---

## Getting Started

### 1. Prerequisites
```bash
# Install dependencies
brew install docker docker-compose node python@3.13 tailscale

# Verify installation
docker --version
docker compose version
node --version
python3 --version
```

### 2. Clone Repository
```bash
git clone <your-repo-url> oneclaw
cd oneclaw
```

### 3. Configure Secrets
```bash
# Create secrets directory
mkdir -p docker/secrets

# Add your API keys
echo "your-openai-key" > docker/secrets/openai_api_key.txt
echo "your-anthropic-key" > docker/secrets/anthropic_api_key.txt
echo "your-gateway-password" > docker/secrets/gateway_password.txt

# Set permissions
chmod 600 docker/secrets/*.txt
```

### 4. Start Services
```bash
# Start containers
docker compose -f docker/docker-compose.yml up -d

# Wait for health checks (60-90 seconds)
docker compose -f docker/docker-compose.yml ps

# Verify security
./docker/scripts/verify-security.sh
```

### 5. Access Control UI
```bash
# Open browser
open http://localhost:18790

# Enter gateway password (from docker/secrets/gateway_password.txt)
# Complete device pairing
```

**Complete setup guide:** [docs/setup/OPENCLAW_SETUP.md](docs/setup/OPENCLAW_SETUP.md)

---

## Use Cases

### Personal AI Assistant
- Telegram-based interaction with Claude Opus 4.6
- Secure credential access via 1Password
- Calendar, email, and service integrations
- Voice commands (via iOS/macOS Shortcuts)

### Secure Development
- SSH to remote development servers
- Git operations on authorized machines
- Docker container management
- Autonomous code deployment

### Bot Development Team (Raspberry Pi)
- Autonomous development server
- Continuous integration and testing
- Self-healing deployments
- Distributed task execution

**See:** [docs/setup/BOT_DEVELOPMENT_TEAM_RPI_SETUP.md](docs/setup/BOT_DEVELOPMENT_TEAM_RPI_SETUP.md)

---

## Security & Privacy

### Threat Model
SecureClaw protects against:
- ✅ Prompt injection attacks
- ✅ Data exfiltration
- ✅ Unauthorized access to real accounts
- ✅ Supply chain attacks (skill verification)
- ✅ Network-based attacks (isolation)
- ✅ Privilege escalation (seccomp, capabilities)

### Mitigations
- **Network isolation**: No LAN access, localhost-only
- **PII sanitization**: Automatic redaction of sensitive data
- **Approval queue**: User confirmation for high-risk actions
- **Audit ledger**: Complete activity log with SHA-256 hashing
- **Kill switch**: Immediate shutdown with credential revocation

### Known Limitations
- OpenClaw container not read-only (disabled during development)
- No egress filtering (planned for Phase 7)
- No prompt injection detection (planned for Phase 7)

**See:** [docs/security/SECURITY_ARCHITECTURE.md](docs/security/SECURITY_ARCHITECTURE.md)

---

## Contributing

### Development Workflow
We follow **GitHub Flow**:

1. **Create feature branch** from `main`
   ```bash
   git checkout -b feature-your-feature-name
   ```

2. **Make changes** and commit
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

3. **Push and create PR**
   ```bash
   git push origin feature-your-feature-name
   # Create PR on GitHub
   ```

4. **Code review** and merge to `main`

### Commit Message Format
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `security:` Security improvements
- `refactor:` Code refactoring
- `test:` Test additions/changes

### Running Tests
```bash
# Gateway tests
cd gateway
pytest --cov=ingest_api tests/

# Security verification
./docker/scripts/verify-security.sh
./docker/scripts/scan.sh
```

---

## Roadmap

### ✅ v0.2.0 - Phases 1-5 Complete
See [Current Status](#current-status-v020) table above for completed phases:
- Phase 1: Foundation
- Phase 2: Gateway Layer
- Phase 3A/3B: Security Hardening
- Phase 4: SSH Proxy + Approval Integration
- Phase 5: Live Dashboard + WebSocket Events

### v0.4.0 (Phase 6)
- [ ] Tailscale serve script
- [ ] IEC 62443 compliance matrix
- [ ] Complete documentation

### v0.5.0 (Phase 7)
- [ ] PromptGuard / input filtering
- [ ] Outbound allowlist (egress filtering)
- [ ] Read-only reader agent
- [ ] Drift detection
- [ ] MEMORY.md scrubber
- [ ] Session isolation

### v1.0.0 (Phase 8)
- [ ] Production-ready release
- [ ] Public documentation
- [ ] Example deployments
- [ ] Community support

**See:** [docs/architecture/PHASE3_REQUIREMENTS.md](docs/architecture/PHASE3_REQUIREMENTS.md)

---

## License

[Specify your license here - MIT, Apache 2.0, etc.]

---

## Support

### Deploy on macOS

1. **Prerequisites**: Docker Desktop, Git
2. **Clone**: `git clone https://github.com/idallasj/oneclaw.git && cd oneclaw`
3. **Create secrets**:
   ```bash
   mkdir -p docker/secrets
   echo "your-openai-key" > docker/secrets/openai_api_key.txt
   echo "your-anthropic-key" > docker/secrets/anthropic_api_key.txt
   python3 -c "import secrets; print(secrets.token_hex(32))" > docker/secrets/gateway_password.txt
   # 1Password secrets (optional):
   echo "email" > docker/secrets/1password_bot_email.txt
   echo "password" > docker/secrets/1password_bot_master_password.txt
   echo "secret-key" > docker/secrets/1password_bot_secret_key.txt
   ```
4. **Configure**: Edit `secureclaw.yaml` — set `gateway.auth_token`
5. **Build & run**:
   ```bash
   cd docker
   docker compose build
   docker compose up -d
   ```
6. **Access**:
   - Gateway API: http://localhost:8080/status
   - Dashboard: http://localhost:8080/dashboard?token=YOUR_AUTH_TOKEN
   - OpenClaw UI: http://localhost:18790

---

## Documentation
- **Index**: [docs/README.md](docs/README.md)
- **Setup**: [docs/setup/](docs/setup/)
- **Security**: [docs/security/](docs/security/)

### Issues
- GitHub Issues: [Create an issue](<your-repo-url>/issues)
- Security Issues: Email security@[yourdomain]

### Community
- Telegram: @therealidallasj
- OpenClaw Discord: https://discord.gg/openclaw

---

**Built with**: FastAPI, Docker, OpenClaw, Claude Opus 4.6
**Security**: Defense in depth, zero trust architecture
**Status**: v0.2.0 — SSH proxy + live dashboard
**Next**: Phase 6 — Tailscale integration and documentation
