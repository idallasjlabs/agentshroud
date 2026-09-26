---
source_file: "docker/falco/rules.yaml"
type: "rationale"
community: "TestOutboundClassifierHelpers"
location: "L11-L19"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestOutboundClassifierHelpers
---

# container macro (always-true placeholder inside the gateway)

## Connections
- [[Gateway Service]] - `references` [EXTRACTED]
- [[Rule Container Shell Spawned]] - `references` [EXTRACTED]
- [[Rule Crypto Mining Detection]] - `references` [EXTRACTED]
- [[Rule File Access Outside Workspace]] - `references` [EXTRACTED]
- [[Rule Privilege Escalation Attempt]] - `references` [EXTRACTED]
- [[Rule Secret File Access]] - `references` [EXTRACTED]
- [[Rule Unexpected Outbound Connection from AgentShroud]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestOutboundClassifierHelpers