---
source_file: "docs/diagrams/images/diagram-09-data-lineage.png"
type: "concept"
community: "Diagram 09 Data Lineage (images)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Diagram_09_Data_Lineage_images
---

# PII Redaction (Presidio-style pattern matching: PHONE_NUMBER, EMAIL_ADDRESS, SSN, etc.)

## Connections
- [[Data Lineage Diagram (5-Layer Pipeline)]] - `conceptually_related_to` [EXTRACTED]
- [[Layer 1 — Source (TelegramiMessageCron)]] - `shares_data_with` [EXTRACTED]
- [[PII redaction result (hash only in ledger, never persisted raw)]] - `semantically_similar_to` [INFERRED]
- [[SHA-256 content hashing (original_content_hash + sanitized content_hash)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Diagram_09_Data_Lineage_images