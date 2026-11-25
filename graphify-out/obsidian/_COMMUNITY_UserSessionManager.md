---
type: community
members: 57
---

# UserSessionManager

**Members:** 57 nodes

## Members
- [[dot-__init__()_187]] - code - gateway/security/session_manager.py
- [[dot-_load_sessions()]] - code - gateway/security/session_manager.py
- [[dot-_save_sessions()]] - code - gateway/security/session_manager.py
- [[dot-_session_key()]] - code - gateway/security/session_manager.py
- [[dot-_validate_bot_id()]] - code - gateway/security/session_manager.py
- [[dot-_validate_user_id()]] - code - gateway/security/session_manager.py
- [[dot-add_conversation_message()]] - code - gateway/security/session_manager.py
- [[dot-can_user_access_session()]] - code - gateway/security/session_manager.py
- [[dot-get_or_create_group_session()]] - code - gateway/security/session_manager.py
- [[dot-get_or_create_session()]] - code - gateway/security/session_manager.py
- [[dot-get_session_context()]] - code - gateway/security/session_manager.py
- [[dot-get_session_prompt_addition()]] - code - gateway/security/session_manager.py
- [[dot-get_user_workspace_path()]] - code - gateway/security/session_manager.py
- [[dot-list_sessions_for_user()]] - code - gateway/security/session_manager.py
- [[dot-reanchor_system_prompt()]] - code - gateway/security/session_manager.py
- [[dot-test_complete_user_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_owner_admin_access()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_persistence()]] - code - gateway/tests/test_session_isolation.py
- [[dot-to_dict()_9]] - code - gateway/security/session_manager.py
- [[dot-update_user_trust_level()]] - code - gateway/security/session_manager.py
- [[A single message in a conversation.]] - rationale - gateway/security/session_manager.py
- [[Add a message to the user's conversation history for a specific bot.]] - rationale - gateway/security/session_manager.py
- [[Any_71]] - code
- [[Atomically persist current sessions to the metadata file. Writes are serialized…]] - rationale - gateway/security/session_manager.py
- [[Check if a user can access another user's session.]] - rationale - gateway/security/session_manager.py
- [[ConversationMessage]] - code - gateway/security/session_manager.py
- [[Convert session to dictionary for serialization.]] - rationale - gateway/security/session_manager.py
- [[End-to-end integration tests for session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Get existing session or create a new one for the (user_id, bot_id) pair. Each…]] - rationale - gateway/security/session_manager.py
- [[Get or create a shared workspace + MEMORY.md for a group.]] - rationale - gateway/security/session_manager.py
- [[Get session context for injection into agent request.]] - rationale - gateway/security/session_manager.py
- [[Get session-specific prompt addition for the agent.]] - rationale - gateway/security/session_manager.py
- [[Get the workspace path for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[Group Shared Memory Manager (v0.9.0 Tranche 1) Provides a high-level API for…]] - rationale - gateway/security/shared_memory.py
- [[GroupSession]] - code - gateway/security/session_manager.py
- [[Initialize session manager. Args base_workspace Base directory for user…]] - rationale - gateway/security/session_manager.py
- [[List session keys that the requesting user is allowed to see. Returns the full…]] - rationale - gateway/security/session_manager.py
- [[Load existing sessions from metadata file. Handles both the new…]] - rationale - gateway/security/session_manager.py
- [[Manages per-user, per-bot session isolation. Sessions are keyed by (user_id,…]] - rationale - gateway/security/session_manager.py
- [[Path_64]] - code
- [[Represents a shared workspace + memory for a group.]] - rationale - gateway/security/session_manager.py
- [[Return the cache key string for a (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Return the system prompt with a re-anchoring preamble prepended. Called after a…]] - rationale - gateway/security/session_manager.py
- [[Session Manager - Per-User Session Isolation Implements per-user session…]] - rationale - gateway/security/session_manager.py
- [[Test Session Isolation - Comprehensive tests for per-user session isolation.…]] - rationale - gateway/tests/test_session_isolation.py
- [[Test complete isolation between two users.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owneradmin can access all user sessions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that sessions persist across manager restarts.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestSessionIsolationEndToEnd]] - code - gateway/tests/test_session_isolation.py
- [[Update the trust level for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[UserSessionManager]] - code - gateway/security/session_manager.py
- [[Validate and sanitize bot_id to prevent path traversal. Allows alphanumeric…]] - rationale - gateway/security/session_manager.py
- [[Validate and sanitize user_id to prevent path traversal. Only allows…]] - rationale - gateway/security/session_manager.py
- [[session_manager.py]] - code - gateway/security/session_manager.py
- [[shared_memory.py]] - code - gateway/security/shared_memory.py
- [[test_session_isolation.py]] - code - gateway/tests/test_session_isolation.py
- [[webhook_receiver.py]] - code - gateway/proxy/webhook_receiver.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserSessionManager
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_SharedMemoryManager]]
- 9 edges to [[_COMMUNITY_TestMiddlewareSessionEnforcement]]
- 9 edges to [[_COMMUNITY_test_session_manager.py]]
- 5 edges to [[_COMMUNITY_RBACConfig]]
- 4 edges to [[_COMMUNITY_WebhookReceiver]]
- 4 edges to [[_COMMUNITY_GroupWorkspaceManager]]
- 4 edges to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 3 edges to [[_COMMUNITY_TestAtomicRegistryWrites]]
- 3 edges to [[_COMMUNITY_TestUserSessionManager]]
- 3 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 3 edges to [[_COMMUNITY_TestMultiBotIsolation]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_test_file_sandbox_message_gate.py]]
- 3 edges to [[_COMMUNITY_test_middleware_coverage.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_AgentTarget]]

## Top bridge nodes
- [[UserSessionManager]] - degree 64, connects to 17 communities
- [[session_manager.py]] - degree 19, connects to 9 communities
- [[test_session_isolation.py]] - degree 12, connects to 6 communities
- [[shared_memory.py]] - degree 12, connects to 4 communities
- [[webhook_receiver.py]] - degree 7, connects to 4 communities
