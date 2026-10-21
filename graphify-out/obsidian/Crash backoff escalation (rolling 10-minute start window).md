---
source_file: "docker/bots/hermes/start.sh"
type: "rationale"
community: "_make_cve"
location: "L27-L65"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_cve
---

# Crash backoff escalation (rolling 10-minute start window)

## Connections
- [[_release_telegram_lock]] - `conceptually_related_to` [INFERRED]
- [[start.sh (Hermes s6 main program  startup wrapper)]] - `implements` [EXTRACTED]
- [[telegram_api_proxy()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_cve
