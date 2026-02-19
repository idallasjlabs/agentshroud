# IEC 62443 Compliance Matrix — AgentShroud

> Last updated: 2026-02-18 | AgentShroud v0.2.0

## Overview

IEC 62443 defines security levels (SL) for Industrial Automation and Control Systems (IACS). This matrix maps AgentShroud's security features to the seven Foundational Requirements (FR) across four security levels.

| Level | Description | Threat Actor |
|-------|-------------|-------------|
| SL 1 | Prevent unauthorized disclosure | Casual/unintentional |
| SL 2 | Prevent unauthorized disclosure using low resources | Motivated individual, low skill |
| SL 3 | Prevent unauthorized disclosure using moderate resources | Motivated group, moderate skill |
| SL 4 | Prevent unauthorized disclosure using extended resources | Nation-state, advanced capability |

## Current Assessment: **SL 2** (with SL 3 capabilities in several areas)

---

## FR 1: Identification and Authentication Control (IAC)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Human user ID & auth | ✅ | ✅ | ✅ | ⬜ | Telegram user ID + configurable `ALLOWED_USERS` allowlist | Implemented |
| Software process ID & auth | ✅ | ✅ | ⬜ | ⬜ | API token auth for gateway endpoints | Implemented |
| Unique identification | ✅ | ✅ | ✅ | ⬜ | Telegram numeric user IDs are globally unique | Implemented |
| Multi-factor auth | ⬜ | ⬜ | ⬜ | ⬜ | Not yet — relies on Telegram's own 2FA | Gap |
| Password/credential mgmt | ✅ | ✅ | ✅ | ⬜ | 1Password + Docker Secrets, no plaintext secrets | Implemented |

**Current Level: SL 2** | **Gap to SL 3:** Add MFA for sensitive operations (kill switch, SSH)

---

## FR 2: Use Control (UC)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Authorization enforcement | ✅ | ✅ | ✅ | ⬜ | Approval queue for privileged operations | Implemented |
| Least privilege | ✅ | ✅ | ✅ | ⬜ | Bot runs as unprivileged `agentshroud-bot` user | Implemented |
| Permission management | ✅ | ✅ | ⬜ | ⬜ | Role-based via allowed users config | Implemented |
| Session lock/termination | ✅ | ✅ | ✅ | ⬜ | Kill switch: freeze/shutdown/disconnect modes | Implemented |

**Current Level: SL 3** | **Gap to SL 4:** Fine-grained RBAC, session timeout policies

---

## FR 3: System Integrity (SI)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Communication integrity | ✅ | ✅ | ⬜ | ⬜ | Tailscale WireGuard encryption (in-transit) | Implemented |
| Input validation | ✅ | ✅ | ✅ | ⬜ | PII sanitizer scrubs all LLM-bound messages | Implemented |
| Malicious code protection | ✅ | ✅ | ⬜ | ⬜ | Credential blocking in command output | Implemented |
| Software integrity | ✅ | ⬜ | ⬜ | ⬜ | Container image from pinned base | Partial |

**Current Level: SL 2** | **Gap to SL 3:** Image signing/verification, SBOM generation

---

## FR 4: Data Confidentiality (DC)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Confidentiality at rest | ✅ | ✅ | ⬜ | ⬜ | Secrets in 1Password/Docker Secrets, not on disk | Implemented |
| Confidentiality in transit | ✅ | ✅ | ✅ | ⬜ | Tailscale (WireGuard), Telegram TLS | Implemented |
| PII protection | ✅ | ✅ | ✅ | ✅ | PII sanitizer with regex + pattern matching | Implemented |
| Credential protection | ✅ | ✅ | ✅ | ✅ | Credential blocker prevents leakage in output | Implemented |

**Current Level: SL 3** | **Gap to SL 4:** Encrypted audit ledger at rest

---

## FR 5: Restricted Data Flow (RDF)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Network segmentation | ✅ | ✅ | ⬜ | ⬜ | Docker bridge network, Tailscale ACLs | Implemented |
| Zone boundary protection | ✅ | ⬜ | ⬜ | ⬜ | Single-host deployment currently | Gap |
| Information flow control | ✅ | ✅ | ✅ | ⬜ | Sanitizer sits between user input and LLM | Implemented |

**Current Level: SL 2** | **Gap to SL 3:** Network policies, dedicated DMZ

---

## FR 6: Timely Response to Events (TRE)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Audit log accessibility | ✅ | ✅ | ✅ | ⬜ | Append-only audit ledger with dashboard view | Implemented |
| Continuous monitoring | ✅ | ✅ | ⬜ | ⬜ | Event bus for real-time security events | Implemented |
| Incident response | ✅ | ✅ | ✅ | ⬜ | Kill switch with three escalation modes | Implemented |
| Log integrity | ✅ | ✅ | ⬜ | ⬜ | Append-only design; no tamper-proofing yet | Partial |

**Current Level: SL 2** | **Gap to SL 3:** Cryptographic log integrity, SIEM integration

---

## FR 7: Resource Availability (RA)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Denial of service protection | ✅ | ⬜ | ⬜ | ⬜ | Rate limiting on Telegram side only | Gap |
| Resource management | ✅ | ✅ | ⬜ | ⬜ | Docker resource limits (planned) | Partial |
| System backup | ✅ | ⬜ | ⬜ | ⬜ | Manual backup procedures documented | Gap |
| System recovery | ✅ | ✅ | ⬜ | ⬜ | Docker Compose redeploy | Implemented |

**Current Level: SL 1** | **Gap to SL 2:** Automated backups, rate limiting, health checks

---

## Summary

| Foundational Requirement | Current SL | Target SL | Priority |
|---|:---:|:---:|---|
| FR 1: Identification & Auth | **2** | 3 | High — add MFA |
| FR 2: Use Control | **3** | 3 | ✅ Met |
| FR 3: System Integrity | **2** | 3 | Medium — image signing |
| FR 4: Data Confidentiality | **3** | 3 | ✅ Met |
| FR 5: Restricted Data Flow | **2** | 3 | Medium — network policies |
| FR 6: Timely Response | **2** | 3 | Medium — log integrity |
| FR 7: Resource Availability | **1** | 2 | High — backups, rate limiting |

**Overall AgentShroud Rating: SL 2**

### Key Components Referenced

| Component | IEC 62443 Role |
|---|---|
| PII Sanitizer | FR 4 (DC), FR 3 (SI) — data confidentiality, input validation |
| Credential Blocker | FR 4 (DC) — prevents credential leakage |
| Audit Ledger | FR 6 (TRE) — event logging, accountability |
| Kill Switch | FR 2 (UC), FR 6 (TRE) — session control, incident response |
| Approval Queue | FR 2 (UC) — authorization enforcement |
| Allowed Users | FR 1 (IAC) — identification and authentication |
| Docker Secrets | FR 4 (DC) — secret management at rest |
| Tailscale | FR 3 (SI), FR 4 (DC), FR 5 (RDF) — encrypted transport, segmentation |
