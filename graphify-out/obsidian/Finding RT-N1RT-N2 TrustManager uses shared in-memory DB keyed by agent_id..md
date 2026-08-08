---
source_file: "gateway/tests/test_security_regressions_v1_2.py"
type: "rationale"
community: "Group Workspace Isolation"
location: "L161"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# Finding RT-N1/RT-N2: TrustManager uses shared in-memory DB keyed by agent_id.

## Connections
- [[TestCrossBotTrustPivot]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_Workspace_Isolation