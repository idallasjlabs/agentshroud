---
type: community
cohesion: 0.02
members: 112
---

# Community 27

**Cohesion:** 0.02 - loosely connected
**Members:** 112 nodes

## Members
- [[.get_active_project_for_user()]] - code - gateway/security/group_config.py
- [[.get_all_member_ids()]] - code - gateway/security/group_config.py
- [[.get_group_admin_ids()]] - code - gateway/security/group_config.py
- [[.get_group_safe_response_prefix()]] - code - gateway/security/group_config.py
- [[.get_user_collab_mode()]] - code - gateway/security/group_config.py
- [[.get_user_groups()]] - code - gateway/security/group_config.py
- [[.get_user_projects()]] - code - gateway/security/group_config.py
- [[.is_admin()]] - code - gateway/security/group_config.py
- [[.is_group_admin()]] - code - gateway/security/group_config.py
- [[.is_member()]] - code - gateway/security/group_config.py
- [[.model_post_init()_1]] - code - gateway/security/group_config.py
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
- [[.test_group_write_invisible_from_user_dm()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
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
- [[Back-compat existing callers that pass no author_idrbac_config keep working.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Back-compat with no RBAC context supplied, the namespace-isolation         call]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Content written to a group must not appear in any user's private DM memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content written to a user DM must not appear in any group memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Group workspace content must not leak into any user's DM workspace.]] - rationale - gateway/tests/test_group_isolation.py
- [[If the underlying session store raises, the authorized write reports         fai]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Merge group_overrides.json additions into the in-memory TeamsConfig.]] - rationale - gateway/security/group_config.py
- [[No RBAC principal → cannot authorize → deny (fail-closed).]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Return all groups the user belongs to.]] - rationale - gateway/security/group_config.py
- [[Return all projects accessible to the user via group membership.]] - rationale - gateway/security/group_config.py
- [[Return deduplicated list of all user IDs across all groups.]] - rationale - gateway/security/group_config.py
- [[Return mapping of group_id → admin_user_id for all groups that have an admin.]] - rationale - gateway/security/group_config.py
- [[Return the effective collab_mode for a user.          Resolution order]] - rationale - gateway/security/group_config.py
- [[Return the first project accessible to a user (primary project).]] - rationale - gateway/security/group_config.py
- [[Return the safe_response_prefix for the first group that the user belongs to]] - rationale - gateway/security/group_config.py
- [[TeamsConfig]] - code - gateway/security/group_config.py
- [[Test Group Config]] - code - gateway/tests/test_group_config.py
- [[TestAuthorizationHelper]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestGroupMemoryInvisibleFromDM]] - code - gateway/tests/test_group_isolation.py
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
- [[Top-level teams configuration parsed from agentshroud.yaml `teams` section.]] - rationale - gateway/security/group_config.py
- [[User DM content must not leak into a group the user is NOT a member of.]] - rationale - gateway/tests/test_group_isolation.py
- [[Writing to a group that does not exist in the RBAC config is denied.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[_apply_persisted_overrides()]] - code - gateway/security/group_config.py
- [[agent_isolation.py (AgentRegistry)]] - code - gateway/security/agent_isolation.py
- [[get_merged_memory_for_user returns group section and private section separately.]] - rationale - gateway/tests/test_group_isolation.py
- [[group_config.py (TeamsConfig)]] - code - gateway/security/group_config.py
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
TABLE source_file, type FROM #community/Community_27
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_RBAC & SOC Realtime]]
- 20 edges to [[_COMMUNITY_Group RBAC & Tool ACL]]
- 18 edges to [[_COMMUNITY_Community 49]]
- 18 edges to [[_COMMUNITY_Community 62]]
- 17 edges to [[_COMMUNITY_Session Management]]
- 16 edges to [[_COMMUNITY_Community 57]]
- 9 edges to [[_COMMUNITY_Community 141]]
- 7 edges to [[_COMMUNITY_Community 87]]
- 6 edges to [[_COMMUNITY_Community 51]]
- 2 edges to [[_COMMUNITY_Community 43]]
- 2 edges to [[_COMMUNITY_Community 200]]
- 2 edges to [[_COMMUNITY_Community 774]]
- 1 edge to [[_COMMUNITY_Community 14]]
- 1 edge to [[_COMMUNITY_Security Audit & Drift Detection]]

## Top bridge nodes
- [[TeamsConfig]] - degree 99, connects to 11 communities
- [[test_group_isolation.py]] - degree 19, connects to 5 communities
- [[TestGroupMemoryInvisibleFromDM]] - degree 12, connects to 4 communities
- [[session_manager.py (UserSessionManager)]] - degree 6, connects to 4 communities
- [[test_shared_memory_write_acl.py]] - degree 14, connects to 3 communities