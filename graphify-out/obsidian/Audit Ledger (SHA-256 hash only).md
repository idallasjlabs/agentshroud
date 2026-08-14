---
source_file: "docs/diagrams/images/diagram-07-data-flow.svg"
type: "concept"
community: "Bot Skill Config"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# Audit Ledger (SHA-256 hash only)

## Connections
- [[ADR-005 SHA-256 Hash Chain Audit Integrity]] - `conceptually_related_to` [EXTRACTED]
- [[MCP Inspector]] - `shares_data_with` [EXTRACTED]
- [[PII Sanitizer (Presidio + Regex)]] - `calls` [EXTRACTED]
- [[PII Sanitizer (Presidio  regex)]] - `shares_data_with` [EXTRACTED]
- [[SSH Proxy]] - `shares_data_with` [EXTRACTED]
- [[TrustManager_5]] - `calls` [EXTRACTED]
- [[ledger.db (90-day retention)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Bot_Skill_Config