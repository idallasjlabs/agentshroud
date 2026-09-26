---
source_file: "docker/bots/hermes/start.sh"
type: "rationale"
community: "MockValidator"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/MockValidator
---

# Crash backoff escalation — >5 restarts/600s pauses 300s (raw curl, helpers not yet defined)

## Connections
- [[_telegram_send()]] - `semantically_similar_to` [INFERRED]
- [[start.sh — Hermes s6-overlay startup wrapper (main program)]] - `calls` [EXTRACTED]

#graphify/rationale #graphify/INFERRED #community/MockValidator