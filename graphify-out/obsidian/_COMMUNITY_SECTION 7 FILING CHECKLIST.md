---
type: community
members: 5
---

# SECTION 7: FILING CHECKLIST

**Members:** 5 nodes

## Members
- [[dot-test_empty_dir_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_fresh_file_returns_true()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_old_file_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_stat_error_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestIsFresh_1]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SECTION_7_FILING_CHECKLIST
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MiddlewareManager (3) (2)]]
- 1 edge to [[_COMMUNITY_UserSessionManager (3) (2)]]
- 1 edge to [[_COMMUNITY_AgentShroud Consolidated Issues Report]]

## Top bridge nodes
- [[dot-test_old_file_returns_false()]] - degree 3, connects to 2 communities
- [[TestIsFresh_1]] - degree 5, connects to 1 community
- [[dot-test_fresh_file_returns_true()]] - degree 2, connects to 1 community
