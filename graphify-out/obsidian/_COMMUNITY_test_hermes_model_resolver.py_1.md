---
type: community
cohesion: 0.21
members: 15
---

# test_hermes_model_resolver.py

**Cohesion:** 0.21 - loosely connected
**Members:** 15 nodes

## Members
- [[dot-test_allowed_chain_passes()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_analyzer_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_blocked_rewrite_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_blocked_with_chain_match()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_blocked_without_chain_match()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_cross_user_path_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_isolation_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_own_workspace_path_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_owner_bypasses_sandbox()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_sandbox_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_unblocked_rewrite_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[TestFileSandboxStep]] - code - gateway/tests/test_middleware_coverage.py
- [[TestPathIsolationStep]] - code - gateway/tests/test_middleware_coverage.py
- [[TestToolChainAnalyzer_1]] - code - gateway/tests/test_middleware_coverage.py
- [[_tool_req()]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_hermes_model_resolverpy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_MiddlewareManager]]
- 6 edges to [[_COMMUNITY__req]]
- 3 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 3 edges to [[_COMMUNITY_UserSessionManager_3]]

## Top bridge nodes
- [[TestFileSandboxStep]] - degree 9, connects to 4 communities
- [[TestToolChainAnalyzer_1]] - degree 9, connects to 4 communities
- [[TestPathIsolationStep]] - degree 8, connects to 4 communities
- [[_tool_req()]] - degree 13, connects to 1 community
- [[dot-test_owner_bypasses_sandbox()]] - degree 3, connects to 1 community
