---
source_file: "gateway/tests/test_group_workspace_manager.py"
type: "code"
community: "RBACConfig"
location: "L186"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/RBACConfig
---

# TestCrossGroupIsolation

## Connections
- [[.test_group_a_write_invisible_from_group_b()_1]] - `method` [EXTRACTED]
- [[.test_member_of_a_cannot_read_group_b_memory()]] - `method` [EXTRACTED]
- [[.test_member_of_a_denied_group_b()]] - `method` [EXTRACTED]
- [[.test_workspace_ids_are_distinct_per_group()]] - `method` [EXTRACTED]
- [[GroupAccessDenied]] - `uses` [INFERRED]
- [[GroupWorkspaceManager]] - `uses` [INFERRED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[SharedMemoryManager]] - `uses` [INFERRED]
- [[TeamsConfig_2]] - `uses` [INFERRED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_group_workspace_manager.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/RBACConfig