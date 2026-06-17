---
source_file: "docs/vault/00 - START HERE/System Overview.md"
type: "concept"
community: "Module Group 105"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Module_Group_105
---

# Security Pipeline Layers (Auth → Middleware → Input Norm → PII → PromptGuard → Egress → Pipeline → Proxy → Ledger → Approval)

## Connections
- [[AgentShroud System Overview]] - `describes` [EXTRACTED]
- [[Approval Queue (Human-in-the-Loop for Sensitive Actions)]] - `includes` [EXTRACTED]
- [[Architecture Overview — AgentShroud]] - `describes` [EXTRACTED]
- [[Auth Module (Bearer token + token-bucket rate limiter, hmac.compare_digest)]] - `includes` [EXTRACTED]
- [[DataLedger (SQLite WAL, SHA-256 hash chain, privacy-by-design — hashes only, 90-day retention)]] - `includes` [EXTRACTED]
- [[EgressFilter (Network-level Outbound Control Module)]] - `includes` [EXTRACTED]
- [[Full System Flowchart Diagram]] - `describes` [EXTRACTED]
- [[PII Sanitizer (Microsoft Presidio, 0.9 Confidence Minimum)]] - `includes` [EXTRACTED]
- [[PromptGuard (Prompt Injection and Jailbreak Detection)]] - `contains` [INFERRED]
- [[Security Pipeline Flow Diagram]] - `describes` [EXTRACTED]
- [[TrustManager (Cryptographic Agent Identity Verification)]] - `contains` [INFERRED]
- [[main.py — Gateway Core Module]] - `implements` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Module_Group_105