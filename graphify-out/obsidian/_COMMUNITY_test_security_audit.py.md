---
type: community
cohesion: 0.02
members: 146
---

# test_security_audit.py

**Cohesion:** 0.02 - loosely connected
**Members:** 146 nodes

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
- [[.test_empty_author_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_enabled_default_true()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_foreign_writer_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_group_a_write_invisible_from_group_b()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_group_keyed_by_raw_chat_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_group_write_invisible_from_dm()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_group_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_legacy_no_author_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_manager_is_wired()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_allowed_in_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_authorized()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_member_can_access_group_workspace()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_contextvar_preserved()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_of_a_cannot_read_group_b_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_of_a_denied_group_b()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_member_resolves_to_shared_workspace_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_members_share_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_memory_helpers_require_shared_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_missing_rbac_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_no_rbac_owner_check_is_false()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_no_teams_config_fails_closed()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_non_member_blocked_in_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_non_member_contextvar_isolated_to_none()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_owner_allowed_in_any_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_owner_write_into_user_memory_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_rbac_without_is_owner_callable()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_run_standalone_sets_matching_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_self_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_stranger_cannot_access()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_cannot_read_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_cannot_write_group_memory()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_stranger_resolve_raises()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_system_owner_can_access_any_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_two_members_of_same_group_share_one_workspace_id()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_unknown_group_denied()]] - code - gateway/tests/test_group_workspace_manager.py
- [[.test_user_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_workspace_ids_are_distinct_per_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[A non-owner author cannot write into another user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user may write into their own private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[AgentRegistry must accept group-{chat_id} agent IDs with chat_type metadata.]] - rationale - gateway/tests/test_group_isolation.py
- [[An emptyNone author is never authorized.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Append a timestamped entry to the group shared memory file.          Authorizati]] - rationale - gateway/security/shared_memory.py
- [[Append content to user's private memory file.          Authorization (RT-5, WS-E]] - rationale - gateway/security/shared_memory.py
- [[Append to a group's shared memory, gated by member access (fail-closed).]] - rationale - gateway/security/group_workspace.py
- [[Append to a user's private DM memory (isolated from every group).]] - rationale - gateway/security/group_workspace.py
- [[Back-compat existing callers that pass no author_idrbac_config keep working.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Build merged memory context for bot prompt injection.          Includes]] - rationale - gateway/security/shared_memory.py
- [[Canonical workspace id for a direct-message context ``dm-{user_id}``.]] - rationale - gateway/security/group_workspace.py
- [[Canonical workspace id for a group chat_id ``group-{chat_id}``.]] - rationale - gateway/security/group_workspace.py
- [[GroupAccessDenied]] - code - gateway/security/group_workspace.py
- [[GroupWorkspaceManager]] - code - gateway/security/group_workspace.py
- [[Hermes's dashboard binds 127.0.0.1 inside its own container (vendor     hermes-a]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[High-level shared-memory API wrapping UserSessionManager storage.]] - rationale - gateway/security/shared_memory.py
- [[If the underlying session store raises, the authorized write reports         fai]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Isolated temporary workspace for session manager.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[No RBAC principal → cannot authorize → deny (fail-closed).]] - rationale - gateway/tests/test_shared_memory_write_acl.py
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
- [[Simulate the chokepoint a non-member's active group id is cleared.]] - rationale - gateway/tests/test_group_workspace_manager.py
- [[Test Group Config]] - code - gateway/tests/test_group_config.py
- [[TestAgentRegistryGroupIdentity]] - code - gateway/tests/test_group_isolation.py
- [[TestAuthorizationHelper]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestConfigGate]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestCrossGroupIsolation]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestDefensiveGuards]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestDmIsolation]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestHermesDashboardBridgeReachability]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestInboundChokepointWiring]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestMembersShareGroupWorkspace]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestNonMemberDenied]] - code - gateway/tests/test_group_workspace_manager.py
- [[TestUserMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestWriteFailurePath]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[The owner may write into any user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[WorkspaceContext]] - code - gateway/security/group_workspace.py
- [[agent_isolation.py (AgentRegistry)]] - code - gateway/security/agent_isolation.py
- [[group_workspace.py]] - code - gateway/security/group_workspace.py
- [[group_workspace.py (GroupWorkspaceManager)]] - code - gateway/security/group_workspace.py
- [[manager()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[rbac()]] - code - gateway/tests/test_group_isolation.py
- [[rbac()_2]] - code - gateway/tests/test_group_workspace_manager.py
- [[rbac()_5]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[run-standalone.sh is the actual deploy path for Hermes (docker run, not]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[session_manager()_1]] - code - gateway/tests/test_group_isolation.py
- [[session_manager()_2]] - code - gateway/tests/test_group_workspace_manager.py
- [[session_manager()_3]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[session_manager()_4]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[session_manager.py (UserSessionManager)]] - code - gateway/security/session_manager.py
- [[shared_memory()]] - code - gateway/tests/test_group_isolation.py
- [[shared_memory()_1]] - code - gateway/tests/test_group_workspace_manager.py
- [[shared_memory()_2]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[shared_memory.py]] - code - gateway/security/shared_memory.py
- [[shared_memory.py (SharedMemoryManager)]] - code - gateway/security/shared_memory.py
- [[smm()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[teams()_2]] - code - gateway/tests/test_group_isolation.py
- [[teams()_4]] - code - gateway/tests/test_group_workspace_manager.py
- [[test_group_isolation.py]] - code - gateway/tests/test_group_isolation.py
- [[test_group_workspace_manager.py]] - code - gateway/tests/test_group_workspace_manager.py
- [[test_security_regressions_v1_2.py]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[test_shared_memory_write_acl.py]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[tmp_workspace()]] - code - gateway/tests/test_group_isolation.py
- [[tmp_workspace()_1]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[trust_manager()_5]] - code - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_auditpy
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 23 edges to [[_COMMUNITY_MiddlewareManager]]
- 23 edges to [[_COMMUNITY_KeyVaultConfig]]
- 11 edges to [[_COMMUNITY_FileSandbox]]
- 11 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 8 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 7 edges to [[_COMMUNITY_The 8D Investigation Process]]
- 2 edges to [[_COMMUNITY_TestPathIsolationManager]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_check_message()]]
- 2 edges to [[_COMMUNITY_Core Principles]]
- 2 edges to [[_COMMUNITY_icloudscriptscalendar.js]]
- 2 edges to [[_COMMUNITY_TestAuditStore]]
- 2 edges to [[_COMMUNITY_Skill Hermes Dev Workflow (HDEV)]]
- 2 edges to [[_COMMUNITY_agentshroud.yaml]]
- 1 edge to [[_COMMUNITY_StdioConnection]]
- 1 edge to [[_COMMUNITY__make_stream_app_state()]]
- 1 edge to [[_COMMUNITY_EgressAction]]
- 1 edge to [[_COMMUNITY_SCLClient]]
- 1 edge to [[_COMMUNITY_Athena — Knowledge Distiller]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[SharedMemoryManager]] - degree 56, connects to 11 communities
- [[GroupWorkspaceManager]] - degree 42, connects to 7 communities
- [[test_group_isolation.py]] - degree 18, connects to 6 communities
- [[test_security_regressions_v1_2.py]] - degree 18, connects to 6 communities
- [[test_group_workspace_manager.py]] - degree 22, connects to 4 communities