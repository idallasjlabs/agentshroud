---
source_file: "docker/bots/hermes/start.sh"
type: "rationale"
community: "_seed_cron"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_seed_cron
---

# Post-migration model lock — resolve_model.py sets model.default/provider + cron.model after readiness

## Connections
- [[Referenced resolve_model.py (usrlocallibagentshroudresolve_model.py)]] - `references` [EXTRACTED]
- [[Sandboxed terminal config — terminal.docker_ keys set via `hermes config set`, not env vars]] - `references` [EXTRACTED]
- [[_seed_cron]] - `shares_data_with` [INFERRED]
- [[start.sh — Hermes s6-overlay startup wrapper (main program)]] - `calls` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_seed_cron