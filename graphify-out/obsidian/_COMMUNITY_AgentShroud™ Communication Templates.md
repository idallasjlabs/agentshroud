---
type: community
cohesion: 0.17
members: 16
---

# AgentShroud™ Communication Templates

**Cohesion:** 0.17 - loosely connected
**Members:** 16 nodes

## Members
- [[.__init__()_176]] - code - gateway/tests/test_middleware_coverage.py
- [[.check_permission()_1]] - code - gateway/tests/test_middleware_coverage.py
- [[.check_tool_permission()_2]] - code - gateway/tests/test_middleware_coverage.py
- [[.get_user_role()_2]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_fallback_without_rbac_manager()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_rbac_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_rbac_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_rbac_pass_logs_role_and_allows()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_rbac_requires_approval()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_tool_permission_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_tool_permission_requires_approval()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_with_rbac_manager()]] - code - gateway/tests/test_middleware_coverage.py
- [[Deterministic stand-in for RBACManager.]] - rationale - gateway/tests/test_middleware_coverage.py
- [[TestIsOwner]] - code - gateway/tests/test_middleware_coverage.py
- [[TestProcessRequestRBAC]] - code - gateway/tests/test_middleware_coverage.py
- [[_FakeRBAC]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Communication_Templates
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_CredentialValidator]]
- 6 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_ResourceGuard]]
- 3 edges to [[_COMMUNITY_KeyVaultConfig]]
- 3 edges to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]
- 1 edge to [[_COMMUNITY_Himalaya Email CLI]]

## Top bridge nodes
- [[_FakeRBAC]] - degree 21, connects to 6 communities
- [[TestProcessRequestRBAC]] - degree 11, connects to 4 communities
- [[TestIsOwner]] - degree 7, connects to 4 communities
- [[.test_rbac_denied()]] - degree 3, connects to 1 community
- [[.test_rbac_exception_fails_closed()]] - degree 3, connects to 1 community