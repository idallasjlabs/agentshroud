# Changelog

All notable changes to AgentShroud (AgentShroud) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-02-18

### Summary

**First stable release!** Complete enterprise security proxy with 12 security modules, 351 tests at 92%+ coverage, professional documentation, and CI/CD pipeline.

### Added

#### Phase 6: Tailscale & Documentation
- **Tailscale integration** for secure remote access
- **IEC 62443 compliance** documentation and alignment
- **Security policies** and operational runbooks
- **Comprehensive documentation** site (architecture, setup, reference, deploy)

#### Phase 7: Security Hardening
- **PromptGuard module** — detects and blocks prompt injection attacks
- **Egress filter** — network-level outbound connection control
- **Drift detector** — monitors container filesystem for unauthorized changes
- **Trust manager** — cryptographic verification of agent identity
- **Encrypted store** — at-rest encryption for sensitive configuration
- **Agent isolation** — enhanced seccomp profiles and resource limits
- **Peer review system** — automated multi-model security review for PRs

#### Phase 8: Polish & Publish
- **README overhaul** — professional documentation with architecture diagram
- **SECURITY.md** — vulnerability reporting and disclosure policy
- **CONTRIBUTING.md** — contributor guide with code style and PR process
- **LICENSE** — MIT License (Isaiah Jefferson)
- **Example configurations** — minimal, recommended, paranoid env files
- **Docker Compose examples** — minimal and production deployments
- **GitHub Actions CI** — automated testing, coverage, security scan, linting
- **OpenClaw Version Manager** — security-reviewed version upgrades/downgrades

### Changed
- Upgraded test suite from 89% to 92%+ coverage
- Improved PII sanitizer with additional entity types
- Enhanced approval queue with SQLite persistence
- Expanded SSH proxy command allowlists

### Security
- Mitigated gateway auth bypass (SC-2026-001) via mandatory auth enforcement
- Added prompt injection detection
- Network egress filtering blocks LAN access by default
- All mutations require human approval

---

## [0.2.0] - 2026-02-17

### Summary
SSH proxy capability with approval workflow, live dashboard with real-time WebSocket events.

### Added

#### Phase 4: SSH Capability
- **SSH proxy** with command allowlists and denied command patterns
- **Approval integration** — SSH commands routed through approval queue
- **Auto-approve** for safe read-only commands (git status, ls, whoami)
- **Session management** with timeout enforcement
- **Command audit trail** in SQLite ledger

#### Phase 5: Dashboard
- **Real-time dashboard** with WebSocket live activity feed
- **Approval management** — approve/deny from dashboard UI
- **System health** monitoring (gateway, agent, ledger stats)
- **WebSocket event bus** for push notifications
- **Static file serving** for dashboard assets

### Changed
- Approval queue now persisted in SQLite (was in-memory)
- Router supports SSH-type forwarding

---

## [0.1.0] - 2026-02-16

### Summary
First tagged release with core security framework.

### Added

#### Phase 1: Foundation
- OpenClaw container deployment
- Telegram bot integration (@therealidallasj_bot)
- Basic control UI

#### Phase 2: Gateway Layer
- **PII sanitizer** — Microsoft Presidio-powered detection & redaction
- **Audit ledger** — SQLite-backed immutable log
- **Approval queue** — human-in-the-loop for sensitive actions
- **Multi-agent router** — routes content to appropriate agents
- **Authentication** — HMAC shared secret and JWT support
- **Data forwarding API** — REST endpoints for content ingestion

#### Phase 3A/3B: Security Hardening
- **Seccomp profiles** with ARM64 support
- **Docker secrets** management
- **Kill switch** — emergency freeze/shutdown/disconnect
- **Security verification** script (13 automated checks)
- **Read-only rootfs** preparation
- **mDNS/Bonjour** disabled
- **Tmpfs mounts** for writable paths

### Security
- 26/26 security checks passing
- Gateway authentication enforced
- Container isolation with resource limits

---

## Migration Guide: v0.2.0 → v1.0.0

### Breaking Changes
None. v1.0.0 is backwards compatible with v0.2.0 configurations.

### New Required Configuration
None. All new features are opt-in.

### Recommended Steps
1. Update your `.env` with new security module settings (see `examples/recommended.env`)
2. Enable PromptGuard: `PROMPT_GUARD_ENABLED=true`
3. Enable egress filtering: `EGRESS_FILTER_ENABLED=true`
4. Review `examples/paranoid.env` for maximum security settings
5. Set up GitHub Actions CI (copy `.github/workflows/ci.yml`)
6. Run the version manager: `scripts/openclaw-manage.sh check`
