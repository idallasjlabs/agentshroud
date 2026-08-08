---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "Group Workspace Isolation"
location: "L232"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# If the underlying session store raises, the authorized write reports         fai

## Connections
- [[.test_group_write_io_failure_returns_false()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_Workspace_Isolation