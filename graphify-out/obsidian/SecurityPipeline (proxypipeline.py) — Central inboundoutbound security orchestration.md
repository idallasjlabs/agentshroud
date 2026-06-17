---
source_file: "docs/security/security-inventory.md"
type: "code"
community: "Module Group 274"
location: "gateway/security/proxy/pipeline.py"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Module_Group_274
---

# SecurityPipeline (proxy/pipeline.py) — Central inbound/outbound security orchestration

## Connections
- [[58 Security Modules (Inbound 6, Outbound 6, PII 3, Access Control 7, NetworkEgress 6, MCPTool 6, Supply ChainBrowser 2, Audit 4, Infra 8, Encryption 3, External 4, Orchestration 3)]] - `includes` [EXTRACTED]
- [[AuditStore (audit_store.py) — SHA-256 tamper-evident hash chain]] - `writes_to` [INFERRED]
- [[EgressFilter (egress_filter.py) — Outbound domain allowlistdenylist, default-deny]] - `orchestrates` [EXTRACTED]
- [[PII Sanitizer (Presidio + regex, 0.9 confidence minimum)]] - `orchestrates` [EXTRACTED]
- [[PromptGuard (prompt_guard.py) — 49 regex patterns, 35+ languages, weighted scoring]] - `orchestrates` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Module_Group_274