# 🛡️ AgentShroud Release Plan

**Created:** 2026-03-04
**Last Updated:** 2026-03-14
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

## v1.0.0 "Fortress" — Polish + Public Release (38 items)

*Goal: Production-ready, installable, documented, red-team-tested.*

### One-Click Install (5 items)

81. **curl installer** — `curl -sSL https://install.agentshroud.ai | bash`
82. **Interactive setup wizard** — OS detection, runtime check, credential setup.
83. **One-click OpenClaw updates** from command center.
84. **`agentshroud update` CLI** — One-command upgrade with auto-rollback.
85. **Auto-rollback** on failed health check (60s).

### Command Center — Web (11 items)

86. **Branded web dashboard** — Real API backing. Brand palette #1583f0 / #161c27.
87. **Real-time activity feed** — WebSocket, filterable, searchable.
88. **Approval queue UI** — One-click approve/deny.
89. **Module control panel** — Enable/disable, mode toggle, config editor.
90. **Security posture dashboard** — Risk scores, CVEs, compliance status.
91. **Audit trail viewer** — Searchable, exportable, chain verification.
92. **Agent management** — View, kill, restart, logs, cost.
93. **Mobile-responsive PWA** — Works on iPhone/iPad.
94. **Authentication** — Cookie + TOTP 2FA + Tailscale.
95. **Text-browser compatible** — w3m, links2, lynx, elinks.
96. **Progressive enhancement** — Core works without JS.

### Command Center — CLI/TUI (4 items)

97. **`agentshroud` CLI** — status, logs, approve, deny, kill commands.
98. **TUI dashboard** — rich/textual for SSH/tmux sessions.
99. **TUI chat console** — Talk to OpenClaw from terminal.
100. **Blink Shell (iPad) compatible**.

### SSH Chat Interface (3 items)

101. **SSH-accessible chat** — `ssh chat@agentshroud-gateway`.
102. **tmux-friendly**, full OpenClaw capability.
103. **Approval notifications inline**.

### Documentation (8 items)

104. **Installation guide** — Every platform (macOS, Linux, Docker, Podman, Colima, Apple Containers).
105. **Configuration reference** — Every setting, every module.
106. **Architecture deep-dive** — Branded Mermaid diagrams.
107. **Security model docs** — STPA-Sec, threat model, trust model.
108. **API reference** — Gateway endpoints, WebSocket protocol.
109. **Runbooks** — Incident response, key rotation, backup/restore.
110. **User guide + FAQ** — First 30 minutes, common tasks.
111. **Whitepaper update** with proxy verification results.

### Final Hardening + Release (5 items)

112. **Red team remediation** — All Steve Hay findings from Phases 1-6.
113. **Token rotation** — All tokens/secrets rotated to production values.
114. **Final peer review** — Multi-model (Claude, Gemini, Codex).
115. **Tag v1.0.0** — GitHub release with full changelog.
116. **agentshroud.ai launch page** — Branded, functional.

### Trademark / IP (2 items)

117. **File USPTO application** — TEAS Plus ($250-500).
118. **Prior use documentation** maintained.

---

## Post-v1.0.0 — Deferred (53 items)

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

---

## Summary

| Version | Codename | Items | Focus |
|---------|----------|-------|-------|
| v0.8.0 | Watchtower | 104 | Security fixes, module wiring, Steve prep |
| v0.9.0 | Sentinel | 37 | **Data isolation, SOC**, remediation, iMessage, security tools |
| v1.0.0 | Fortress | 38 | Polish, install, docs, release |
| Post-v1 | — | 53 | Voice, integrations, advanced features |

**Total tracked: 232 items**

### Key Changes (2026-03-04 12:16 UTC)
- **Added to v0.9.0:** Private service data isolation (6 items), Security Operations Center (6 items)
- **Moved to post-v1.0.0:** Secure Voice (6 items), Colima verification, Multi-host test runner
