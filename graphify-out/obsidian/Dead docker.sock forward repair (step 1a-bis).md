---
source_file: "docker/scripts/colima-health-check.sh"
type: "rationale"
community: "AgentTarget"
location: "docker/scripts/colima-health-check.sh:239"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AgentTarget
---

# Dead docker.sock forward repair (step 1a-bis)

## Connections
- [[Auto-start a stopped Colima VM (step 1a)]] - `conceptually_related_to` [EXTRACTED]
- [[_bounce()]] - `references` [EXTRACTED]
- [[_colima_vm_flags()]] - `references` [EXTRACTED]
- [[_hc()]] - `references` [EXTRACTED]
- [[_upgrade_in_progress()]] - `references` [EXTRACTED]
- [[lazydocker docker.sock connection leak]] - `conceptually_related_to` [EXTRACTED]
- [[resolve_docker_host()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AgentTarget
