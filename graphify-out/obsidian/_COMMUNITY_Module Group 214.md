---
type: community
cohesion: 0.08
members: 22
---

# Module Group 214

**Cohesion:** 0.08 - loosely connected
**Members:** 22 nodes

## Members
- [[.test_critical_tool_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_default_deny()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_delete_action()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_direct_field()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_exception_fails_secure()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_execute_action_medium_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_high_tool_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_metadata_fallback()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_missing_returns_none()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_no_session_manager_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_other_user_under_users_base_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_own_workspace_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_owner_bypass()_3]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_question_defaults_to_read_system()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_read_action_low_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_session_context_priority()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_unknown_defaults_to_tool_use()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_users_heuristic_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_write_action_no_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[TestAnalyzeRequestForRBAC]] - code - gateway/tests/test_middleware_coverage.py
- [[TestExtractUserId]] - code - gateway/tests/test_middleware_coverage.py
- [[TestIsPathAllowedForUser]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_214
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 3 edges to [[_COMMUNITY_Session Manager & Webhook]]
- 3 edges to [[_COMMUNITY_Middleware Coverage Tests]]

## Top bridge nodes
- [[TestAnalyzeRequestForRBAC]] - degree 13, connects to 4 communities
- [[TestIsPathAllowedForUser]] - degree 12, connects to 4 communities
- [[TestExtractUserId]] - degree 9, connects to 4 communities
