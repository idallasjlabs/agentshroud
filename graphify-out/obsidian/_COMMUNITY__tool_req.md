---
type: community
members: 15
---

# _tool_req

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
- [[TestToolChainAnalyzer]] - code - gateway/tests/test_middleware_coverage.py
- [[_tool_req()]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_tool_req
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_middleware_coverage.py]]
- 1 edge to [[_COMMUNITY__FakeRBAC]]
- 1 edge to [[_COMMUNITY__req]]

## Top bridge nodes
- [[_tool_req()]] - degree 13, connects to 2 communities
- [[TestFileSandboxStep]] - degree 5, connects to 1 community
- [[TestToolChainAnalyzer]] - degree 5, connects to 1 community
- [[TestPathIsolationStep]] - degree 4, connects to 1 community
- [[dot-test_owner_bypasses_sandbox()]] - degree 3, connects to 1 community
