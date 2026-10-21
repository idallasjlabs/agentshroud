---
type: community
members: 30
---

# KillSwitchMonitor (5)

**Members:** 30 nodes

## Members
- [[dot-test_group_a_write_invisible_from_group_b()]] - code - gateway/tests/test_group_isolation.py
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
- [[Test Group Config]] - code - gateway/tests/test_group_config.py
- [[TestGroupMemoryInvisibleFromDM]] - code - gateway/tests/test_group_isolation.py
- [[TestGroupMemoryNamespaceIsolation]] - code - gateway/tests/test_group_isolation.py
- [[User DM content must not leak into a group the user is NOT a member of.]] - rationale - gateway/tests/test_group_isolation.py
- [[Writes in group-A must not be readable from group-B.]] - rationale - gateway/tests/test_group_isolation.py
- [[agent_isolation.py (AgentRegistry)]] - code - gateway/security/agent_isolation.py
- [[get_merged_memory_for_user returns group section and private section separately.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-A and group-B memory files must be in separate directories.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-{chat_id} sessions must live under the 'groups' subdirectory.]] - rationale - gateway/tests/test_group_isolation.py
- [[rbac()_2]] - code - gateway/tests/test_group_isolation.py
- [[session_manager()_1]] - code - gateway/tests/test_group_isolation.py
- [[shared_memory()]] - code - gateway/tests/test_group_isolation.py
- [[teams()_2]] - code - gateway/tests/test_group_isolation.py
- [[test_group_isolation.py]] - code - gateway/tests/test_group_isolation.py
- [[tmp_workspace()_2]] - code - gateway/tests/test_group_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KillSwitchMonitor_5
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 4 edges to [[_COMMUNITY_colima-health-check.sh]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 4 edges to [[_COMMUNITY_RBACConfig]]
- 4 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer (3)]]

## Top bridge nodes
- [[test_group_isolation.py]] - degree 18, connects to 6 communities
- [[TestGroupMemoryNamespaceIsolation]] - degree 13, connects to 5 communities
- [[TestGroupMemoryInvisibleFromDM]] - degree 12, connects to 5 communities
- [[rbac()_2]] - degree 2, connects to 1 community
- [[session_manager()_1]] - degree 2, connects to 1 community
