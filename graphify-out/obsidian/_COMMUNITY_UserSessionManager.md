---
type: community
members: 90
---

# UserSessionManager

**Members:** 90 nodes

## Members
- [[dot-__init__()_184]] - code - gateway/proxy/webhook_receiver.py
- [[dot-__init__()_185]] - code - gateway/security/session_manager.py
- [[dot-_can_create_directory()]] - code - gateway/proxy/webhook_receiver.py
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
- [[dot-middleware_manager()]] - code - gateway/tests/test_session_isolation.py
- [[dot-mock_forwarder()]] - code - gateway/tests/test_session_isolation.py
- [[dot-mock_pipeline()]] - code - gateway/tests/test_session_isolation.py
- [[dot-reanchor_system_prompt()]] - code - gateway/security/session_manager.py
- [[dot-session_manager()]] - code - gateway/tests/test_session_isolation.py
- [[dot-session_manager()_1]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_1]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_2]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_3]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_complete_user_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_owner_admin_access()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_persistence()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[dot-to_dict()_11]] - code - gateway/security/session_manager.py
- [[dot-update_user_trust_level()]] - code - gateway/security/session_manager.py
- [[A single message in a conversation.]] - rationale - gateway/security/session_manager.py
- [[Add a message to the user's conversation history for a specific bot.]] - rationale - gateway/security/session_manager.py
- [[Any_75]] - code
- [[Atomically persist current sessions to the metadata file. Writes are serialized…]] - rationale - gateway/security/session_manager.py
- [[Check if a user can access another user's session.]] - rationale - gateway/security/session_manager.py
- [[Check if we can create the given directory path.]] - rationale - gateway/proxy/webhook_receiver.py
- [[ConversationMessage]] - code - gateway/security/session_manager.py
- [[Convert session to dictionary for serialization.]] - rationale - gateway/security/session_manager.py
- [[Create a mock forwarder.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a mock security pipeline.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a session manager with temporary workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a session manager.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace for testing.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace for testing._1]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace._1]] - rationale - gateway/tests/test_session_isolation.py
- [[Create middleware manager with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
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
- [[Path_65]] - code
- [[Receives webhooks and routes them through the security pipeline. In production,…]] - rationale - gateway/proxy/webhook_receiver.py
- [[Represents a shared workspace + memory for a group.]] - rationale - gateway/security/session_manager.py
- [[Return the cache key string for a (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Return the system prompt with a re-anchoring preamble prepended. Called after a…]] - rationale - gateway/security/session_manager.py
- [[Session Manager - Per-User Session Isolation Implements per-user session…]] - rationale - gateway/security/session_manager.py
- [[Test Session Isolation - Comprehensive tests for per-user session isolation.…]] - rationale - gateway/tests/test_session_isolation.py
- [[Test WebhookReceiver integration with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test complete isolation between two users.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that conversations are logged per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owneradmin can access all user sessions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is injected into forwarded requests.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that sessions persist across manager restarts.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user IDs are properly extracted from webhook payloads.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestSessionIsolationEndToEnd]] - code - gateway/tests/test_session_isolation.py
- [[TestWebhookReceiverIntegration]] - code - gateway/tests/test_session_isolation.py
- [[Update the trust level for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[UserSessionManager]] - code - gateway/security/session_manager.py
- [[Validate and sanitize bot_id to prevent path traversal. Allows alphanumeric…]] - rationale - gateway/security/session_manager.py
- [[Validate and sanitize user_id to prevent path traversal. Only allows…]] - rationale - gateway/security/session_manager.py
- [[WebhookReceiver]] - code - gateway/proxy/webhook_receiver.py
- [[fixture_125]] - code
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
- 9 edges to [[_COMMUNITY_TestMiddlewareSessionEnforcement]]
- 9 edges to [[_COMMUNITY_test_session_manager.py]]
- 8 edges to [[_COMMUNITY_dot-process_webhook]]
- 7 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 6 edges to [[_COMMUNITY_socrouter.py]]
- 5 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_GroupWorkspaceManager]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_TestUserSessionManager]]
- 4 edges to [[_COMMUNITY_test_group_isolation.py]]
- 4 edges to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 4 edges to [[_COMMUNITY_test_shared_memory.py]]
- 4 edges to [[_COMMUNITY_TeamsConfig]]
- 3 edges to [[_COMMUNITY_TestAtomicRegistryWrites]]
- 3 edges to [[_COMMUNITY_TestMultiBotIsolation]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_test_file_sandbox_message_gate.py]]
- 3 edges to [[_COMMUNITY_test_middleware_coverage.py]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_run]]
- 1 edge to [[_COMMUNITY_SharedMemoryManager]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY__make_proxy]]
- 1 edge to [[_COMMUNITY_email_send]]
- 1 edge to [[_COMMUNITY_test_webhook_receiver_passes_agent_id_as_bot_id]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[UserSessionManager]] - degree 64, connects to 17 communities
- [[session_manager.py]] - degree 19, connects to 10 communities
- [[WebhookReceiver]] - degree 30, connects to 8 communities
- [[shared_memory.py]] - degree 12, connects to 7 communities
- [[test_session_isolation.py]] - degree 12, connects to 5 communities
