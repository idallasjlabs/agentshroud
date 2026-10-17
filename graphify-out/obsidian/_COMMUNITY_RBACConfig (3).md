---
type: community
members: 57
---

# RBACConfig (3)

**Members:** 57 nodes

## Members
- [[dot-get_active_project_for_user()]] - code - gateway/security/group_config.py
- [[dot-get_all_member_ids()]] - code - gateway/security/group_config.py
- [[dot-get_group_admin_ids()]] - code - gateway/security/group_config.py
- [[dot-get_group_safe_response_prefix()]] - code - gateway/security/group_config.py
- [[dot-get_user_collab_mode()]] - code - gateway/security/group_config.py
- [[dot-get_user_groups()]] - code - gateway/security/group_config.py
- [[dot-get_user_projects()]] - code - gateway/security/group_config.py
- [[dot-is_admin()]] - code - gateway/security/group_config.py
- [[dot-is_group_admin()]] - code - gateway/security/group_config.py
- [[dot-is_member()]] - code - gateway/security/group_config.py
- [[dot-model_post_init()]] - code - gateway/security/group_config.py
- [[dot-test_active_group_appears_first()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_append_to_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_append_to_user_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_clean_text_not_flagged()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_collaborator_gets_filtered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_api_key_pattern()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_bearer_token()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_private_section_header()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_get_group_memory_empty_initially()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_get_user_memory_returns_string()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_multiple_appends_accumulate()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_owner_gets_unfiltered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_owner_sees_all_groups()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_strip_private_content_redacts_api_key()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_strip_private_section()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_topic_scoped_excludes_non_matching_project_scoped_group()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_topic_scoped_includes_local_only_group()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_topic_scoped_returns_matching_group()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_unknown_user_sees_only_private_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_does_not_see_other_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_memory_isolated_between_users()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_sees_own_private_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_sees_their_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[Merge group_overrides.json additions into the in-memory TeamsConfig.]] - rationale - gateway/security/group_config.py
- [[Return all groups the user belongs to.]] - rationale - gateway/security/group_config.py
- [[Return all projects accessible to the user via group membership.]] - rationale - gateway/security/group_config.py
- [[Return deduplicated list of all user IDs across all groups.]] - rationale - gateway/security/group_config.py
- [[Return mapping of group_id → admin_user_id for all groups that have an admin.]] - rationale - gateway/security/group_config.py
- [[Return the effective collab_mode for a user.          Resolution order]] - rationale - gateway/security/group_config.py
- [[Return the first project accessible to a user (primary project).]] - rationale - gateway/security/group_config.py
- [[Return the safe_response_prefix for the first group that the user belongs to]] - rationale - gateway/security/group_config.py
- [[TeamsConfig]] - code - gateway/security/group_config.py
- [[TestGroupMemoryReadWrite]] - code - gateway/tests/test_shared_memory.py
- [[TestMergedMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestPrivateContentDetection]] - code - gateway/tests/test_shared_memory.py
- [[TestTopicScopedMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestUserPrivateMemory]] - code - gateway/tests/test_shared_memory.py
- [[Top-level teams configuration parsed from agentshroud.yaml `teams` section.]] - rationale - gateway/security/group_config.py
- [[_apply_persisted_overrides()]] - code - gateway/security/group_config.py
- [[rbac()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[rbac()_1]] - code - gateway/tests/test_shared_memory.py
- [[session_mgr()]] - code - gateway/tests/test_shared_memory.py
- [[smm()_1]] - code - gateway/tests/test_shared_memory.py
- [[teams()_1]] - code - gateway/tests/test_group_isolation.py
- [[test_shared_memory.py]] - code - gateway/tests/test_shared_memory.py
- [[tmp_workspace()_1]] - code - gateway/tests/test_shared_memory.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RBACConfig_3
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_RBACConfig]]
- 16 edges to [[_COMMUNITY_telegram_proxy.py]]
- 15 edges to [[_COMMUNITY_MiddlewareManager]]
- 13 edges to [[_COMMUNITY_RBACConfig (2)_1]]
- 11 edges to [[_COMMUNITY_RBACConfig (2)]]
- 9 edges to [[_COMMUNITY_GroupConfig]]
- 7 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 7 edges to [[_COMMUNITY_RBACConfig (3)_1]]
- 5 edges to [[_COMMUNITY_RBACConfig (2) (2)]]
- 4 edges to [[_COMMUNITY_telegram_proxy.py (3)]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_RBACConfig (2) (3)]]
- 1 edge to [[_COMMUNITY_RBACConfig (2) (4)]]
- 1 edge to [[_COMMUNITY_RBACConfig (5)]]

## Top bridge nodes
- [[TeamsConfig]] - degree 100, connects to 15 communities
- [[test_shared_memory.py]] - degree 13, connects to 3 communities
- [[TestPrivateContentDetection]] - degree 13, connects to 3 communities
- [[TestMergedMemory]] - degree 11, connects to 3 communities
- [[TestGroupMemoryReadWrite]] - degree 8, connects to 3 communities
