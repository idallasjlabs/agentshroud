---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "Group Workspace Isolation"
location: "L129"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# The owner may write into any group's memory.

## Connections
- [[.test_owner_write_succeeds()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_Workspace_Isolation