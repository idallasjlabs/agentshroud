---
type: community
cohesion: 0.40
members: 5
---

# TestInputValidation

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_empty_user_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_long_user_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_path_traversal_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_special_chars_rejected()]] - code - gateway/tests/test_session_manager.py
- [[TestInputValidation]] - code - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestInputValidation
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_UserSession]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[TestInputValidation]] - degree 7, connects to 2 communities