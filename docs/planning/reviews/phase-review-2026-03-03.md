# AgentShroud Phase Review — 2026-03-03

**Reviewer:** Claude Code (Primary Developer)
**Scope:** Post-v0.7.0 phase assessment (Feb 25 – Mar 3, 2026)
**Current Version:** v0.7.0 (stable), v0.8.0 (in progress)
**Commits This Phase:** ~50 (of 415 total since project inception Feb 14)
**Test Suite:** 96 test files, 25,659 lines of test code, 79% measured coverage
**Security Modules:** 61 Python files in `gateway/security/`, 33+ wired into live pipeline

---

## 1. Accomplishments This Phase (Feb 25 – Mar 3)

### Delivered

| Deliverable | Files | Impact |
|-------------|-------|--------|
| **All v0.7.0 feature branches merged** | 12 branches → `main` | 33 security modules active and enforcing in live pipeline |
| **LLM API Reverse Proxy** | `gateway/proxy/llm_proxy.py` (220 lines), `docker/scripts/patch-anthropic-sdk.sh` | Every Anthropic API call now passes through gateway — PII scanning, injection detection, credential leak filtering on LLM traffic |
| **Telegram API Reverse Proxy** | `docker/scripts/patch-telegram-sdk.sh`, `gateway/ingest_api/main.py` | All bot Telegram API calls routed through gateway for PII filtering and audit |
| **HTTP CONNECT Proxy enforcement** | `gateway/proxy/http_proxy.py`, Docker Compose network config | Bot container has no direct internet — all outbound TCP goes through gateway proxy with domain allowlist |
| **SDK patching system** | `patch-anthropic-sdk.sh`, `patch-telegram-sdk.sh` | Anthropic and grammY SDKs patched at container startup to route through gateway — enforcement at the library level |
| **SecurityPipeline fully wired** | `gateway/proxy/pipeline.py`, `gateway/ingest_api/middleware.py` | CanaryTripwire, EncodingDetector, all P0-P3 modules connected to live request flow |
| **Multi-host deployment** | `docker-compose.marvin-prod.yml`, `docker-compose.pi.yml`, `docker-compose.trillian.yml` | Deployable across Marvin, Raspberry Pi, and Trillian hosts |
| **Docker VPN networking fix** | `docker/DOCKER-VPN-NETWORKING.md` | Resolved Docker Desktop + Cisco AnyConnect conflict via vpnkit-userspace |
| **RBAC fixes** | `gateway/security/rbac.py` | Collaborator READ/SYSTEM permissions corrected; AlertDispatcher path fix |

### What This Means

The critical accomplishment this phase was **closing the proxy loop**. Prior to Feb 26, the bot container could theoretically make direct API calls to Anthropic and Telegram, bypassing the gateway. Now:

- LLM traffic → patched SDK → `http://gateway:8080/v1/messages` → SecurityPipeline → Anthropic API
- Telegram traffic → patched SDK → `http://gateway:8080/telegram/` → SecurityPipeline → Telegram API
- All other HTTP/HTTPS → HTTP CONNECT proxy on gateway:8181 → domain allowlist enforcement

This is the difference between "security modules exist" and "security modules are inescapable."

---

## 2. Security Value Audit

For each major component: does it provide **real, measurable protection** or **perceived protection** (security theater)?

### REAL PROTECTION (functional enforcement, would stop actual attacks)

| Component | Verdict | Evidence |
|-----------|---------|----------|
| **SecurityPipeline (fail-closed)** | **Real** | `RuntimeError` on missing PII sanitizer. Every message traverses inbound + outbound chains. Not optional. |
| **PII Sanitizer** | **Real** | Microsoft Presidio + spaCy NLP + regex fallback. Blocks SSNs, credit cards, API keys, SSH keys on untrusted channels. Tested across Python 3.9–3.14. |
| **PromptGuard** | **Real** | 24 weighted regex patterns covering injection, jailbreak, multilingual attacks, encoding smuggling, markdown exfiltration. Scoring with configurable block/warn thresholds. |
| **Credential Isolation** | **Real** | Bot container holds only gateway password + Telegram token. All API keys (Anthropic, OpenAI, 1Password) live in gateway only. Docker Secrets mount, not env vars. Outbound leak scanning with 15 credential patterns. |
| **MCP Proxy (fail-closed)** | **Real** | `mcp-proxy-wrapper.js` intercepts every `tools/call`, sends to gateway for inspection. Gateway unreachable = tool call BLOCKED. Not a best-effort check. |
| **Egress Filter** | **Real** | Default-deny domain allowlist. SSRF protection blocks RFC 1918, loopback, link-local. CIDR matching. Enforce mode active. |
| **Kill Switch** | **Real** | Three modes: freeze (forensic), shutdown (graceful), disconnect (credential destruction + incident report). `killswitch.sh` is 304 lines of functional emergency response. |
| **Container Hardening** | **Real** | `cap_drop: ALL`, `no-new-privileges`, custom seccomp profiles (default SCMP_ACT_ERRNO), read-only rootfs, tmpfs noexec. Industry-standard Docker hardening. |
| **Audit Hash Chain** | **Real** | SHA-256 chain with genesis hash. Tamper detection via chain verification. Every security decision recorded. |
| **SDK Patching** | **Real** | Anthropic and Telegram SDKs patched at startup to hardcode gateway URLs. Enforcement at the library level, not just network config. |

### PARTIAL PROTECTION (real logic, but gaps or dependencies)

| Component | Verdict | Gap |
|-----------|---------|-----|
| **Network Isolation** | **Partial** | `agentshroud-isolated` has `internal: false` due to macOS Docker Desktop limitation. Isolation is application-enforced (HTTP_PROXY) not network-enforced. On Linux with proper Docker networking, this would be fully enforced. |
| **ClamAV/Trivy/Falco/Wazuh** | **Partial** | Integration wrappers are real code, but enforcement depends on external binaries being deployed. Graceful degradation means "logs a warning and continues" — not fail-closed. |
| **Trust Manager** | **Partial** | SQLite-backed progressive trust with decay and violation penalties. The logic is real, but trust score manipulation via carefully crafted benign requests before a malicious one is not well-defended. |
| **Approval Queue** | **Partial** | Human-in-the-loop for dangerous actions works. But queue fatigue (rubber-stamping after many benign requests) is a human factor not addressed. |
| **Multi-Turn Tracker** | **Partial** | Tracks conversation patterns across turns. The detection logic exists, but the threshold tuning for real attack patterns vs. legitimate multi-step workflows is untested against sophisticated adversaries. |

### SECURITY THEATER RISK (looks good, limited real value)

| Component | Verdict | Why |
|-----------|---------|-----|
| **33-module count marketing** | **Theater risk** | Counting ClamAV wrapper + Trivy wrapper + Falco wrapper + Wazuh wrapper as 4 "security modules" inflates the number. These are thin integration layers that do nothing without external tools. Honest count: ~29 self-contained modules + 4 external tool integrations. |
| **79% test coverage claim** | **Misleading** | The `.coverage` file shows 1,073/1,363 covered statements. But the gateway codebase is much larger than 1,363 statements (main.py alone is 3,209 lines). Coverage measurement appears to only cover a subset of the codebase, not the full 61 security modules. |
| **Extensive documentation** | **Theater risk** | 30+ docs in `docs/` directory. Documentation that describes security architecture is not security. Some docs describe features as "implemented" that are aspirational (e.g., mutual TLS in threat model — not implemented). |

---

## 3. Brutally Honest Self-Assessment

### Are we adding real value?

**Yes, with caveats.** If an autonomous agent ran through AgentShroud today, it would be meaningfully safer than without it. Specifically:

- **Prompt injection via tool results** would be detected by PromptGuard's 24-pattern scanner before reaching the agent's context. Without AgentShroud, the raw injection payload reaches the LLM unchecked.
- **Credential exfiltration** would fail because the agent never holds the credentials to exfiltrate. The gateway holds API keys; the bot holds only a gateway password and Telegram token.
- **PII leakage to external APIs** would be caught by the sanitizer scanning every outbound message. Without AgentShroud, an agent can freely send SSNs, credit cards, and API keys to any API.
- **Unauthorized network access** would be blocked by the default-deny egress filter. Without AgentShroud, the agent can connect to any IP/domain.

**What would NOT be stopped that simpler means could address:**
- A sufficiently novel prompt injection that doesn't match any of 24 regex patterns would pass through. A more sophisticated ML-based classifier (not regex) would catch more. But regex is fast, deterministic, and auditable — ML classifiers introduce their own attack surface.
- The SDK patching approach is fragile — if OpenClaw updates its SDK usage or adds a new HTTP client, the patch could break silently. Environment variable enforcement (`ANTHROPIC_BASE_URL`) is the real enforcement; the SDK patch is belt-and-suspenders.

### Have we implemented real security?

**Yes — substantially.** This is not scaffolding pretending to be security.

**Implemented and enforcing:**
- SecurityPipeline with fail-closed design (3,200+ line main.py wiring everything together)
- 61 security module files totaling ~16,600 lines of Python
- 96 test files with 25,659 lines of test code
- MCP proxy wrapper with fail-closed interception
- Kill switch with credential destruction
- Docker container hardening with custom seccomp profiles
- SHA-256 audit hash chain

**Not implemented (despite documentation suggesting otherwise):**
- Mutual TLS (mentioned in threat model, not in code)
- Enterprise SIEM/SOAR integration (Alert Dispatcher exists but doesn't connect to Splunk/Sentinel/etc.)
- HSM-backed key management (EncryptedStore uses AES-256-GCM in software)
- Automated threat intelligence feed consumption

### Are we covering known attack vectors?

| Attack Vector | Coverage | Assessment |
|---------------|----------|------------|
| **Prompt injection** | Strong | 24 patterns, multilingual, encoding-aware, normalized input. Gap: novel/zero-day injections beyond pattern library. |
| **Credential exfiltration** | Strong | Gateway-side isolation, Docker Secrets, outbound leak scanning, 1Password path allowlisting. |
| **Tool abuse** | Strong | MCP fail-closed proxy, per-tool permissions, rate limiting, sensitive tool detection, tool chain analysis. |
| **Data leakage (PII)** | Strong | Presidio + regex, channel-based blocking, outbound filter. Gap: structured data exfil via non-obvious encoding. |
| **Session hijacking** | Moderate | Session manager, per-user isolation, token validation. Gap: no session binding to client fingerprint or IP. |
| **Supply chain attacks on MCP servers** | Moderate | MCP inspector scans tool results, fail-closed proxy blocks on gateway failure. Gap: no verification of MCP server binary integrity at startup, no SBOM enforcement. |
| **Container escape** | Moderate | seccomp, cap_drop ALL, no-new-privileges, read-only rootfs. Gap: macOS Docker Desktop has weaker isolation than Linux; `internal: false` on isolated network. |
| **Indirect prompt injection (via fetched content)** | Weak | Web content scanner exists but prompt injection in fetched web pages or document content is only caught if it matches PromptGuard patterns. No content-origin tagging to distinguish trusted vs. untrusted content in the LLM context. |
| **Model extraction / system prompt leaking** | Moderate | Outbound filter + prompt protection with fuzzy matching. Gap: gradual extraction over many turns may evade per-message detection. |
| **Denial of service** | Weak | Rate limiting exists at auth level (100 req/60s). No sophisticated resource exhaustion protection at the agent task level. |

### Are we scanning for emerging threats?

**No automated mechanism exists.** There is no:
- Threat intelligence feed integration
- Automated CVE monitoring for dependencies beyond CI pip-audit
- Agent security research tracking (e.g., monitoring arXiv, security conferences, OWASP agent security project)
- Pattern library update mechanism for PromptGuard when new injection techniques emerge

The threat model (`docs/security/threat-model.md`) is a point-in-time STRIDE analysis, not a living document with update triggers. The prompt injection patterns in PromptGuard were manually curated and will drift as attack techniques evolve.

**This is a real gap.** The agent security landscape is moving fast (new injection techniques, MCP security research, multi-agent attack patterns). A static pattern library will become stale.

### Should we continue or cut losses?

**Continue.** AgentShroud is NOT a sunk cost trap. Here's why:

1. **The core value proposition is valid.** Autonomous agents operating without a security proxy are a genuine risk. The threat model is real and well-documented by the broader security community.
2. **The implementation is substantial and functional.** This is not a README with aspirations — it's ~16,600 lines of security logic, 25,659 lines of tests, and a working Docker deployment across multiple hosts.
3. **The proxy loop is closed.** As of this phase, every communication channel (LLM API, Telegram API, HTTP/HTTPS, MCP tools) flows through the gateway. This is the architectural foundation that makes everything else valuable.
4. **There is no equivalent open-source alternative.** Agent security proxies are an emerging category. AgentShroud is ahead of the market.

**What would make the answer "stop":**
- If the upstream agent platforms (Claude Code, OpenClaw) implemented equivalent security controls natively, making AgentShroud redundant.
- If the SDK patching approach became unmaintainable (every SDK update breaks the patches) and no alternative enforcement mechanism existed.
- If the project scope expanded beyond security proxy into becoming a full agent platform (competing with OpenClaw rather than securing it).

### Is the investment still justified?

**Original value proposition:** A security governance proxy that makes autonomous AI agents safe for enterprise use by intercepting, inspecting, and enforcing policies on all agent communications.

**Current trajectory:** Tracking toward the value proposition. The proxy architecture is sound, the security pipeline is enforcing, and the deployment model works across multiple hosts. 415 commits in 17 days represents extraordinary velocity.

**Scope drift concerns:**
- The `chatbot/` directory, `whogoesthere/` persona files, and branding assets suggest some effort went into making AgentShroud a "product" rather than purely a security tool. This is minor but worth watching.
- The 3,209-line `main.py` monolith needs decomposition. At current growth rate, this becomes a maintenance liability.
- Documentation volume (30+ docs, 87KB whitepaper) is disproportionate to a pre-1.0 project. Documentation effort could have been code effort.

**Net assessment:** Investment is justified. The core security value is real. The risk is over-engineering and scope creep, not lack of substance.

---

## 4. Remaining Work — Prioritized by Value

### Tier 1: Critical (directly increases real security)

| Priority | Task | Value | Risk Mitigated |
|----------|------|-------|----------------|
| **1** | **Fix network isolation on macOS** | High | `internal: false` on isolated network means bot can bypass HTTP_PROXY if it discovers gateway IP. Investigate Docker Desktop alternatives or add iptables rules inside container. |
| **2** | **PromptGuard pattern update mechanism** | High | Static patterns will go stale. Implement a versioned pattern library that can be updated without redeploying the gateway. Even a YAML file with hot-reload. |
| **3** | **Coverage measurement fix** | High | 79% on 1,363 statements doesn't reflect the full codebase. Fix pytest coverage config to measure all `gateway/` code. Real coverage number is likely lower — know the truth. |
| **4** | **Content-origin tagging** | High | Mark content from external sources (web fetches, tool results, file reads) as untrusted in the LLM context. Currently, injection via fetched content is only caught by pattern matching, not by origin-based trust. |
| **5** | **MCP server integrity verification** | Medium-High | Verify MCP server binaries/checksums at startup. A compromised MCP server binary bypasses all proxy inspection. |

### Tier 2: Important (hardens existing security)

| Priority | Task | Value | Risk Mitigated |
|----------|------|-------|----------------|
| **6** | **Decompose main.py** | Medium-High | 3,209-line monolith is a maintenance and review liability. Extract route handlers, startup sequence, and health checks into separate modules. Not security per se, but maintainability directly affects security review quality. |
| **7** | **Session binding** | Medium | Bind sessions to client fingerprint (IP, user-agent) to prevent session hijacking. |
| **8** | **Gradual extraction defense** | Medium | Add cross-turn analysis to detect gradual system prompt extraction over many messages. Multi-turn tracker exists but doesn't specifically target this. |
| **9** | **SDK patch resilience** | Medium | Add a startup verification that confirms SDK patches are active (probe the patched URL, verify gateway receives the request). Silent patch failure = silent security bypass. |
| **10** | **Resource exhaustion protection** | Medium | Agent-level rate limiting and task timeout enforcement beyond the basic 100 req/60s auth rate limit. |

### Tier 3: Nice to Have (adds value but not critical)

| Priority | Task | Value | Risk Mitigated |
|----------|------|-------|----------------|
| **11** | **Threat intelligence integration** | Medium-Low | Even a weekly manual review of agent security research would help. Automated feed is ideal but not urgent. |
| **12** | **Enterprise SIEM integration** | Low | AlertDispatcher → Splunk/Sentinel. Only matters for enterprise deployment, not current use case. |
| **13** | **Multi-runtime testing (Podman, Apple Containers)** | Low | Nice for portability, doesn't add security value. |
| **14** | **Observatory Mode** | Low | Passive monitoring mode is useful for evaluation but doesn't enforce anything. |

### Deprioritized (complexity without proportional value)

| Task | Why Deprioritized |
|------|-------------------|
| **HSM-backed key management** | AES-256-GCM in software is adequate for current threat model. HSM adds operational complexity for marginal gain. |
| **Mutual TLS between containers** | Docker network + shared secret auth is sufficient for same-host deployment. mTLS is over-engineering for this topology. |
| **ML-based prompt injection classifier** | Regex is fast, deterministic, auditable. ML adds latency, false positives, and its own attack surface. Keep regex, expand patterns. |
| **Kubernetes deployment** | Docker Compose is appropriate for current scale (1-3 hosts). K8s adds enormous operational overhead. |

---

## 5. Risks & Gaps

### Critical Risks

| Risk | Severity | Status |
|------|----------|--------|
| **macOS network isolation bypass** | High | `internal: false` documented but unmitigated. Bot could bypass proxy if it discovers gateway IP directly. |
| **SDK patch fragility** | High | OpenClaw or SDK updates could silently break patches. No verification mechanism. |
| **Coverage measurement gap** | Medium-High | Stated coverage may not reflect actual codebase coverage. Decisions based on false confidence. |
| **main.py monolith** | Medium | 3,209 lines, 76 git changes. Single point of complexity. Hard to review, easy to introduce bugs. |

### Design Decisions That Could Backfire

| Decision | Risk |
|----------|------|
| **Regex-only prompt injection** | Adequate today, but novel injection techniques could bypass all 24 patterns. Pattern library needs active maintenance. |
| **SQLite for audit/trust/sessions** | Fine for single-host. Becomes a bottleneck if multi-gateway deployment is ever needed. Not urgent but architectural debt. |
| **Python for security-critical proxy** | Performance ceiling for high-throughput scenarios. Acceptable for current scale (1 agent, 1 gateway). |
| **OpenClaw dependency** | AgentShroud's bot layer depends entirely on OpenClaw. If OpenClaw changes its architecture, patches break. |

### Deferred Items That Matter

| Item | Why It Matters |
|------|----------------|
| **No automated threat intel** | Prompt injection landscape evolves weekly. Static defenses age fast. |
| **No MCP server supply chain verification** | A compromised MCP server binary completely bypasses AgentShroud's proxy inspection for that tool. |
| **No content-origin tagging** | Indirect prompt injection via fetched web content or document content is the #1 emerging agent attack vector. Current defense (pattern matching only) is insufficient. |

---

## 6. Go / No-Go Recommendation

### **GO — Continue Development**

AgentShroud delivers genuine, measurable security value. The proxy architecture is sound, the implementation is substantial (not scaffolding), and the core security controls (credential isolation, PII filtering, prompt injection detection, egress filtering, MCP fail-closed proxy, kill switch) are functional and enforcing. There is no equivalent open-source tool that provides this level of agent security governance.

### Conditions for Continued Investment

1. **Fix the macOS network isolation gap within the next sprint.** Application-layer proxy enforcement is necessary but not sufficient. If Docker Desktop cannot support `internal: true`, add in-container iptables/nftables rules or switch to Colima/Lima on macOS.

2. **Add SDK patch verification within the next sprint.** A startup health check that confirms patched SDKs are actually routing through the gateway. Log CRITICAL and refuse to start if verification fails (fail-closed, consistent with existing design philosophy).

3. **Fix coverage measurement to reflect the full codebase.** Know the real number. If it's 40%, that's fine — but make decisions based on truth, not a subset measurement.

4. **Decompose main.py before it crosses 4,000 lines.** This is not cosmetic — a 3,200-line file is a security review liability. Reviewers skip long files. Bugs hide in monoliths.

### Next Milestone That Validates the Investment

**v0.8.0 Definition of Done:**
- macOS network isolation mitigated
- SDK patch startup verification (fail-closed)
- Coverage measured on full `gateway/` codebase
- Content-origin tagging for tool results and web fetches (even if basic)
- main.py decomposed to <1,000 lines per module

If v0.8.0 ships with these items, AgentShroud will be the most comprehensive open-source agent security proxy available — with real enforcement, not just architecture diagrams.

### What Would Change This to NO-GO

- If macOS network isolation proves unfixable AND Linux deployment is not viable for the primary developer environment
- If OpenClaw introduces breaking changes that make SDK patching unmaintainable and no alternative enforcement exists
- If the project pivots from security proxy to agent platform (building features that compete with OpenClaw rather than securing it)
- If 3+ months pass without addressing Tier 1 priorities listed above
