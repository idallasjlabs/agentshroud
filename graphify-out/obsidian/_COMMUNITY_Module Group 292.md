---
type: community
cohesion: 0.21
members: 15
---

# Module Group 292

**Cohesion:** 0.21 - loosely connected
**Members:** 15 nodes

## Members
- [[.test_allowed_chain_passes()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_analyzer_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_blocked_rewrite_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_blocked_with_chain_match()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_blocked_without_chain_match()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_cross_user_path_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_isolation_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_own_workspace_path_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_owner_bypasses_sandbox()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_sandbox_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_unblocked_rewrite_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[TestFileSandboxStep]] - code - gateway/tests/test_middleware_coverage.py
- [[TestPathIsolationStep]] - code - gateway/tests/test_middleware_coverage.py
- [[TestToolChainAnalyzer]] - code - gateway/tests/test_middleware_coverage.py
- [[_tool_req()]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_292
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 6 edges to [[_COMMUNITY_Middleware Coverage Tests]]
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 3 edges to [[_COMMUNITY_Session Manager & Webhook]]

## Top bridge nodes
- [[TestFileSandboxStep]] - degree 9, connects to 4 communities
- [[TestToolChainAnalyzer]] - degree 9, connects to 4 communities
- [[TestPathIsolationStep]] - degree 8, connects to 4 communities
- [[_tool_req()]] - degree 13, connects to 1 community
- [[.test_owner_bypasses_sandbox()]] - degree 3, connects to 1 community
