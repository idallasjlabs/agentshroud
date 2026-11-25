---
type: community
members: 105
---

# SharedMemoryManager

**Members:** 105 nodes

## Members
- [[dot-__init__()_88]] - code - gateway/security/shared_memory.py
- [[dot-_is_authorized_group_writer()]] - code - gateway/security/shared_memory.py
- [[dot-_strip_private_content()]] - code - gateway/security/shared_memory.py
- [[dot-append_to_group_memory()]] - code - gateway/security/shared_memory.py
- [[dot-append_to_user_memory()]] - code - gateway/security/shared_memory.py
- [[dot-contains_private_content()]] - code - gateway/security/shared_memory.py
- [[dot-get_group_memory()]] - code - gateway/security/shared_memory.py
- [[dot-get_merged_memory_for_user()]] - code - gateway/security/shared_memory.py
- [[dot-get_topic_scoped_memory()]] - code - gateway/security/shared_memory.py
- [[dot-get_user_groups_by_id()]] - code - gateway/security/rbac_config.py
- [[dot-get_user_memory()]] - code - gateway/security/shared_memory.py
- [[dot-is_owner()_3]] - code - gateway/security/rbac_config.py
- [[dot-test_active_group_appears_first()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_append_to_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_append_to_user_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_clean_text_not_flagged()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_collaborator_gets_filtered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_api_key_pattern()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_bearer_token()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_private_section_header()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_empty_author_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_foreign_writer_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_get_group_memory_empty_initially()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_get_user_memory_returns_string()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_group_write_invisible_from_user_dm()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_legacy_no_author_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_member_authorized()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_merged_memory_separates_group_and_dm()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_missing_rbac_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_multiple_appends_accumulate()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_owner_gets_unfiltered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_owner_sees_all_groups()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_owner_write_into_user_memory_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_self_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_strip_private_content_redacts_api_key()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_strip_private_section()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_topic_scoped_excludes_non_matching_project_scoped_group()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_topic_scoped_includes_local_only_group()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_topic_scoped_returns_matching_group()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_unknown_user_sees_only_private_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_dm_write_invisible_from_group()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_user_dm_write_invisible_from_other_group()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_user_does_not_see_other_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_memory_isolated_between_users()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_sees_own_private_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_sees_their_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[A non-owner author cannot write into another user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user may write into their own private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[An emptyNone author is never authorized.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Append a timestamped entry to the group shared memory file. Authorization…]] - rationale - gateway/security/shared_memory.py
- [[Append content to user's private memory file. Authorization (RT-5, WS-E HIGH)…]] - rationale - gateway/security/shared_memory.py
- [[Back-compat existing callers that pass no author_idrbac_config keep working.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Build merged memory context for bot prompt injection. Includes 1. User's own…]] - rationale - gateway/security/shared_memory.py
- [[Check if user is the owner (any platform).]] - rationale - gateway/security/rbac_config.py
- [[Content written to a group must not appear in any user's private DM memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content written to a user DM must not appear in any group memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Group workspace content must not leak into any user's DM workspace.]] - rationale - gateway/tests/test_group_isolation.py
- [[High-level shared-memory API wrapping UserSessionManager storage.]] - rationale - gateway/security/shared_memory.py
- [[If the underlying session store raises, the authorized write reports failure…]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[No RBAC principal → cannot authorize → deny (fail-closed).]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Read raw group shared memory. Returns empty string if not yet created.]] - rationale - gateway/security/shared_memory.py
- [[Read raw private memory for a user. Args user_id The user whose memory to…]] - rationale - gateway/security/shared_memory.py
- [[Remove private-looking content from shared memory before serving to non-owner…]] - rationale - gateway/security/shared_memory.py
- [[Return True if ``author_id`` may WRITE to ``group_id`` shared memory. RT-5…]] - rationale - gateway/security/shared_memory.py
- [[Return True if text contains patterns matching privatesensitive content.]] - rationale - gateway/security/shared_memory.py
- [[Return member IDs of a group, or empty list if no teams config.]] - rationale - gateway/security/rbac_config.py
- [[Return memory from groups whose focus_topics match the query text. For…]] - rationale - gateway/security/shared_memory.py
- [[SharedMemoryManager]] - code - gateway/security/shared_memory.py
- [[TDD — WS-E finding RT-5 (HIGH) shared-memory write access control. Before this…]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[TDD — Workstream A (v1.2.0) Group memory namespace isolation. Tests that -…]] - rationale - gateway/tests/test_group_isolation.py
- [[TestAuthorizationHelper]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestGroupMemoryInvisibleFromDM]] - code - gateway/tests/test_group_isolation.py
- [[TestGroupMemoryReadWrite]] - code - gateway/tests/test_shared_memory.py
- [[TestMergedMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestPrivateContentDetection]] - code - gateway/tests/test_shared_memory.py
- [[TestTopicScopedMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestUserMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestUserPrivateMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestWriteFailurePath]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[Tests for gatewaysecurityshared_memory.py — V9-T1 Group shared memory +…]] - rationale - gateway/tests/test_shared_memory.py
- [[The owner may write into any user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[User DM content must not leak into a group the user is NOT a member of.]] - rationale - gateway/tests/test_group_isolation.py
- [[_boom()_21]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[_boom()_22]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[fixture_64]] - code
- [[fixture_65]] - code
- [[fixture_66]] - code
- [[get_merged_memory_for_user returns group section and private section separately.]] - rationale - gateway/tests/test_group_isolation.py
- [[rbac()_2]] - code - gateway/tests/test_group_isolation.py
- [[rbac()_3]] - code - gateway/tests/test_shared_memory.py
- [[rbac()_4]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[session_manager()_2]] - code - gateway/tests/test_group_isolation.py
- [[session_manager()_3]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[session_mgr()]] - code - gateway/tests/test_shared_memory.py
- [[shared_memory()_1]] - code - gateway/tests/test_group_isolation.py
- [[shared_memory()_2]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[smm()_1]] - code - gateway/tests/test_shared_memory.py
- [[teams()_3]] - code - gateway/tests/test_group_isolation.py
- [[test_group_isolation.py]] - code - gateway/tests/test_group_isolation.py
- [[test_shared_memory.py]] - code - gateway/tests/test_shared_memory.py
- [[test_shared_memory_write_acl.py]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[tmp_workspace()_1]] - code - gateway/tests/test_group_isolation.py
- [[tmp_workspace()_2]] - code - gateway/tests/test_shared_memory.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SharedMemoryManager
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_UserSessionManager]]
- 12 edges to [[_COMMUNITY_RBACConfig]]
- 9 edges to [[_COMMUNITY_TeamsConfig]]
- 4 edges to [[_COMMUNITY_AgentRegistry]]
- 3 edges to [[_COMMUNITY_GroupWorkspaceManager]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 1 edge to [[_COMMUNITY_TestGroupMemoryWriteACL]]
- 1 edge to [[_COMMUNITY_TestGroupMemoryNamespaceIsolation]]

## Top bridge nodes
- [[SharedMemoryManager]] - degree 27, connects to 5 communities
- [[test_group_isolation.py]] - degree 20, connects to 5 communities
- [[test_shared_memory_write_acl.py]] - degree 16, connects to 4 communities
- [[test_shared_memory.py]] - degree 18, connects to 3 communities
- [[dot-is_owner()_3]] - degree 7, connects to 2 communities
