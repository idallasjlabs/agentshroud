# 🛡️ AgentShroud Release Plan

**Created:** 2026-03-04
**Source:** Full chat history audit (2,919 messages, Feb 20 – Mar 4)
**Related:** MASTER-FEATURE-LIST.md (206 items total with post-v1.0)

---

## v0.8.0 "Watchtower" — Security Fixes + Quick Wins (41 items)

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
37. **Refactor main script into modules** — Main gateway/startup script is unwieldy. Split into separate files by concern: startup/init, security pipeline, middleware chain, proxy routes, config loading, credential management, notification system. Each file independently testable.

### 📊 Exit Criteria (5 items)

37. **E2E test suite** — 10 scenarios: PII, injection, approval, audit chain, bypass, kill switch, egress, trust, response scan, chain integrity.
38. **Canary system** — Hourly fake PII message + verification.
39. **Zero defects** — 0 errors, 0 warnings, 0 skipped tests.
40. **Internal blue team** — Passes 100% (all modules enforcing).
41. **Module audit** — All modules confirmed in enforce mode, not monitor.

---

## v0.9.0 "Sentinel" — Blue Team Remediation + Integrations (27 items)

*Goal: Fix Steve's findings, add iMessage/voice, full security tooling.*

### Steve Hay Remediation
42. **Triage + fix all findings** from Steve's blue team test.
43. **Automated key rotation** — Zero-downtime. Steve Tier 3: R-22.
44. **Progressive trust activation** — Graduated permissions based on behavior. Steve Tier 3: R-23.
45. **Red team preparation** — Prep for Phases 1-6.

### Apple Messages
46. **iMessage activation** — agentshroud.ai@icloud.com on Marvin.
47. **GUI sign-in** — One-time physical access by Isaiah for agentshroud-bot user.
48. **Messages relay daemon** — launchd + AppleScript on Marvin.
49. **Chris Shelton routing** — His Telegram is deactivated (403), needs iMessage route.

### Secure Voice
50. **ElevenLabs Conversational AI** — Real-time voice conversations.
51. **Twilio phone number** — For phone calls.
52. **Voice injection detection** — Prompt injection via voice input.
53. **Call recording/audit** — Full logging.

### Security Tools (Full Integration, Not Stubs)
54. **Wazuh** — Full agent, real-time alerting, dashboard integration.
55. **Trivy** — Container scanning on every rebuild, CVE dashboard.
56. **ClamAV** — File scanning on uploads/downloads.
57. **OpenSCAP** — CIS Docker Benchmark, compliance reports.
58. **Unified security dashboard** — All scanners in one view.

### Infrastructure
59. **Podman support** — Fix Pi (requires Podman 4.x, current 3.0.1 too old).
60. **Apple Containers** — macOS Tahoe support.
61. **Colima verification** — Confirm working end-to-end.
62. **Multi-host test runner** — SSH + report aggregation across all hosts.
63. **Dynamic Tailscale IP resolution** — Sidecar that resolves hostnames, eliminates IP pinning.
64. **Port scanner for test instances** — Find available ports + Tailscale serve setup.
65. **Multi-language support planning** — Languages supported by OpenClaw/Claude.

### Multi-Agent Architecture
66. **Peer-to-peer leadership protocol** — Any bot can lead or follow, no fixed hierarchy.
67. **Cross-instance gateway communication** — Instances call each other's gateways.
68. **Leader/follower handoff** — Owner assigns/revokes leadership mid-conversation.

---

## v1.0.0 "Fortress" — Polish + Public Release (25 items)

*Goal: Production-ready, installable, documented, red-team-tested.*

### One-Click Install
69. **curl installer** — `curl -sSL https://install.agentshroud.ai | bash`
70. **Interactive setup wizard** — OS detection, runtime check, credential setup.
71. **`agentshroud update` CLI** — One-command upgrade with auto-rollback on failed health check.

### Command Center (Web)
72. **Branded web dashboard** — Real API backing, not hardcoded data. Brand palette #1583f0 / #161c27.
73. **Approval queue UI** — One-click approve/deny.
74. **Module control panel** — Enable/disable, mode toggle, config editor.
75. **Security posture dashboard** — Risk scores, CVEs, compliance status.
76. **Mobile-responsive PWA** — Works on iPhone/iPad.
77. **Text-browser compatible** — w3m, links2, lynx, elinks.
78. **Authentication** — Cookie + TOTP 2FA + Tailscale.

### CLI/TUI
79. **`agentshroud` CLI** — status, logs, approve, deny, kill commands.
80. **TUI dashboard** — rich/textual for SSH/tmux sessions.
81. **TUI chat console** — Talk to OpenClaw from terminal.
82. **SSH chat interface** — `ssh chat@agentshroud-gateway`.

### Documentation
83. **Installation guide** — Every platform (macOS, Linux, Docker, Podman, Colima, Apple Containers).
84. **Architecture deep-dive** — Branded Mermaid diagrams.
85. **Security model docs** — STPA-Sec, threat model, trust model.
86. **API reference** — Gateway endpoints, WebSocket protocol.
87. **User guide + FAQ** — First 30 minutes, common tasks.

### Release
88. **Red team remediation** — All Steve Hay findings from Phases 1-6.
89. **Token rotation** — All tokens/secrets rotated to production values.
90. **Final peer review** — Multi-model (Claude, Gemini, Codex).
91. **Tag v1.0.0** — GitHub release with full changelog.
92. **agentshroud.ai launch page** — Branded, functional.
93. **USPTO trademark filing** — TEAS Plus application ($250-500).

---

## Post-v1.0.0 — Deferred (100+ items)

See `MASTER-FEATURE-LIST.md` for full details:
- Integration Hub (Top 50 MCP servers)
- Browser Extension (URL forwarder, page clipper)
- iOS/macOS Shortcuts (Siri, share sheet, clipboard relay)
- Mac Mini Onboarding (iCloud MCP, Google Workspace)
- Personal Infrastructure Monitor (Home Assistant, Nessus, Pi-hole, NAS)
- Security Operations Center (unified dashboard, CVE tracking, compliance)
- Full Configuration System (YAML/TOML, web editor, alert rules)
- Advanced Integrations (AWS, financial, Zabbix, M365)
- Multi-Host Deployment (coordinated deploy, health checks)

---

## Summary

| Version | Codename | Items | Focus |
|---------|----------|-------|-------|
| v0.8.0 | Watchtower | 41 | Security fixes, Steve prep |
| v0.9.0 | Sentinel | 27 | Remediation, iMessage, voice |
| v1.0.0 | Fortress | 25 | Polish, install, docs, release |
| Post-v1 | — | 100+ | Integrations, advanced features |

**Total tracked: 206 items**
