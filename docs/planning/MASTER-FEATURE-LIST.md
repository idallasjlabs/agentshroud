# AgentShroud — Master Feature List (Everything Ever Mentioned)

**Compiled:** 2026-03-04 (updated 12:16 UTC)
**Sources:** All memory files (Feb 16-27, Mar 3-4), planning docs, roadmap (Phases 1-19), Steve Hay assessment/plan, daily logs, code review, RECOVERY_PLAN, PLAN-RESET, regression tests, peer reviews

**Legend:** ✅ Done | 🔧 In Progress | 📋 Planned | 🧊 Deferred

---

## v0.8.0 — "Watchtower" (Complete Security + Everything We Know Today)

### A. Steve Hay — ALL Tiers (14 features, 23 requirements)

**Tier 1 — Deployment Blockers:**
1. 📋 Enforce-by-default for core modules (R-02, R-03)
2. 📋 Outbound information filtering (R-01) — new module
3. 📋 Per-user session isolation (R-04, R-05) — new module
4. 📋 Separation of privilege (R-06, R-07)
5. 📋 Human-in-the-loop for high-risk tool calls (R-08, R-09)
6. 📋 Credential isolation (R-10, R-11, R-12) — remove secrets from bot

**Tier 2 — Compliance:**
7. 📋 Per-user RBAC at MCP Proxy (R-13)
8. 📋 Compliance-ready audit export CEF/JSON-LD (R-14)
9. 📋 Kill switch verification — automated, <1s FREEZE, <5s SHUTDOWN (R-15, R-16)
10. 📋 PII scanning on MCP tool results (R-17)
11. 📋 Memory lifecycle — retention, integrity checks (R-18, R-19)
12. 📋 Network scope enforcement — egress enforce, SSRF hard blocks (R-20, R-21)

**Tier 3 — Operational Maturity:**
13. 📋 Automated key rotation — zero-downtime (R-22)
14. 📋 Progressive trust activation — graduated permissions (R-23)

### B. Wire ALL Modules Into Request Path
15. 📋 DNSFilter → egress path
16. 📋 DriftDetector → periodic + startup
17. 📋 EgressMonitor → outbound requests (slow-drip detection)
18. 📋 KeyRotationManager → credential lifecycle
19. 📋 MultiTurnTracker → inbound messages (crescendo attacks)
20. 📋 NetworkValidator → startup + periodic
21. 📋 OutputCanary → outbound responses
22. 📋 PathIsolationManager → file operations
23. 📋 ToolChainAnalyzer → tool call path
24. 📋 EnhancedToolResultSanitizer → tool result path
25. 📋 BrowserSecurityGuard → web fetch path
26. 📋 OAuthSecurityValidator → auth flow
27. 📋 ApprovalHardening → approval queue
28. 📋 CredentialInjector → egress path (transparent server-side injection)

### C. Bug Fixes
29. 📋 ContextGuard `should_block_message()` always returns False
30. 📋 GitGuard is a no-op (logs only)
31. 📋 FileSandbox false positives blocking owner messages (regex + no admin bypass)
32. 📋 Anthropic API bypasses gateway (SDK patch not working)
33. 📋 Op-proxy vault name mismatch ("Agent Shroud" vs "AgentShroud")
34. 📋 Egress allowlist missing `*.1password.com` (blocks op-proxy from inside gateway)
35. 📋 Telegram CONNECT proxy tunnel intermittent failures
36. 📋 `final/network-lockdown` branch is DESTRUCTIVE — delete or rebase (deletes 12k+ lines)
37. 📋 Pi deploy blocked: Podman 3.0.1 too old, no sudo
38. 📋 Production instance (Docker Desktop) inaccessible from agentshroud-bot user

### D. Interactive Egress Firewall ("Little Snitch for Agents")
39. 📋 All outbound traffic requires explicit approval
40. 📋 Telegram inline keyboard: Allow always / Allow once / Deny
41. 📋 Persistent allowlist in egress_rules.json
42. 📋 Risk assessment heuristic (green/yellow/red)
43. 📋 Dashboard live connection log
44. 📋 Emergency "block all" button
45. 📋 Connection timeout (default 30s)

### E. Observatory Mode (Global Monitor/Enforce Switch)
46. 📋 `AGENTSHROUD_GLOBAL_MODE=monitor|enforce` env var
47. 📋 `/manage/mode` API endpoint (GET/SET)
48. 📋 Per-module pin overrides (keep killswitch enforcing in monitor mode)
49. 📋 Auto-revert timer (safety net back to enforce)
50. 📋 Dashboard + TUI mode indicators
51. 📋 All would-block events tagged [MONITOR]

### F. Prompt Injection Hardening
52. 📋 Fix ContextGuard enforcement (should_block_message)
53. 📋 Expand PromptGuard — 20+ new patterns
54. 📋 Multilingual injection defense — 35+ languages
55. 📋 Input normalization (NFKC, zero-width strip, HTML decode, URL decode, base64 detect)
56. 📋 Cross-turn correlation (MultiTurnTracker — crescendo attacks)
57. 📋 Tool result sanitization (strip markdown image/link injection)
58. 📋 Output canary system (invisible tokens detect prompt leakage)
59. 📋 ML-based injection classifier (stretch — DistilBERT for uncertain zone, ~20h)

### G. Encrypted Container-to-Container Communication
60. 📋 mTLS via step-ca (internal CA)
61. 📋 All gateway ↔ bot traffic encrypted
62. 📋 All gateway ↔ external service traffic encrypted
63. 📋 Certificate rotation automated
64. 📋 Verify zero plaintext (tcpdump)

### H. Pi-hole as Default Stack Component
65. 📋 Pi-hole container in default docker-compose
66. 📋 All containers use Pi-hole as DNS
67. 📋 Default blocklists (Steven Black, OISD, Phishing Army, Malware Domains)
68. 📋 AgentShroud custom threat intel blocklist
69. 📋 Auto-update cron for blocklists
70. 📋 Web console DNS security page (novice + advanced views)
71. 📋 `/manage/dns` API endpoint
72. 📋 Query logs → AuditStore integration
73. 📋 Dual-layer enforcement: Pi-hole DNS + proxy egress

### I. Enhanced Audit & Compliance
74. 📋 SIEM-compatible log format (CEF, JSON-LD)
75. 📋 Real-time audit event streaming via WebSocket
76. 📋 Compliance report generator (SOC 2 mapping)
77. 📋 Tamper-evident audit log with hash chains (exists, verify working)
78. 📋 Export to external SIEM (Splunk, ELK, Wazuh)

### J. Phase 8.5 E2E Verification
79. 📋 10-scenario E2E test suite (PII, injection, approval, audit, bypass, kill, egress, trust, response scan, chain integrity)
80. 📋 Canary system — hourly fake PII message + verification
81. 📋 Smoke test dashboard indicators
82. 📋 Verification scripts (verify-proxy.sh — full, quick, canary, chain, bypass)

### K. Merge Pending PRs / Code Cleanup
83. 📋 Merge Phases 9, 10, 11 (pending merge since Feb 18)
84. 📋 Fix workspace file ownership (UID 14664 → 1000)
85. 📋 SSH key persistence across container rebuilds (mount as volume/secret)
86. 📋 Clean up stale branches
87. 📋 Refactor main script into modules — Split by concern: startup/init, security pipeline, middleware chain, proxy routes, config loading, credential management, notification system. Each file independently testable.

### L. Multi-Agent Architecture
88. 📋 Peer-to-peer leadership protocol (any bot can lead or follow)
89. 📋 Leader mode: orchestrate chat groups, delegate to followers
90. 📋 Follower mode: receive instructions, return results
91. 📋 Handoff: owner assigns/revokes leadership
92. 📋 Cross-instance gateway communication

### M. Misc Quick Wins
93. 📋 Fix startup/shutdown messages — Format: `agentshroud-bot@hostname` not `[production]`
94. 📋 Fix chat-console — Python syntax error in `chat_console.py` line 59
95. 📋 Fix start-control-center script — Not found / broken
96. 📋 Fix workspace file ownership — uid 14664 → node (from backup restore)
97. 📋 Collaborator interaction logs — Persist forever, never delete
98. 📋 Bot config protection — Cannot change any configuration unless directed by admin from communication channel
99. 📋 Replace GitHub PAT — Switch to fine-grained token
100. 📋 Delete destructive branch — `final/network-lockdown` deletes 12k+ lines, block via GitHub workflow
101. 📋 Copyright/trademark — Add to all appropriate files
102. 📋 Merge pending PRs — Phases 9, 10, 11 branches (pending since Feb 18)
103. 📋 Org chart — Agile team structure: Isaiah = PO, AgentShroud bot = Scrum Master, Claude Code = Engineers, Gemini/Codex = QA
104. 📋 Quarantine blocked messages instead of discarding — Admin messages blocked by security pipeline should be queued for review, not silently destroyed. Admin can review and release via Telegram inline buttons or dashboard.

---

## v0.9.0 — "Sentinel" (Blue Team Remediation + Data Isolation + SOC)

### A. Private Service Data Isolation
105. 📋 **Tool-level access control** — Collaborators cannot invoke tools that access admin-only services (Gmail, Home Assistant, iCloud, financial, etc.)
106. 📋 **Response filtering** — Admin-private data never leaks into collaborator sessions; if a tool result contains admin-private data, it's stripped/blocked
107. 📋 **Memory isolation hardening** — Admin-private data in memory files inaccessible to collaborator sessions. Gap found Feb 26: collaborators could `memory_search` and read `MEMORY.md`. Needs enforcement.
108. 📋 **Prompt injection defense for data isolation** — Collaborator cannot trick the bot into revealing admin data via indirect prompts
109. 📋 **Audit + alerting for private data access** — All access attempts to admin-private services logged and alerted
110. 📋 **Privacy policy file** — Admin defines which services are "private" vs "shared" in a clear config file

### B. Security Operations Center (SOC)
111. 📋 **Unified security dashboard** — Single pane of glass for all security events
112. 📋 **OpenClaw upstream CVE tracking** — Monitor for vulnerabilities in OpenClaw itself
113. 📋 **ClawHub skill vetting** — 26% of skills have vulnerabilities; automated scanning
114. 📋 **Network security correlation** — Cross-reference DNS, egress, and audit events
115. 📋 **Compliance reporting** — IEC 62443 and other frameworks
116. 📋 **Incident response automation** — Playbooks for common security events

### C. Steve Hay Remediation
117. 📋 Triage + fix all findings from Steve's blue team test
118. 📋 Automated key rotation — Zero-downtime. Steve Tier 3: R-22
119. 📋 Progressive trust activation — Graduated permissions based on behavior. Steve Tier 3: R-23
120. 📋 Red team preparation — Prep for Phases 1-6

### D. Apple Messages Integration
121. 📋 iMessage activation — agentshroud.ai@icloud.com on Marvin
122. 📋 GUI sign-in — One-time physical access by Isaiah for agentshroud-bot user
123. 📋 Messages relay daemon — launchd + AppleScript on Marvin
124. 📋 Chris Shelton routing — His Telegram is deactivated (403), needs iMessage route

### E. Security Tools (Full Integration, Not Stubs)
125. 📋 Wazuh — Full agent, real-time alerting, dashboard integration
126. 📋 Trivy — Container scanning on every rebuild, CVE dashboard
127. 📋 ClamAV — File scanning on uploads/downloads
128. 📋 OpenSCAP — CIS Docker Benchmark, compliance reports
129. 📋 Unified security scanner dashboard — All scanners in one view

### F. Infrastructure
130. 📋 Podman support — Fix Pi (requires Podman 4.x, current 3.0.1 too old)
131. 📋 Apple Containers — macOS Tahoe support
132. 📋 Dynamic Tailscale IP resolution — Sidecar that resolves hostnames, eliminates IP pinning
133. 📋 Port scanner for test instances — Find available ports + Tailscale serve setup
134. 📋 Multi-language support planning — Languages supported by OpenClaw/Claude

### G. Multi-Agent Architecture
135. 📋 Peer-to-peer leadership protocol — Any bot can lead or follow, no fixed hierarchy
136. 📋 Cross-instance gateway communication — Instances call each other's gateways
137. 📋 Leader/follower handoff — Owner assigns/revokes leadership mid-conversation

### H. Development Infrastructure
138. 📋 direnv + Nix for reproducible dev environment
139. 📋 Dependency management framework (GSD or equivalent)
140. 📋 Orchestration framework for multi-agent development
141. 📋 MCP integration with Lucy (compliance orchestration)

---

## v1.0.0 — "Fortress" (Polish + Public Release)

### A. One-Click Install & Updates
142. 📋 `curl -sSL https://install.agentshroud.ai | bash`
143. 📋 Interactive setup wizard (OS detection, runtime check)
144. 📋 One-click OpenClaw updates from command center
145. 📋 `agentshroud update` CLI + rollback
146. 📋 Auto-rollback on failed health check (60s)

### B. Professional Branded Web Command Center
147. 📋 Complete redesign (brand palette #1583f0 / #161c27)
148. 📋 Real-time activity feed (WebSocket, filterable, searchable)
149. 📋 Approval queue UI (one-click approve/deny)
150. 📋 Module control panel (enable/disable, mode toggle, config editor)
151. 📋 Security posture dashboard (risk scores, CVEs, compliance)
152. 📋 Audit trail viewer (searchable, exportable, chain verification)
153. 📋 Agent management (view, kill, restart, logs, cost)
154. 📋 Mobile-responsive PWA
155. 📋 Authentication (cookie + TOTP 2FA + Tailscale)
156. 📋 Text-browser compatible (w3m, links2, lynx, elinks)
157. 📋 Progressive enhancement (core works without JS)

### C. Text/CLI Command Center
158. 📋 `agentshroud status/logs/approve/deny/kill` CLI commands
159. 📋 TUI dashboard (rich/textual) for SSH/tmux sessions
160. 📋 TUI chat console — talk to OpenClaw from terminal
161. 📋 Blink Shell (iPad) compatible

### D. SSH Chat Interface
162. 📋 SSH-accessible chat (`ssh chat@agentshroud-gateway`)
163. 📋 tmux-friendly, full OpenClaw capability
164. 📋 Approval notifications inline

### E. Full Documentation
165. 📋 Installation guide (every platform)
166. 📋 Configuration reference (every setting, every module)
167. 📋 Architecture deep-dive (branded Mermaid diagrams)
168. 📋 Security model docs (STPA-Sec, threat model, trust model)
169. 📋 API reference (gateway endpoints, WebSocket protocol)
170. 📋 Runbooks (incident response, key rotation, backup/restore)
171. 📋 User guide (first 30 minutes, common tasks, FAQ)
172. 📋 Whitepaper update with proxy verification results

### F. Final Hardening + Release
173. 📋 Red team remediation (Steve Hay Phases 1-6)
174. 📋 All tokens rotated to production values
175. 📋 Final peer review (multi-model)
176. 📋 Tag v1.0.0, GitHub release
177. 📋 agentshroud.ai website launch page

### G. Trademark / IP
178. 📋 File USPTO application (TEAS Plus, $250-500)
179. 📋 Prior use documentation maintained

---

## Post-v1.0.0 — Deferred

### Secure Voice (moved from v0.9.0 → post-v1.0.0 on 2026-03-04)
180. 🧊 ElevenLabs Conversational AI — Real-time voice conversations
181. 🧊 Twilio phone number — For phone calls
182. 🧊 Voice injection detection — Prompt injection via voice input
183. 🧊 Call recording/audit — Full logging
184. 🧊 Auth on chatCompletions endpoint (API key or mTLS)
185. 🧊 Rate limiting, IP allowlist, caller allowlist

### Infrastructure — Deferred (moved from v0.9.0 → post-v1.0.0 on 2026-03-04)
186. 🧊 Colima verification — Confirm working end-to-end
187. 🧊 Multi-host test runner — SSH + report aggregation across all hosts

### Multi-Platform Container Support
188. 🧊 Colima support (current — verify)
189. 🧊 Docker Desktop support
190. 🧊 Nix flakes support
191. 🧊 Container runtime abstraction layer (`AGENTSHROUD_RUNTIME` auto-detect)

### Integration Hub (Phase 13)
192. 🧊 Top 50 MCP server compatibility matrix
193. 🧊 iCloud MCP (31 tools via Mac Mini)
194. 🧊 Google Workspace MCP
195. 🧊 Home Assistant MCP
196. 🧊 GitHub, 1Password, AWS, Docker, Brave Search MCPs
197. 🧊 MCP security policy engine (trust levels, PII rules per MCP)

### Browser Extension
198. 🧊 URL forwarder (toolbar button + right-click)
199. 🧊 Page clipper (Readability-style extraction)
200. 🧊 Form fill request (reverse flow)
201. 🧊 Safari Web Extension wrapper

### iOS/macOS Shortcuts
202. 🧊 Universal share sheet shortcut
203. 🧊 Voice capture ("Hey Siri, send to AgentShroud")
204. 🧊 Screenshot-to-agent (on-device OCR, strips status bar)
205. 🧊 Clipboard relay (macOS menu bar)
206. 🧊 Photo forwarder (batch, EXIF stripped)

### Mac Mini Onboarding (Phase 14)
207. 🧊 agentshroud-bot macOS account setup
208. 🧊 iCloud MCP local mode
209. 🧊 Google Workspace MCP
210. 🧊 LaunchAgent background services

### Personal Infrastructure Monitor (Phase 15)
211. 🧊 Home Assistant integration
212. 🧊 Nessus integration (CRITICAL + HIGH reports)
213. 🧊 Pi-hole monitoring (DNS health + anomalies)
214. 🧊 Synology NAS monitoring
215. 🧊 Backup aggregator (CCC, CrashPlan, Time Machine, NAS)
216. 🧊 Daily morning brief
217. 🧊 Alert engine (priority, quiet hours, dedup)

### Full Configuration System (Phase 18)
218. 🧊 YAML/TOML config with hot-reload
219. 🧊 Web UI config editor with validation
220. 🧊 Integration wizard (OAuth flows)
221. 🧊 Alert rules engine (IF condition THEN action)
222. 🧊 Dashboard builder (drag-and-drop)
223. 🧊 Notification preferences (per-channel, quiet hours)
224. 🧊 Backup & restore

### Advanced Integrations (Phase 19)
225. 🧊 AWS security audit (open ports, public S3, IAM, cost)
226. 🧊 Financial monitoring (Banktivity, Fidelity)
227. 🧊 Zabbix personal infrastructure
228. 🧊 Microsoft 365 (calendar, email, Teams)
229. 🧊 Productivity dashboard (Todoist, calendars, inbox zero)

### Multi-Host Deployment
230. 🧊 Coordinated deployment across Marvin/Trillian/Pi
231. 🧊 Health check dashboard for all hosts
232. 🧊 ARM32 / low-resource support (Pi 3B+, 1GB RAM)

---

## Apple Reminders — Items Recovered

### SecureClaw Tasks (all overdue, added to v0.8.0):
- !!!! AWS access key detection pattern (#added to v0.8.0 bugs)
- !! Persist approval queue to SQLite (#added to v0.8.0 bugs)
- !!! Install 1Password CLI on Pi (#added to v0.9.0 infra)
- !!! Replace GitHub PAT with fine-grained token (#added to v0.8.0 security)
- ! Presidio test coverage → 90%+ (#added to v0.8.0 verification)
- ! WebSocket tests → 80%+ (#added to v0.8.0 verification)

### AgentShroud Shared Tasks:
- Review IEEE paper draft (✅ completed — paper written in IEEE format)
- Deploy AgentShroud to Trillian (🔧 in progress — building now)
- Set up iMessage relay under admin account (📋 in v0.9.0)

## Collaborators
- Brett Galura (8506022825) — needs to message @agentshroud_bot (was on old bot)
- Chris Shelton (8545356403) — Telegram deactivated (403), needs iMessage route
- Gabriel (15712621992)
- Steve Hay (8279589982) — red team assessor, STPA-Sec methodology
- TJ Winter (8526379012) — added 2026-02-22

## Infrastructure
- Marvin: 192.168.7.137 (Mac, Colima, primary dev)
- Trillian: 192.168.7.97 (Mac, x86_64)
- Raspberry Pi: 192.168.7.25 (Debian 11, arm64, Podman 3.0.1 too old)
- Repo: github.com/idallasj/agentshroud
- Current branch: main (HEAD: b6e3622)
- 1987 tests passing (as of Feb 27)
- Domains secured: agentshroud.ai, .com, .net

---

## Summary

| Version | Codename | Items | Focus |
|---------|----------|-------|-------|
| v0.8.0 | Watchtower | 104 | Security fixes, module wiring, Steve prep |
| v0.9.0 | Sentinel | 37 | Data isolation, SOC, remediation, iMessage, security tools |
| v1.0.0 | Fortress | 38 | Polish, install, docs, release |
| Post-v1 | — | 53 | Voice, integrations, advanced features |

**Total tracked: 232 items**
