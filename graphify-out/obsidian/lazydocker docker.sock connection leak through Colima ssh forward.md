---
source_file: "INCIDENT_2026-10-16_conduit-outage.md"
type: "rationale"
community: "run-standalone.sh (Hermes docker run launcher)"
location: "L205-L222"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/run-standalonesh_Hermes_docker_run_launcher
---

# lazydocker docker.sock connection leak through Colima ssh forward

## Connections
- [[Compose version mismatch forces network recreate + stale endpoints]] - `conceptually_related_to` [EXTRACTED]
- [[Incident 2026-10-16 ConduitHermes instability record]] - `references` [EXTRACTED]
- [[Sunday-upgrade no-op gate hardening (CLAUDE.md section 0.0)]] - `conceptually_related_to` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/run-standalonesh_Hermes_docker_run_launcher
