---
type: community
cohesion: 0.36
members: 8
---

# test_prompt_guard.py

**Cohesion:** 0.36 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-test_exception_fails_open()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_log_action_no_patterns_returns_original()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_log_action_with_patterns_returns_original()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_no_scanner_passthrough()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_strip_action_returns_sanitized()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_warn_action_returns_sanitized()]] - code - gateway/tests/test_middleware_coverage.py
- [[TestScanToolResult]] - code - gateway/tests/test_middleware_coverage.py
- [[_scan_result()]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_prompt_guardpy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__req]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_UserSessionManager_3]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]

## Top bridge nodes
- [[TestScanToolResult]] - degree 11, connects to 4 communities
- [[_scan_result()]] - degree 5, connects to 1 community
