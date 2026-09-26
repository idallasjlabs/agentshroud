---
type: community
cohesion: 0.06
members: 32
---

# ModuleStatsCollector

**Cohesion:** 0.06 - loosely connected
**Members:** 32 nodes

## Members
- [[.middleware_manager()]] - code - gateway/tests/test_session_isolation.py
- [[.temp_workspace()_2]] - code - gateway/tests/test_session_isolation.py
- [[.temp_workspace()_3]] - code - gateway/tests/test_session_isolation.py
- [[.test_complete_user_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_cross_session_blocking()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_file_path_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_normalizes_invisible_unicode()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_own_workspace_allowed()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_owner_bypass()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_user_identification()]] - code - gateway/tests/test_session_isolation.py
- [[.test_multi_turn_block_reason_hides_score()]] - code - gateway/tests/test_session_isolation.py
- [[.test_owner_admin_access()]] - code - gateway/tests/test_session_isolation.py
- [[.test_session_persistence()]] - code - gateway/tests/test_session_isolation.py
- [[Blocked multi-turn sessions should not disclose scoring details.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create middleware manager with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[End-to-end integration tests for session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Input normalization should strip zero-width obfuscation before guards run.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test complete isolation between two users.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test middleware enforcement of session boundaries.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware blocks access to sensitive system files.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware blocks cross-session access attempts.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware injects session context.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware requires user identification.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owner can perform cross-session actions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owneradmin can access all user sessions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that sessions persist across manager restarts.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that users can access their own workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestMiddlewareSessionEnforcement]] - code - gateway/tests/test_session_isolation.py
- [[TestSessionIsolationEndToEnd]] - code - gateway/tests/test_session_isolation.py
- [[test_session_isolation.py]] - code - gateway/tests/test_session_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ModuleStatsCollector
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_KeyVaultConfig]]
- 4 edges to [[_COMMUNITY_TrustManager]]
- 4 edges to [[_COMMUNITY_GitHub Copilot CLI Setup Guide]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_Pre-Purge Secret Rotation Checklist]]

## Top bridge nodes
- [[test_session_isolation.py]] - degree 8, connects to 5 communities
- [[TestMiddlewareSessionEnforcement]] - degree 16, connects to 4 communities
- [[TestSessionIsolationEndToEnd]] - degree 10, connects to 4 communities
- [[.middleware_manager()]] - degree 4, connects to 2 communities
- [[.test_complete_user_isolation()]] - degree 3, connects to 1 community