---
type: community
cohesion: 0.04
members: 77
---

# RBACConfig

**Cohesion:** 0.04 - loosely connected
**Members:** 77 nodes

## Members
- [[dot-__init__()_187]] - code - gateway/security/group_workspace.py
- [[dot-__init__()_188]] - code - gateway/security/shared_memory.py
- [[dot-_is_authorized_group_writer()]] - code - gateway/security/shared_memory.py
- [[dot-_is_owner()_1]] - code - gateway/security/group_workspace.py
- [[dot-_require_memory()]] - code - gateway/security/group_workspace.py
- [[dot-append_dm_memory()]] - code - gateway/security/group_workspace.py
- [[dot-append_group_memory()]] - code - gateway/security/group_workspace.py
- [[dot-append_to_group_memory()]] - code - gateway/security/shared_memory.py
- [[dot-append_to_user_memory()]] - code - gateway/security/shared_memory.py
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
- [[dot-test_group_a_write_invisible_from_group_b()_1]] - code - gateway/tests/test_group_workspace_manager.py
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
- [[Append a timestamped entry to the group shared memory file.          Authorizati]] - rationale - gateway/security/shared_memory.py
- [[Append content to user's private memory file.          Authorization (RT-5, WS-E]] - rationale - gateway/security/shared_memory.py
- [[Append to a group's shared memory, gated by member access (fail-closed).]] - rationale - gateway/security/group_workspace.py
- [[Append to a user's private DM memory (isolated from every group).]] - rationale - gateway/security/group_workspace.py
- [[Canonical workspace id for a direct-message context ``dm-{user_id}``.]] - rationale - gateway/security/group_workspace.py
- [[Canonical workspace id for a group chat_id ``group-{chat_id}``.]] - rationale - gateway/security/group_workspace.py
- [[GroupAccessDenied]] - code - gateway/security/group_workspace.py
- [[GroupWorkspaceManager]] - code - gateway/security/group_workspace.py
- [[High-level shared-memory API wrapping UserSessionManager storage.]] - rationale - gateway/security/shared_memory.py
- [[Raised when a user is not permitted to access a group workspace.      Subclasses]] - rationale - gateway/security/group_workspace.py
- [[Read a group's shared memory, gated by member access (fail-closed).]] - rationale - gateway/security/group_workspace.py
- [[Read a user's private DM memory (isolated from every group).]] - rationale - gateway/security/group_workspace.py
- [[Resolve and access-control shared group workspaces.      Args         teams_con]] - rationale - gateway/security/group_workspace.py
- [[Resolve the workspacecontext for an inbound message, fail-closed.          Retu]] - rationale - gateway/security/group_workspace.py
- [[Resolved workspacecontext identity for a single inbound message.      Attribute]] - rationale - gateway/security/group_workspace.py
- [[Return True if ``author_id`` may WRITE to ``group_id`` shared memory.          R]] - rationale - gateway/security/shared_memory.py
- [[Return True if user_id is the system owner (oversight override).]] - rationale - gateway/security/group_workspace.py
- [[Return True if user_id may access the workspace for ``group_chat_id``.]] - rationale - gateway/security/group_workspace.py
- [[SharedMemoryManager]] - code - gateway/security/shared_memory.py
- [[TestConfigGate]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestCrossGroupIsolation]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestDefensiveGuards]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestDmIsolation]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestMembersShareGroupWorkspace]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestNonMemberDenied]] - code - gateway/tests/test_group_workspace_manager.py
- [[WorkspaceContext]] - code - gateway/security/group_workspace.py
- [[group_workspace.py]] - code - gateway/security/group_workspace.py
- [[group_workspace.py (GroupWorkspaceManager)]] - code - gateway/security/group_workspace.py
- [[manager()_4]] - code - gateway/tests/test_group_workspace_manager.py
- [[rbac()_6]] - code - gateway/tests/test_group_workspace_manager.py
- [[session_manager()_4]] - code - gateway/tests/test_group_workspace_manager.py
- [[shared_memory()_2]] - code - gateway/tests/test_group_workspace_manager.py
- [[shared_memory.py]] - code - gateway/security/shared_memory.py
- [[teams()_4]] - code - gateway/tests/test_group_workspace_manager.py
- [[test_group_workspace_manager.py]] - code - gateway/tests/test_group_workspace_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RBACConfig
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_MiddlewareManager]]
- 13 edges to [[_COMMUNITY_telegram_proxy.py]]
- 10 edges to [[_COMMUNITY_UserSessionManager_3]]
- 8 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 7 edges to [[_COMMUNITY_DataLedger]]
- 7 edges to [[_COMMUNITY_ApprovalQueueConfig_8]]
- 6 edges to [[_COMMUNITY_EgressFilterConfig_3]]
- 4 edges to [[_COMMUNITY_diagramsREADME_1]]
- 4 edges to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]
- 3 edges to [[_COMMUNITY_telegram_proxy.py_1]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 1 edge to [[_COMMUNITY_dot-_enforce_group_workspace_access]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_GroupRoleResolver]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)_2]]

## Top bridge nodes
- [[SharedMemoryManager]] - degree 47, connects to 10 communities
- [[GroupWorkspaceManager]] - degree 42, connects to 8 communities
- [[test_group_workspace_manager.py]] - degree 22, connects to 6 communities
- [[GroupAccessDenied]] - degree 15, connects to 4 communities
- [[TestNonMemberDenied]] - degree 14, connects to 4 communities
