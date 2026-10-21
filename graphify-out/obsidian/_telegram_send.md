---
source_file: "docker/bots/hermes/start.sh"
type: "code"
community: "_make_cve"
location: "L98-L115"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_cve
---

# _telegram_send

## Connections
- [[LLMProxy._emit_failover_notice]] - `semantically_similar_to` [INFERRED]
- [[_telegram_alert()]] - `semantically_similar_to` [INFERRED]
- [[_telegram_bot_token]] - `calls` [EXTRACTED]
- [[start.sh (Hermes s6 main program  startup wrapper)]] - `defines` [EXTRACTED]
- [[start.sh script]] - `calls` [EXTRACTED]
- [[telegram_api_proxy()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_cve
