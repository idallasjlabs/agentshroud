---
type: community
cohesion: 0.17
members: 12
---

# Community 774

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[.test_group_a_write_invisible_from_group_b()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_b_write_invisible_from_group_a()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_id_uses_group_prefix_namespace()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_memory_physically_isolated()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_writes_are_independent_namespaces()]] - code - gateway/tests/test_group_isolation.py
- [[Both groups store separate content with no cross-contamination.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content appended to group-A memory must not appear in group-B memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content appended to group-B must not appear in group-A memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[TestGroupMemoryNamespaceIsolation]] - code - gateway/tests/test_group_isolation.py
- [[Writes in group-A must not be readable from group-B.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-A and group-B memory files must be in separate directories.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-{chat_id} sessions must live under the 'groups' subdirectory.]] - rationale - gateway/tests/test_group_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_774
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 51]]
- 2 edges to [[_COMMUNITY_Community 27]]
- 1 edge to [[_COMMUNITY_RBAC & SOC Realtime]]
- 1 edge to [[_COMMUNITY_Session Management]]
- 1 edge to [[_COMMUNITY_Community 62]]

## Top bridge nodes
- [[TestGroupMemoryNamespaceIsolation]] - degree 13, connects to 5 communities