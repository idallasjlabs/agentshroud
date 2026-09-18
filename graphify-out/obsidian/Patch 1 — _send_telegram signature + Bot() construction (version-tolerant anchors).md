---
source_file: "docker/bots/hermes/patch_telegram_send_base_url.py"
type: "code"
community: "OpenClaw cron: AgentShroud Daily Check-in (disab"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/OpenClaw_cron_AgentShroud_Daily_Check-in_disab
---

# Patch 1 — _send_telegram signature + Bot() construction (version-tolerant anchors)

## Connections
- [[Vendor target _send_telegram (toolssend_message_tool.py or send_message_senders.py)]] - `references` [EXTRACTED]
- [[_read]] - `calls` [EXTRACTED]
- [[config.yaml seedupgrade — adds telegram.extra.base_url for gateway routing]] - `shares_data_with` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/OpenClaw_cron_AgentShroud_Daily_Check-in_disab