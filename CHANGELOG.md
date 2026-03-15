# Changelog — AgentShroud™

All notable changes to AgentShroud™ will be documented in this file.
AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026. Federal trademark registration pending.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased] — feat/v0.8.0-enforcement-hardening (session 3 — 2026-03-15)

### Summary

v0.8.0 completion — tranches V8-1 through V8-6 implemented and verified. All high-priority leakage, egress, rate-limit, and no-response issues closed.

### Fixed

- **Callback token leakage** — `_contains_internal_approval_banner` now detects `egress_allow_always_`, `egress_allow_once_`, `egress_deny_` callback data patterns; prevents inline keyboard tokens from reaching collaborators.
- **XML tool-call leakage** — `_contains_high_risk_collaborator_leakage` adds `<invoke name=` / `</invoke>` Anthropic XML format to unconditional block patterns.
- **False-positive in filename leakage filter** — `bootstrap.md`, `identity.md`, `memory.md` etc. now only trigger the high-risk filter when appearing in a content-revealing context; denial messages mentioning these filenames no longer double-filter.
- **Own protected notices no longer double-filtered** — `_contains_high_risk_collaborator_leakage` skips text already starting with `🛡️ Protected by AgentShroud`.
- **Raw `web_fetch` JSON rewritten for owner** — bot returning raw tool JSON (instead of executing) now shows an actionable advisory; collaborator sees `_COLLABORATOR_EGRESS_NOTICE`.
- **Egress approval artifacts** — collaborator-initiated web requests route approval to `owner_chat`; collaborator sees only `_COLLABORATOR_EGRESS_PENDING_NOTICE`.

### Tests

- `TestOutboundClassifierHelpers` — 14 new assertions: callback token detection, `<invoke>` XML, filename-vs-domain classification, context-aware denial bypass, protected-header skip.
- `TestCollaboratorRateLimitRecovery` — 2 tests: post-window recovery, owner unaffected by collaborator limiter.
- `TestNoResponseGuarantee` — 3 tests: generic message always answered, blocked command always produces notice, unknown user always gets pending or rate-limit notice.
- Full suite: **541+ passed, ≤1 failed** (pre-existing combined-run async ordering issue).

### Tranche Status

| Tranche | Status |
|---------|--------|
| V8-1 Onboarding reliability | ✅ Complete |
| V8-2 Command contract | ✅ Complete |
| V8-3 No-response elimination | ✅ Complete |
| V8-4 Egress semantics | ✅ Complete |
| V8-5 Leak suppression | ✅ Complete |
| V8-6 Rate limit UX | ✅ Complete |
| V8-7 3-pass assessment | Pending live run |

---

## [Unreleased] — feat/v0.8.0-enforcement-hardening (session 2 — 2026-03-14)

### Summary

v0.8.0 stabilization — stranger rate limiting, per-collaborator memory isolation, collaborator report cron fix, competitive analysis prompt update.
Full 218-probe live assessment: **208 PASS / 5 WARN / 1 FAIL (false positive)** — 97.2% pass rate.

### Added

- **Stranger rate limiter** — unknown/unapproved Telegram users throttled to 5 access requests/hour (default, env-configurable) before queuing owner approval. Prevents approval-queue flooding.
- **Stranger rate-limit notice** — `_send_stranger_rate_limit_notice()` sends throttled unknowns an exact UTC reset time (`HH:MM UTC`).
- **Per-collaborator isolated agents** — each of the 6 known collaborators gets a dedicated OpenClaw agent (`collab-{uid}`) with a private workspace (`.agentshroud/collab-{uid}/`) on the persistent `agentshroud-config` volume. Memory never bleeds between collaborators or to the owner. Persists across restarts and rebuilds. Generic `collaborator` agent retained for dynamically approved users.

### Fixed

- **Collaborator daily report stale data** — cron Morning, Evening, and Daily Digest messages now filter only files whose filename starts with today's YYYY-MM-DD prefix. Reports correctly show "No collaborator activity in the last 24 hours" when no activity occurred.
- **Rate-limit notice** — now includes absolute UTC reset time ("Rate limit resets at HH:MM UTC") instead of minutes-only estimate.

### Changed

- **Competitive analysis cron** — both landscape update crons now use a 4-section structured prompt: Market Analysis, Competitor Matrix, Autonomous Agent Ecosystem, Next Steps. Zero-hallucinations rule. Output to `reports/competitive-report-[DATE].md`; trend appended to `reports/trend-log.md`.
- **Email cron messages** — prefer today's dated report file over static fallback.

### Tests

- `TestStrangerRateLimit` (4 tests): within-limit approval flow, rate-limited owner suppression, cooldown deduplication, reset-time format — **4/4 pass**.
- Combined inbound + outbound + pipeline suite: **527 passed, 1 failed** (pre-existing combined-run async ordering issue; passes in isolation).
- 218-probe live Telegram security assessment: **208 PASS, 5 WARN (over-restriction), 1 FAIL (false positive on BOOTSTRAP.md mention-in-denial)**.

---

## [Unreleased] — feat/http-connect-proxy + feat/credential-isolation

### Summary

Two new security modules landing via open PRs (#24, #25). Dependency: P1 must merge before P2.

Additional stabilization work in current cycle focuses on v0.8.0 Telegram security-path reliability, collaborator safety-response consistency, owner-gated approval semantics, and regression expansion.

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

### Changed
- Telegram protected-response wording standardized to canonical header:
  - `🛡️ Protected by AgentShroud` + two newlines
- Collaborator egress redaction wording now explicitly states owner-gated behavior.
- Owner target parsing for collaborator management commands expanded to support:
  - numeric user IDs,
  - static aliases,
  - pending username aliases (e.g. `/approve ana`, `/deny ana`).

### Fixed
- Pending collaborator notice delivery now uses deterministic local fallback path to reduce no-response scenarios.
- Block-notification path now has deterministic fallback behavior for both collaborator and owner contexts when primary send fails.
- Local command normalization/regression coverage expanded for:
  - `/whoami@bot` variants
  - plain `whoami` local handling.

### Added
- New v0.8.0 execution summary draft:
  - `docs/planning/v0.8.0-execution-summary-draft.md`
- Updated release planning tracker section:
  - `docs/planning/RELEASE-PLAN.md` → “Current Execution Tracker (2026-03-14)”
- Updated tranche execution checklist with explicit v0.8.0/v0.9.0 remaining verification gates:
  - `remaining-code-only-tranches.md`

### Tests
- Gateway Telegram proxy stabilization regressions expanded (inbound/outbound).
- Latest full gateway run:
  - `pytest -q gateway/tests/test_telegram_proxy_inbound.py gateway/tests/test_telegram_proxy_outbound.py`
  - **516 passed, 0 failed, 0 skipped**

---

## [0.7.0] - 2026-02-25

### Summary
Major security hardening release. All 33 modules enforcing, prompt injection defense expanded, input normalization layer added. Full test suite: 1953 passed, 0 failed, 0 skipped, 0 warnings on both macOS (Python 3.14) and Docker/Linux (Python 3.13).

### Added
- **Input Normalizer** — NFKC normalization, zero-width char stripping, HTML/URL decode before all scanning
- **7 new PromptGuard patterns** — multilingual injection (6 languages), chat format injection (LLaMA/ChatML/Phi), payload-after-benign, echo traps, few-shot poisoning, markdown exfiltration, emoji unlock
- **ContextGuard enforcement** — `should_block_message()` now blocks high-severity attacks (was detect-only)
- **SecurityPipeline** — all 33 modules wired across P0/P1/P2/P3 tiers
- **FileSandbox enforce mode** — read/write allowlists, path traversal blocked
- **RBAC** — owner/collaborator/viewer roles, viewer blocked from manage operations
- **Session isolation** — per-user workspaces, cross-user access blocked
- **Path isolation** — per-user temp directories, cross-user file access blocked
- **Audit export** — JSON, CEF, JSON-LD formats with hash chain verification
- **Key rotation**, **memory lifecycle**, **credential isolation** modules
- **Prompt protection** — outbound system prompt leak detection with fuzzy matching
- **`/manage/modules` endpoint** — returns all 33 modules with tier + status
- **Enforcement audit script** — 40-check automated verification

### Fixed
- Middleware `_is_path_allowed_for_user` changed from fail-open to FileSandbox fallback
- `datetime.utcnow()` → `datetime.now(tz=timezone.utc)` for Python 3.13 compat
- macOS `/private` prefix normalization in path comparisons
- pytest cache warnings eliminated via `pytest.ini`

### Security
- 33/33 modules active and enforcing
- PromptGuard: 18 patterns (was 11), now blocks multilingual + encoding evasion
- ContextGuard: blocks high-severity injection (was monitor-only)
- FileSandbox: enforce mode blocks `/etc/shadow`, SSH keys, path traversal
- EgressFilter: enforce mode blocks unlisted domains
- MCP proxy: fail-closed on error

---

## [0.6.0] - 2026-02-23

### Summary
First production-ready release. All 30 original security modules wired into live pipeline. Web Control Center and TUI Console delivered.

### Added
- **Web Control Center** — 7-page dashboard for security management
- **TUI Console** — terminal-based control center + chat console
- **All 30 security modules** wired into SecurityPipeline
- **`GET /manage/modules`** — module status endpoint
- **Docker deployment** — Colima support for non-admin users
- **Per-host Telegram bots** — separate bot tokens per deployment

### Fixed
- Gateway binds 127.0.0.1 (was 0.0.0.0)
- PII redaction threshold tuned to 0.9
- Python 3.9 compat across 50+ files

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
