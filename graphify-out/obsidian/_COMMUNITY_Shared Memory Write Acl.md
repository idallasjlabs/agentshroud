---
type: community
cohesion: 0.02
members: 126
---

# Shared Memory Write Acl

**Cohesion:** 0.02 - loosely connected
**Members:** 126 nodes

## Members
- [[.__init__()_117]] - code - gateway/security/shared_memory.py
- [[._is_authorized_group_writer()]] - code - gateway/security/shared_memory.py
- [[._strip_private_content()]] - code - gateway/security/shared_memory.py
- [[.append_to_group_memory()]] - code - gateway/security/shared_memory.py
- [[.append_to_user_memory()]] - code - gateway/security/shared_memory.py
- [[.contains_private_content()]] - code - gateway/security/shared_memory.py
- [[.get_group_memory()]] - code - gateway/security/shared_memory.py
- [[.get_merged_memory_for_user()]] - code - gateway/security/shared_memory.py
- [[.get_topic_scoped_memory()]] - code - gateway/security/shared_memory.py
- [[.get_user_memory()]] - code - gateway/security/shared_memory.py
- [[.test_active_group_appears_first()]] - code - gateway/tests/test_shared_memory.py
- [[.test_append_to_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_append_to_user_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_clean_text_not_flagged()]] - code - gateway/tests/test_shared_memory.py
- [[.test_collaborator_gets_filtered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_cross_group_member_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_detects_api_key_pattern()]] - code - gateway/tests/test_shared_memory.py
- [[.test_detects_bearer_token()]] - code - gateway/tests/test_shared_memory.py
- [[.test_detects_private_section_header()]] - code - gateway/tests/test_shared_memory.py
- [[.test_empty_author_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_foreign_writer_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_get_group_memory_empty_initially()]] - code - gateway/tests/test_shared_memory.py
- [[.test_get_user_memory_returns_string()]] - code - gateway/tests/test_shared_memory.py
- [[.test_group_a_write_invisible_from_group_b()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_b_write_invisible_from_group_a()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_id_uses_group_prefix_namespace()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_memory_physically_isolated()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_write_invisible_from_user_dm()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_group_writes_are_independent_namespaces()]] - code - gateway/tests/test_group_isolation.py
- [[.test_legacy_no_author_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_legacy_no_rbac_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_member_authorized()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_member_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_merged_memory_separates_group_and_dm()]] - code - gateway/tests/test_group_isolation.py
- [[.test_missing_rbac_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_multiple_appends_accumulate()]] - code - gateway/tests/test_shared_memory.py
- [[.test_non_member_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_owner_gets_unfiltered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_owner_sees_all_groups()]] - code - gateway/tests/test_shared_memory.py
- [[.test_owner_write_into_user_memory_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_owner_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_self_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_strip_private_content_redacts_api_key()]] - code - gateway/tests/test_shared_memory.py
- [[.test_strip_private_section()]] - code - gateway/tests/test_shared_memory.py
- [[.test_topic_scoped_excludes_non_matching_project_scoped_group()]] - code - gateway/tests/test_shared_memory.py
- [[.test_topic_scoped_includes_local_only_group()]] - code - gateway/tests/test_shared_memory.py
- [[.test_topic_scoped_returns_matching_group()]] - code - gateway/tests/test_shared_memory.py
- [[.test_unknown_group_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_unknown_user_sees_only_private_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_user_dm_write_invisible_from_group()]] - code - gateway/tests/test_group_isolation.py
- [[.test_user_dm_write_invisible_from_other_group()]] - code - gateway/tests/test_group_isolation.py
- [[.test_user_does_not_see_other_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_user_memory_isolated_between_users()]] - code - gateway/tests/test_shared_memory.py
- [[.test_user_sees_own_private_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_user_sees_their_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_user_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[A legitimate group member's write lands.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A member of group B cannot write into group A's memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A non-owner author cannot write into another user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user may write into their own private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user who is NOT a member of the target group cannot poison its memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[An emptyNone author is never authorized.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Append a timestamped entry to the group shared memory file.          Authorizati]] - rationale - gateway/security/shared_memory.py
- [[Append content to user's private memory file.          Authorization (RT-5, WS-E]] - rationale - gateway/security/shared_memory.py
- [[Back-compat existing callers that pass no author_idrbac_config keep working.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Back-compat with no RBAC context supplied, the namespace-isolation         call]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Both groups store separate content with no cross-contamination.]] - rationale - gateway/tests/test_group_isolation.py
- [[Build merged memory context for bot prompt injection.          Includes]] - rationale - gateway/security/shared_memory.py
- [[Content appended to group-A memory must not appear in group-B memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content appended to group-B must not appear in group-A memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content written to a group must not appear in any user's private DM memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content written to a user DM must not appear in any group memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Group workspace content must not leak into any user's DM workspace.]] - rationale - gateway/tests/test_group_isolation.py
- [[High-level shared-memory API wrapping UserSessionManager storage.]] - rationale - gateway/security/shared_memory.py
- [[If the underlying session store raises, the authorized write reports         fai]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[No RBAC principal → cannot authorize → deny (fail-closed).]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Read raw group shared memory. Returns empty string if not yet created.]] - rationale - gateway/security/shared_memory.py
- [[Read raw private memory for a user.          Args             user_id The user]] - rationale - gateway/security/shared_memory.py
- [[Remove private-looking content from shared memory before serving         to non-]] - rationale - gateway/security/shared_memory.py
- [[Resolved workspacecontext identity for a single inbound message.      Attribute]] - rationale - gateway/security/group_workspace.py
- [[Return True if ``author_id`` may WRITE to ``group_id`` shared memory.          R]] - rationale - gateway/security/shared_memory.py
- [[Return True if text contains patterns matching privatesensitive content.]] - rationale - gateway/security/shared_memory.py
- [[Return memory from groups whose focus_topics match the query text.          For]] - rationale - gateway/security/shared_memory.py
- [[SharedMemoryManager]] - code - gateway/security/shared_memory.py
- [[Test Group Config]] - code - gateway/tests/test_group_config.py
- [[TestAuthorizationHelper]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestGroupMemoryInvisibleFromDM]] - code - gateway/tests/test_group_isolation.py
- [[TestGroupMemoryNamespaceIsolation]] - code - gateway/tests/test_group_isolation.py
- [[TestGroupMemoryReadWrite]] - code - gateway/tests/test_shared_memory.py
- [[TestGroupMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestMergedMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestPrivateContentDetection]] - code - gateway/tests/test_shared_memory.py
- [[TestTopicScopedMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestUserMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestUserPrivateMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestWriteFailurePath]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[The owner may write into any group's memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[The owner may write into any user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[User DM content must not leak into a group the user is NOT a member of.]] - rationale - gateway/tests/test_group_isolation.py
- [[WorkspaceContext]] - code - gateway/security/group_workspace.py
- [[Writes in group-A must not be readable from group-B.]] - rationale - gateway/tests/test_group_isolation.py
- [[Writing to a group that does not exist in the RBAC config is denied.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[agent_isolation.py (AgentRegistry)]] - code - gateway/security/agent_isolation.py
- [[get_merged_memory_for_user returns group section and private section separately.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-A and group-B memory files must be in separate directories.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-{chat_id} sessions must live under the 'groups' subdirectory.]] - rationale - gateway/tests/test_group_isolation.py
- [[group_config.py (TeamsConfig)]] - code - gateway/security/group_config.py
- [[group_workspace.py]] - code - gateway/security/group_workspace.py
- [[rbac()]] - code - gateway/tests/test_group_isolation.py
- [[rbac()_4]] - code - gateway/tests/test_shared_memory.py
- [[rbac()_5]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[session_manager()_1]] - code - gateway/tests/test_group_isolation.py
- [[session_manager()_4]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[session_manager.py (UserSessionManager)]] - code - gateway/security/session_manager.py
- [[session_mgr()]] - code - gateway/tests/test_shared_memory.py
- [[shared_memory()]] - code - gateway/tests/test_group_isolation.py
- [[shared_memory()_2]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[shared_memory.py (SharedMemoryManager)]] - code - gateway/security/shared_memory.py
- [[smm()_1]] - code - gateway/tests/test_shared_memory.py
- [[teams()_2]] - code - gateway/tests/test_group_isolation.py
- [[test_group_isolation.py]] - code - gateway/tests/test_group_isolation.py
- [[test_shared_memory.py]] - code - gateway/tests/test_shared_memory.py
- [[test_shared_memory_write_acl.py]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[tmp_workspace()]] - code - gateway/tests/test_group_isolation.py
- [[tmp_workspace()_2]] - code - gateway/tests/test_shared_memory.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Shared_Memory_Write_Acl
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 19 edges to [[_COMMUNITY_Group Config & Collaborator Responses]]
- 18 edges to [[_COMMUNITY_Middleware & Session Isolation]]
- 17 edges to [[_COMMUNITY_Group Workspace Manager]]
- 11 edges to [[_COMMUNITY_Security Regressions V1 2]]
- 8 edges to [[_COMMUNITY_Security Hardening]]
- 2 edges to [[_COMMUNITY_SOC Router (Collaborator Mgmt)]]
- 1 edge to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Session Manager]]

## Top bridge nodes
- [[SharedMemoryManager]] - degree 56, connects to 6 communities
- [[test_group_isolation.py]] - degree 19, connects to 4 communities
- [[TestGroupMemoryNamespaceIsolation]] - degree 13, connects to 4 communities
- [[TestGroupMemoryInvisibleFromDM]] - degree 12, connects to 4 communities
- [[session_manager.py (UserSessionManager)]] - degree 6, connects to 4 communities