---
type: community
members: 8
---

# TestSessionPathSeparation

**Members:** 8 nodes

## Members
- [[dot-test_path_traversal_rejected_for_crafted_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_path_traversal_rejected_for_crafted_user_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_user_session_paths_contain_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Session directory path must embed bot_id so filesystem confirms isolation.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject bot_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject user_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[TestSessionPathSeparation]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Verifies per-bot session path layout is correctly separated.]] - rationale - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSessionPathSeparation
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_security_regressions_v1_2.py]]

## Top bridge nodes
- [[TestSessionPathSeparation]] - degree 5, connects to 1 community
