---
source_file: "docs/diagrams/images/diagram-09-data-lineage.png"
type: "image"
community: "Community 353"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/Community_353
---

# Layer 4 — Processing (Bot: LLM API call, MCP-inspected tool call)

## Connections
- [[Data Lineage Diagram (5-Layer Pipeline)]] - `conceptually_related_to` [EXTRACTED]
- [[Layer 5 — Consumption (auto-delete at expires_at, audit query, user response)]] - `shares_data_with` [EXTRACTED]
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - `shares_data_with` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/Community_353