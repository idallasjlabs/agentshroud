---
source_file: "gateway/tests/test_group_workspace_manager.py"
type: "code"
community: "Group Workspace Manager"
location: "L247"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Group_Workspace_Manager
---

# TestConfigGate

## Connections
- [[.test_disabled_manager_denies_group_resolve()]] - `method` [EXTRACTED]
- [[.test_disabled_manager_still_allows_dm()]] - `method` [EXTRACTED]
- [[.test_enabled_default_true()]] - `method` [EXTRACTED]
- [[GroupAccessDenied]] - `uses` [INFERRED]
- [[GroupWorkspaceManager]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[SharedMemoryManager]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_group_workspace_manager.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Group_Workspace_Manager