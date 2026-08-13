# AgentShroud Threat Model (STRIDE Analysis)

## Executive Summary

This document provides a comprehensive STRIDE-based threat analysis for AgentShroud, identifying potential security threats and corresponding mitigation strategies. The analysis covers the complete attack surface including network communications, container isolation, data flows, and administrative interfaces.

## Threat Modeling Scope

### System Components in Scope
- AgentShroud Gateway (FastAPI application)
- Container network isolation (external/internal networks)
- Audit system and hash chain integrity
- PII detection and sanitization
- Agent trust management and progressive security controls
- Administrative dashboard and approval workflows

### Assets Under Protection
- **OpenClaw Agent Containers**: Core AI agent functionality and memory
- **API Keys and Credentials**: Third-party service authentication tokens
- **Audit Logs**: Comprehensive security event history with hash chain integrity
- **User Data**: Personal and sensitive information processed by agents
- **Security Policies**: Trust levels, approval workflows, and enforcement rules

## STRIDE Threat Analysis

### S - Spoofing Identity

#### Threat: Agent Identity Spoofing
**Description**: Malicious actor impersonates legitimate OpenClaw agent to bypass security controls.

**Attack Vectors**:
- Container escape and lateral movement to impersonate trusted agent
- Network packet injection with spoofed source addresses
- Stolen agent certificates or authentication tokens

**Attack Tree**:
```
Agent Identity Spoofing
├── Container Compromise
│   ├── Vulnerability Exploitation → Container Escape
│   └── Privilege Escalation → Host Access
├── Network Attack
│   ├── ARP Spoofing → Network Position
│   └── Packet Injection → False Identity
└── Credential Theft
    ├── Memory Dump → Extract Tokens
    └── File System Access → Steal Certificates
```

**Mitigation**:
- **Network Isolation**: Docker internal networks prevent external spoofing
- **Container Security**: seccomp profiles and capability dropping limit escape
- **Mutual TLS**: Certificate-based authentication for all agent communications
- **Behavioral Analysis**: Trust Manager detects anomalous behavior patterns

#### Threat: API Key Impersonation
**Description**: Attacker uses stolen or guessed API keys to impersonate legitimate services.

**Mitigation**:
- **Proxy-Side Key Storage**: API keys never exposed to agent containers (ADR-004)
- **Key Rotation**: Automated rotation with revocation capabilities
- **Request Signing**: HMAC signatures for API request authentication
- **Rate Limiting**: Per-key rate limits prevent abuse

### T - Tampering with Data

#### Threat: Audit Log Tampering
**Description**: Attacker modifies audit logs to hide malicious activities or create false evidence.

**Attack Tree**:
```
Audit Log Tampering
├── Database Access
│   ├── SQL Injection → Direct Database Modification
│   └── File System Access → SQLite File Manipulation
├── Memory Corruption
│   ├── Buffer Overflow → Runtime Memory Modification
│   └── Race Condition → Inconsistent State
└── Hash Chain Attack
    ├── Hash Collision → Chain Poisoning
    └── Genesis Block Modification → Chain Reset
```

**Mitigation**:
- **SHA-256 Hash Chain**: Cryptographic integrity ensures tamper detection (ADR-005)
- **Database WAL Mode**: Write-ahead logging provides transaction integrity
- **File System Permissions**: Restricted access to audit database files
- **Chain Validation**: Periodic verification of complete hash chain integrity

#### Threat: Configuration Drift
**Description**: Unauthorized changes to security policies and configurations.

**Mitigation**:
- **Configuration Signing**: Digital signatures for all policy changes
- **Drift Detection**: Automated monitoring of configuration changes
- **Version Control**: Git-based configuration management with approval workflows
- **Immutable Infrastructure**: Container-based deployment prevents drift

### R - Repudiation

#### Threat: Non-Repudiation Bypass
**Description**: Users or agents deny performing logged actions.

**Mitigation**:
- **Cryptographic Audit Trail**: SHA-256 hash chain provides mathematical proof of event sequence
- **Multi-Factor Logging**: Correlation across multiple log sources
- **Timestamp Authority**: Network Time Protocol (NTP) synchronization for accurate timestamps
- **Digital Signatures**: RSA signatures for high-value transactions

### I - Information Disclosure

#### Threat: PII Leakage in Logs
**Description**: Personally identifiable information exposed through log files or error messages.

**Attack Tree**:
```
PII Information Disclosure
├── Log File Access
│   ├── File System Breach → Direct Log Access
│   └── Log Aggregation System → Centralized Exposure
├── Error Message Leakage
│   ├── Stack Trace Exposure → Debug Information
│   └── Database Error → Query Parameter Disclosure
└── Network Interception
    ├── Unencrypted Transport → Packet Capture
    └── TLS Downgrade → Man-in-the-Middle
```

**Mitigation**:
- **PII Sanitizer**: Presidio + custom regex patterns for comprehensive detection
- **Log Sanitization**: Multi-layer PII removal before log persistence
- **Error Handling**: Sanitized error messages with correlation IDs
- **TLS Everywhere**: End-to-end encryption for all communications

#### Threat: Environment Variable Leakage
**Description**: Sensitive configuration exposed through environment variables.

**Mitigation**:
- **Secrets Management**: Docker secrets and external vault integration
- **Environment Guards**: Automatic detection and redaction of sensitive env vars
- **Container Scanning**: Pre-deployment scanning for embedded secrets

#### Threat: SSRF (Server-Side Request Forgery)
**Description**: Agent manipulated to make requests to internal services or networks.

**Mitigation**:
- **URL Analysis**: Machine learning-based malicious URL detection
- **Network Segmentation**: Internal services isolated from agent networks
- **Request Validation**: Whitelist-based URL filtering
- **DNS Filtering**: Prevent resolution of internal or malicious domains

#### Threat: DNS Data Exfiltration
**Description**: Sensitive data exfiltrated through DNS queries.

**Mitigation**:
- **DNS Filtering**: Statistical analysis of query patterns and sizes
- **Query Logging**: Complete DNS query audit trail with anomaly detection
- **Allowlist DNS**: Restrict DNS queries to approved domains
- **DNS-over-HTTPS**: Encrypted DNS to prevent interception

### D - Denial of Service

#### Threat: Resource Exhaustion
**Description**: Attacker consumes system resources to deny service to legitimate users.

**Attack Tree**:
```
Denial of Service
├── Resource Exhaustion
│   ├── Memory Exhaustion → OOM Kill
│   ├── CPU Exhaustion → System Slowdown
│   └── Disk Space → Storage Full
├── Network Flooding
│   ├── Connection Flooding → Port Exhaustion
│   └── Bandwidth Saturation → Network Congestion
└── Application Layer
    ├── Expensive Operations → Compute Exhaustion
    └── Database Locking → Transaction Deadlock
```

**Mitigation**:
- **Resource Guards**: Container memory and CPU limits with monitoring
- **Rate Limiting**: Adaptive rate limiting based on request patterns
- **Connection Limits**: Maximum concurrent connections per source
- **Circuit Breakers**: Automatic service degradation under load

#### Threat: Context Window Stuffing
**Description**: Large payloads designed to exhaust AI model context windows.

**Mitigation**:
- **Context Guards**: Maximum payload size validation
- **Content Analysis**: Detection of repetitive or generated content
- **Request Preprocessing**: Automatic content summarization for large payloads
- **Priority Queuing**: Legitimate requests prioritized over bulk operations

### E - Elevation of Privilege

#### Threat: Prompt Injection Attacks
**Description**: Malicious prompts designed to manipulate agent behavior or bypass security controls.

**Attack Tree**:
```
Prompt Injection
├── Direct Injection
│   ├── System Prompt Override → Behavior Modification
│   └── Role-Playing Attack → Authority Impersonation
├── Indirect Injection
│   ├── Document Poisoning → Context Manipulation
│   └── Training Data Poisoning → Model Backdoor
└── Multi-Stage Attack
    ├── Social Engineering → Trust Building
    └── Gradual Escalation → Privilege Accumulation
```

**Mitigation**:
- **Prompt Guards**: Pattern matching for known injection techniques
- **Unicode Normalization**: Prevent encoding-based injection bypasses
- **Multi-Layer Decoding**: Detect nested encoding attacks
- **MCP Inspector**: Tool invocation analysis and validation

#### Threat: Container Escape
**Description**: Attacker breaks out of container isolation to access host system.

**Mitigation**:
- **seccomp Profiles**: Restrict system calls available to containers
- **Capability Dropping**: Remove unnecessary Linux capabilities
- **User Namespaces**: Non-root container execution
- **AppArmor/SELinux**: Mandatory access controls

#### Threat: Docker Socket Access
**Description**: Container gains access to Docker socket for privilege escalation.

**Mitigation**:
- **Socket Protection**: Docker socket never mounted in agent containers
- **Compose Validation**: Automated scanning for dangerous volume mounts
- **Rootless Docker**: Run Docker daemon as non-root user where possible
- **Socket Proxying**: Filtered Docker API access through AgentShroud gateway

## A2A (Agent-to-Agent) Protocol Threat Analysis

SCRUM-129. Hermes Agent v0.20.0+ (deployed: v0.20.1) adds support for the real
Google/Linux Foundation A2A v1.0.1 protocol (JSON-RPC 2.0 over HTTP, port 9900),
letting Hermes discover, call, and be called by other A2A-compliant agents. Both
Hermes's inbound A2A platform adapter and its outbound `a2a` toolset are disabled
by default — this analysis, and the `gateway/security/a2a_policy.py` /
`gateway/proxy/a2a_proxy.py` governance module it drives, are the prerequisite for
ever enabling either. Scope: **inbound only** (an external peer calling Hermes).
Outbound governance is architecturally capped by the existing CONNECT-tunnel proxy's
opacity to HTTPS payload content and is tracked as a separate follow-up, not
covered here.

Five specific gaps below (gap #1-#5) come from a direct source-level audit of
Hermes's own A2A plugin (`plugins/platforms/a2a/`, upstream PRs/issues #83701,
#80534/#80779, #78298, #77872, #81042) as of v0.20.1 — all five were still open
(unpatched) at time of writing. AgentShroud's interceptor is designed to catch
each of these independently of whether/when Hermes fixes its own code, since
AgentShroud terminates the inbound connection itself rather than trusting Hermes's
identity/authorization handling.

### S — Spoofing: Peer Identity Collapse Behind a Reverse Proxy

**Description**: Hermes's own identity derivation falls back to the raw socket
address when only a single shared `A2A_BEARER_TOKEN` is configured (gap #80534/
#80779). Behind any reverse proxy — including AgentShroud's own — every distinct
peer sharing that proxy collapses into one identity, silently breaking Hermes's
own rate limiting, peer allow-list, and audit attribution.

**Mitigation**: AgentShroud resolves peer identity itself, from the
`Authorization: Bearer` token's mapped alias (`A2A_PEER_TOKENS` semantics) —
never from socket address or `X-Forwarded-For`. A trusted internal header
(`X-AgentShroud-A2A-Peer-Id`) is forwarded to Hermes so its own broken derivation
is never consulted. This is the same trusted-header pattern used for
`_resolve_effective_agent_id` elsewhere in the gateway.

### T — Tampering: Cross-Tenant Task Ownership via `contextId` Collision

**Description**: Hermes's `contextId` filename sanitization strips all
non-`[A-Za-z0-9_-]` characters, so distinct caller-controlled context IDs (e.g.
`tenant/a` vs `tenanta`) can collide and merge persisted conversation histories on
disk (gap #83701). A peer that predicts or brute-forces another tenant's
`contextId` can read or write into their conversation history via `GetTask`/
`SubscribeToTask`.

**Mitigation**: `A2APolicyEngine` maintains its own `{task_id: peer_id}` map, set
at `SendMessage` task creation using AgentShroud's own resolved peer identity —
never Hermes's contextId handling. Any `GetTask`/`CancelTask`/`SubscribeToTask`
where the caller doesn't own the referenced task is denied before the request
ever reaches Hermes. Logged as `ViolationType.A2A_TASK_OWNERSHIP_VIOLATION`.

### R — Repudiation: Rejected Auth Attempts Not Audited

**Description**: Rejected 401/403 A2A requests were not written to Hermes's own
`a2a_audit.jsonl` (gap #81042; unconfirmed whether patched in v0.20.1) — a
security-relevant signal (who's probing the endpoint) invisible in Hermes's audit
trail.

**Mitigation**: AgentShroud logs every policy decision — ALLOW, DENY, and
auth-failure DENY (checked before `policy_engine.evaluate()` is ever called,
since an unauthenticated caller has no peer_id to evaluate) — through the same
audit path MCP governance already uses. This makes Hermes's own audit gap
irrelevant to AgentShroud's record.

### I — Information Disclosure / Elevation of Privilege: Unsandboxed Live-Session Injection

**Description**: Inbound A2A tasks are injected into Hermes's *live gateway
session* — the same conversation memory and tool access as the human operator's
own session — rather than a sandboxed clone. A malicious or compromised peer's
task therefore doesn't just talk to Hermes; it operates with the same effective
privilege as the operator for the duration of that task. This is a structural
Hermes design decision, not a bug to patch — it defines the ceiling of what a
successfully-authenticated-but-malicious peer can do, and is why default-deny
peer allow-listing (not just method-level policy) is the primary control.

**Mitigation**: `A2APolicyConfig.default_action = DENY` — unknown peers are
rejected outright, before any task is created. `SendStreamingMessage` (the
highest-bandwidth path into the live session) is classified high-risk,
requiring approval-queue sign-off rather than blanket allow even for known
peers. `owner_bypass` defaults `False` unconditionally for A2A — an external
peer is never treated as equivalent to the human operator.

### I — Information Disclosure: SSRF via Push-Notification Callback URLs

**Description**: Hermes's `is_safe_callback_url` SSRF guard on
`SetPushNotificationConfig` does string-prefix hostname matching, then only
re-validates canonical dotted-decimal IPv4 via `ipaddress.ip_address()` — decimal
(`2130706433`), hex (`0x7f000001`), octal (`0177.0.0.1`), and trailing-dot
(`localhost.`) encodings bypass both checks and resolve to blocked ranges
(127.0.0.1, the 169.254.169.254 cloud-metadata endpoint) despite the documented
guard (gap #78298). This is the same class of bug already present in this repo's
own `gateway/security/egress_filter.py::_is_private_ip` (~line 459-480) — noted
as a separate, pre-existing, repo-wide follow-up, not fixed as part of this
ticket's scope.

**Mitigation**: A dedicated hardened callback-URL validator in
`a2a_policy.py` explicitly parses decimal/hex/octal IPv4 literals and
trailing-dot hostnames *before* delegating to `ipaddress`, resolves hostnames
and checks the resolved IP (not just the literal) against private/link-local/
metadata-IP ranges, and re-checks on every use (not just at config-set time) to
guard against DNS rebinding. Rejection is logged as
`ViolationType.A2A_SSRF_CALLBACK_ATTEMPT` and placed in `severe_violation_types`
(immediate trust demotion) — a bypass attempt here is unambiguous malicious
intent, not an accident.

### E — Elevation of Privilege: Cross-Process Isolation Break

**Description**: Hermes's A2A adapter runs on a plain `threading.Thread`, not an
`asyncio.Task` (gap #77872), so Python contextvars used for per-profile
`HERMES_HOME` isolation don't propagate — inbound requests can silently resolve
to the process-wide default profile instead of the intended multi-tenant
profile, breaking trust-gate/audit/persistence isolation between tenants.

**Mitigation**: Detection/containment, not a fix — AgentShroud cannot patch
Hermes's internal thread/contextvar bug. But because `A2AProxy` (not Hermes)
resolves and attaches peer identity, and terminates one connection per request,
the identity AgentShroud recorded and audited stays correct in AgentShroud's own
trust ledger regardless of any internal cross-wiring on Hermes's side — any
resulting Hermes-side misattribution becomes a detectable discrepancy against
AgentShroud's audit trail rather than a silent, unlogged failure.

### Not Yet Mitigated (Explicitly Deferred)

- **Discovery reconnaissance**: `GET /.well-known/agent-card.json` is
  unauthenticated by spec design and intentionally passthrough (not
  policy-gated) — audited, not blocked. Accepted risk: this is the spec's own
  contract, not a Hermes-specific gap.
- **Outbound governance** (Hermes calling other peers): coarse peer-domain
  allow/deny only, riding the existing HTTP CONNECT-tunnel proxy — no
  method-level policy or PII scanning on outgoing `Message` content is possible
  without a materially larger TLS-interception project. Separate ticket.

## Threat Intelligence Integration

AgentShroud integrates with external threat intelligence feeds:

### Threat Feeds
- **DNS Threat Intelligence**: Real-time malicious domain feeds
- **IP Reputation**: Suspicious IP address databases
- **CVE Databases**: Vulnerability information for container images
- **Malware Signatures**: Pattern matching for known attack techniques

### Threat Scoring Matrix
```
Threat Level = Base Score + Context Multiplier + Historical Factor

Base Score:
├── CVE Score (0-10) × 0.3
├── Reputation Score (0-10) × 0.2
├── Pattern Confidence (0-10) × 0.3
└── Impact Assessment (0-10) × 0.2

Context Multiplier:
├── Agent Trust Level: 0.5x (Level 4) to 2.0x (Level 0)
├── Time of Day: 1.0x (business hours) to 1.5x (off-hours)
└── Network Location: 1.0x (internal) to 2.0x (external)
```

## Mitigation Coverage Matrix

| Threat Category | Primary Mitigation | Secondary Mitigation | Detection Method |
|-----------------|-------------------|---------------------|------------------|
| Agent Spoofing | Network Isolation | Mutual TLS | Behavioral Analysis |
| API Key Theft | Proxy-Side Storage | Key Rotation | Usage Monitoring |
| Log Tampering | Hash Chain | File Permissions | Chain Validation |
| PII Disclosure | Presidio Scanner | Error Sanitization | Pattern Detection |
| Resource DoS | Container Limits | Rate Limiting | Resource Monitoring |
| Prompt Injection | Pattern Matching | Unicode Normalization | Anomaly Detection |
| Container Escape | seccomp Profiles | Capability Dropping | Runtime Monitoring |
| A2A Identity Collapse | Trusted-Header Resolution | Bearer-Token Peer Mapping | Audit Trail |
| A2A Task Ownership Violation | Task-Owner Tracking | Default-Deny Peer Allowlist | Trust Ledger Decay |
| A2A SSRF (Callback URLs) | Hardened IP Canonicalization | Re-check on Every Use | Severe Violation Demotion |

This comprehensive threat model ensures AgentShroud addresses security risks across all STRIDE categories while providing layered defenses and comprehensive monitoring for threat detection and response.
