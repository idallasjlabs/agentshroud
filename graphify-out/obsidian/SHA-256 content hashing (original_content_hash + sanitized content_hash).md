---
source_file: "docs/diagrams/images/diagram-09-data-lineage.png"
type: "concept"
community: "Community 353"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Community_353
---

# SHA-256 content hashing (original_content_hash + sanitized content_hash)

## Connections
- [[PII Redaction (Presidio-style pattern matching PHONE_NUMBER, EMAIL_ADDRESS, SSN, etc.)]] - `shares_data_with` [EXTRACTED]
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Community_353