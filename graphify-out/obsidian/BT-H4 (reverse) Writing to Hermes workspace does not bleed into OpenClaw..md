---
source_file: "gateway/tests/test_security_regressions_v1_2.py"
type: "rationale"
community: "Group Workspace Isolation"
location: "L107"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# BT-H4 (reverse): Writing to Hermes workspace does not bleed into OpenClaw.

## Connections
- [[.test_hermes_memory_write_does_not_appear_in_openclaw_memory()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_Workspace_Isolation