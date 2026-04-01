# AgentShroud™ v1.0.0 "Fortress" — Release Announcement

## GitHub Release Notes

```markdown
# AgentShroud™ v1.0.0 "Fortress"

AgentShroud™ is an enterprise governance proxy that sits transparently between autonomous
AI agents — Claude Code, Gemini CLI, Codex, OpenClaw — and every system they touch. Every
API call, file write, cloud mutation, and tool invocation is intercepted, inspected,
logged, and policy-enforced in real time without disrupting the agent's native workflow.
If you run AI agents in production, AgentShroud is the control plane you didn't know you
were missing.

---

## What's New in v1.0.0 "Fortress"

### 76 Active Security Modules — Zero Stubs
All 76 security modules are fully wired in the request pipeline across 7 defense layers.
No dead code, no placeholders. Every module enforces policy on every request.

### IEC 62443 Alignment
- **FR3 → SL3** — System Integrity: Cosign image signing, Trivy CVE scanning, Falco
  runtime enforcement, Semgrep SAST (CWE-78, CWE-22, CWE-798, CWE-918, CWE-502)
- **FR6 → SL3** — Audit logging: SHA-256 hash chain + Wazuh SIEM integration
- **FR7 → SL2** — Resource availability hardened against agent-induced exhaustion

### CVE Registry — 9 OpenClaw CVEs Fully Mitigated
All 9 OpenClaw CVEs disclosed in March 2026 are documented and mitigated. See the
SOC "CVE Intelligence" dashboard for defense layer mapping.

### SOC Team Collaboration Dashboard
A 7-page web control center lets security operators monitor agent activity, review egress
approvals, manage delegations, inspect shared memory, and enforce tool ACLs in real time.

### Daily CVE Reports via Telegram
Trivy-powered CVE digests delivered daily to the owner's Telegram. Severity-filtered,
owner-gated, with error-report fallback if scanner is unavailable.

### Human-in-the-Loop Approval Queue
Actions touching `email_sending`, `file_deletion`, `external_api_calls`, and
`skill_installation` route through the approval queue. Full persistence, bounded memory.

### Credential Hygiene
`docker/setup-secrets.sh` integrates with 1Password CLI, macOS Keychain, and
`secret-tool`. No plaintext secrets on host disk during normal operation.

---

## Security Highlights

### 9 OpenClaw CVEs — All Fully Mitigated

| CVE | CVSS | Title | Status |
|-----|------|-------|--------|
| CVE-2026-22172 | 9.9 CRITICAL | WebSocket Scope Self-Declaration | ✅ Fully mitigated |
| CVE-2026-32051 | 8.8 HIGH | Privilege Escalation operator.write | ✅ Fully mitigated |
| CVE-2026-22171 | 8.2 HIGH | Path Traversal in Feishu Media | ✅ Fully mitigated |
| CVE-2026-32025 | 7.5 HIGH | WebSocket Brute-Force (ClawJacked) | ✅ Fully mitigated |
| CVE-2026-32048 | 7.5 HIGH | Sandbox Escape via sessions_spawn | ✅ Fully mitigated |
| CVE-2026-32049 | 7.5 HIGH | Oversized Media Payload DoS | ✅ Fully mitigated |
| CVE-2026-32032 | 7.0 HIGH | Arbitrary Shell via SHELL env var | ✅ Fully mitigated |
| CVE-2026-29607 | 6.4 MEDIUM | Allow-Always Wrapper Persistence | ✅ Fully mitigated |
| CVE-2026-28460 | 5.9 MEDIUM | Allowlist Bypass via Shell Continuation | ✅ Fully mitigated |

### Defense Layer Summary

| Layer | Coverage |
|-------|----------|
| P0 Core Pipeline | PromptGuard, TrustManager, EgressFilter, PII Sanitizer |
| P1 Middleware | SessionManager, RBAC, ToolACL, Delegation, PrivacyPolicy, SubagentMonitor |
| P2 Network | EgressApproval, DNSFilter, NetworkValidator, WebContentScanner |
| P3 Infrastructure | ClamAV, Trivy, Falco, Wazuh, DriftDetector, ConfigIntegrity, Canary |

---

## Getting Started

```bash
git clone https://github.com/idallasj/agentshroud.git
cd agentshroud
./docker/setup-secrets.sh store   # store credentials (1Password / Keychain / secret-tool)
scripts/asb up                    # bring up the stack
```

Full setup guide: [README](https://github.com/idallasj/agentshroud#readme)

---

## Stats

- **3,724+ tests — 94% coverage**
- **76 active security modules — 0 stubs**
- **< 0.5 ms** inbound request latency at P99 (arm64/macOS baseline)

---

## Support

If AgentShroud is useful to you:
[ko-fi.com/agentshroud](https://ko-fi.com/agentshroud) | [GitHub Sponsors](https://github.com/sponsors/agentshroud-ai)

---

> AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
> Patent Pending — U.S. Provisional Application No. 64/018,744
> Licensed under the MIT License.
```

---

## LinkedIn Post

```
Excited to announce AgentShroud™ v1.0.0 "Fortress" — open source, MIT licensed, and built
for teams running autonomous AI agents in production.

AgentShroud sits as a transparent proxy between your AI agents (Claude Code, Gemini CLI,
Codex) and every system they interact with. Every tool call, API request, file write, and
cloud mutation is intercepted, inspected, and policy-enforced — without modifying the agent.

What ships in v1.0.0:

▸ 76 fully active security modules across 7 defense layers — zero stubs
▸ IEC 62443 aligned (FR3→SL3, FR6→SL3, FR7→SL2)
▸ 9 OpenClaw CVEs fully mitigated (March 2026 disclosure)
▸ SOC collaboration dashboard — approvals, delegations, tool ACLs, live monitoring
▸ Daily CVE reports delivered via Telegram
▸ Human-in-the-loop approval queue for high-risk agent actions
▸ 3,724+ tests, 94% coverage

If your team is deploying LLM agents against real infrastructure, the governance gap is
real. This closes it.

GitHub: github.com/idallasj/agentshroud
Support: ko-fi.com/agentshroud

Patent Pending No. 64/018,744.

#AISecurity #LLMSecurity #AgentSecurity #OpenSource #IEC62443 #AgentShroud
```

---

## Awesome-List PR Templates

### awesome-ai-security

**PR Title:** `Add AgentShroud — enterprise governance proxy for autonomous AI agents`

**PR Body:**
> AgentShroud™ is an enterprise governance proxy that intercepts, inspects, and
> policy-enforces every action taken by autonomous AI agents before it reaches any
> downstream system. It directly addresses the agentic AI threat surface: prompt
> injection, PII exfiltration, egress abuse, privilege escalation via tool calls, and
> container-level runtime threats — backed by IEC 62443 alignment and a full CVE registry.
>
> - Open source: MIT licensed
> - Actively maintained: v1.0.0 released April 2026, 3,724+ tests, 94% coverage
> - Production-grade: 76 active modules, Falco + Wazuh + ClamAV sidecar stack

**List entry:**
```markdown
- [AgentShroud](https://github.com/idallasj/agentshroud) — Enterprise governance proxy for autonomous AI agents. 76 security modules, IEC 62443 aligned, prompt injection defense, egress filtering, PII sanitization, and human-in-the-loop approval queue.
```

---

### awesome-llm-apps / awesome-llm

**PR Title:** `Add AgentShroud — security proxy for LLM agent deployments`

**PR Body:**
> AgentShroud™ is a transparent security proxy that wraps AI agent runtimes (Claude Code,
> Gemini CLI, Codex, OpenClaw) with enterprise-grade governance — intercepting every tool
> call and API request at the boundary without modifying the agent itself. It solves a
> real production problem: how do you safely deploy autonomous agents against live
> infrastructure without losing auditability, policy control, or the ability to intervene?
>
> - Open source: MIT licensed
> - Works with all major LLM agent frameworks
> - Ships as a self-hosted Docker stack with no external cloud dependencies

**List entry:**
```markdown
- [AgentShroud](https://github.com/idallasj/agentshroud) — Security proxy that wraps AI agents (Claude, Gemini, Codex) with defense-in-depth: 76 active security modules, SOC dashboard, daily CVE reports, and IEC 62443 compliance.
```

---

### awesome-security / defensive security list

**PR Title:** `Add AgentShroud — AI agent governance proxy covering OWASP LLM Top 10 and IEC 62443`

**PR Body:**
> AgentShroud™ is an AI agent governance proxy that intercepts and policy-enforces every
> LLM tool invocation before it reaches any downstream system. It covers the full OWASP
> LLM Top 10: prompt injection (LLM01), insecure output handling (LLM02), sensitive data
> exposure (LLM06), excessive agency (LLM08), and supply chain risks (LLM05). IEC 62443
> alignment at FR3→SL3 makes it suitable for industrial and OT-adjacent deployments.
>
> - Open source: MIT licensed
> - USPTO trademark + patent pending
> - v1.0.0, April 2026 — 3,724+ tests, 94% coverage

**List entry:**
```markdown
- [AgentShroud](https://github.com/idallasj/agentshroud) — AI agent governance proxy. Intercepts and policy-enforces every LLM tool call. Covers OWASP LLM Top 10, IEC 62443, prompt injection, PII leakage, egress exfiltration, and container escape mitigation.
```
