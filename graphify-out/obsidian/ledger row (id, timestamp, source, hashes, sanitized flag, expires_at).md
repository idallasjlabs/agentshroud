---
source_file: "docs/diagrams/images/diagram-09-data-lineage.svg"
type: "concept"
community: "ledger row (id, timestamp, source, hashes, sanit"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/ledger_row_id_timestamp_source_hashes_sanit
---

# ledger row (id, timestamp, source, hashes, sanitized flag, expires_at)

## Connections
- [[Audit query GET ledger (hashes only)]] - `shares_data_with` [EXTRACTED]
- [[Auto-delete at expires_at]] - `shares_data_with` [EXTRACTED]
- [[LLM API call (sanitized text only)]] - `calls` [EXTRACTED]
- [[PII Redaction (PHONE_NUMBER, EMAIL_ADDRESS, SSN)]] - `shares_data_with` [EXTRACTED]
- [[content_hash = SHA-256(sanitized)]] - `shares_data_with` [EXTRACTED]
- [[original_content_hash = SHA-256(raw)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/ledger_row_id_timestamp_source_hashes_sanit