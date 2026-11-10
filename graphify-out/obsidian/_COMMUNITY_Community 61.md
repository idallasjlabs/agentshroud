---
type: community
members: 88
---

# Community 61

**Members:** 88 nodes

## Members
- [[.__init__()_84]] - code - gateway/security/group_workspace.py
- [[.__init__()_117]] - code - gateway/security/shared_memory.py
- [[._is_authorized_group_writer()]] - code - gateway/security/shared_memory.py
- [[._is_owner()_1]] - code - gateway/security/group_workspace.py
- [[._require_memory()]] - code - gateway/security/group_workspace.py
- [[._strip_private_content()]] - code - gateway/security/shared_memory.py
- [[.append_dm_memory()]] - code - gateway/security/group_workspace.py
- [[.append_group_memory()]] - code - gateway/security/group_workspace.py
- [[.append_to_group_memory()]] - code - gateway/security/shared_memory.py
- [[.append_to_user_memory()]] - code - gateway/security/shared_memory.py
- [[.can_access()]] - code - gateway/security/group_workspace.py
- [[.contains_private_content()]] - code - gateway/security/shared_memory.py
- [[.dm_workspace_id()]] - code - gateway/security/group_workspace.py
- [[.get_group_memory()]] - code - gateway/security/shared_memory.py
- [[.get_merged_memory_for_user()]] - code - gateway/security/shared_memory.py
- [[.get_topic_scoped_memory()]] - code - gateway/security/shared_memory.py
- [[.get_user_memory()]] - code - gateway/security/shared_memory.py
- [[.group_workspace_id()]] - code - gateway/security/group_workspace.py
- [[.read_dm_memory()]] - code - gateway/security/group_workspace.py
- [[.read_group_memory()]] - code - gateway/security/group_workspace.py
- [[.resolve_workspace()]] - code - gateway/security/group_workspace.py
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
- [[.test_member_can_access_group_workspace()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_of_a_cannot_read_group_b_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_of_a_denied_group_b()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_resolves_to_shared_workspace_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_members_share_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_memory_helpers_require_shared_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_no_rbac_owner_check_is_false()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_no_teams_config_fails_closed()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_rbac_without_is_owner_callable()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_cannot_access()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_cannot_read_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_cannot_write_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_resolve_raises()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_system_owner_can_access_any_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_two_members_of_same_group_share_one_workspace_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_unknown_group_denied()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_workspace_ids_are_distinct_per_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[Append a timestamped entry to the group shared memory file.          Authorizati]] - rationale - gateway/security/shared_memory.py
- [[Append content to user's private memory file.          Authorization (RT-5, WS-E]] - rationale - gateway/security/shared_memory.py
- [[Append to a group's shared memory, gated by member access (fail-closed).]] - rationale - gateway/security/group_workspace.py
- [[Append to a user's private DM memory (isolated from every group).]] - rationale - gateway/security/group_workspace.py
- [[Build merged memory context for bot prompt injection.          Includes]] - rationale - gateway/security/shared_memory.py
- [[Canonical workspace id for a direct-message context ``dm-{user_id}``.]] - rationale - gateway/security/group_workspace.py
- [[Canonical workspace id for a group chat_id ``group-{chat_id}``.]] - rationale - gateway/security/group_workspace.py
- [[GroupAccessDenied]] - code - gateway/security/group_workspace.py
- [[GroupWorkspaceManager]] - code - gateway/security/group_workspace.py
- [[High-level shared-memory API wrapping UserSessionManager storage.]] - rationale - gateway/security/shared_memory.py
- [[Raised when a user is not permitted to access a group workspace.      Subclasses]] - rationale - gateway/security/group_workspace.py
- [[Read a group's shared memory, gated by member access (fail-closed).]] - rationale - gateway/security/group_workspace.py
- [[Read a user's private DM memory (isolated from every group).]] - rationale - gateway/security/group_workspace.py
- [[Read raw group shared memory. Returns empty string if not yet created.]] - rationale - gateway/security/shared_memory.py
- [[Read raw private memory for a user.          Args             user_id The user]] - rationale - gateway/security/shared_memory.py
- [[Remove private-looking content from shared memory before serving         to non-]] - rationale - gateway/security/shared_memory.py
- [[Resolve and access-control shared group workspaces.      Args         teams_con]] - rationale - gateway/security/group_workspace.py
- [[Resolve the workspacecontext for an inbound message, fail-closed.          Retu]] - rationale - gateway/security/group_workspace.py
- [[Resolved workspacecontext identity for a single inbound message.      Attribute]] - rationale - gateway/security/group_workspace.py
- [[Return True if ``author_id`` may WRITE to ``group_id`` shared memory.          R]] - rationale - gateway/security/shared_memory.py
- [[Return True if text contains patterns matching privatesensitive content.]] - rationale - gateway/security/shared_memory.py
- [[Return True if user_id is the system owner (oversight override).]] - rationale - gateway/security/group_workspace.py
- [[Return True if user_id may access the workspace for ``group_chat_id``.]] - rationale - gateway/security/group_workspace.py
- [[Return memory from groups whose focus_topics match the query text.          For]] - rationale - gateway/security/shared_memory.py
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
- [[manager()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[rbac()_2]] - code - gateway/tests/test_group_workspace_manager.py
- [[session_manager()_2]] - code - gateway/tests/test_group_workspace_manager.py
- [[shared_memory()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[smm()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[test_group_workspace_manager.py]] - code - gateway/tests/test_group_workspace_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_61
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Community 196]]
- 13 edges to [[_COMMUNITY_Community 6]]
- 12 edges to [[_COMMUNITY_Community 1]]
- 9 edges to [[_COMMUNITY_Community 1305]]
- 8 edges to [[_COMMUNITY_Community 14]]
- 7 edges to [[_COMMUNITY_Community 60]]
- 4 edges to [[_COMMUNITY_Community 223]]
- 4 edges to [[_COMMUNITY_Community 1289]]
- 4 edges to [[_COMMUNITY_Community 479]]
- 2 edges to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 96]]
- 1 edge to [[_COMMUNITY_Community 2036]]
- 1 edge to [[_COMMUNITY_Community 33]]
- 1 edge to [[_COMMUNITY_Community 20]]
- 1 edge to [[_COMMUNITY_Community 181]]
- 1 edge to [[_COMMUNITY_Community 52]]

## Top bridge nodes
- [[SharedMemoryManager]] - degree 56, connects to 9 communities
- [[GroupWorkspaceManager]] - degree 42, connects to 9 communities
- [[test_group_workspace_manager.py]] - degree 22, connects to 6 communities
- [[GroupAccessDenied]] - degree 15, connects to 4 communities
- [[TestNonMemberDenied]] - degree 14, connects to 4 communities