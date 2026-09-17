---
source_file: "gateway/security/group_workspace.py"
type: "code"
community: "Community 53"
location: "L80"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_53
---

# GroupWorkspaceManager

## Connections
- [[dot-__init__()_159]] - `method` [EXTRACTED]
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
- [[Any_67]] - `uses` [INFERRED]
- [[GroupRoleResolver]] - `semantically_similar_to` [INFERRED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[Resolve and access-control shared group workspaces.      Args         teams_con]] - `rationale_for` [EXTRACTED]
- [[SharedMemoryManager]] - `uses` [INFERRED]
- [[TeamsConfig_2]] - `uses` [INFERRED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[TestConfigGate]] - `uses` [INFERRED]
- [[TestCrossGroupIsolation]] - `uses` [INFERRED]
- [[TestDefensiveGuards]] - `uses` [INFERRED]
- [[TestDmIsolation]] - `uses` [INFERRED]
- [[TestInboundChokepointWiring]] - `uses` [INFERRED]
- [[TestMembersShareGroupWorkspace]] - `uses` [INFERRED]
- [[TestNonMemberDenied]] - `uses` [INFERRED]
- [[_OutboundScan]] - `uses` [INFERRED]
- [[group_config.py]] - `shares_data_with` [EXTRACTED]
- [[group_workspace.py]] - `contains` [EXTRACTED]
- [[manager()_2]] - `calls` [EXTRACTED]
- [[rbac_config.py]] - `shares_data_with` [EXTRACTED]
- [[shared_memory.py]] - `shares_data_with` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[test_group_workspace_manager.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_53