---
source_file: "docs/diagrams/images/diagram-09-data-lineage.png"
type: "concept"
community: "Community 376"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Community_376
---

# ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)

## Connections
- [[Alert Thresholds (health check 3x10s, 200K token hard limit196K compaction trigger, 1h approval timeout, 90-day ledger retention, op-proxy 6 cascading retries)]] - `references` [EXTRACTED]
- [[Approval Queue (human-in-the-loop)_1]] - `shares_data_with` [EXTRACTED]
- [[Approval Queue State Diagram (pending → approvedrejectedexpired)]] - `shares_data_with` [EXTRACTED]
- [[Data Lineage Diagram (5-Layer Pipeline)]] - `conceptually_related_to` [EXTRACTED]
- [[Layer 4 — Processing (Bot LLM API call, MCP-inspected tool call)]] - `shares_data_with` [EXTRACTED]
- [[Layer 5 — Consumption (auto-delete at expires_at, audit query, user response)]] - `shares_data_with` [EXTRACTED]
- [[SHA-256 content hashing (original_content_hash + sanitized content_hash)]] - `shares_data_with` [EXTRACTED]
- [[Telegram Message Sequence Diagram]] - `conceptually_related_to` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Community_376