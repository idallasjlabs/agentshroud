---
source_file: "docker/scripts/colima-health-check.sh"
type: "rationale"
community: "AgentTarget (5)"
location: "docker/scripts/colima-health-check.sh:201"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AgentTarget_5
---

# Auto-start a stopped Colima VM (step 1a)

## Connections
- [[Dead docker.sock forward repair (step 1a-bis)]] - `conceptually_related_to` [EXTRACTED]
- [[_colima_vm_flags()]] - `references` [EXTRACTED]
- [[hc_run()]] - `references` [EXTRACTED]
- [[resolve_docker_host()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AgentTarget_5
