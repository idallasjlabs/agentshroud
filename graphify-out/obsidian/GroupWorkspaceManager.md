---
source_file: "gateway/security/group_workspace.py"
type: "code"
community: "GroupWorkspaceManager"
location: "L80"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/GroupWorkspaceManager
---

# GroupWorkspaceManager

## Connections
- [[dot-__init__()_33]] - `method` [EXTRACTED]
- [[dot-_group_workspace_manager()]] - `calls` [EXTRACTED]
- [[dot-_is_owner()_1]] - `method` [EXTRACTED]
- [[dot-_require_memory()]] - `method` [EXTRACTED]
- [[dot-append_dm_memory()]] - `method` [EXTRACTED]
- [[dot-append_group_memory()]] - `method` [EXTRACTED]
- [[dot-can_access()]] - `method` [EXTRACTED]
- [[dot-dm_workspace_id()]] - `method` [EXTRACTED]
- [[dot-group_workspace_id()]] - `method` [EXTRACTED]
- [[dot-read_dm_memory()]] - `method` [EXTRACTED]
- [[dot-read_group_memory()]] - `method` [EXTRACTED]
- [[dot-resolve_workspace()]] - `method` [EXTRACTED]
- [[dot-test_disabled_manager_denies_group_resolve()]] - `calls` [EXTRACTED]
- [[dot-test_disabled_manager_still_allows_dm()]] - `calls` [EXTRACTED]
- [[dot-test_group_keyed_by_raw_chat_id()]] - `calls` [EXTRACTED]
- [[dot-test_memory_helpers_require_shared_memory()]] - `calls` [EXTRACTED]
- [[dot-test_no_rbac_owner_check_is_false()]] - `calls` [EXTRACTED]
- [[dot-test_no_teams_config_fails_closed()]] - `calls` [EXTRACTED]
- [[dot-test_rbac_without_is_owner_callable()]] - `calls` [EXTRACTED]
- [[dot-test_two_members_of_same_group_share_one_workspace_id()]] - `calls` [EXTRACTED]
- [[Resolve and access-control shared group workspaces. Args teams_config…]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[TestConfigGate]] - `uses` [INFERRED]
- [[TestDefensiveGuards]] - `uses` [INFERRED]
- [[TestMembersShareGroupWorkspace]] - `uses` [INFERRED]
- [[TestNonMemberDenied]] - `uses` [INFERRED]
- [[group_workspace.py]] - `contains` [EXTRACTED]
- [[manager()_1]] - `uses` [INFERRED]
- [[telegram_proxy.py_2]] - `imports` [EXTRACTED]
- [[test_group_workspace_manager.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/GroupWorkspaceManager
