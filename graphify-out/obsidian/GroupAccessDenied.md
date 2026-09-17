---
source_file: "gateway/security/group_workspace.py"
type: "code"
community: "RBACConfig"
location: "L54"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/RBACConfig
---

# GroupAccessDenied

## Connections
- [[.resolve_workspace()]] - `calls` [EXTRACTED]
- [[PermissionError]] - `inherits` [EXTRACTED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[Raised when a user is not permitted to access a group workspace.      Subclasses]] - `rationale_for` [EXTRACTED]
- [[SharedMemoryManager]] - `uses` [INFERRED]
- [[TeamsConfig_2]] - `uses` [INFERRED]
- [[TestConfigGate]] - `uses` [INFERRED]
- [[TestCrossGroupIsolation]] - `uses` [INFERRED]
- [[TestDefensiveGuards]] - `uses` [INFERRED]
- [[TestDmIsolation]] - `uses` [INFERRED]
- [[TestInboundChokepointWiring]] - `uses` [INFERRED]
- [[TestMembersShareGroupWorkspace]] - `uses` [INFERRED]
- [[TestNonMemberDenied]] - `uses` [INFERRED]
- [[group_workspace.py]] - `contains` [EXTRACTED]
- [[test_group_workspace_manager.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/RBACConfig