---
source_file: "gateway/tests/test_group_isolation.py"
type: "code"
community: "Group Workspace Isolation"
location: "L95"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# TestGroupMemoryNamespaceIsolation

## Connections
- [[.test_group_a_write_invisible_from_group_b()]] - `method` [EXTRACTED]
- [[.test_group_b_write_invisible_from_group_a()]] - `method` [EXTRACTED]
- [[.test_group_id_uses_group_prefix_namespace()]] - `method` [EXTRACTED]
- [[.test_group_memory_physically_isolated()]] - `method` [EXTRACTED]
- [[.test_group_writes_are_independent_namespaces()]] - `method` [EXTRACTED]
- [[AgentRegistry]] - `uses` [INFERRED]
- [[ContainerConfig]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[SharedMemoryManager]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[Writes in group-A must not be readable from group-B.]] - `rationale_for` [EXTRACTED]
- [[test_group_isolation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Group_Workspace_Isolation