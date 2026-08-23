---
type: community
cohesion: 0.04
members: 76
---

# Group Workspace Manager

**Cohesion:** 0.04 - loosely connected
**Members:** 76 nodes

## Members
- [[.__init__()_84]] - code - gateway/security/group_workspace.py
- [[._is_owner()_1]] - code - gateway/security/group_workspace.py
- [[._require_memory()]] - code - gateway/security/group_workspace.py
- [[.append_dm_memory()]] - code - gateway/security/group_workspace.py
- [[.append_group_memory()]] - code - gateway/security/group_workspace.py
- [[.can_access()]] - code - gateway/security/group_workspace.py
- [[.dm_workspace_id()]] - code - gateway/security/group_workspace.py
- [[.group_workspace_id()]] - code - gateway/security/group_workspace.py
- [[.proxy()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.read_dm_memory()]] - code - gateway/security/group_workspace.py
- [[.read_group_memory()]] - code - gateway/security/group_workspace.py
- [[.resolve_workspace()]] - code - gateway/security/group_workspace.py
- [[.test_cross_group_member_blocked()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_disabled_gate_returns_none_manager()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_disabled_manager_denies_group_resolve()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_disabled_manager_still_allows_dm()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_dm_context_needs_no_membership()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_dm_context_resolves_to_user_namespace()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_dm_workspace_id_differs_from_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_dm_write_invisible_from_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_enabled_default_true()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_group_a_write_invisible_from_group_b()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_group_keyed_by_raw_chat_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_group_write_invisible_from_dm()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_manager_is_wired()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_allowed_in_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_can_access_group_workspace()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_contextvar_preserved()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_of_a_cannot_read_group_b_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_of_a_denied_group_b()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_resolves_to_shared_workspace_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_members_share_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_memory_helpers_require_shared_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_no_rbac_owner_check_is_false()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_no_teams_config_fails_closed()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_non_member_blocked_in_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_non_member_contextvar_isolated_to_none()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_owner_allowed_in_any_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_rbac_without_is_owner_callable()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_cannot_access()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_cannot_read_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_cannot_write_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_resolve_raises()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_system_owner_can_access_any_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_two_members_of_same_group_share_one_workspace_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_unknown_group_denied()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_workspace_ids_are_distinct_per_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[Append to a group's shared memory, gated by member access (fail-closed).]] - rationale - gateway/security/group_workspace.py
- [[Append to a user's private DM memory (isolated from every group).]] - rationale - gateway/security/group_workspace.py
- [[Canonical workspace id for a direct-message context ``dm-{user_id}``.]] - rationale - gateway/security/group_workspace.py
- [[Canonical workspace id for a group chat_id ``group-{chat_id}``.]] - rationale - gateway/security/group_workspace.py
- [[GroupAccessDenied]] - code - gateway/security/group_workspace.py
- [[GroupWorkspaceManager]] - code - gateway/security/group_workspace.py
- [[Raised when a user is not permitted to access a group workspace.      Subclasses]] - rationale - gateway/security/group_workspace.py
- [[Read a group's shared memory, gated by member access (fail-closed).]] - rationale - gateway/security/group_workspace.py
- [[Read a user's private DM memory (isolated from every group).]] - rationale - gateway/security/group_workspace.py
- [[Resolve and access-control shared group workspaces.      Args         teams_con]] - rationale - gateway/security/group_workspace.py
- [[Resolve the workspacecontext for an inbound message, fail-closed.          Retu]] - rationale - gateway/security/group_workspace.py
- [[Return True if user_id is the system owner (oversight override).]] - rationale - gateway/security/group_workspace.py
- [[Return True if user_id may access the workspace for ``group_chat_id``.]] - rationale - gateway/security/group_workspace.py
- [[Simulate the chokepoint a non-member's active group id is cleared.]] - rationale - gateway/tests/test_group_workspace_manager.py
- [[TestConfigGate]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestCrossGroupIsolation]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestDefensiveGuards]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestDmIsolation]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestInboundChokepointWiring]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestMembersShareGroupWorkspace]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestNonMemberDenied]] - code - gateway/tests/test_group_workspace_manager.py
- [[group_workspace.py (GroupWorkspaceManager)]] - code - gateway/security/group_workspace.py
- [[manager()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[rbac()_2]] - code - gateway/tests/test_group_workspace_manager.py
- [[session_manager()_2]] - code - gateway/tests/test_group_workspace_manager.py
- [[shared_memory()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[shared_memory.py]] - code - gateway/security/shared_memory.py
- [[teams()_4]] - code - gateway/tests/test_group_workspace_manager.py
- [[test_group_workspace_manager.py]] - code - gateway/tests/test_group_workspace_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Group_Workspace_Manager
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_Shared Memory Write Acl]]
- 14 edges to [[_COMMUNITY_Group Config & Collaborator Responses]]
- 12 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 12 edges to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 10 edges to [[_COMMUNITY_Middleware & Session Isolation]]
- 1 edge to [[_COMMUNITY_Progressive Lockdown]]
- 1 edge to [[_COMMUNITY_Group Rbac]]
- 1 edge to [[_COMMUNITY_Soc Services Coverage]]
- 1 edge to [[_COMMUNITY_Rbac Config (security)]]

## Top bridge nodes
- [[GroupWorkspaceManager]] - degree 42, connects to 7 communities
- [[test_group_workspace_manager.py]] - degree 22, connects to 5 communities
- [[TestInboundChokepointWiring]] - degree 17, connects to 5 communities
- [[TestNonMemberDenied]] - degree 14, connects to 5 communities
- [[TestDmIsolation]] - degree 13, connects to 5 communities