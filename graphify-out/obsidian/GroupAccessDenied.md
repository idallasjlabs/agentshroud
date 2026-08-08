---
source_file: "gateway/security/group_workspace.py"
type: "code"
community: "Group Workspace Isolation"
location: "L54"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Group_Workspace_Isolation
---

# GroupAccessDenied

## Connections
- [[.resolve_workspace()]] - `calls` [EXTRACTED]
- [[PermissionError]] - `inherits` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Raised when a user is not permitted to access a group workspace.      Subclasses]] - `rationale_for` [EXTRACTED]
- [[SharedMemoryManager]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[TestConfigGate]] - `uses` [INFERRED]
- [[TestCrossGroupIsolation]] - `uses` [INFERRED]
- [[TestDefensiveGuards]] - `uses` [INFERRED]
- [[TestDmIsolation]] - `uses` [INFERRED]
- [[TestInboundChokepointWiring]] - `uses` [INFERRED]
- [[TestMembersShareGroupWorkspace]] - `uses` [INFERRED]
- [[TestNonMemberDenied]] - `uses` [INFERRED]
- [[group_workspace.py]] - `contains` [EXTRACTED]
- [[test_group_workspace_manager.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Group_Workspace_Isolation