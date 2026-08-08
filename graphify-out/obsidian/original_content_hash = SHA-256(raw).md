---
source_file: "docs/diagrams/images/diagram-09-data-lineage.svg"
type: "concept"
community: "docs/diagrams"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/docs/diagrams
---

# original_content_hash = SHA-256(raw)

## Connections
- [[PII Redaction (PHONE_NUMBER, EMAIL_ADDRESS, SSN)]] - `calls` [EXTRACTED]
- [[Telegram message (raw user text)]] - `shares_data_with` [EXTRACTED]
- [[iMessage (raw user text)]] - `shares_data_with` [EXTRACTED]
- [[ledger row (id, timestamp, source, hashes, sanitized flag, expires_at)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/docs/diagrams