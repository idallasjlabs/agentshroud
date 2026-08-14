---
source_file: "docs/diagrams/images/diagram-14-logic-flow.svg"
type: "concept"
community: "Bot Skill Config"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# Isaiah decides (approved / rejected / timeout)

## Connections
- [[Approval queue (notify Isaiah via Telegram, wait up to 1 hour)]] - `calls` [EXTRACTED]
- [[Execute action via HTTP CONNECT proxy]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Bot_Skill_Config