---
type: community
members: 4
---

# Claude Code (PRIMARY agent)

**Members:** 4 nodes

## Members
- [[dot-test_full_compose()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_no_compose_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_unreadable_first_path_falls_through()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestResourceAvailability]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Claude_Code_PRIMARY_agent
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MiddlewareManager (3) (2)]]
- 1 edge to [[_COMMUNITY_UserSessionManager (3) (2)]]

## Top bridge nodes
- [[TestResourceAvailability]] - degree 4, connects to 1 community
- [[dot-test_full_compose()]] - degree 2, connects to 1 community
- [[dot-test_unreadable_first_path_falls_through()]] - degree 2, connects to 1 community
