# IEC 62443 Compliance Matrix — AgentShroud

> Last updated: 2026-03-31 | AgentShroud v1.0.0

## Overview

IEC 62443 defines security levels (SL) for Industrial Automation and Control Systems (IACS). This matrix maps AgentShroud's security features to the seven Foundational Requirements (FR) across four security levels.

| Level | Description | Threat Actor |
|-------|-------------|-------------|
| SL 1 | Prevent unauthorized disclosure | Casual/unintentional |
| SL 2 | Prevent unauthorized disclosure using low resources | Motivated individual, low skill |
| SL 3 | Prevent unauthorized disclosure using moderate resources | Motivated group, moderate skill |
| SL 4 | Prevent unauthorized disclosure using extended resources | Nation-state, advanced capability |

## Current Assessment: **SL 2** (with SL 3 capabilities in FR 2, FR 3, FR 4, FR 6)

---

## FR 1: Identification and Authentication Control (IAC)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Human user ID & auth | ✅ | ✅ | ✅ | ⬜ | Telegram user ID + `ALLOWED_USERS` allowlist + RBAC Owner/Operator/Collaborator/Viewer roles | Implemented |
| Software process ID & auth | ✅ | ✅ | ⬜ | ⬜ | SCL session token auth for SOC endpoints; API token for gateway | Implemented |
| Unique identification | ✅ | ✅ | ✅ | ⬜ | Telegram numeric user IDs are globally unique; per-agent `agent_id` registration | Implemented |
| Multi-factor auth | ⬜ | ⬜ | ⬜ | ⬜ | Relies on Telegram's own 2FA — no native MFA layer | Gap |
| Password/credential mgmt | ✅ | ✅ | ✅ | ⬜ | 1Password CLI / macOS Keychain / Linux secret-tool / Docker Secrets; `setup-secrets.sh store/extract` workflow; no plaintext secrets on disk | Implemented |
| Privilege delegation | ✅ | ✅ | ✅ | ⬜ | `delegation.py` — time-bounded owner delegation with `DelegationToken`; auto-revoke on expiry | Implemented |

**Current Level: SL 2** | **Gap to SL 3:** Add MFA for sensitive operations (kill switch activation, SSH access)

---

## FR 2: Use Control (UC)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Authorization enforcement | ✅ | ✅ | ✅ | ⬜ | `EnhancedApprovalQueue` with SQLite persistence; tool-risk tier classification; approval required for `email_sending`, `file_deletion`, `external_api_calls`, `skill_installation` | Implemented |
| Least privilege | ✅ | ✅ | ✅ | ⬜ | Bot runs as unprivileged `agentshroud-bot` user (gosu); Seccomp + AppArmor profiles | Implemented |
| Permission management | ✅ | ✅ | ✅ | ⬜ | `tool_acl.py` — per-user/group tool allowlist/blocklist with PRIVATE/ADMIN/COLLABORATOR tiers; precedence: user deny > group deny > user allow > group allow | Implemented |
| Session lock/termination | ✅ | ✅ | ✅ | ⬜ | Kill switch: freeze/shutdown/disconnect modes; `ProgressiveLockdown` auto-escalates on repeated violations | Implemented |
| Use control for AI agents | ✅ | ✅ | ✅ | ⬜ | `SubagentMonitor`, `AgentRegistry`, `ToolChainAnalyzer` — per-agent action tracking and anomaly detection | Implemented |

**Current Level: SL 3** | **Gap to SL 4:** Session timeout policies; dynamic capability revocation

---

## FR 3: System Integrity (SI)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Communication integrity | ✅ | ✅ | ⬜ | ⬜ | Tailscale WireGuard encryption (in-transit); `InstructionEnvelope` HMAC signing for agent instructions | Implemented |
| Input validation | ✅ | ✅ | ✅ | ⬜ | PII sanitizer; `EncodingDetector` (base64/hex obfuscation); `ContextGuard`; `InputNormalizer` | Implemented |
| Malicious code protection | ✅ | ✅ | ✅ | ⬜ | ClamAV real-time scanning sidecar; `PromptGuard` injection detection; `HeuristicClassifier` | Implemented |
| Software integrity | ✅ | ✅ | ✅ | ⬜ | Cosign keyless image signing via Sigstore OIDC; Trivy CVE scanning; Syft SBOM (SPDX-JSON); Semgrep SAST (9 custom rules, CWE-78/22/798/918/502/89/532) | Implemented |
| Runtime integrity | ✅ | ✅ | ✅ | ⬜ | Falco runtime anomaly detection; `ConfigIntegrityMonitor` SHA-256 hashes `openclaw.json` at startup | Implemented |

**Current Level: SL 3** | **Gap to SL 4:** Signed audit log entries; hardware attestation (TPM)

---

## FR 4: Data Confidentiality (DC)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Confidentiality at rest | ✅ | ✅ | ⬜ | ⬜ | Secrets via 1Password CLI / Keychain / secret-tool / Docker Secrets; `EncryptedStore` for sensitive config | Implemented |
| Confidentiality in transit | ✅ | ✅ | ✅ | ⬜ | Tailscale WireGuard; Telegram TLS; SOC WebSocket over TLS | Implemented |
| PII protection | ✅ | ✅ | ✅ | ✅ | `PIISanitizer` (presidio 0.9 confidence minimum); regex engine for offline environments; all LLM-bound messages scrubbed | Implemented |
| Credential protection | ✅ | ✅ | ✅ | ✅ | `OutboundFilter` blocks credential patterns; `LogSanitizer` prevents secrets in logs; `XMLLeakFilter` prevents data exfiltration | Implemented |
| Service data privacy | ✅ | ✅ | ✅ | ⬜ | `privacy_policy.py` — service privacy tiers (private/shared/group_only); response content filtering | Implemented |

**Current Level: SL 3** | **Gap to SL 4:** Encrypted audit ledger at rest (hash chain exists; encryption deferred)

---

## FR 5: Restricted Data Flow (RDF)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Network segmentation | ✅ | ✅ | ⬜ | ⬜ | Docker bridge network; Tailscale ACLs; `DNSFilter` blocks unauthorized resolvers | Implemented |
| Zone boundary protection | ✅ | ⬜ | ⬜ | ⬜ | Single-host deployment; no dedicated DMZ or Kubernetes network policies | Gap |
| Information flow control | ✅ | ✅ | ✅ | ⬜ | `EgressFilter` + `EgressApproval` for all outbound; `OutboundFilter` blocks internal info disclosure; `WebContentScanner` inspects fetched pages | Implemented |
| Egress control | ✅ | ✅ | ✅ | ⬜ | Per-domain egress allowlist with TTL; `CONNECT_FORCE_BLOCK_DOMAINS` blocks CONNECT tunnel bypasses; port-level filtering | Implemented |

**Current Level: SL 2** | **Gap to SL 3:** Dedicated DMZ; network policy enforcement (requires multi-node deployment)

---

## FR 6: Timely Response to Events (TRE)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Audit log accessibility | ✅ | ✅ | ✅ | ⬜ | `AuditStore` + `AuditExport` (CEF format); SOC dashboard real-time view; JSONL audit trail | Implemented |
| Continuous monitoring | ✅ | ✅ | ✅ | ⬜ | Falco runtime monitoring; Wazuh FIM + SIEM agent; Fluent Bit log forwarding; `SOCCorrelation` event correlation | Implemented |
| Incident response | ✅ | ✅ | ✅ | ⬜ | Kill switch (freeze/shutdown/disconnect); Telegram owner alerts; `AlertDispatcher` with severity routing | Implemented |
| Log integrity | ✅ | ✅ | ✅ | ⬜ | `AuditStore` SHA-256 hash chain with `verify_hash_chain()` — each entry chains to the previous; tamper-evident append-only design | Implemented |

**Current Level: SL 3** | **Gap to SL 4:** Cryptographically signed log entries (hash chain implemented; signing deferred)

---

## FR 7: Resource Availability (RA)

| Requirement | SL1 | SL2 | SL3 | SL4 | AgentShroud Implementation | Status |
|---|:---:|:---:|:---:|:---:|---|---|
| Denial of service protection | ✅ | ✅ | ⬜ | ⬜ | `ProgressiveLockdown` rate limiting (5 req/hr for unknown users; escalates on violations); `NetworkValidator` connection limiting | Implemented |
| Resource management | ✅ | ✅ | ⬜ | ⬜ | Docker resource limits in compose files; `HealthReport` module with system metrics | Implemented |
| System backup | ✅ | ✅ | ⬜ | ⬜ | `backup-bot-memory.sh` + `restore-backup.sh` scripts; named volumes for memory persistence | Implemented |
| System recovery | ✅ | ✅ | ⬜ | ⬜ | Docker Compose redeploy; `docker-cleanup.sh` with BuildKit cache pruning; Colima VM restart procedures documented | Implemented |

**Current Level: SL 2** | **Gap to SL 3:** Automated scheduled backups; resource quotas per agent; active DoS mitigation

---

## Summary

| Foundational Requirement | v0.2.0 SL | v1.0.0 SL | Change | Remaining Gap |
|---|:---:|:---:|:---:|---|
| FR 1: Identification & Auth | **2** | **2** | — | MFA for sensitive ops |
| FR 2: Use Control | **3** | **3** | ✅ | Session timeout policies |
| FR 3: System Integrity | **2** | **3** | ⬆️ | Hardware attestation |
| FR 4: Data Confidentiality | **3** | **3** | ✅ | Encrypted audit ledger |
| FR 5: Restricted Data Flow | **2** | **2** | — | DMZ (multi-node only) |
| FR 6: Timely Response | **2** | **3** | ⬆️ | Signed log entries |
| FR 7: Resource Availability | **1** | **2** | ⬆️ | Scheduled backups, per-agent quotas |

**Overall AgentShroud v1.0.0 Rating: SL 2** (with SL 3 capabilities in FR 2, FR 3, FR 4, FR 6)

**Uplifts from v0.2.0 → v1.0.0:** FR 3 (image signing + Cosign + Trivy + Falco + Semgrep), FR 6 (SHA-256 hash chain + Wazuh SIEM), FR 7 (rate limiting + health report + backup scripts)

---

### Key Components Referenced (v1.0.0)

| Component | Module | IEC 62443 Role |
|---|---|---|
| PII Sanitizer | `gateway/ingest_api/sanitizer.py` | FR 4 (DC), FR 3 (SI) |
| Credential Blocker / OutboundFilter | `gateway/security/outbound_filter.py` | FR 4 (DC), FR 5 (RDF) |
| Audit Store (hash chain) | `gateway/security/audit_store.py` | FR 6 (TRE) — tamper-evident log |
| Kill Switch | `gateway/security/killswitch_monitor.py` | FR 2 (UC), FR 6 (TRE) |
| Approval Queue | `gateway/approval_queue/` | FR 2 (UC) |
| Tool ACL | `gateway/security/tool_acl.py` | FR 2 (UC) — per-user/group permission tiers |
| RBAC + Delegation | `gateway/security/rbac.py`, `delegation.py` | FR 1 (IAC), FR 2 (UC) |
| Egress Filter + Approval | `gateway/security/egress_filter.py`, `egress_approval.py` | FR 5 (RDF) |
| Progressive Lockdown | `gateway/security/progressive_lockdown.py` | FR 7 (RA), FR 2 (UC) |
| Prompt Guard + Heuristic Classifier | `gateway/security/prompt_guard.py`, `heuristic_classifier.py` | FR 3 (SI) |
| Encoding Detector | `gateway/security/encoding_detector.py` | FR 3 (SI) — obfuscation detection |
| Config Integrity Monitor | `gateway/security/config_integrity.py` | FR 3 (SI) — runtime config tamper detection |
| ClamAV Scanner | `gateway/security/clamav_scanner.py` | FR 3 (SI) — malware scanning |
| Falco Runtime Monitor | `docker/falco/` | FR 3 (SI), FR 6 (TRE) |
| Wazuh SIEM Agent | `docker/wazuh/` | FR 6 (TRE) — SIEM integration |
| Fluent Bit Log Forwarder | `docker/fluent-bit/` | FR 6 (TRE) — log aggregation |
| Cosign / Trivy / Syft | `scripts/security-scan.sh` | FR 3 (SI) — image signing, CVE scan, SBOM |
| Semgrep SAST | `.semgrep.yml` | FR 3 (SI) — CWE-78/22/798/918/502/89/532 |
| Encrypted Store + Key Vault | `gateway/security/encrypted_store.py`, `key_vault.py` | FR 4 (DC) |
| Docker Secrets + setup-secrets.sh | `docker/setup-secrets.sh` | FR 1 (IAC), FR 4 (DC) |
| Tailscale | Infrastructure | FR 3 (SI), FR 4 (DC), FR 5 (RDF) |
| SOC Dashboard + WebSocket | `gateway/soc/` | FR 6 (TRE) — real-time monitoring |
| Health Report | `gateway/security/health_report.py` | FR 7 (RA) |
| Backup Scripts | `scripts/backup-bot-memory.sh` | FR 7 (RA) |
