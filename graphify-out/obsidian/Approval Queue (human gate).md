---
source_file: "docs/diagrams/images/diagram-07-data-flow.svg"
type: "concept"
community: "Bot Skill Config"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# Approval Queue (human gate)

## Connections
- [[PII Sanitizer (Presidio  regex)]] - `shares_data_with` [EXTRACTED]
- [[Telegram API]] - `calls` [EXTRACTED]
- [[approval_queue.py]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Bot_Skill_Config