---
source_file: "/Users/ijefferson.admin/Development/agentshroud/docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md"
type: "concept"
community: "Module Group 450"
location: "Hash Chain Structure"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Module_Group_450
---

# Hash Chain Structure: sequence + timestamp + event_data + content_hash + previous_hash + chain_hash; validates every 1000 entries

## Connections
- [[ADR-005 SHA-256 Hash Chain for Audit Integrity]] - `defines` [EXTRACTED]
- [[Audit Ledger (SQLite + SHA-256 Hash Chain)]] - `implements` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Module_Group_450