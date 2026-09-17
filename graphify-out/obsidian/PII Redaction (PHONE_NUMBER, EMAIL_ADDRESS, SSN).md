---
source_file: "docs/diagrams/images/diagram-09-data-lineage.svg"
type: "concept"
community: "ledger row (id, timestamp, source, hashes, sanit"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/ledger_row_id_timestamp_source_hashes_sanit
---

# PII Redaction ([PHONE_NUMBER], [EMAIL_ADDRESS], [SSN])

## Connections
- [[content_hash = SHA-256(sanitized)]] - `calls` [EXTRACTED]
- [[ledger row (id, timestamp, source, hashes, sanitized flag, expires_at)]] - `shares_data_with` [EXTRACTED]
- [[original_content_hash = SHA-256(raw)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/ledger_row_id_timestamp_source_hashes_sanit