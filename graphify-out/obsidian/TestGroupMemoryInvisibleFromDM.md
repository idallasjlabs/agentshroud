---
source_file: "gateway/tests/test_group_isolation.py"
type: "code"
community: "Shared Memory Write Acl"
location: "L147"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Shared_Memory_Write_Acl
---

# TestGroupMemoryInvisibleFromDM

## Connections
- [[.test_group_write_invisible_from_user_dm()]] - `method` [EXTRACTED]
- [[.test_merged_memory_separates_group_and_dm()]] - `method` [EXTRACTED]
- [[.test_user_dm_write_invisible_from_group()]] - `method` [EXTRACTED]
- [[.test_user_dm_write_invisible_from_other_group()]] - `method` [EXTRACTED]
- [[AgentRegistry]] - `uses` [INFERRED]
- [[ContainerConfig]] - `uses` [INFERRED]
- [[Group workspace content must not leak into any user's DM workspace.]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[SharedMemoryManager]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_group_isolation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Shared_Memory_Write_Acl