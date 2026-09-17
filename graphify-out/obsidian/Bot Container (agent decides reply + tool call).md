---
source_file: "docs/diagrams/images/diagram-15-sequence-telegram.svg"
type: "concept"
community: "Bot Container (agent decides: reply + tool call)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Bot_Container_agent_decides_reply__tool_call
---

# Bot Container (agent decides: reply + tool call)

## Connections
- [[Gateway (HMAC auth check, PII redaction via Presidio, route to agent)]] - `calls` [EXTRACTED]
- [[MCP inspection (injection scan NONE, PII scan NONE, sensitive op NONE)]] - `calls` [EXTRACTED]
- [[ledger.db (INSERT INTO ledger)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Bot_Container_agent_decides_reply__tool_call