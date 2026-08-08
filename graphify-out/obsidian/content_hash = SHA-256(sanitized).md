---
source_file: "docs/diagrams/images/diagram-09-data-lineage.svg"
type: "concept"
community: "docs/diagrams"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/docs/diagrams
---

# content_hash = SHA-256(sanitized)

## Connections
- [[Cron trigger (no user content)]] - `shares_data_with` [EXTRACTED]
- [[PII Redaction (PHONE_NUMBER, EMAIL_ADDRESS, SSN)]] - `calls` [EXTRACTED]
- [[ledger row (id, timestamp, source, hashes, sanitized flag, expires_at)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/docs/diagrams