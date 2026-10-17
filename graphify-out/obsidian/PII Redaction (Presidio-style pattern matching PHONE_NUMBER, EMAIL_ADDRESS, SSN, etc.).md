---
source_file: "docs/diagrams/images/diagram-09-data-lineage.png"
type: "concept"
community: "AgentShroud Development Roadmap — 2026 Gantt Chart"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AgentShroud_Development_Roadmap__2026_Gantt_Chart
---

# PII Redaction (Presidio-style pattern matching: PHONE_NUMBER, EMAIL_ADDRESS, SSN, etc.)

## Connections
- [[Data Lineage Diagram (5-Layer Pipeline)]] - `conceptually_related_to` [EXTRACTED]
- [[Layer 1 — Source (TelegramiMessageCron)]] - `shares_data_with` [EXTRACTED]
- [[PII redaction result (hash only in ledger, never persisted raw)]] - `semantically_similar_to` [INFERRED]
- [[SHA-256 content hashing (original_content_hash + sanitized content_hash)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/AgentShroud_Development_Roadmap__2026_Gantt_Chart
