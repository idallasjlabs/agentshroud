---
type: community
cohesion: 0.08
members: 25
---

# TestUserSessionManager

**Cohesion:** 0.08 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-session_manager()_1]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_2]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_3]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_conversation_history_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_memory_file_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_owner_access_control()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_context_generation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_creation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_isolation_directories()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_listing_authorization()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_prompt_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_trust_level_per_user()]] - code - gateway/tests/test_session_isolation.py
- [[Create a session manager with temporary workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace for testing.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that conversation histories are isolated per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that each user gets isolated directories.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that memory files are isolated per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owner can access all sessions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is properly generated.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session listing respects authorization.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session prompts include isolation instructions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that trust levels are tracked per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user sessions are created properly.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test the UserSessionManager for per-user isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestUserSessionManager]] - code - gateway/tests/test_session_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestUserSessionManager
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_WebhookReceiver]]
- 2 edges to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY_TestMiddlewareSessionEnforcement]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_Role]]

## Top bridge nodes
- [[TestUserSessionManager]] - degree 17, connects to 5 communities
- [[dot-session_manager()_1]] - degree 3, connects to 1 community
- [[dot-temp_workspace()_3]] - degree 2, connects to 1 community
