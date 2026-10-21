---
source_file: "docker/bots/hermes/start.sh"
type: "code"
community: "_make_cve"
location: "L177-L190"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_cve
---

# _release_telegram_lock

## Connections
- [[Crash backoff escalation (rolling 10-minute start window)]] - `conceptually_related_to` [INFERRED]
- [[_telegram_bot_token]] - `calls` [EXTRACTED]
- [[start.sh (Hermes s6 main program  startup wrapper)]] - `defines` [EXTRACTED]
- [[telegram_api_proxy()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_cve
