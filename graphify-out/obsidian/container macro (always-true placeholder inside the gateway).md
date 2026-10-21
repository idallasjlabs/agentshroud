---
source_file: "docker/falco/rules.yaml"
type: "rationale"
community: "test_collaborator_tracker.py (4)"
location: "L11-L19"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_collaborator_trackerpy_4
---

# container macro (always-true placeholder inside the gateway)

## Connections
- [[Rule Container Shell Spawned]] - `references` [EXTRACTED]
- [[Rule Crypto Mining Detection]] - `references` [EXTRACTED]
- [[Rule File Access Outside Workspace]] - `references` [EXTRACTED]
- [[Rule Privilege Escalation Attempt]] - `references` [EXTRACTED]
- [[Rule Secret File Access]] - `references` [EXTRACTED]
- [[Rule Unexpected Outbound Connection from AgentShroud]] - `references` [EXTRACTED]
- [[gateway service (sole egress, FalcoClamAV in-process)]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_collaborator_trackerpy_4
