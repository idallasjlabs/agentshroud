# AgentShroud v0.8.0 — 25-Domain Prompt Injection Defense Assessment & Roadmap

## Context

AgentShroud has 65+ security modules across 7 defense layers, all in enforce mode, with 2,286 passing tests. Steve Hay's STPA-Sec assessment (Feb 2026) found 0% effective enforcement against vanilla OpenClaw. The v0.8.0 hardening branch closed all 6 Tier 1 deployment blockers and wired the SecurityPipeline into the Telegram message path. This assessment audits the current codebase against a comprehensive 25-domain prompt injection defense framework to identify remaining gaps before the next blue team assessment and the v1.0 release.

---

## DELIVERABLE 1 — Domain-by-Domain Assessment

### Domain 1 — Threat Modeling and Security Boundaries
**Status:** PARTIAL
**Coverage:** 7 ADRs define trust zones (ADR-001 proxy model, ADR-003 network isolation, ADR-004 credential isolation). STPA-Sec methodology used in Steve Hay assessment. 17 UCAs identified across 4 loss categories. Named trust zones exist: user input (inbound pipeline), tool output (ToolResultInjectionScanner), agent responses (outbound pipeline), external content (EgressFilter), memory (DriftDetector).
**Gaps:** No formal threat model document covering all 25 domains. Long-horizon multi-step attacks not modeled. Cross-agent laundering not addressed (only 1 bot currently). No attack tree or STRIDE model maintained in docs.
**Risk:** MEDIUM

### Domain 2 — Instruction / Data Separation
**Status:** PARTIAL
**Coverage:** Pipeline separates processing by step (PromptGuard on raw input, PII on sanitized, trust check on action). Bot's SOUL.md provides system-level instructions separated from user input. `apply-patches.js` configures distinct agent personalities (main vs collaborator).
**Gaps:** No structural tagging of content by trust level or source within the pipeline. Messages are strings, not typed objects with provenance metadata. Tool results re-enter the LLM context without source labels.
**Risk:** HIGH

### Domain 3 — Taint Tracking and Data Lineage
**Status:** GAP
**Coverage:** AuditChain records message hashes per direction. PipelineResult tracks which checks ran and what was redacted. CollaboratorTracker logs per-user activity.
**Gaps:** No token-level or chunk-level taint tracking. No way to determine which tool result influenced which output tokens. No taint propagation through LLM reasoning. Trust boundaries are implicit in pipeline step ordering, not explicit metadata.
**Risk:** HIGH

### Domain 4 — Capability Security and Least Privilege
**Status:** IMPLEMENTED
**Coverage:** ADR-004 (API keys never in agent container). KeyVault with per-agent scoping. Docker secrets gateway-only. Bot tool deny list (20+ tools blocked for collaborators). `workspaceOnly=true`. read_only rootfs, cap_drop ALL, no-new-privileges. Per-agent egress policies via BotConfig.egress_domains. TrustManager gates actions by trust level.
**Gaps:** KeyRotation EXPERIMENTAL and not wired at startup. No per-task credential scoping (credentials are per-agent, not per-request).
**Risk:** LOW

### Domain 5 — Tool-Call Governance
**Status:** IMPLEMENTED
**Coverage:** MCPProxy (permissions + inspector + audit, enforce mode). ApprovalQueue (SQLite, tool risk tiers: low/med/high/critical, Telegram inline buttons). ToolChainAnalyzer (recon-exec-exfil pattern detection). FileSandbox (path enforcement). SubagentMonitor (concurrency limits). Tool deny list in apply-patches.js. Rate limiting on collaborators (20/hr).
**Gaps:** No dry-run mode for tool calls. No justification fields. No replay protection (same tool call could be submitted twice). MCP tool parameters validated by schema but not by semantic policy.
**Risk:** LOW

### Domain 6 — Egress Control and Exfiltration Resistance
**Status:** IMPLEMENTED
**Coverage:** EgressFilter (default-deny domain allowlist, per-agent policies, SSRF blocking for RFC1918/loopback/link-local). HTTPConnectProxy (port 8181). DNSBlocklist (StevenBlack+Hagezi). DNSFilter (tunneling detection). InputNormalizer strips markdown image exfil links. Bot routes all traffic via HTTP_PROXY=gateway:8181. 3-network Docker isolation. OutboundInfoFilter blocks credential/infrastructure patterns. EncodingDetector catches base64/hex/rot13 encoded exfil.
**Gaps:** HTTPS payload inspection impossible through CONNECT tunnel. No DLP-style content classification on allowed-domain traffic. Timing-based covert channels not addressed.
**Risk:** LOW

### Domain 7 — Retrieval and RAG Hardening
**Status:** GAP
**Coverage:** No RAG system currently in use. Web content scanning exists in WebContentScanner (prompt injection detection in fetched pages). ToolResultInjectionScanner checks tool outputs.
**Gaps:** No retrieval pipeline exists to harden. When/if RAG is added, no trust-tiered ranking, quarantine, or provenance checking infrastructure exists. Tool results from web fetches enter context without "untrusted" labels.
**Risk:** MEDIUM (no RAG = reduced attack surface, but web fetch results are untagged)

### Domain 8 — Memory Hardening
**Status:** PARTIAL → **IMPLEMENTED** (v0.8.0)
**Coverage:** MemoryIntegrityMonitor (SHA-256 file integrity, inode ctime attribution) and MemoryLifecycleManager (retention policies, PII/injection scanning on writes) are **fully implemented**. DriftDetector wired and running. EncryptedStore (AES-256-GCM) for data at rest.
**v0.8.0 fix:** MemoryIntegrityMonitor and MemoryLifecycleManager are now started in lifespan.py after DriftDetector initialization. Both modules appear in startup logs. Hash baseline established on startup.
**Gaps:** Memory files can still be modified between periodic scans (scan interval: 5 min). No real-time inotify/fsevents file watcher.
**Risk:** MEDIUM (reduced from HIGH)

### Domain 9 — Multi-Agent Trust Architecture
**Status:** IMPLEMENTED
**Coverage:** AgentRegistry with shared-nothing verification at startup. IsolationVerifier checks network/volume/security isolation. BotConfig per-agent. Per-agent egress policies. Bot tool deny list separates main vs collaborator agent capabilities. SubagentMonitor with concurrency limits and trust-gated tool access.
**Gaps:** Only 1 bot currently deployed (OpenClaw) — multi-agent isolation is verified structurally but not battle-tested. Sub-agent output is trusted once it passes pipeline. No adversarial reviewer agent.
**Risk:** LOW

### Domain 10 — Human Approval Design
**Status:** IMPLEMENTED
**Coverage:** EnhancedApprovalQueue (SQLite, tool risk tiers, Telegram inline approve/deny buttons, auto-deny timeout). ApprovalHardening. EgressTelegramNotifier (inline keyboard for unknown domains). Approval callbacks handled in telegram_proxy.py.
**Gaps:** No approval escalation chains (single approver: owner). No structured diff display in Telegram approval messages. Approval fatigue risk — no smart batching or risk-based filtering of approval requests.
**Risk:** MEDIUM

### Domain 11 — Prompt and Policy Hardening
**Status:** IMPLEMENTED
**Coverage:** SOUL.md defines identity constraints. PromptGuard patterns for prompt_extraction and prompt_leak. PromptProtection (fuzzy matching of system prompt content, blocks at risk_score>100). OutboundInfoFilter blocks architecture/infrastructure disclosure. Bot explicitly instructed to never disclose module names, paths, code, hostnames, credentials.
**Gaps:** Policies are enforced by the gateway (outside the model) which is correct, but the model's own compliance relies on SOUL.md instructions which can be overridden by sufficiently clever injection. No recurring goal restatement within conversation context.
**Risk:** MEDIUM

### Domain 12 — Output Validation and Secondary Controls
**Status:** PARTIAL → **IMPROVED** (v0.8.0)
**Coverage:** Outbound pipeline has 10 steps: XML strip → PII → OutboundInfoFilter → PromptProtection → EncodingDetector → CanaryTripwire → EnhancedToolSanitizer → OutputCanary → EgressFilter → AuditChain. LogSanitizer on all Python logging handlers. PromptProtection uses fuzzy matching as secondary validation.
**v0.8.0 fix:** Streaming responses now run through the full security pipeline. `llm_proxy.py:_filter_outbound_streaming()` buffers the complete SSE stream (urllib.request reads it fully before delivery), extracts accumulated text, and runs `pipeline.process_outbound()`. BLOCK events replace the response with a synthetic error SSE; REDACT events consolidate sanitized text into a single delta event.
**Gaps:** SSE reconstruction is simplified (single consolidated delta). No semantic validator. No secondary model reviewer.
**Risk:** LOW (reduced from CRITICAL)

### Domain 13 — Sandboxing and Execution Isolation
**Status:** IMPLEMENTED
**Coverage:** 9 container hardening controls. read_only rootfs, cap_drop ALL, no-new-privileges, seccomp profiles, tmpfs noexec/nosuid. 3-network isolation. FileSandbox + PathIsolation. Resource limits (mem, pids, cpu). Base image SHA256 pinned. Setuid stripped. Perl removed.
**Gaps:** No gVisor/Firecracker for VM-level isolation (deferred to v1.0). Bot gets 4GB memory / 512 pids — generous. No per-task container (persistent bot container). No automatic destruction after task completion.
**Risk:** LOW

### Domain 14 — Browser and Document Ingestion Hardening
**Status:** PARTIAL
**Coverage:** BrowserSecurityGuard (URL reputation). WebContentScanner (response body scanning for injection, hidden content). URLAnalyzer (SSRF detection, PII in URLs). Web fetch tools denied for collaborators.
**Gaps:** **No OCR-based injection scanning for images.** No PDF/DOCX content extraction and scanning. No HTML sanitization to safe intermediate representation. No image metadata (EXIF) inspection. Images pass directly to LLM without text extraction.
**Risk:** HIGH

### Domain 15 — Secret Management and Anti-Exfiltration Design
**Status:** IMPLEMENTED
**Coverage:** KeyVault (per-agent scoping, KeyInjector transparent header injection, KeyLeakDetector pattern scanning). CredentialInjector. Docker secrets gateway-only (ADR-004). CanaryTripwire includes test API key canary. LogSanitizer. OutboundInfoFilter blocks credential patterns. EncryptedStore (AES-256-GCM) for data at rest.
**Gaps:** No honeytokens beyond CanaryTripwire's static set. No cloud metadata endpoint blocking (169.254.169.254). KeyRotation EXPERIMENTAL.
**Risk:** LOW

### Domain 16 — Detection Engineering and Monitoring
**Status:** PARTIAL → **IMPROVED** (v0.8.0)
**Coverage:** AuditChain + AuditStore log every pipeline event. CEF export. AlertDispatcher. CollaboratorTracker. DriftDetector. KillSwitchMonitor (heartbeat + anomaly). Falco rules defined. Wazuh client. ClamAV. Trivy. LogSanitizer filters sensitive data from logs. MultiTurnTracker scores cumulative disclosure risk.
**v0.8.0 fix:** BLOCK events now use `await audit_chain.append_block()` — guaranteed SQLite write before response returns. All 8 block paths in SecurityPipeline updated. Periodic chain verification heartbeat (60s interval) logs CRITICAL if chain integrity fails.
**Gaps:** Falco/Wazuh are module loaders, not running daemons in current deployment. No centralized SIEM integration.
**Risk:** LOW (reduced from MEDIUM)

### Domain 17 — Canary and Tripwire Strategies
**Status:** IMPLEMENTED
**Coverage:** CanaryTripwire (3 planted canary values: SSN, test API key, project name; 7 detection methods: plain/reversed/alphanumeric/base64/rot13/URL/hex). OutputCanary (canary token injection + leak detection). Canary pipeline integrity check (on-demand). File integrity canaries on 3 critical files.
**Gaps:** Static canary values — discoverable by probing. No dynamic/rotating canary generation. No honey documents or honey API endpoints.
**Risk:** LOW

### Domain 18 — Policy-as-Code and Formal Guardrails
**Status:** GAP
**Coverage:** agentshroud.yaml provides declarative config for module modes, allowed domains, tool risk tiers. BotConfig includes egress_domains. Tool deny list in apply-patches.js.
**Gaps:** No formal policy language (OPA/Rego/Cedar). Security rules are hardcoded across 65+ Python modules. No policy versioning or rollback. No composable rule engine. No invariant checks ("untrusted content cannot authorize external communication" is a convention, not an enforced invariant).
**Risk:** MEDIUM

### Domain 19 — Resilience Against Long-Horizon Attacks
**Status:** PARTIAL
**Coverage:** MultiTurnTracker scores cumulative disclosure risk per session. ContextGuard detects cross-turn injection. Collaborator rate limit (20/hr). Session cleanup after 90 days inactivity.
**Gaps:** No task duration caps. No chain depth limits. No re-anchoring to original goal at checkpoints. No plan drift detection across conversation. No cumulative risk scoring that triggers re-validation.
**Risk:** MEDIUM

### Domain 20 — Training, Tuning, and Specialized Models
**Status:** GAP
**Coverage:** None. PromptGuard and HeuristicClassifier are regex/heuristic-based. No fine-tuned models. No specialized classifiers.
**Gaps:** No fine-tuned injection classifier. No RLHF on prompt-injection resistance. No specialized models for planning vs extraction vs review. Industry is moving to model-based detection.
**Risk:** MEDIUM (regex coverage is broad but brittle)

### Domain 21 — Secure UX and Operator Ergonomics
**Status:** PARTIAL
**Coverage:** Telegram block notifications with friendly reasons (promptguard, rbac, gitguard, etc.). Collaborator disclosure notice on first message. Rate limit notices. Command-blocked notices. `/manage/modules` endpoint shows all module status.
**Gaps:** No trust-level visualization per message. No provenance display for operators. No one-click quarantine. No sandbox replay for investigation. Approval messages don't show structured diffs.
**Risk:** LOW

### Domain 22 — Incident Response and Recovery
**Status:** PARTIAL
**Coverage:** KillSwitchMonitor (heartbeat + anomaly detection). Graceful shutdown with audit flush. AlertDispatcher routes findings. AuditChain provides forensic trail. Session cleanup.
**Gaps:** No documented incident response playbooks. No automated containment (e.g., auto-kill on canary trigger + revoke credentials + quarantine memory). No panic button for instant all-stop. Kill switch is heartbeat-based, not push-based.
**Risk:** MEDIUM

### Domain 23 — Red Teaming and Continuous Evaluation
**Status:** PARTIAL → **IMPROVED** (v0.8.0)
**Coverage:** 2,286+ tests (70+ security-focused). Steve Hay manual assessment (phases 0+F complete). Internal blue-team assessment (v0.8.0 B+ grade). Multilingual injection patterns (20+ languages).
**v0.8.0 addition:** `gateway/tests/test_adversarial_injection.py` — 110+ payloads across 8 categories (classic override, persona hijack, context injection, prompt extraction, goal hijack, multilingual, encoding bypass, multi-step). CI gate at 40% overall detection rate (measured v0.8.0 baseline; v1.0 target ≥85%).
**Gaps:** No continuous red-team in CI/CD (scheduled runs). Steve Hay phases 1-6 still awaiting authorization. No benchmark against tensor trust / HackAPrompt full datasets.
**Risk:** MEDIUM (reduced from HIGH)

### Domain 24 — Supply Chain and Ecosystem Controls
**Status:** PARTIAL
**Coverage:** Base image SHA256 pinned. Trivy installed with checksum verification. 1Password CLI with GPG signature verification. `requirements.txt` with version pins. `docker>=7.0.0,<8.0.0`, `python-multipart>=0.0.18,<1.0.0`.
**Gaps:** No SBOM generation. No dependency vulnerability scanning in CI/CD (Trivy is available but not run automatically on builds). MCP servers are configured but not integrity-verified. No signed policy bundles.
**Risk:** MEDIUM

### Domain 25 — Governance and Change Control
**Status:** PARTIAL → **IMPLEMENTED** (v0.8.0)
**Coverage:** 9 ADRs for architectural decisions. agentshroud.yaml as versioned config. Git-based change control. Pre-commit hooks (git-secrets, gitleaks). CLAUDE.md defines development governance.
**v0.8.0 fix:** ADR-002 status updated to "Superseded by ADR-009". ADR-009 created documenting the enforce-by-default philosophy change from v0.8.0 with policy table, configuration baseline, and migration guidance.
**Gaps:** No mandatory threat review process for new tools. No environment separation documented (dev/test/prod). No formal approval on policy relaxations beyond code review.
**Risk:** LOW

---

## Additional Controls Checklist

| Control | Status | Notes |
|---------|--------|-------|
| Untrusted content labeled in approvals | GAP | Approval messages show action but not "untrusted" source label |
| Tool outputs not reinserted as trusted instructions | PARTIAL | ToolResultInjectionScanner scans but no trust-level demotion |
| Summaries inherit source trust level | GAP | No trust propagation through summarization |
| Scratchpads cannot become policy | IMPLEMENTED | Gateway is external proxy; agent scratchpads don't reach gateway policy |
| Agents cannot update own guardrails | IMPLEMENTED | read_only rootfs, FileSandbox, separation of privilege |
| Cross-tenant content isolation | IMPLEMENTED | UserSessionManager, per-user workspaces |
| Auto plugin/tool discovery disabled | IMPLEMENTED | Tool deny list, MCP server registry is explicit |
| Unicode normalized, homoglyphs inspected | IMPLEMENTED | InputNormalizer NFKC + EncodingDetector homoglyph map |
| Markdown/HTML/metadata as injection carriers | IMPLEMENTED | InputNormalizer strips markdown exfil, XMLLeakFilter, MetadataGuard |
| Generated code treated as untrusted | PARTIAL | No code-specific scanning beyond general injection patterns |
| Approvals show exact effect (not just summary) | GAP | Telegram messages show action name but not full diff |
| Destination reputation checks | PARTIAL | DNSBlocklist for known-bad; no real-time reputation API |
| Redacted vs full content recorded | GAP | Audit logs record sanitized version; original not separately stored |
| Explicit task scoping enforced | GAP | No formal task scope definition for validators |

---

## DELIVERABLE 2 — Maturity Scorecard

| Layer | Score (1-5) | v0.8.0 Delta | Rationale |
|-------|:-----------:|:---:|-----------|
| **Policy** | 3 | +1 | ADR-009 formalizes enforce-by-default; stale ADR-002 corrected |
| **Context** | 4 | — | ContextGuard + MultiTurnTracker + PromptGuard + HeuristicClassifier; missing crescendo detection |
| **Reasoning** | 2 | — | No taint tracking, no semantic analysis of LLM reasoning chains, trust boundaries implicit |
| **Action** | 4 | — | ToolChainAnalyzer + ApprovalQueue + FileSandbox + SubagentMonitor + tool deny list |
| **Execution** | 4 | — | 9 container hardening controls, seccomp, read-only rootfs, cap_drop ALL; no gVisor |
| **Egress** | 4 | — | Default-deny allowlist, HTTP CONNECT proxy, DNS blocklist, SSRF blocking, 3-network isolation |
| **Memory+RAG** | 3 | +1 | MemoryIntegrity/Lifecycle now started at runtime; DriftDetector runs |
| **Observability** | 4 | +0.5 | BLOCK events guaranteed persist (await); chain heartbeat; fire-and-forget only for non-blocks |
| **Approval** | 4 | — | Telegram approval with risk tiers, inline buttons, SQLite persistence; single approver |
| **Recovery** | 3 | — | KillSwitch + heartbeat + graceful shutdown; no panic button, no automated playbooks |

**Composite Score: 3.55 / 5.0** (up from 3.3 pre-v0.8.0)

---

## Top-10 Gaps by Exploitability x Impact (Post v0.8.0)

| Rank | Gap | Exploitability | Impact | Risk | v0.8.0 Status |
|------|-----|:-:|:-:|:-:|:-:|
| 1 | **~~Streaming responses bypass ALL outbound filtering~~** | ~~TRIVIAL~~ | ~~CRITICAL~~ | ~~CRITICAL~~ | **FIXED** |
| 2 | **~~MemoryIntegrity/Lifecycle modules not started at runtime~~** | ~~LOW~~ | ~~HIGH~~ | ~~HIGH~~ | **FIXED** |
| 3 | **No multimodal injection scanning** (images pass to LLM unscanned) | MODERATE | HIGH | HIGH | Open |
| 4 | **No taint tracking / data lineage** through LLM reasoning | MODERATE | HIGH | HIGH | Open |
| 5 | **~~LLM proxy user_id hardcoded "unknown"~~** — RBAC bypassed | ~~TRIVIAL~~ | ~~MEDIUM~~ | ~~HIGH~~ | **FIXED** |
| 6 | **No adversarial red-team test suite** — defenses unproven | N/A (meta) | HIGH | HIGH | **PARTIAL** (110+ payloads added) |
| 7 | **Regex-only prompt injection** — paraphrasing evades patterns | MODERATE | HIGH | MEDIUM | Open |
| 8 | **~~Audit chain fire-and-forget persistence~~** — entries may be lost under load | ~~LOW~~ | ~~MEDIUM~~ | ~~MEDIUM~~ | **FIXED** |
| 9 | **No instruction/data separation metadata** — all content is untyped strings | MODERATE | MEDIUM | MEDIUM | Open |
| 10 | **~~ADR-002 stale~~** — says "Default-Allow" but v0.8+ is enforce-by-default | ~~N/A~~ | ~~LOW~~ | ~~LOW~~ | **FIXED** |

---

## DELIVERABLE 3 — v0.8.0 Implementation Items

### Item 1: Streaming Response Outbound Filtering — **DONE (v0.8.0)**
**Addresses:** Domain 12 (Output Validation), former Gap #1
**Implementation:**
- `llm_proxy.py:_filter_outbound_streaming()` — buffers complete SSE stream, extracts `text_delta` content, runs through `pipeline.process_outbound()`
- `_extract_sse_text()` — parses Anthropic SSE format, accumulates all `text_delta` events
- `_build_blocked_sse()` — synthesizes replacement SSE stream with block notification when pipeline returns BLOCK
- `_rebuild_sse()` — reconstructs SSE stream with sanitized text (single consolidated delta) when pipeline redacts
- Stats: `streaming_responses_scanned`, `streaming_responses_blocked`, `streaming_responses_redacted`
**Files:** `gateway/proxy/llm_proxy.py`

### Item 2: Wire MemoryIntegrity/Lifecycle at Startup — **DONE (v0.8.0)**
**Addresses:** Domain 8 (Memory Hardening), former Gap #2
**Implementation:**
- `lifespan.py` — MemoryIntegrityMonitor initialized after DriftDetector; `scan_all_monitored_files()` establishes SHA-256 baseline on startup
- `lifespan.py` — MemoryLifecycleManager initialized with PII + injection scanning config
- `state.py` — `memory_integrity: Optional[object]` and `memory_lifecycle: Optional[object]` type hints added
- Workspace path resolved from default bot config (`BotConfig.workspace_path`), falls back to `/app/workspace`
**Files:** `gateway/ingest_api/lifespan.py`, `gateway/ingest_api/state.py`

### Item 3: LLM Proxy User Identity Propagation — **DONE (v0.8.0)**
**Addresses:** Domain 2 (Instruction/Data Separation), former Gap #5
**Implementation:**
- `llm_proxy.py:proxy_messages()` — `user_id: str = "unknown"` parameter added
- `llm_proxy.py:_scan_inbound()` — `user_id: str = "unknown"` parameter added; propagated to middleware `request_data`
- `main.py:llm_api_proxy()` — extracts `X-AgentShroud-User-Id` header; passes to `proxy_messages()`
**Files:** `gateway/proxy/llm_proxy.py`, `gateway/ingest_api/main.py`

### Item 4: Adversarial Prompt Injection Test Suite — **DONE (v0.8.0)**
**Addresses:** Domain 23 (Red Teaming), former Gap #6
**Implementation:**
- `gateway/tests/test_adversarial_injection.py` — 110+ payloads across 8 categories
- Categories: classic override, persona hijack, context injection, prompt extraction, goal hijack, multilingual (17 languages), encoding bypass, multi-step escalation
- Tests: PromptGuard, HeuristicClassifier, InputNormalizer (combined and per-module)
- CI gate: `≥40%` overall detection rate (v0.8.0 measured baseline); per-category gates calibrated to baselines
- Per-category breakdown reported in test output
**Files:** `gateway/tests/test_adversarial_injection.py`

### Item 5: Audit Chain Guaranteed Persistence for BLOCK Events — **DONE (v0.8.0)**
**Addresses:** Domain 16 (Detection), former Gap #8
**Implementation:**
- `AuditChain.append()` — `_skip_task: bool = False` parameter; when True, suppresses fire-and-forget `create_task` for block events
- `AuditChain.append_block()` — new `async` method; calls `append(_skip_task=True)` then directly `await`s `audit_store.log_event()` with `severity="CRITICAL"`
- 8 BLOCK paths in `SecurityPipeline` updated: `self.audit_chain.append(...)` → `await self.audit_chain.append_block(...)` for all inbound/outbound block directions
- Audit chain verification heartbeat in `lifespan.py` (60s interval, CRITICAL log on chain integrity failure)
**Files:** `gateway/proxy/pipeline.py`, `gateway/ingest_api/lifespan.py`

### Item 6: Update ADR-002 to Reflect Enforce-by-Default — **DONE (v0.8.0)**
**Addresses:** Domain 25 (Governance), former Gap #10
**Implementation:**
- `ADR-002` status updated to "Superseded — see ADR-009"
- `ADR-009` created: enforce-by-default philosophy, policy table (v0.7 vs v0.8+), configuration baseline, migration guidance, related ADRs
**Files:** `docs/architecture/adr/ADR-002-default-allow-security-philosophy.md`, `docs/architecture/adr/ADR-009-enforce-by-default.md`

---

## Implementation Sequence (v0.8.0 Execution Order)

```
Step 1: Item 3 (LLM proxy user_id)          [S]  — DONE
Step 2: Item 5 (Audit persistence)           [S]  — DONE  (parallel with Step 1)
Step 3: Item 6 (ADR-002 update)              [S]  — DONE  (parallel with Steps 1-2)
Step 4: Item 2 (Memory wiring)               [M]  — DONE
Step 5: Item 1 (Streaming outbound filter)   [L]  — DONE
Step 6: Item 4 (Adversarial test suite)      [M]  — DONE
```

---

## DELIVERABLE 4 — v1.0 Roadmap

### Phase 1: Foundation Hardening (v0.8.0, completed)
- [x] Wire SecurityPipeline into Telegram path (DONE — v0.8.0)
- [x] Streaming response outbound filtering (DONE — v0.8.0, Item 1)
- [x] Wire MemoryIntegrity/Lifecycle at startup (DONE — v0.8.0, Item 2)
- [x] LLM proxy user_id propagation (DONE — v0.8.0, Item 3)
- [x] Audit chain guaranteed persistence (DONE — v0.8.0, Item 5)
- [x] ADR-009: Enforce-by-Default (DONE — v0.8.0, Item 6)
- **Success metric:** No outbound path bypasses; all memory writes scanned; all BLOCK events persisted

### Phase 2: Detection Enhancement (v0.9.3–v0.9.5, Weeks 5-10)
- [x] Adversarial injection test suite (DONE — v0.8.0, Item 4)
- [ ] Multimodal injection scanning (OCR via Tesseract for image content blocks)
- [ ] Dynamic canary rotation (session-scoped, randomly generated canary tokens)
- [ ] Taint metadata on PipelineResult (tag outputs with source: user_input | tool_result | system_prompt)
- [ ] Cloud metadata endpoint blocking (169.254.169.254 in EgressFilter)
- **New ADR:** ADR-010 (Taint Tracking Architecture)
- **Success metric:** ≥85% detection rate on public injection datasets; OCR injection blocked; canaries rotate per session

### Phase 3: Operational Maturity (v0.9.6–v1.0.0, Weeks 11-16)
- [ ] Policy-as-code engine (OPA/Rego integration for declarative security rules)
- [ ] gVisor sandbox for bot container (VM-level isolation)
- [ ] Continuous automated red-team pipeline (scheduled adversarial runs in CI)
- [ ] Incident response playbook automation (panic button, auto-containment, evidence preservation)
- [ ] External audit witness (remote hash attestation to immutable store)
- [ ] Falco runtime enforcement (sidecar with active blocking)
- [ ] SBOM generation and dependency vulnerability scanning in CI
- **New ADRs:** ADR-011 (Policy Engine), ADR-012 (VM-Level Isolation)
- **Success metric:** Policy rules declarative and versioned; sub-second kill switch; automated incident containment; SBOM in every build

---

## Verification Plan

```bash
# After v0.8.0 implementation:
cd gateway && python -m pytest -q --tb=short   # zero failures

# Item 1 (streaming filter):
# Verify: grep "streaming_responses_scanned" in /llm-proxy/stats response
# Test: send request with stream=true containing canary value → verify blocked

# Item 2 (memory wiring):
# Verify: grep "MemoryIntegrityMonitor" in gateway startup logs
# Verify: grep "MemoryLifecycleManager" in gateway startup logs

# Item 3 (user_id):
# Verify: grep "unknown" absent from LLM proxy middleware logs when
#         X-AgentShroud-User-Id header is present

# Item 4 (adversarial suite):
cd gateway && python -m pytest tests/test_adversarial_injection.py -v
# Verify ≥40% overall detection rate in output (v0.8.0 measured baseline)

# Item 5 (audit persistence):
# Verify: startup logs show "AuditChain verification heartbeat started"
# Verify: BLOCK events appear in audit.db within 1s

# Item 6 (ADR governance):
ls docs/architecture/adr/ADR-009-enforce-by-default.md
grep "Superseded" docs/architecture/adr/ADR-002-default-allow-security-philosophy.md

# Full build + deploy:
docker compose -f docker/docker-compose.yml build --no-cache
docker compose -f docker/docker-compose.yml up -d
curl http://localhost:8080/status
curl -H "Authorization: Bearer $TOKEN" http://localhost:8080/manage/modules | \
  jq '.modules | to_entries[] | select(.value.status != "active")'
```

---

## Critical Files (v0.8.0 Changes)

| File | Changes |
|------|---------|
| `gateway/proxy/llm_proxy.py` | Streaming outbound filter; user_id propagation; `_filter_outbound_streaming()`, `_extract_sse_text()`, `_build_blocked_sse()`, `_rebuild_sse()` |
| `gateway/proxy/pipeline.py` | `AuditChain.append_block()` async method; `_skip_task` flag; 8 block paths updated |
| `gateway/ingest_api/lifespan.py` | MemoryIntegrityMonitor + MemoryLifecycleManager wired; audit chain heartbeat |
| `gateway/ingest_api/state.py` | `memory_integrity`, `memory_lifecycle` type hints |
| `gateway/ingest_api/main.py` | `X-AgentShroud-User-Id` header extraction; pass to `proxy_messages()` |
| `gateway/tests/test_adversarial_injection.py` | New: 110+ adversarial payloads, 8 categories, 40% CI gate (v0.8.0 baseline) |
| `docs/architecture/adr/ADR-002-*.md` | Status: Superseded by ADR-009 |
| `docs/architecture/adr/ADR-009-*.md` | New: Enforce-by-Default philosophy |

---

*Generated: 2026-03-08 | Branch: feat/v0.8.0-enforcement-hardening | Assessment author: Isaiah Jefferson*
