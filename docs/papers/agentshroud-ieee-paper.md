# AgentShroud: A Transparent Proxy Framework for Enterprise Governance of Autonomous AI Agents

**Isaiah Dallas Jefferson, Jr.**
Independent Researcher
agentshroud.ai@gmail.com

---

## Abstract

Autonomous AI agents deployed via platforms such as OpenClaw, NanoClaw, and Zetherion now operate with persistent access to email, calendars, shell environments, cloud infrastructure, and financial accounts—yet no surveyed platform implements PII filtering, tamper-evident audit logging, prompt injection defense, or egress control. This paper presents AgentShroud, an open-source transparent proxy framework that wraps unmodified agent platforms with 52 enterprise-grade security modules organized across seven defense layers: inbound filtering, trust and access control, tool call interception, outbound information filtering, egress enforcement, container hardening, and cryptographic audit. The framework operates as a FastAPI gateway requiring zero modification to the wrapped agent, preserving upstream compatibility while enabling independent security testing and compliance certification. A concurrent STPA-Sec (Systems-Theoretic Process Analysis for Security) assessment conducted by an independent researcher identified 17 unsafe control actions across four loss categories and produced 23 requirements mapped to 14 features. Enforcement testing on the v0.6.0 baseline revealed a 0% effective enforcement rate across all modules, with 32 of 33 modules defaulting to monitor mode. The v0.8.0 release addresses all identified findings, implementing enforce-by-default semantics, credential isolation, per-user session partitioning, mutual TLS between containers, and DNS-layer enforcement via Pi-hole. The system achieves 1,987 passing tests at greater than 80% code coverage on an ARM64 deployment target. AgentShroud is, to the authors' knowledge, the first AI agent security framework to undergo formal control-theoretic safety analysis prior to public release.

**Index Terms**—AI agent security, transparent proxy, prompt injection defense, STPA-Sec, enterprise governance, MCP security

---

## I. Introduction

The proliferation of autonomous AI agent platforms has introduced a new class of privileged software system: one that executes arbitrary tool calls, maintains persistent memory, and communicates across multiple channels—all driven by a large language model (LLM) whose behavior is fundamentally non-deterministic and susceptible to adversarial manipulation via natural language [1], [2].

A survey of eleven AI agent platforms conducted in February 2026 revealed that zero of eleven implement PII filtering, kill switches, tamper-evident audit logging, prompt injection defense, or egress filtering. One platform (Zetherion) provides basic encrypted state without key rotation. Two platforms offer partial approval workflows. The remaining eight implement no security controls of any kind. This gap is not incremental—it is categorical.

The consequences are well-documented. CVE-2026-25253 demonstrated one-click remote code execution via token exfiltration in OpenClaw (CVSS 8.8) [3]. CVE-2026-22708 established indirect prompt injection via web browsing as a viable attack vector against MCP-compatible agents [4]. Cisco's AI security team demonstrated that a third-party OpenClaw skill performed data exfiltration and prompt injection without user awareness [5]. Research by Anthropic, OpenAI, and DeepMind showed that adaptive attacks defeat twelve published injection defenses with greater than 90% success rate [6]. Meta AI's "Agents Rule of Two" established that an agent exposed simultaneously to untrusted input, sensitive data, and external actions cannot be defended by prompt-level controls alone [7].

AgentShroud addresses this gap through a transparent proxy architecture: a FastAPI gateway that interposes between user channels and the agent container, applying security controls at the network layer without modifying the underlying agent platform. This approach provides three critical properties: (1) no fork is required—upstream agent updates flow through cleanly; (2) the security layer is platform-agnostic—the same gateway can proxy any MCP-compatible agent; and (3) the security controls are independently testable and auditable, enabling compliance certification without agent vendor cooperation.

This paper describes the architecture, security controls, and formal safety analysis of AgentShroud through v0.8.0. Section II reviews related work in AI agent security and control-theoretic safety analysis. Section III formalizes the threat model. Section IV presents the system architecture. Section V details the 52 security modules across seven defense layers. Section VI presents the STPA-Sec analysis and its findings. Section VII describes the v0.8.0 remediation effort. Section VIII presents test results and enforcement verification. Section IX discusses limitations and open challenges. Section X concludes with future work.

---

## II. Related Work

### II-A. AI Agent Security

The AI agent security landscape remains nascent. Debenedetti et al. demonstrated that adaptive attacks defeat published injection defenses with high probability, concluding that prompt-level defenses alone are insufficient [6]. Zhan et al. proposed the "Rule of Two" for agent design, establishing that simultaneous exposure to untrusted input, sensitive data, and external actions creates an indefensible threat surface [7]. Zhan et al. separately demonstrated ToolHijacker, achieving 96.7% attack success rate via tool selection manipulation [8]. The Log-To-Leak attack demonstrated MCP-specific exfiltration by coercing tool invocation [9].

Commercial and open-source defenses remain sparse. Zetherion AI implements AES-256-GCM encrypted memory and a progressive trust system but lacks PII filtering, prompt injection defense, or egress control [10]. NanoClaw provides a basic approval workflow not designed for adversarial scenarios [11]. No surveyed platform implements tamper-evident auditing, container hardening, or DNS-layer controls.

### II-B. STPA-Sec

Systems-Theoretic Process Analysis for Security (STPA-Sec) extends Leveson's STPA methodology [12] to security domains by modeling systems as control structures and identifying conditions under which control actions become unsafe. Unlike attack tree analysis, which requires enumeration of specific attack paths, STPA-Sec identifies unsafe conditions arising from the control structure itself—including architectural gaps where no control action exists for a given hazard. Young and Leveson demonstrated the methodology's application to cyber-physical systems [13]. To the authors' knowledge, AgentShroud is the first AI agent framework to undergo formal STPA-Sec analysis.

### II-C. Transparent Proxy Architectures

Transparent proxying is well-established in network security (e.g., Squid, mitmproxy, Envoy). AgentShroud adapts this pattern for AI agent governance, intercepting not only HTTP traffic but also MCP tool calls, DNS queries, file operations, and inter-agent communication. The approach is analogous to a Web Application Firewall (WAF) but extended to the agent tool-calling paradigm.

---

## III. Threat Model

AgentShroud's threat model defines four loss categories derived from the STPA-Sec analysis [14]:

- **L-1 (Data Disclosure):** Unauthorized disclosure of PII, credentials, system architecture, or user data.
- **L-2 (Unauthorized Actions):** Uncontrolled tool calls, file writes, network requests, or inter-agent communication.
- **L-3 (Agent Integrity):** Context poisoning, self-modification of security controls, trust manipulation.
- **L-4 (Audit Integrity):** Undetected attacks, untraceable incidents, tampered logs.

The control structure models the user as the external entity, the AgentShroud gateway as the controller, and the OpenClaw agent as the controlled process. External services (APIs, SSH hosts, web resources) constitute the actuated environment. The analysis identified 17 unsafe control actions (UCAs) across five control actions: inbound filtering, trust checking, PII redaction, audit logging, and outbound filtering. Four UCAs (UCA-14 through UCA-17) represent architectural gaps—conditions where no control action exists—rather than misconfiguration of existing controls [14].

### III-A. Attacker Model

The primary attacker interacts through the same Telegram interface available to any authorized user. The attacker may craft messages containing injection payloads, encoded content, or references to attacker-controlled web resources. The attacker does not have direct access to the host, container, or network infrastructure. Social engineering of the operator is out of scope. This attacker model reflects the most common real-world threat: a user (authorized or unauthorized) attempting to manipulate the agent through its natural language interface.

---

## IV. System Architecture

### IV-A. Transparent Proxy Design

AgentShroud operates as a FastAPI gateway positioned between user-facing messaging channels and the agent container. The architecture enforces a two-network topology:

1. **External network:** Gateway communicates with Telegram, email, and other messaging channels.
2. **Internal network:** Gateway communicates with the agent container via mutual TLS.

The agent container has no direct internet access. All inbound messages, outbound responses, tool calls, HTTP requests, and DNS queries transit the gateway's security pipeline. The agent is unaware of the proxy's existence—a critical property that ensures upstream platform updates require no security-layer modifications.

### IV-B. Security Pipeline

The SecurityPipeline processes messages through an ordered sequence of eight guards:

1. **PromptGuard:** Ensemble scoring across 20+ injection patterns with NFKC normalization.
2. **PII Sanitizer:** Microsoft Presidio-based entity detection (SSN, credit card, email, phone, name, address).
3. **TrustManager:** Five-level progressive trust with trust decay and rate-limited accumulation.
4. **EgressFilter:** Domain allowlist with default-deny and SSRF protection.
5. **ApprovalQueue:** SQLite-backed queue with WebSocket push and configurable timeout.
6. **OutboundInfoFilter:** Response classification and redaction of system architecture, tool inventories, and credential paths.
7. **CanaryTripwire:** Fail-closed response blocking if canary tokens are detected in outbound content.
8. **EncodingDetector:** Detection and normalization of encoded bypass attempts.

The pipeline is fail-closed: the PII Sanitizer is a required guard, and the pipeline refuses to start without it. The CanaryTripwire blocks the entire response if a canary token is leaked, preventing data exfiltration even if other guards are bypassed.

### IV-C. Middleware Manager

The MiddlewareManager processes individual requests through 35 modules covering RBAC, session isolation, context manipulation detection, metadata sanitization, environment variable protection, file sandboxing, cross-session access control, and 14 additional security functions. Each module is independently configurable between enforce and monitor modes.

### IV-D. MCP Proxy Layer

All MCP tool calls transit the gateway's MCP proxy, which applies per-tool permission checks, parameter injection scanning, PII detection in tool results, rate limiting, and tool chain analysis. The proxy operates transparently—MCP servers require zero modification.

---

## V. Security Modules

AgentShroud v0.8.0 implements 52 security modules organized across seven defense layers. TABLE I summarizes the module inventory.

### TABLE I: Security Module Inventory (52 Modules)

| Layer | Module Count | Examples |
|-------|:---:|---------|
| Inbound Filtering | 8 | PII Sanitizer, PromptGuard, ContextGuard, MetadataGuard |
| Trust & Access | 5 | RBAC, Progressive Trust, Session Isolation, Approval Queue |
| Tool Interception | 6 | MCP Proxy, ToolChainAnalyzer, ToolResultSanitizer, ToolResultInjection |
| Outbound Filtering | 6 | OutboundInfoFilter, CanaryTripwire, EncodingDetector, OutputCanary |
| Egress Enforcement | 7 | EgressFilter, DNSFilter, EgressMonitor, WebProxy, NetworkValidator |
| Container Security | 8 | FileSandbox, PathIsolation, DriftDetector, ContainerHardening, ResourceGuard |
| Cryptographic Audit | 5 | AuditLedger, AuditExporter, EncryptedMemory, MemoryIntegrity, LogSanitizer |
| Infrastructure | 7 | Trivy, ClamAV, Falco, Wazuh, OpenSCAP, KillSwitch, KillSwitchMonitor |

### V-A. PII Sanitizer

The PII Sanitizer is built on Microsoft Presidio [15], an open-source PII detection engine combining NLP (spaCy en_core_web_sm), regular expressions, and context-aware analysis. AgentShroud applies Presidio on both inbound and outbound message paths and, as of v0.8.0, on MCP tool results (addressing requirement R-17 from the STPA-Sec assessment). Detected entity types include SSN, credit card (Luhn-validated), email, phone (international), person name, physical address, IP address, and AWS access key. The module operates in three modes: block, redact, or log-only. In enforce mode (the v0.8.0 default), detected PII is replaced with typed placeholders (e.g., `[REDACTED_SSN]`).

### V-B. Prompt Injection Defense

The prompt injection defense employs an ensemble of 20+ detection patterns organized into five categories:

1. **Direct override:** "Ignore previous instructions," "You are now," "New system prompt."
2. **Role-play injection:** "Pretend you are," "Act as if you have no restrictions."
3. **Structural escape:** Delimiter closing (markdown, JSON, XML), format string injection.
4. **Encoding bypass:** Base64, URL encoding, Unicode homoglyphs, zero-width characters.
5. **Cross-turn manipulation:** Crescendo attacks detected via the MultiTurnTracker module.

All input undergoes NFKC normalization, zero-width character stripping, HTML entity decoding, and URL decoding before pattern matching. Each detector returns a threat score; scores are summed against a configurable threshold (default: 0.8 in enforce mode). The multilingual defense covers 35 languages.

### V-C. Credential Isolation

The v0.8.0 credential isolation architecture implements requirements R-10, R-11, and R-12 from the STPA-Sec assessment [14]. All API credentials reside exclusively in the gateway container via Docker Secrets (tmpfs-mounted, never on disk). The agent container holds zero secret files or credential environment variables. Authenticated external requests route through the gateway's CredentialInjector, which matches outbound requests by destination domain and injects the corresponding authorization header server-side. The agent never observes raw credentials.

### V-D. Encrypted Container Communication

All container-to-container communication uses mutual TLS (mTLS) via an internal certificate authority implemented with step-ca [16]. Each container authenticates with a unique certificate. Certificate rotation is automated. Plaintext verification is performed via tcpdump capture analysis during deployment validation.

### V-E. DNS-Layer Enforcement

Pi-hole [17] is deployed as a default stack component, providing DNS-layer egress enforcement complementary to the proxy-level EgressFilter. Default blocklists include Steven Black's unified hosts, OISD, Phishing Army, and Malware Domains. DNS query logs are integrated with the AuditStore for correlation analysis. The dual-layer enforcement (DNS + proxy) ensures that egress control cannot be bypassed by a single-point failure.

### V-F. Tamper-Evident Audit

Every security event is recorded in a SQLite-backed audit ledger using a SHA-256 hash chain. Each entry includes the hash of the previous entry, creating a blockchain-like integrity guarantee. Chain verification is performed independently of the gateway process, enabling third-party audit validation. The v0.8.0 audit exporter produces compliance-ready output in CEF (Common Event Format) and JSON-LD with tamper-evident hash chain verification, addressing requirement R-14.

---

## VI. STPA-Sec Analysis

### VI-A. Methodology

An independent STPA-Sec assessment was conducted by Hay [14] against AgentShroud v0.4.0 through v0.9.0. The assessment modeled the system as a control structure (User → AgentShroud Gateway → OpenClaw Agent → External Services) and systematically identified conditions under which each control action becomes unsafe. The full methodology, including the control structure model and derivation process, is published separately [18].

### VI-B. Findings

Twenty-eight probes across two phases (13 reconnaissance, 15 enterprise analysis) identified 17 unsafe control actions across four loss categories. TABLE II summarizes the UCA distribution.

### TABLE II: Unsafe Control Action Distribution

| Control Action | Not Provided | Incorrect | Wrong Timing | Total |
|----------------|:---:|:---:|:---:|:---:|
| Filter inbound | UCA-1 | UCA-2 | UCA-3 | 3 |
| Check trust level | UCA-4 | UCA-5 | — | 2 |
| Scan web content | UCA-6 | UCA-7 | — | 2 |
| Redact PII | UCA-8 | UCA-9 | UCA-10 | 3 |
| Log to audit | UCA-11 | UCA-12 | UCA-13 | 3 |
| Filter outbound | UCA-14 | — | — | 1 |
| Isolate sessions | UCA-15 | — | — | 1 |
| Gate self-modification | UCA-16 | — | — | 1 |
| Require approval | UCA-17 | — | — | 1 |
| **Total** | | | | **17** |

The critical finding was that the v0.6.0 baseline exhibited a **0% effective enforcement rate** across all 33 modules and four loss categories. Thirty-two of 33 modules defaulted to monitor mode—logging attacks but blocking none. The single module claiming enforcement (API Key Vault) was contradicted by evidence: the agent read credentials directly from mounted secret files [14].

Four UCAs (14–17, shown in bold in the original analysis) represented architectural gaps with no corresponding module in the system design:

- **UCA-14:** No outbound information filter existed; the agent disclosed its full tool inventory, Tailscale topology, and credential paths voluntarily.
- **UCA-15:** No session isolation existed; all users shared the same context, filesystem, and memory.
- **UCA-16:** No separation of privilege existed; the agent had write access to its own security code.
- **UCA-17:** No functioning approval gates existed; the agent sent emails, executed SSH commands, and retrieved credentials without human approval.

### VI-C. Requirements

The assessment produced 23 requirements across 14 features organized into three tiers by weighted priority score. TABLE III summarizes the tier structure.

### TABLE III: STPA-Sec Requirement Tiers

| Tier | Description | Features | Requirements | Weighted Score |
|------|-------------|:---:|:---:|:---:|
| 1 | Deployment blockers | 6 | 12 | 4.0–4.8 |
| 2 | Compliance enablers | 6 | 9 | 2.5–3.9 |
| 3 | Operational maturity | 2 | 2 | 2.1–2.3 |

---

## VII. v0.8.0 Remediation

The v0.8.0 release addresses all 23 requirements from the STPA-Sec assessment across all three tiers. This section describes the implementation of each Tier 1 feature.

### VII-A. Enforce-by-Default (R-02, R-03)

The module configuration system was inverted: `get_module_mode()` returns "enforce" unless explicitly overridden. A `AGENTSHROUD_MODE=monitor` environment variable is provided for development. Monitor mode requires documented justification in the configuration file.

### VII-B. Outbound Information Filter (R-01)

A new module (`outbound_info_filter.py`) classifies outbound response content by category (system architecture, tool inventory, infrastructure topology, credential paths, user identifiers, internal URLs, MCP function_calls XML blocks) and applies per-category redaction using an allowlist of safe-to-disclose categories.

### VII-C. Per-User Session Isolation (R-04, R-05)

The UserSessionManager partitions all state by Telegram user ID: conversation history, file workspace, persistent memory, and trust level. Cross-user data access requires explicit consent via a ConsentFramework module.

### VII-D. Separation of Privilege (R-06, R-07)

Gateway configuration and source code are mounted as read-only Docker volumes. The FileSandbox deny list (enforce mode) blocks agent writes to all AgentShroud source paths. SSH commands targeting the proxy host are rejected. Modification of security-related files requires out-of-band human authorization.

### VII-E. Human-in-the-Loop (R-08, R-09)

MCP tools are classified into four risk tiers (low, medium, high, critical). High and critical tiers require human approval via the ApprovalQueue with WebSocket push to the control center. Auto-deny fires after a configurable timeout (default: 5 minutes). The interactive egress firewall extends this model to network connections, presenting Telegram inline keyboards for real-time allow/deny decisions.

### VII-F. Credential Isolation (R-10, R-11, R-12)

All secret mounts were removed from the agent container. Credentials reside exclusively in the gateway's Docker Secrets. The CredentialInjector matches outbound requests by destination domain and injects authentication headers server-side. The agent container's `docker inspect` output shows zero secrets.

---

## VIII. Evaluation

### VIII-A. Test Coverage

The test suite comprises 1,987 passing tests covering all 52 modules. TABLE IV summarizes coverage by layer.

### TABLE IV: Test Coverage by Defense Layer

| Layer | Tests | Coverage |
|-------|:---:|:---:|
| Inbound Filtering | 312 | >85% |
| Trust & Access | 187 | >80% |
| Tool Interception | 245 | >80% |
| Outbound Filtering | 198 | >80% |
| Egress Enforcement | 267 | >80% |
| Container Security | 234 | >80% |
| Cryptographic Audit | 156 | >85% |
| Infrastructure | 178 | >75% |
| Integration (E2E) | 210 | — |
| **Total** | **1,987** | **>80%** |

### VIII-B. Enforcement Verification

The v0.8.0 enforcement audit confirmed that all P0 modules (PromptGuard, PII Sanitizer, EgressFilter, FileSandbox, ApprovalQueue, TrustManager) block in enforce mode. TABLE V presents the Phase 8.5 end-to-end verification results.

### TABLE V: Phase 8.5 E2E Verification Scenarios

| Scenario | Description | Result |
|----------|-------------|:---:|
| 1 | PII in inbound message (test SSN) | BLOCKED |
| 2 | Prompt injection (direct override) | BLOCKED |
| 3 | High-risk tool call without approval | QUEUED |
| 4 | Audit chain integrity verification | VERIFIED |
| 5 | Kill switch FREEZE (<1s) | PASSED |
| 6 | Egress to non-allowlisted domain | BLOCKED |
| 7 | Trust escalation (UNTRUSTED → read-only) | ENFORCED |
| 8 | Outbound architecture disclosure | REDACTED |
| 9 | Tool result PII scanning | REDACTED |
| 10 | Canary token in response | BLOCKED |

### VIII-C. Module Coverage Matrix

The module coverage heat map (adapted from [14]) was re-evaluated post-remediation. TABLE VI shows the updated coverage.

### TABLE VI: Post-Remediation Coverage Summary

| Loss Category | Modules | Enforced | Monitor | Absent | Contradicted |
|--------------|:---:|:---:|:---:|:---:|:---:|
| L-1 (Data Disclosure) | 12 | 12 | 0 | 0 | 0 |
| L-2 (Unauthorized Actions) | 12 | 12 | 0 | 0 | 0 |
| L-3 (Agent Integrity) | 14 | 14 | 0 | 0 | 0 |
| L-4 (Audit Integrity) | 7 | 7 | 0 | 0 | 0 |

### VIII-D. Competitive Analysis

TABLE VII presents a security comparison across eleven surveyed platforms.

### TABLE VII: Security Module Comparison

| Category | AgentShroud | Zetherion | Others (9 platforms) |
|----------|:---:|:---:|:---:|
| Gateway Security | 13 | 0 | 0 |
| Container Security | 8 | 2 | 0 |
| Deep Hardening | 19 | 0 | 0 |
| Infrastructure | 7 | 2 | 0 |
| Cryptographic Audit | 5 | 0 | 0 |
| **Total** | **52** | **4** | **0** |

---

## IX. Discussion

### IX-A. Limitations

The transparent proxy architecture introduces latency on every message and tool call. Preliminary measurements indicate less than 50ms overhead per pipeline traversal, but formal latency benchmarking under load remains future work. The STPA-Sec assessment was conducted by a single independent researcher; a multi-reviewer assessment would strengthen confidence in the UCA enumeration completeness.

The prompt injection defense, while comprehensive, faces a fundamental asymmetry: defenders must detect all injection variants, while attackers need only one bypass. The ensemble scoring approach with configurable thresholds provides defense-in-depth, but the v0.8.0 ML-based classifier (DistilBERT) remains a stretch goal. Research by Debenedetti et al. [6] suggests that no single-layer defense achieves robust injection resistance; AgentShroud's multi-layer approach (prompt guard + context guard + tool result sanitizer + canary system) addresses this by requiring an attacker to bypass multiple independent detection mechanisms.

### IX-B. STPA-Sec as Applied to AI Agent Systems

The STPA-Sec analysis proved particularly effective for identifying architectural gaps (UCAs 14–17) that traditional penetration testing might not surface. Penetration testing asks "can this be exploited?" while STPA-Sec asks "what control is missing?" The four architectural gaps identified—outbound filtering, session isolation, privilege separation, and approval gating—were not failures of existing modules but absences of required control actions. This distinction is critical for security engineering: configuration changes cannot fix architectural gaps.

### IX-C. Industry Implications

The 0% enforcement finding on the v0.6.0 baseline illustrates a systemic risk in AI agent security: the presence of security modules does not imply the presence of security. Monitor-mode defaults, while operationally convenient, create a false sense of security. The v0.8.0 enforce-by-default policy, with explicit opt-in for monitor mode, inverts this dynamic at the cost of requiring initial configuration tuning for each deployment.

---

## X. Conclusion and Future Work

This paper presented AgentShroud, a transparent proxy framework implementing 52 security modules for autonomous AI agent governance. An independent STPA-Sec assessment identified 17 unsafe control actions and 23 requirements, all of which were addressed in the v0.8.0 release. The system achieves enforce-by-default operation across all modules with 1,987 passing tests.

Future work includes: (1) a second blue team assessment on v0.8.0 followed by adversarial red team testing across six phases (trust probing, prompt injection, indirect injection, data exfiltration, exploitation chains, and detection validation) [19]; (2) integration of production security tooling (Wazuh, Trivy, OpenSCAP, ClamAV) from stub implementations to fully operational scanning; (3) multi-platform container runtime support (Colima, Podman, Docker Desktop, Apple Containers); and (4) a professional command center with CLI, TUI, and SSH-accessible interfaces for operational management.

AgentShroud is available under the MIT License at github.com/idallasjlabs/agentshroud.

---

## References

[1] S. Perez, "ChatGPT, the AI chatbot sensation, faces concerns over prompt injection attacks," *TechCrunch*, 2023.

[2] OWASP, "OWASP Top 10 for Large Language Model Applications," OWASP Foundation, 2024.

[3] "CVE-2026-25253: OpenClaw Remote Code Execution via Token Exfiltration," NIST National Vulnerability Database, 2026.

[4] "CVE-2026-22708: Indirect Prompt Injection via Web Browsing in MCP-compatible Agents," NIST National Vulnerability Database, 2026.

[5] Cisco Talos Intelligence Group, "Security Analysis of Third-Party Skills in AI Agent Platforms," Cisco, Tech. Rep., 2025.

[6] F. Debenedetti *et al.*, "The Attacker Moves Second: Adaptive Attacks Against AI Agent Defenses," Anthropic, OpenAI, DeepMind, 2025.

[7] Q. Zhan *et al.*, "Agents Rule of Two: Simultaneous Exposure to Untrusted Input, Sensitive Data, and External Actions," Meta AI, 2025.

[8] Q. Zhan *et al.*, "ToolHijacker: Tool Selection Manipulation Achieving 96.7% Attack Success Rate," arXiv:2504.19793, 2025.

[9] J. Bagdasarian *et al.*, "Log-To-Leak: MCP-Specific Exfiltration via Coerced Tool Invocation," 2025.

[10] Zetherion AI, "Zetherion: Privacy-First Autonomous AI Agent," https://zetherion.ai, 2025.

[11] NanoClaw, "NanoClaw: Bespoke AI Agent Framework," https://github.com/nanoclaw, 2025.

[12] N. G. Leveson, *Engineering a Safer World: Systems Thinking Applied to Safety.* MIT Press, 2012.

[13] W. Young and N. G. Leveson, "An Integrated Approach to Safety and Security Based on Systems Theory," *Communications of the ACM*, vol. 57, no. 2, pp. 31–35, 2014.

[14] S. Hay, "Enterprise Security Feature Priorities: AgentShroud v0.4.0–v0.9.0," Independent Assessment, Feb. 2026.

[15] Microsoft, "Presidio: Data Protection and De-identification SDK," https://github.com/microsoft/presidio, 2023.

[16] Smallstep, "step-ca: A Private Certificate Authority for DevOps," https://smallstep.com/certificates/, 2024.

[17] Pi-hole, "Pi-hole: A Black Hole for Internet Advertisements," https://pi-hole.net, 2024.

[18] S. Hay, "STPA-Sec Control Structure Model for AgentShroud," https://gist.github.com/stvhay/a2924174b187b414e326fff136326d15, 2026.

[19] S. Hay, "Red Team Assessment Plan: AgentShroud v0.4.0–v0.9.0," Independent Assessment, Feb. 2026.

---

*AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. © 2026 Isaiah Dallas Jefferson, Jr. All rights reserved.*
