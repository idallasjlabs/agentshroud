---
source_file: "gateway/security/agent_isolation.py"
type: "code"
community: "Gateway Test Suite"
location: "L45"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# IsolationCheck

## Connections
- [[.verify_network_isolation()]] - `references` [EXTRACTED]
- [[.verify_shared_nothing()]] - `references` [EXTRACTED]
- [[.verify_volume_isolation()]] - `references` [EXTRACTED]
- [[ContainerConfig_1]] - `uses` [INFERRED]
- [[TestAgentRegistry]] - `uses` [INFERRED]
- [[TestGenerateCompose]] - `uses` [INFERRED]
- [[TestNetworkIsolation]] - `uses` [INFERRED]
- [[TestSharedNothing]] - `uses` [INFERRED]
- [[TestVolumeIsolation]] - `uses` [INFERRED]
- [[agent_isolation.py]] - `contains` [EXTRACTED]
- [[test_agent_isolation.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Gateway_Test_Suite