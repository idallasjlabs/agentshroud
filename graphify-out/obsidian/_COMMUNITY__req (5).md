---
type: community
members: 6
---

# _req (5)

**Members:** 6 nodes

## Members
- [[dot-test_clean_message_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_dict_message_handled()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_direct_no_session_manager_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_non_owner_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_owner_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[TestCrossSessionAccess]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_req_5
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY__req]]
- 1 edge to [[_COMMUNITY__req (2)]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]

## Top bridge nodes
- [[TestCrossSessionAccess]] - degree 10, connects to 4 communities
- [[dot-test_non_owner_blocked()]] - degree 2, connects to 1 community
- [[dot-test_owner_allowed()]] - degree 2, connects to 1 community
