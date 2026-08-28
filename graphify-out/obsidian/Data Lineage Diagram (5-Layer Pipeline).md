---
source_file: "docs/diagrams/images/diagram-09-data-lineage.png"
type: "image"
community: "Community 376"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/Community_376
---

# Data Lineage Diagram (5-Layer Pipeline)

## Connections
- [[Layer 1 — Source (TelegramiMessageCron)]] - `conceptually_related_to` [EXTRACTED]
- [[Layer 4 — Processing (Bot LLM API call, MCP-inspected tool call)]] - `conceptually_related_to` [EXTRACTED]
- [[Layer 5 — Consumption (auto-delete at expires_at, audit query, user response)]] - `conceptually_related_to` [EXTRACTED]
- [[PII Redaction (Presidio-style pattern matching PHONE_NUMBER, EMAIL_ADDRESS, SSN, etc.)]] - `conceptually_related_to` [EXTRACTED]
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - `conceptually_related_to` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/Community_376