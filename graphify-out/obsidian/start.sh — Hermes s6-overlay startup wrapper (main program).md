---
source_file: "docker/bots/hermes/start.sh"
type: "code"
community: "_seed_cron"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_seed_cron
---

# start.sh — Hermes s6-overlay startup wrapper (main program)

## Connections
- [[Crash backoff escalation — 5 restarts600s pauses 300s (raw curl, helpers not yet defined)]] - `calls` [EXTRACTED]
- [[Post-migration model lock — resolve_model.py sets model.defaultprovider + cron.model after readiness]] - `calls` [EXTRACTED]
- [[init-config.sh (Hermes first-boot config materialisation)]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_seed_cron