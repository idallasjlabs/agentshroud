---
type: community
members: 9
---

# AgentShroud v1.2.0 — Red Team Assessment

**Members:** 9 nodes

## Members
- [[dot-test_critical_tool_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_delete_action()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_execute_action_medium_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_high_tool_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_question_defaults_to_read_system()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_read_action_low_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_unknown_defaults_to_tool_use()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_write_action_no_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[TestAnalyzeRequestForRBAC]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_v120__Red_Team_Assessment
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_export_bot]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]

## Top bridge nodes
- [[TestAnalyzeRequestForRBAC]] - degree 13, connects to 4 communities
