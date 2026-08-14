---
source_file: "docs/diagrams/images/diagram-15-sequence-telegram.svg"
type: "concept"
community: "Bot Skill Config"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# Bot Container (agent decides: reply + tool call)

## Connections
- [[Gateway (HMAC auth check, PII redaction via Presidio, route to agent)]] - `calls` [EXTRACTED]
- [[MCP inspection (injection scan NONE, PII scan NONE, sensitive op NONE)]] - `calls` [EXTRACTED]
- [[ledger.db (INSERT INTO ledger)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Bot_Skill_Config