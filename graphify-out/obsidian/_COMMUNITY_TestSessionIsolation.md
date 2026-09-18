---
type: community
cohesion: 0.33
members: 6
---

# TestSessionIsolation

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_default_trust_level_is_untrusted()]] - code - gateway/tests/test_session_manager.py
- [[.test_get_or_create_returns_same_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_memory_file_created()]] - code - gateway/tests/test_session_manager.py
- [[.test_sessions_are_isolated()]] - code - gateway/tests/test_session_manager.py
- [[.test_workspace_directory_created()]] - code - gateway/tests/test_session_manager.py
- [[TestSessionIsolation]] - code - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSessionIsolation
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_UserSession]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[TestSessionIsolation]] - degree 8, connects to 2 communities