---
source_file: "docs/vault/09 - Diagrams/Security Pipeline Flow.md"
type: "document"
community: "Module Group 105"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Module_Group_105
---

# Security Pipeline Flow Diagram

## Connections
- [[Approval Queue (Human-in-the-Loop for Sensitive Actions)]] - `describes` [EXTRACTED]
- [[EgressFilter (Network-level Outbound Control Module)]] - `describes` [EXTRACTED]
- [[Full System Flowchart Diagram]] - `references` [EXTRACTED]
- [[Monitor Mode (log-only, no enforcement)]] - `describes` [EXTRACTED]
- [[PII Sanitizer (Microsoft Presidio, 0.9 Confidence Minimum)]] - `describes` [EXTRACTED]
- [[PromptGuard (Prompt Injection and Jailbreak Detection)]] - `describes` [EXTRACTED]
- [[Security Pipeline Layers (Auth → Middleware → Input Norm → PII → PromptGuard → Egress → Pipeline → Proxy → Ledger → Approval)]] - `describes` [EXTRACTED]
- [[TrustManager (Cryptographic Agent Identity Verification)]] - `describes` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Module_Group_105