# 🛡️ AgentShroud Release Plan

**Created:** 2026-03-04
**Last Updated:** 2026-03-20
**Related:** docs/planning/MASTER-FEATURE-LIST.md (232 items total)

---

## Current Execution Tracker (2026-03-14)

This section tracks the **active execution state** for v0.8.0 closure and v0.9.0 code-only rollout.

### Live tracker files
- v0.8.0 draft execution summary:
  - `docs/planning/v0.8.0-execution-summary-draft.md`
- Remaining tranche checklist + per-tranche verification:
  - `remaining-code-only-tranches.md`

### Current status snapshot

| Track | Status | Verification Basis |
|---|---|---|
| v0.8.0 baseline delivery | Documented complete baseline | `docs/v0.8.0-feature-list-final.md`, phase-review artifacts |
| v0.8.0 stabilization hardening | In progress | Telegram proxy inbound/outbound test suites + security assessment passes |
| v0.9.0 code-only plan | In progress | Remaining tranches tracked in `remaining-code-only-tranches.md` |
| External infra/ops actions | Deferred | Explicitly excluded from current code-only tranche execution |

### Current hard gate
Every tranche must satisfy all of:
1. Targeted tests for touched behaviors pass.
2. Full Telegram gateway suites pass with no failures/skips.
3. Manual Telegram role-behavior checks pass (owner vs collaborator).
4. Security assessment report shows deterministic response behavior (no silent collaborator drops for tested prompts).

---

## v0.8.0 "Watchtower" — Security Fixes + Module Wiring (104 items)

*Goal: Pass Steve Hay's blue team assessment. Zero false positives, zero bypasses.*

### 🔴 P0 — Security Fixes (17 items)

#### Gateway Pipeline
1. **Fix proxy message blocking** — FileSandbox/PathIsolation scanning message TEXT instead of only tool calls. Admin messages getting blocked by content patterns ("memory", file paths). Fix: only apply file-system middlewares to `request.type == 'tool_call'`, not chat messages.
2. **Fix LLM API bypass** — Anthropic SDK not routing through gateway. Bot reaches Anthropic directly, bypassing entire security pipeline. Last gap in full traffic interception.
3. **Fix PII redaction for collaborator messages** — Gateway pipeline not scanning Telegram message content for collaborators. Tested with fake SSN, went through unmasked.
4. **Fix ContextGuard `should_block_message()`** — Always returns False. Documented bug since Feb 25. Detects but never blocks.
5. **Fix GitGuard** — Currently a no-op (logs only, never blocks).
6. **Fix op-proxy vault name mismatch** — "Agent Shroud Bot Credentials" vs "AgentShroud Bot Credentials" (with/without space).

#### Module Enforcement
7. **Wire remaining 14 modules into request path** — DNSFilter, DriftDetector, EgressMonitor, KeyRotationManager, MultiTurnTracker, NetworkValidator, OutputCanary, PathIsolationManager, ToolChainAnalyzer, EnhancedToolResultSanitizer, BrowserSecurityGuard, OAuthSecurityValidator, ApprovalHardening, CredentialInjector.
8. **Enforce-by-default for core modules** — Steve Hay Tier 1: R-02, R-03.
9. **Outbound information filtering** — New module, Steve R-01.
10. **Per-user session isolation** — New module, Steve R-04, R-05.
11. **Credential isolation** — Remove secrets from bot container, all credentials in gateway vault with transparent injection. Steve R-10, R-11, R-12.

#### Prompt Injection Hardening
12. **Expand PromptGuard** — 20+ new patterns (multilingual, chat format injection, LLaMA format, echo traps, payload splitting).
13. **Multilingual injection defense** — 35+ languages.
14. **Input normalization** — NFKC, zero-width character strip, HTML decode, URL decode, base64 detection.
15. **Cross-turn correlation** — MultiTurnTracker for crescendo attack detection.
16. **Tool result sanitization** — Strip markdown image/link injection from tool outputs.
17. **Output canary system** — Invisible tokens detect prompt leakage.

### 🟡 P1 — High Priority (8 items)

18. **Observatory Mode** — Global `AGENTSHROUD_GLOBAL_MODE=monitor|enforce` switch. `/manage/mode` API. Per-module pin overrides (keep killswitch enforcing). Auto-revert timer. Dashboard indicator.
19. **Interactive Egress Firewall ("Little Snitch for Agents")** — All outbound requires explicit approval. Telegram inline keyboard: Allow always / Allow once / Deny. Persistent allowlist. Risk assessment heuristic (green/yellow/red). Emergency "block all" button.
20. **Kill switch verification** — Automated testing, <1s FREEZE, <5s SHUTDOWN. Steve Tier 2: R-15, R-16.
21. **Per-user RBAC at MCP Proxy** — Steve Tier 2: R-13.
22. **PII scanning on MCP tool results** — Steve Tier 2: R-17.
23. **Compliance-ready audit export** — CEF/JSON-LD format. Steve Tier 2: R-14.
24. **mTLS between containers** — step-ca internal CA. All gateway ↔ bot traffic encrypted. Certificate rotation. Verify zero plaintext (tcpdump).
25. **Pi-hole DNS filtering** — Default docker-compose component. All containers use Pi-hole as DNS. Default blocklists (Steven Black, OISD, Phishing Army). Auto-update cron. `/manage/dns` API endpoint.

### 🟢 P2 — Quick Wins (11 items)

26. **Fix startup/shutdown messages** — Format: `agentshroud-bot@hostname` not `[production]`.
27. **Fix chat-console** — Python syntax error in `chat_console.py` line 59.
28. **Fix start-control-center script** — Not found / broken.
29. **Fix workspace file ownership** — uid 14664 → node (from backup restore).
30. **Collaborator interaction logs** — Persist forever, never delete.
31. **Bot config protection** — Cannot change any configuration unless directed by admin from communication channel.
32. **Replace GitHub PAT** — Switch to fine-grained token.
33. **Delete destructive branch** — `final/network-lockdown` deletes 12k+ lines, block via GitHub workflow.
34. **Copyright/trademark** — Add to all appropriate files.
35. **Merge pending PRs** — Phases 9, 10, 11 branches (pending since Feb 18).
36. **Org chart** — Agile team structure: Isaiah = PO, AgentShroud bot = Scrum Master, Claude Code = Engineers, Gemini/Codex = QA.

### 🔧 Code Quality (2 items)

37. **Quarantine blocked messages instead of discarding** — Admin messages blocked by security pipeline should be queued for review, not silently destroyed. Admin can review and release via Telegram inline buttons or dashboard.
38. **Refactor main script into modules** — Split by concern: startup/init, security pipeline, middleware chain, proxy routes, config loading, credential management, notification system. Each independently testable.

### 📊 Exit Criteria (5 items)

39. **E2E test suite** — 10 scenarios: PII, injection, approval, audit chain, bypass, kill switch, egress, trust, response scan, chain integrity.
40. **Canary system** — Hourly fake PII message + verification.
41. **Zero defects** — 0 errors, 0 warnings, 0 skipped tests.
42. **Internal blue team** — Passes 100% (all modules enforcing).
43. **Module audit** — All modules confirmed in enforce mode, not monitor.

---

## v0.9.0 "Sentinel" — Data Isolation + SOC + Remediation (37 items)

*Goal: Private service data isolation, Security Operations Center, fix Steve's blue team findings, add iMessage.*

### 🔴 Private Service Data Isolation (6 items)

44. **Tool-level access control** — Collaborators cannot invoke tools that access admin-only services (Gmail, Home Assistant, iCloud, financial, etc.). Per-user tool allowlist/blocklist at the MCP proxy layer.
45. **Response filtering** — Admin-private data never leaks into collaborator sessions. If a tool result contains admin-private data, it's stripped or blocked before reaching the collaborator.
46. **Memory isolation hardening** — Admin-private data in memory files inaccessible to collaborator sessions. Gap found Feb 26: collaborators could `memory_search` and read `MEMORY.md`. Needs enforcement at the OpenClaw/gateway level.
47. **Prompt injection defense for data isolation** — Collaborator cannot trick the bot into revealing admin data via indirect prompts, jailbreaks, or multi-turn escalation.
48. **Audit + alerting for private data access** — All access attempts (successful or blocked) to admin-private services logged and alerted to admin via Telegram.
49. **Privacy policy file** — Admin defines which services are "private" vs "shared" in a clear config file. Enforced by gateway pipeline. Example: Gmail = private, web_search = shared.

### 🔴 Security Operations Center (SOC) (6 items)

50. **Unified security dashboard** — Single pane of glass for all security events across all modules.
51. **OpenClaw upstream CVE tracking** — Monitor for vulnerabilities in OpenClaw itself, alert on new CVEs.
52. **ClawHub skill vetting** — 26% of skills have vulnerabilities; automated scanning before install.
53. **Network security correlation** — Cross-reference DNS, egress, and audit events for threat detection.
54. **Compliance reporting** — IEC 62443 and other frameworks, automated report generation.
55. **Incident response automation** — Playbooks for common security events (credential leak, injection detected, etc.).

### 🟡 Steve Hay Remediation (4 items)

56. **Triage + fix all findings** from Steve's blue team test.
57. **Automated key rotation** — Zero-downtime. Steve Tier 3: R-22.
58. **Progressive trust activation** — Graduated permissions based on behavior. Steve Tier 3: R-23.
59. **Red team preparation** — Prep for Phases 1-6.

### 🟡 Apple Messages Integration (4 items)

60. **iMessage activation** — agentshroud.ai@icloud.com on Marvin.
61. **GUI sign-in** — One-time physical access by Isaiah for agentshroud-bot user.
62. **Messages relay daemon** — launchd + AppleScript on Marvin.
63. **Chris Shelton routing** — His Telegram is deactivated (403), needs iMessage route.

### 🟡 Security Tools — Full Integration (5 items)

64. **Wazuh** — Full agent, real-time alerting, dashboard integration.
65. **Trivy** — Container scanning on every rebuild, CVE dashboard.
66. **ClamAV** — File scanning on uploads/downloads.
67. **OpenSCAP** — CIS Docker Benchmark, compliance reports.
68. **Unified security scanner dashboard** — All scanners in one view.

### 🟢 Infrastructure (5 items)

69. **Podman support** — Fix Pi (requires Podman 4.x, current 3.0.1 too old).
70. **Apple Containers** — macOS Tahoe support.
71. **Dynamic Tailscale IP resolution** — Sidecar that resolves hostnames, eliminates IP pinning.
72. **Port scanner for test instances** — Find available ports + Tailscale serve setup.
73. **Multi-language support planning** — Languages supported by OpenClaw/Claude.

### 🟢 Multi-Agent Architecture (3 items)

74. **Peer-to-peer leadership protocol** — Any bot can lead or follow, no fixed hierarchy.
75. **Cross-instance gateway communication** — Instances call each other's gateways.
76. **Leader/follower handoff** — Owner assigns/revokes leadership mid-conversation.

### 🟢 Development Infrastructure (4 items)

77. **direnv + Nix** for reproducible dev environment.
78. **Dependency management framework** (GSD or equivalent).
79. **Orchestration framework** for multi-agent development.
80. **MCP integration with Lucy** (compliance orchestration).

---

## v1.0.0 "Fortress" — Ship-Ready Public Release (116 items)

*Goal: Production-ready, installable, documented, red-team-tested.*

### Phase 1: Security & Secrets (14 items)

1. 🔴 Secret scanner on full git history (trufflehog/gitleaks, all commits)
2. 🔴 Rotate all credentials to production values (was #113)
3. Verify .gitignore covers all secret patterns (verify-only)
4. Verify pre-commit hooks enforce secret scanning (verify-only)
5. Audit all example files use fake placeholders
6. Verify .env.example committed for all secret-bearing dirs (verify-only)
7. Codebase audit: no hardcoded IPs or hostnames
8. Codebase audit: no debug/default credentials
9. Review SECURITY.md — add assumed model compromise section, verify disclosure process
10. Dependency vulnerability audit (pip audit, npm audit, Trivy)
11. Pin base image to digest (`@sha256:...` not tag)
12. 🔴 Verify non-root container user on ALL services
13. Remove `privileged: true` from docker-compose (line 229)
14. 🔴 Verify runtime secret injection (no secrets baked into image layers)

### Phase 2: Repo Hygiene (10 items)

15. Remove build artifacts from repo
16. Remove IDE configs from repo; add to .gitignore
17. 🔴 Resolve all TODO/FIXME on security-critical paths
18. Dead code removal pass
19. Add directory-level READMEs (gateway/, docker/, docs/, scripts/)
20. Consistent naming convention audit
21. Audit test fixtures for real PII — replace with synthetic data
22. Verify git history clean after secret scanner (#1)
23. Enable branch protection on main (require PR reviews, status checks, no force push)
24. Delete stale remote branches

### Phase 3: Container & Runtime Hardening (11 items)

25. Verify .dockerignore completeness (verify-only)
26. Convert to multi-stage Dockerfile (separate build/runtime stages)
27. Document image sizes for gateway and bot
28. Verify graceful SIGTERM shutdown (all services)
29. Audit for hardcoded container paths — replace with env vars
30. 🔴 Verify logs go to stdout/stderr (no file-only logging)
31. 🔴 Configure log rotation (Docker log driver or compose log options)
32. Document writable volumes explicitly
33. 🔴 Document resource limits and minimum requirements (RAM, CPU, disk)
34. Resource pressure testing (verify behavior under memory/CPU/disk pressure)
35. Verify timezone handling (UTC internally, configurable TZ for display)

### Phase 4: Dependencies (7 items)

36. Pin all dependency versions (requirements.txt uses `==`)
37. Commit lockfiles
38. Document vendored/patched tools (grammY SDK patch, etc.)
39. Document dependency upgrade procedure
40. Audit for abandoned/CVE-bearing dependencies
41. Separate optional vs required deps (requirements.txt vs requirements-dev.txt)
42. Verify SBOM generation in CI (syft); publish as release artifact

### Phase 5: Networking (5 items)

43. Document all exposed ports (purpose, protocol, public/internal)
44. Audit 0.0.0.0 bindings — verify intentional, document rationale
45. Document TLS/HTTPS configuration path (certs, reverse proxy)
46. Document firewall requirements (inbound/outbound)
47. Document DNS dependencies (Telegram API, model APIs, etc.)

### Phase 6: Testing (7 items)

48. 🔴 Verify test suite passes on fresh clone
49. 🔴 Audit skipped tests — every skip must have tracked reason
50. Verify tests don't require internet (all external calls mocked)
51. Coverage audit — verify no `# pragma: no cover` abuse
52. Extend CI to target platforms (add macOS runner to matrix)
53. 🔴 Smoke/acceptance test script (single script validates fresh deployment e2e)
54. Failure mode testing (network loss, service crash, disk full, OOM)

### Phase 7: Documentation (12 items)

55. README: clear purpose statement + demo screenshot/GIF
56. 🔴 Installation guide — every platform, exact version requirements (was #104)
57. 🔴 Quick-start tested in clean environment (fresh macOS + Ubuntu VM)
58. Architecture deep-dive — branded Mermaid diagrams (was #106)
59. Configuration reference — every setting, module, env var (was #105)
60. Security model docs — STPA-Sec, threat model, trust boundaries (was #107)
61. API reference — gateway endpoints, WebSocket protocol (was #108)
62. Runbooks — incident response, key rotation, backup/restore, troubleshooting (was #109)
63. User guide + FAQ (was #110)
64. Whitepaper update with proxy verification results (was #111)
65. 🔴 Docs accuracy audit — remove aspirational/unimplemented features from all docs
66. Prompt injection demo in README — show AgentShroud blocking a real attack

### Phase 8: Operational Readiness (7 items)

67. Observability hooks — structured metrics export (Prometheus-compatible or JSON)
68. Parseable structured log format — JSON with severity, timestamp, component
69. PII scrubbing in application logs (extend pipeline redaction to app logs)
70. 🔴 Startup/shutdown structured events with timestamp and version
71. Version visible at runtime (`/status` returns version from build metadata)
72. Data migration strategy for config/data format changes between versions
73. Backup/restore procedure documented (volume backup, config export, restore)

### Phase 9: Legal & IP (7 items)

74. Verify LICENSE file correct (verify-only)
75. Dependency license compatibility audit (all transitive deps compatible with MIT)
76. Copyright headers in all source files (.py, .js, .sh)
77. NOTICE/ATTRIBUTIONS file for bundled dependencies
78. Asset license audit (images, fonts, icons)
79. USPTO TEAS Plus filing — $250-500 (was #117)
80. Prior use documentation maintained (was #118)

### Phase 10: Community & GitHub Setup (10 items)

81. Issue templates (bug report, feature request, security vulnerability)
82. PR template with contributor checklist
83. CODEOWNERS file — auto-assign reviewers per directory
84. Squash-and-merge policy + auto-delete branches (GitHub settings)
85. Collaborator access: Write only, no Admin (GitHub settings)
86. Maintainer contact in SECURITY.md and README
87. Sustainability/bus-factor note
88. CODE_OF_CONDUCT.md (Contributor Covenant)
89. COLLABORATING.md — trust boundary docs for AgentShroud contributors
90. Review CONTRIBUTING.md completeness (verify-only)

### Phase 11: Command Center — Web (11 items)

91. Branded web dashboard — real API backing, #1583f0/#161c27 palette (was #86)
92. Real-time activity feed — WebSocket, filterable, searchable (was #87)
93. Approval queue UI — one-click approve/deny (was #88)
94. Module control panel — enable/disable, mode toggle, config editor (was #89)
95. Security posture dashboard — risk scores, CVEs, compliance (was #90)
96. Audit trail viewer — searchable, exportable, chain verification (was #91)
97. Agent management — view, kill, restart, logs, cost (was #92)
98. Mobile-responsive PWA (was #93)
99. Authentication — Cookie + TOTP 2FA + Tailscale (was #94)
100. Text-browser compatible — w3m, links2, lynx, elinks (was #95)
101. Progressive enhancement — core works without JS (was #96)

### Phase 12: One-Click Install (5 items)

102. curl installer — `curl -sSL https://install.agentshroud.ai | bash` (was #81)
103. Interactive setup wizard — OS detection, runtime, credentials (was #82)
104. One-click OpenClaw updates from command center (was #83)
105. `agentshroud update` CLI with auto-rollback (was #84)
106. Auto-rollback on failed health check, 60s (was #85)

### Phase 13: Final Hardening + Release (10 items)

107. Red team remediation — all Steve Hay Phases 1-6 findings (was #112)
108. Final peer review — multi-model cold-eye (Claude, Gemini, Codex) (was #114)
109. Support matrix — documented OS/runtime/arch combinations
110. Reproducible build artifacts — deterministic Docker builds
111. Container image tagged + published to GHCR
112. Tag v1.0.0 — GitHub release, full changelog, breaking changes, SHA256 checksums (was #115)
113. agentshroud.ai launch page (was #116)
114. CHANGELOG.md v1.0.0 entry
115. Smoke test on release artifacts (download, install, verify e2e)
116. Update RELEASE-PLAN.md — mark v1.0.0 complete

---

## v1.1.0 "Groups" — Workspaces for Teams (6 items)

*Goal: Group-based project workspaces. Bot joins Telegram groups and Slack channels, silently logs all conversation to group memory, and responds only when @mentioned.*

**Branch:** `feat-v1.1.0-workspaces-for-teams`

**Foundation (already shipped):** `rbac.py` groups, `shared_memory.py`, `tool_acl.py`, `delegation.py`, `privacy_policy.py`, `slack_channel_bridge.py`

1. **Group workspaces** — create groups for projects with isolated workspace per team; per-group memory, egress rules, tool ACLs
2. **Telegram group membership** — bot joins Telegram group chats; all messages logged to group memory regardless of @mention
3. **@mention-only response** — bot only sends a response when explicitly @mentioned; otherwise silently observes
4. **Slack channel membership** — same pattern: join Slack channels, log conversation, respond only on @mention
5. **Group memory isolation** — each group workspace has its own isolated memory context (extends `shared_memory.py` group scoping)
6. **Group-scoped policies** — per-group tool ACLs and egress rules (extends `tool_acl.py`, `EgressScope` `kind="group"`)

---

## v1.2.0 "Local LLMs" — Offline Model Support (4 items)

*Goal: Run AgentShroud without cloud API keys using local models via Ollama, LM Studio, or mlx_lm.*

**Branch:** `feat-v1.2.0-local-llms`

**Status:** 3 commits shipped (Ollama + LM Studio + mlx_lm backends, model routing, tag format fixes).

1. **Ollama backend** — route models through Ollama; colon-tag format (e.g. `qwen3-coder:30`)
2. **LM Studio + mlx_lm backends** — Anchor/Coding (LM Studio) and Reasoning (mlx_lm) profiles
3. **Model switching** — `scripts/switch_model.sh` for runtime model selection
4. **Gateway proxy routing** — all local model traffic routes through AgentShroud gateway pipeline

---

## v1.3.0 — Platform Expansion (53 items)

*Goal: All remaining post-v1.0 deferred items.*

**Branch:** `feat-v1.3.0` (TBD)

### Secure Voice (moved from v0.9.0 on 2026-03-04)
- ElevenLabs Conversational AI — Real-time voice conversations
- Twilio phone number — For phone calls
- Voice injection detection — Prompt injection via voice input
- Call recording/audit — Full logging
- Auth on chatCompletions endpoint (API key or mTLS)
- Rate limiting, IP allowlist, caller allowlist

### Infrastructure (moved from v0.9.0 on 2026-03-04)
- Colima verification — Confirm working end-to-end
- Multi-host test runner — SSH + report aggregation across all hosts

### Multi-Platform Container Support
- Docker Desktop support
- Nix flakes support
- Container runtime abstraction layer (`AGENTSHROUD_RUNTIME` auto-detect)

### Integration Hub
- Top 50 MCP server compatibility matrix
- iCloud MCP (31 tools via Mac Mini)
- Google Workspace MCP, Home Assistant MCP
- GitHub, 1Password, AWS, Docker, Brave Search MCPs
- MCP security policy engine (trust levels, PII rules per MCP)

### Browser Extension
- URL forwarder, page clipper, form fill request, Safari Web Extension wrapper

### iOS/macOS Shortcuts
- Universal share sheet, Siri capture, screenshot-to-agent, clipboard relay, photo forwarder

### Mac Mini Onboarding
- agentshroud-bot macOS account, iCloud MCP, Google Workspace MCP, LaunchAgent services

### Personal Infrastructure Monitor
- Home Assistant, Nessus, Pi-hole monitoring, Synology NAS, backup aggregator, daily brief, alert engine

### Full Configuration System
- YAML/TOML config, web UI editor, integration wizard, alert rules, dashboard builder, notification preferences, backup/restore

### Advanced Integrations
- AWS security audit, financial monitoring, Zabbix, Microsoft 365, productivity dashboard

### Multi-Host Deployment
- Coordinated deploy across Marvin/Trillian/Pi, health check dashboard, ARM32 support

### Security Hardening
- FR1: MFA for sensitive operations (kill switch, SSH) — was deferred from v1.0.0
- FR5: Network DMZ — requires multi-node deployment

### Command Center — CLI/TUI (moved from v1.0.0 on 2026-03-20)
- `agentshroud` CLI — status, logs, approve, deny, kill commands
- TUI dashboard — rich/textual for SSH/tmux sessions
- TUI chat console — Talk to OpenClaw from terminal
- Blink Shell (iPad) compatible

### SSH Chat Interface (moved from v1.0.0 on 2026-03-20)
- SSH-accessible chat — `ssh chat@agentshroud-gateway`
- tmux-friendly, full OpenClaw capability
- Approval notifications inline

---

## Summary

| Version | Codename | Items | Focus | Branch |
|---------|----------|-------|-------|--------|
| v0.8.0 | Watchtower | 104 | Security fixes, module wiring, Steve prep | merged |
| v0.9.0 | Sentinel | 37 | Data isolation, SOC, remediation, iMessage, security tools | merged |
| v1.0.0 | Fortress | 116 | Ship-ready: security audit, repo hygiene, container hardening, docs, dashboard, installer, release | merged |
| v1.1.0 | Groups | 6 | Group workspaces, @mention-only, Telegram/Slack group membership | `feat-v1.1.0-workspaces-for-teams` |
| v1.2.0 | Local LLMs | 4 | Offline model support via Ollama/LM Studio/mlx_lm | `feat-v1.2.0-local-llms` |
| v1.3.0 | Platform | 53 | Voice, CLI/TUI, SSH chat, Apple integration, advanced features | TBD |

**Total tracked: 320 items**

### Key Changes (2026-04-08)
- **Versioned Post-v1.0 backlog:** Replaced unversioned "Post-v1.0.0" bucket with v1.1.0/v1.2.0/v1.3.0 milestones
- **v1.1.0 scope defined:** Group workspaces + @mention-only response (new scope, not previously listed)
- **v1.2.0 scope confirmed:** Local LLM support (3 commits already shipped on branch)
- **v1.3.0:** All 53 original Post-v1.0 items + CHANGELOG MFA/DMZ deferred items

### Key Changes (2026-03-20)
- **Moved to post-v1.0.0:** CLI/TUI (4 items), SSH Chat Interface (3 items)
- **Merged into v1.0.0:** 100-item public release readiness checklist (78 net new after dedup)
- **Reorganized v1.0.0:** 13 execution phases ordered for implementation
- **v1.0.0 item count:** 38 → 116

### Key Changes (2026-03-04 12:16 UTC)
- **Added to v0.9.0:** Private service data isolation (6 items), Security Operations Center (6 items)
- **Moved to post-v1.0.0:** Secure Voice (6 items), Colima verification, Multi-host test runner
