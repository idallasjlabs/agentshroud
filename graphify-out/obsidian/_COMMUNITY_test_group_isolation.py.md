---
type: community
members: 30
---

# test_group_isolation.py

**Members:** 30 nodes

## Members
- [[dot-test_group_a_write_invisible_from_group_b()_1]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_b_write_invisible_from_group_a()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_id_uses_group_prefix_namespace()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_memory_physically_isolated()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_write_invisible_from_user_dm()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_writes_are_independent_namespaces()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_merged_memory_separates_group_and_dm()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_user_dm_write_invisible_from_group()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_user_dm_write_invisible_from_other_group()]] - code - gateway/tests/test_group_isolation.py
- [[Both groups store separate content with no cross-contamination.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content appended to group-A memory must not appear in group-B memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content appended to group-B must not appear in group-A memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content written to a group must not appear in any user's private DM memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content written to a user DM must not appear in any group memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Group workspace content must not leak into any user's DM workspace.]] - rationale - gateway/tests/test_group_isolation.py
- [[TDD — Workstream A (v1.2.0) Group memory namespace isolation. Tests that -…]] - rationale - gateway/tests/test_group_isolation.py
- [[TestGroupMemoryInvisibleFromDM]] - code - gateway/tests/test_group_isolation.py
- [[TestGroupMemoryNamespaceIsolation]] - code - gateway/tests/test_group_isolation.py
- [[User DM content must not leak into a group the user is NOT a member of.]] - rationale - gateway/tests/test_group_isolation.py
- [[Writes in group-A must not be readable from group-B.]] - rationale - gateway/tests/test_group_isolation.py
- [[fixture_106]] - code
- [[get_merged_memory_for_user returns group section and private section separately.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-A and group-B memory files must be in separate directories.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-{chat_id} sessions must live under the 'groups' subdirectory.]] - rationale - gateway/tests/test_group_isolation.py
- [[rbac()_4]] - code - gateway/tests/test_group_isolation.py
- [[session_manager()_4]] - code - gateway/tests/test_group_isolation.py
- [[shared_memory()_2]] - code - gateway/tests/test_group_isolation.py
- [[teams()_4]] - code - gateway/tests/test_group_isolation.py
- [[test_group_isolation.py]] - code - gateway/tests/test_group_isolation.py
- [[tmp_workspace()_1]] - code - gateway/tests/test_group_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_group_isolationpy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_UserSessionManager]]
- 4 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_SharedMemoryManager]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[test_group_isolation.py]] - degree 20, connects to 7 communities
- [[rbac()_4]] - degree 3, connects to 1 community
- [[session_manager()_4]] - degree 3, connects to 1 community
- [[shared_memory()_2]] - degree 3, connects to 1 community
- [[teams()_4]] - degree 3, connects to 1 community
