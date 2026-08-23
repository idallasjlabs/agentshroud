---
source_file: "docs/diagrams/images/diagram-09-data-lineage.png"
type: "concept"
community: "Diagram 09 Data Lineage (images)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Diagram_09_Data_Lineage_images
---

# SHA-256 content hashing (original_content_hash + sanitized content_hash)

## Connections
- [[PII Redaction (Presidio-style pattern matching PHONE_NUMBER, EMAIL_ADDRESS, SSN, etc.)]] - `shares_data_with` [EXTRACTED]
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Diagram_09_Data_Lineage_images