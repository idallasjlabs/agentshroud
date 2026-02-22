# Changelog — AgentShroud™

All notable changes to AgentShroud™ will be documented in this file.
AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026. Federal trademark registration pending.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased] — feat/http-connect-proxy + feat/credential-isolation

### Summary

Two new security modules landing via open PRs (#24, #25). Dependency: P1 must merge before P2.

### Added

#### P1: HTTP CONNECT Proxy (PR #24)
- **HTTP CONNECT proxy** on port 8181 — all bot outbound traffic routed through gateway
- **Domain allowlist enforcement** — default-deny; only approved domains reachable
- **Traffic statistics** endpoint (`GET /proxy/status`) — allowed/blocked counts, recent requests
- **AppState integration** — proxy lifecycle tied to FastAPI lifespan

#### P2: Credential Isolation (PR #25)
- **`/credentials/op-proxy` endpoint** — bot sends `op://` reference, gateway reads secret from 1Password
- **Allowlist validation** — only paths matching `op://AgentShroud Bot Credentials/*` are permitted
- **Path traversal protection** — `fnmatch` pattern check blocks any reference outside allowed vault
- **OpProxyRequest model** — typed Pydantic request for credential proxy
- **Token isolation** — `OP_SERVICE_ACCOUNT_TOKEN` moves to gateway; bot container never holds it
- **Docker config persistence** — cron `jobs.json` and `apply-patches.js` baked into Docker image
- **Init script** — `init-openclaw-config.sh` runs on every startup to guarantee agent routing and bindings
- **Email migration** — bot identity moved from `agentshroud.ai@gmail.com` → `agentshroud.ai@gmail.com`
- **Op-wrapper hardening** — credential retrieval uses Python subprocess (no shell expansion)

### Security
- 1Password service account token isolated to gateway — eliminates bot-side credential exposure
- Bot outbound HTTP restricted to approved domain allowlist
- Shell expansion credential leak pattern eliminated in `op-wrapper.sh`

---

## [0.5.0] - 2026-02-21

### Summary

Full visibility release — all agent routing, binding, and session issues resolved. Bot responses
now reliably reach the main agent (claude-opus-4-6). XML function-call leak to Telegram eliminated.

### Fixed

#### Agent Routing (P0)
- **Main agent not default**: collaborator was sole entry in `agents.list` → all isolated sessions
  routed to collaborator (which has `exec`, `browser`, `cron` in deny list)
- **Fix**: added `main` as first entry in `agents.list` → main is now the system default
- **Telegram binding missing**: Isaiah's peer ID (`8096968754`) had no explicit binding → fell
  through to collaborator default; added explicit `main` binding in `openclaw.json`
- **sessionTarget mismatch**: cron jobs used `systemEvent` + `sessionTarget: main` → events queue
  but LLM never executes; reverted all jobs to `isolated` + `agentTurn` + `agentId: main`

#### Security
- **Leaked Gmail app password purged** from collaborator session logs and cron run logs
- **Hallucinated cron jobs** (every-minute `cron_TIMESTAMP` IDs) identified as collaborator agent
  hallucination — never existed in real storage; confirmed clean

### Added
- **Verified end-to-end**: cron run confirms `sessionKey: agent:main:cron:...`, model `claude-opus-4-6`,
  real diagnostic output (no XML leak)
- **54 pre-existing test failures resolved** (P0 gate-clearing)

---

## [0.4.0] - 2026-02-19

### Summary

**Container security toolchain + XML filter security fix.** 18 security modules, MCP proxy, web traffic proxy, full egress control, 951 tests at 92%+ coverage, and defense-in-depth container scanning (Trivy, ClamAV, Falco, Wazuh, OpenSCAP).

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
- Telegram bot integration (@agentshroud.ai_bot)
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

## Migration Notes

### v0.4.0 → v0.5.0
- No breaking changes to the gateway API
- `openclaw.json` must have `main` as first entry in `agents.list` (handled automatically by `init-openclaw-config.sh`)
- All cron jobs should use `sessionTarget: isolated` + `payload.kind: agentTurn` + `agentId: main`

### v0.3.0 → v0.4.0
- Container security toolchain requires updated Docker images (Trivy, ClamAV, Falco, Wazuh, OpenSCAP)
- `filter_xml_blocks` is now active — raw XML tool calls are stripped from agent responses
- All existing configurations remain compatible

### Recommended Steps
1. Update your `.env` with new security module settings (see `examples/recommended.env`)
2. Enable PromptGuard: `PROMPT_GUARD_ENABLED=true`
3. Enable egress filtering: `EGRESS_FILTER_ENABLED=true`
4. Review `examples/paranoid.env` for maximum security settings
5. Set up GitHub Actions CI (copy `.github/workflows/ci.yml`)
6. Run the version manager: `scripts/openclaw-manage.sh check`
