---
type: community
members: 23
---

# ApprovalQueueConfig (2) (4)

**Members:** 23 nodes

## Members
- [[dot-middleware_manager()]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_2]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_3]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_cross_session_blocking()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_file_path_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_normalizes_invisible_unicode()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_own_workspace_allowed()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_owner_bypass()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_user_identification()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_multi_turn_block_reason_hides_score()]] - code - gateway/tests/test_session_isolation.py
- [[Blocked multi-turn sessions should not disclose scoring details.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create middleware manager with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Input normalization should strip zero-width obfuscation before guards run.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test middleware enforcement of session boundaries.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware blocks access to sensitive system files.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware blocks cross-session access attempts.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware injects session context.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware requires user identification.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owner can perform cross-session actions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that users can access their own workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestMiddlewareSessionEnforcement]] - code - gateway/tests/test_session_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig_2_4
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_AgentTarget]]

## Top bridge nodes
- [[TestMiddlewareSessionEnforcement]] - degree 16, connects to 4 communities
- [[dot-middleware_manager()]] - degree 4, connects to 2 communities
- [[dot-temp_workspace()_3]] - degree 2, connects to 1 community
