---
type: community
members: 8
---

# CI/CD Quality Gates (14 jobs, 6 workflows)

**Members:** 8 nodes

## Members
- [[dot-test_default_deny()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_exception_fails_secure()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_no_session_manager_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_other_user_under_users_base_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_own_workspace_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_owner_bypass()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_users_heuristic_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[TestIsPathAllowedForUser]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CI/CD_Quality_Gates_14_jobs_6_workflows
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_export_bot]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]

## Top bridge nodes
- [[TestIsPathAllowedForUser]] - degree 12, connects to 4 communities
