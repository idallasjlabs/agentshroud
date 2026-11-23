---
type: community
members: 34
---

# TeamsConfig

**Members:** 34 nodes

## Members
- [[dot-get_all_member_ids()]] - code - gateway/security/group_config.py
- [[dot-get_group_safe_response_prefix()]] - code - gateway/security/group_config.py
- [[dot-get_user_collab_mode()]] - code - gateway/security/group_config.py
- [[dot-get_user_groups()]] - code - gateway/security/group_config.py
- [[dot-get_user_projects()]] - code - gateway/security/group_config.py
- [[dot-is_group_admin()_2]] - code - gateway/security/group_config.py
- [[dot-model_post_init()_1]] - code - gateway/security/group_config.py
- [[dot-test_empty_teams_parses()]] - code - gateway/tests/test_group_config.py
- [[dot-test_group_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_parses_groups()]] - code - gateway/tests/test_group_config.py
- [[dot-test_parses_projects()]] - code - gateway/tests/test_group_config.py
- [[dot-test_user_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[If the underlying session store raises, the authorized write reports failure…]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Merge group_overrides.json additions into the in-memory TeamsConfig.]] - rationale - gateway/security/group_config.py
- [[Return all groups the user belongs to.]] - rationale - gateway/security/group_config.py
- [[Return all projects accessible to the user via group membership.]] - rationale - gateway/security/group_config.py
- [[Return deduplicated list of all user IDs across all groups.]] - rationale - gateway/security/group_config.py
- [[Return the effective collab_mode for a user. Resolution order 1. Per-user…]] - rationale - gateway/security/group_config.py
- [[Return the safe_response_prefix for the first group that the user belongs to…]] - rationale - gateway/security/group_config.py
- [[TDD — WS-E finding RT-5 (HIGH) shared-memory write access control. Before this…]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[TeamsConfig]] - code - gateway/security/group_config.py
- [[TestTeamsConfigParsing]] - code - gateway/tests/test_group_config.py
- [[TestWriteFailurePath]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[Top-level teams configuration parsed from agentshroud.yaml `teams` section.]] - rationale - gateway/security/group_config.py
- [[_apply_persisted_overrides()]] - code - gateway/security/group_config.py
- [[_boom()_23]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[_boom()_24]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[fixture_92]] - code
- [[fixture_93]] - code
- [[rbac()_3]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[session_manager()_2]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[shared_memory()_1]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[teams()_3]] - code - gateway/tests/test_group_config.py
- [[test_shared_memory_write_acl.py]] - code - gateway/tests/test_shared_memory_write_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TeamsConfig
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_collaborator_responses.py]]
- 7 edges to [[_COMMUNITY_telegram_proxy.py]]
- 5 edges to [[_COMMUNITY_GroupWorkspaceManager]]
- 4 edges to [[_COMMUNITY_UserSessionManager]]
- 3 edges to [[_COMMUNITY_SharedMemoryManager]]
- 3 edges to [[_COMMUNITY_test_tool_acl.py]]
- 2 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_PrivacyPolicyEnforcer]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_test_group_isolation.py]]
- 2 edges to [[_COMMUNITY_test_group_rbac.py]]
- 2 edges to [[_COMMUNITY_test_shared_memory.py]]
- 1 edge to [[_COMMUNITY_TestGroupMemoryWriteACL]]
- 1 edge to [[_COMMUNITY_TestUserMemoryWriteACL]]
- 1 edge to [[_COMMUNITY_load_config]]

## Top bridge nodes
- [[TeamsConfig]] - degree 40, connects to 11 communities
- [[test_shared_memory_write_acl.py]] - degree 16, connects to 7 communities
- [[_apply_persisted_overrides()]] - degree 5, connects to 2 communities
- [[TestTeamsConfigParsing]] - degree 5, connects to 1 community
- [[dot-get_user_groups()]] - degree 5, connects to 1 community
