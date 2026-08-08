---
source_file: "gateway/security/group_workspace.py"
type: "code"
community: "Gateway Test Suite"
location: "L80"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# GroupWorkspaceManager

## Connections
- [[.__init__()_81]] - `method` [EXTRACTED]
- [[._group_workspace_manager()]] - `calls` [EXTRACTED]
- [[._is_owner()_1]] - `method` [EXTRACTED]
- [[._require_memory()]] - `method` [EXTRACTED]
- [[.append_dm_memory()]] - `method` [EXTRACTED]
- [[.append_group_memory()]] - `method` [EXTRACTED]
- [[.can_access()]] - `method` [EXTRACTED]
- [[.dm_workspace_id()]] - `method` [EXTRACTED]
- [[.group_workspace_id()]] - `method` [EXTRACTED]
- [[.read_dm_memory()]] - `method` [EXTRACTED]
- [[.read_group_memory()]] - `method` [EXTRACTED]
- [[.resolve_workspace()]] - `method` [EXTRACTED]
- [[.test_disabled_manager_denies_group_resolve()]] - `calls` [EXTRACTED]
- [[.test_disabled_manager_still_allows_dm()]] - `calls` [EXTRACTED]
- [[.test_group_keyed_by_raw_chat_id()]] - `calls` [EXTRACTED]
- [[.test_memory_helpers_require_shared_memory()]] - `calls` [EXTRACTED]
- [[.test_no_rbac_owner_check_is_false()]] - `calls` [EXTRACTED]
- [[.test_no_teams_config_fails_closed()]] - `calls` [EXTRACTED]
- [[.test_rbac_without_is_owner_callable()]] - `calls` [EXTRACTED]
- [[.test_two_members_of_same_group_share_one_workspace_id()]] - `calls` [EXTRACTED]
- [[Any_20]] - `uses` [INFERRED]
- [[GroupRoleResolver]] - `semantically_similar_to` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Resolve and access-control shared group workspaces.      Args         teams_con]] - `rationale_for` [EXTRACTED]
- [[SharedMemoryManager]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
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
- [[manager()_1]] - `calls` [EXTRACTED]
- [[rbac_config.py]] - `shares_data_with` [EXTRACTED]
- [[shared_memory.py]] - `shares_data_with` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[test_group_workspace_manager.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite