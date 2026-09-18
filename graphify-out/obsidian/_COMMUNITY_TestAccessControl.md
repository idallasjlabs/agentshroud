---
type: community
cohesion: 0.29
members: 7
---

# TestAccessControl

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_non_owner_cannot_view_other_sessions()]] - code - gateway/tests/test_session_manager.py
- [[.test_non_owner_empty_when_no_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_owner_can_access_any_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_owner_can_view_all_sessions()]] - code - gateway/tests/test_session_manager.py
- [[.test_user_can_access_own_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_user_cannot_access_other_session()]] - code - gateway/tests/test_session_manager.py
- [[TestAccessControl]] - code - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAccessControl
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_UserSession]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[TestAccessControl]] - degree 9, connects to 2 communities