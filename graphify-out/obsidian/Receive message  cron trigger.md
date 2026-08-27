---
source_file: "docs/diagrams/images/diagram-07-data-flow.svg"
type: "concept"
community: "Community 409"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Community_409
---

# Receive message / cron trigger

## Connections
- [[Cron Scheduler (8 scheduled jobs)]] - `calls` [EXTRACTED]
- [[LLM Inference (OpenAI  Anthropic)]] - `calls` [EXTRACTED]
- [[Telegram Input (@agentshroud_bot)]] - `calls` [EXTRACTED]
- [[Web UI Input (localhost18790)]] - `calls` [EXTRACTED]
- [[agentshroud-config volume (openclaw.json)]] - `shares_data_with` [EXTRACTED]
- [[iMessage Input (imsg-ssh bridge)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Community_409