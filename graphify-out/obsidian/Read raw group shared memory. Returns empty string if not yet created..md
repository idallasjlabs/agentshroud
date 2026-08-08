---
source_file: "gateway/security/shared_memory.py"
type: "rationale"
community: "Group Workspace Isolation"
location: "L65"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# Read raw group shared memory. Returns empty string if not yet created.

## Connections
- [[.get_group_memory()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_Workspace_Isolation