---
type: community
cohesion: 0.20
members: 10
---

# TestGroupMemoryInvisibleFromDM

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_group_write_invisible_from_user_dm()]] - code - gateway/tests/test_group_isolation.py
- [[.test_merged_memory_separates_group_and_dm()]] - code - gateway/tests/test_group_isolation.py
- [[.test_user_dm_write_invisible_from_group()]] - code - gateway/tests/test_group_isolation.py
- [[.test_user_dm_write_invisible_from_other_group()]] - code - gateway/tests/test_group_isolation.py
- [[Content written to a group must not appear in any user's private DM memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content written to a user DM must not appear in any group memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Group workspace content must not leak into any user's DM workspace.]] - rationale - gateway/tests/test_group_isolation.py
- [[TestGroupMemoryInvisibleFromDM]] - code - gateway/tests/test_group_isolation.py
- [[User DM content must not leak into a group the user is NOT a member of.]] - rationale - gateway/tests/test_group_isolation.py
- [[get_merged_memory_for_user returns group section and private section separately.]] - rationale - gateway/tests/test_group_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestGroupMemoryInvisibleFromDM
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[TestGroupMemoryInvisibleFromDM]] - degree 12, connects to 4 communities