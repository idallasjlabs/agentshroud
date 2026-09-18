---
type: community
cohesion: 0.33
members: 7
---

# TestSessionPathSeparation

**Cohesion:** 0.33 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_path_traversal_rejected_for_crafted_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_path_traversal_rejected_for_crafted_user_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_user_session_paths_contain_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Session directory path must embed bot_id so filesystem confirms isolation.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject bot_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[TestSessionPathSeparation]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Verifies per-bot session path layout is correctly separated.]] - rationale - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSessionPathSeparation
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_TrustLevel]]
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[TestSessionPathSeparation]] - degree 9, connects to 4 communities