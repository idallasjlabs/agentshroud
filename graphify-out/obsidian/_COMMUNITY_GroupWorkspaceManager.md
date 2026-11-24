---
type: community
members: 68
---

# GroupWorkspaceManager

**Members:** 68 nodes

## Members
- [[dot-__init__()_33]] - code - gateway/security/group_workspace.py
- [[dot-_require_memory()]] - code - gateway/security/group_workspace.py
- [[dot-append_dm_memory()]] - code - gateway/security/group_workspace.py
- [[dot-append_group_memory()]] - code - gateway/security/group_workspace.py
- [[dot-can_access()]] - code - gateway/security/group_workspace.py
- [[dot-dm_workspace_id()]] - code - gateway/security/group_workspace.py
- [[dot-group_workspace_id()]] - code - gateway/security/group_workspace.py
- [[dot-read_dm_memory()]] - code - gateway/security/group_workspace.py
- [[dot-read_group_memory()]] - code - gateway/security/group_workspace.py
- [[dot-resolve_workspace()]] - code - gateway/security/group_workspace.py
- [[dot-test_disabled_manager_denies_group_resolve()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_disabled_manager_still_allows_dm()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_dm_context_needs_no_membership()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_dm_context_resolves_to_user_namespace()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_dm_workspace_id_differs_from_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_dm_write_invisible_from_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_enabled_default_true()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_group_a_write_invisible_from_group_b()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_group_keyed_by_raw_chat_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_group_write_invisible_from_dm()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_member_can_access_group_workspace()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_member_of_a_cannot_read_group_b_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_member_of_a_denied_group_b()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_member_resolves_to_shared_workspace_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_members_share_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_memory_helpers_require_shared_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_no_rbac_owner_check_is_false()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_no_teams_config_fails_closed()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_rbac_without_is_owner_callable()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_stranger_cannot_access()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_stranger_cannot_read_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_stranger_cannot_write_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_stranger_resolve_raises()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_system_owner_can_access_any_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_two_members_of_same_group_share_one_workspace_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_unknown_group_denied()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_workspace_ids_are_distinct_per_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[Append to a group's shared memory, gated by member access (fail-closed).]] - rationale - gateway/security/group_workspace.py
- [[Append to a user's private DM memory (isolated from every group).]] - rationale - gateway/security/group_workspace.py
- [[Canonical workspace id for a direct-message context ``dm-{user_id}``.]] - rationale - gateway/security/group_workspace.py
- [[Canonical workspace id for a group chat_id ``group-{chat_id}``.]] - rationale - gateway/security/group_workspace.py
- [[Group workspace manager — SCRUM-67 WS-A. Turns a Telegram GROUP into a shared…]] - rationale - gateway/security/group_workspace.py
- [[GroupAccessDenied]] - code - gateway/security/group_workspace.py
- [[GroupWorkspaceManager]] - code - gateway/security/group_workspace.py
- [[PermissionError]] - code
- [[Raised when a user is not permitted to access a group workspace. Subclasses…]] - rationale - gateway/security/group_workspace.py
- [[Read a group's shared memory, gated by member access (fail-closed).]] - rationale - gateway/security/group_workspace.py
- [[Read a user's private DM memory (isolated from every group).]] - rationale - gateway/security/group_workspace.py
- [[Resolve and access-control shared group workspaces. Args teams_config…]] - rationale - gateway/security/group_workspace.py
- [[Resolve the workspacecontext for an inbound message, fail-closed. Returns…]] - rationale - gateway/security/group_workspace.py
- [[Resolved workspacecontext identity for a single inbound message. Attributes…]] - rationale - gateway/security/group_workspace.py
- [[Return True if user_id may access the workspace for ``group_chat_id``. A DM…]] - rationale - gateway/security/group_workspace.py
- [[TDD — SCRUM-67 WS-A Group workspace manager. Enforces that a Telegram GROUP…]] - rationale - gateway/tests/test_group_workspace_manager.py
- [[TestConfigGate]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestCrossGroupIsolation]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestDefensiveGuards]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestDmIsolation]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestMembersShareGroupWorkspace]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestNonMemberDenied]] - code - gateway/tests/test_group_workspace_manager.py
- [[WorkspaceContext]] - code - gateway/security/group_workspace.py
- [[fixture_23]] - code
- [[group_workspace.py]] - code - gateway/security/group_workspace.py
- [[manager()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[rbac()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[session_manager()]] - code - gateway/tests/test_group_workspace_manager.py
- [[shared_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[teams()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[test_group_workspace_manager.py]] - code - gateway/tests/test_group_workspace_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GroupWorkspaceManager
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 5 edges to [[_COMMUNITY_SharedMemoryManager]]
- 5 edges to [[_COMMUNITY_TeamsConfig]]
- 5 edges to [[_COMMUNITY_UserSessionManager]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY_telegram_proxy.py]]
- 2 edges to [[_COMMUNITY_TestInboundChokepointWiring]]

## Top bridge nodes
- [[test_group_workspace_manager.py]] - degree 25, connects to 7 communities
- [[group_workspace.py]] - degree 11, connects to 5 communities
- [[GroupWorkspaceManager]] - degree 30, connects to 3 communities
- [[TestDefensiveGuards]] - degree 7, connects to 1 community
- [[fixture_23]] - degree 6, connects to 1 community
