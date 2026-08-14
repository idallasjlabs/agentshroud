---
source_file: "docker/bots/hermes/start.sh"
type: "rationale"
community: "Bot Skill Config"
location: "start.sh:27"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/Bot_Skill_Config
---

# Crash backoff escalation (5 restarts/600s -> 300s pause)

## Connections
- [[patch_telegram_do_request.py]] - `semantically_similar_to` [INFERRED]
- [[start.sh]] - `references` [EXTRACTED]

#graphify/rationale #graphify/INFERRED #community/Bot_Skill_Config