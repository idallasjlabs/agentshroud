---
source_file: "gateway/tests/test_group_isolation.py"
type: "rationale"
community: "Group Workspace Isolation"
location: "L165"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# User DM content must not leak into a group the user is NOT a member of.

## Connections
- [[.test_user_dm_write_invisible_from_other_group()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_Workspace_Isolation