---
source_file: "docs/diagrams/images/diagram-07-data-flow.svg"
type: "concept"
community: "docs/diagrams"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/docs/diagrams
---

# PII Sanitizer (Presidio / regex)

## Connections
- [[Approval Queue (human gate)]] - `shares_data_with` [EXTRACTED]
- [[Audit Ledger (SHA-256 hash only)]] - `shares_data_with` [EXTRACTED]
- [[Execute Action (tool call  reply)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/docs/diagrams