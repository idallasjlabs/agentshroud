---
source_file: "docs/vault/00 - START HERE/System Overview.md"
type: "concept"
community: "Security Docs"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Security_Docs
---

# Security Pipeline Layers (Auth → Middleware → Input Norm → PII → PromptGuard → Egress → Pipeline → Proxy → Ledger → Approval)

## Connections
- [[AgentShroud System Overview]] - `describes` [EXTRACTED]
- [[Architecture Overview — AgentShroud]] - `describes` [EXTRACTED]
- [[Auth Module (Bearer token + token-bucket rate limiter, hmac.compare_digest)]] - `includes` [EXTRACTED]
- [[DataLedger (SQLite WAL, SHA-256 hash chain, privacy-by-design — hashes only, 90-day retention)]] - `includes` [EXTRACTED]
- [[Full System Flowchart Diagram]] - `describes` [EXTRACTED]
- [[Security Pipeline Flow]] - `describes` [EXTRACTED]
- [[main.py — Gateway Core Module]] - `implements` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Security_Docs