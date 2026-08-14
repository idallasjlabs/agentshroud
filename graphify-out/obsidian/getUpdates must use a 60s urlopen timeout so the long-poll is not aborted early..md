---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Bot Skill Config"
location: "L4510"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# getUpdates must use a 60s urlopen timeout so the long-poll is not aborted early.

## Connections
- [[.test_long_poll_timeout_remains_60s()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Bot_Skill_Config