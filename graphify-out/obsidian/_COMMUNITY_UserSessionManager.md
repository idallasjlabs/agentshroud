---
type: community
members: 91
---

# UserSessionManager

**Members:** 91 nodes

## Members
- [[dot-_validate_user_id()]] - code - gateway/security/session_manager.py
- [[dot-can_user_access_session()]] - code - gateway/security/session_manager.py
- [[dot-get_or_create_group_session()]] - code - gateway/security/session_manager.py
- [[dot-middleware_manager()]] - code - gateway/tests/test_session_isolation.py
- [[dot-mock_forwarder()]] - code - gateway/tests/test_session_isolation.py
- [[dot-mock_pipeline()]] - code - gateway/tests/test_session_isolation.py
- [[dot-session_manager()]] - code - gateway/tests/test_session_isolation.py
- [[dot-session_manager()_1]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_1]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_2]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_3]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_complete_user_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_conversation_history_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_memory_file_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_cross_session_blocking()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_file_path_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_normalizes_invisible_unicode()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_own_workspace_allowed()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_owner_bypass()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_middleware_user_identification()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_multi_turn_block_reason_hides_score()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_owner_access_control()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_owner_admin_access()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_context_generation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_creation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_isolation_directories()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_listing_authorization()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_persistence()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_prompt_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_trust_level_per_user()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[Blocked multi-turn sessions should not disclose scoring details.]] - rationale - gateway/tests/test_session_isolation.py
- [[Check if a user can access another user's session.]] - rationale - gateway/security/session_manager.py
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
- [[Get or create a shared workspace + MEMORY.md for a group.]] - rationale - gateway/security/session_manager.py
- [[Group Shared Memory Manager (v0.9.0 Tranche 1) Provides a high-level API for…]] - rationale - gateway/security/shared_memory.py
- [[GroupSession]] - code - gateway/security/session_manager.py
- [[Input normalization should strip zero-width obfuscation before guards run.]] - rationale - gateway/tests/test_session_isolation.py
- [[Manages per-user, per-bot session isolation. Sessions are keyed by (user_id,…]] - rationale - gateway/security/session_manager.py
- [[Represents a shared workspace + memory for a group.]] - rationale - gateway/security/session_manager.py
- [[Session Manager - Per-User Session Isolation Implements per-user session…]] - rationale - gateway/security/session_manager.py
- [[Test Session Isolation - Comprehensive tests for per-user session isolation.…]] - rationale - gateway/tests/test_session_isolation.py
- [[Test WebhookReceiver integration with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test complete isolation between two users.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test middleware enforcement of session boundaries.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that conversation histories are isolated per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that conversations are logged per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that each user gets isolated directories.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that memory files are isolated per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware blocks access to sensitive system files.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware blocks cross-session access attempts.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware injects session context.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware requires user identification.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owner can access all sessions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owner can perform cross-session actions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owneradmin can access all user sessions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is injected into forwarded requests.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is properly generated.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session listing respects authorization.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session prompts include isolation instructions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that sessions persist across manager restarts.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that trust levels are tracked per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user IDs are properly extracted from webhook payloads.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user sessions are created properly.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that users can access their own workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test the UserSessionManager for per-user isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestMiddlewareSessionEnforcement]] - code - gateway/tests/test_session_isolation.py
- [[TestSessionIsolationEndToEnd]] - code - gateway/tests/test_session_isolation.py
- [[TestUserSessionManager]] - code - gateway/tests/test_session_isolation.py
- [[TestWebhookReceiverIntegration]] - code - gateway/tests/test_session_isolation.py
- [[UserSessionManager]] - code - gateway/security/session_manager.py
- [[Validate and sanitize user_id to prevent path traversal. Only allows…]] - rationale - gateway/security/session_manager.py
- [[asyncio_72]] - code
- [[fixture_123]] - code
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
- 15 edges to [[_COMMUNITY_dot-get_or_create_session]]
- 8 edges to [[_COMMUNITY_middleware.py]]
- 8 edges to [[_COMMUNITY_WebhookReceiver]]
- 5 edges to [[_COMMUNITY_GroupWorkspaceManager]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_test_session_manager.py]]
- 4 edges to [[_COMMUNITY_test_group_isolation.py]]
- 4 edges to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 4 edges to [[_COMMUNITY_test_shared_memory.py]]
- 4 edges to [[_COMMUNITY_TeamsConfig]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_TestAtomicRegistryWrites]]
- 3 edges to [[_COMMUNITY_TestMultiBotIsolation]]
- 3 edges to [[_COMMUNITY_test_file_sandbox_message_gate.py]]
- 3 edges to [[_COMMUNITY_test_middleware_coverage.py]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]
- 1 edge to [[_COMMUNITY_SharedMemoryManager]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_ingest_apimodels.py]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]

## Top bridge nodes
- [[UserSessionManager]] - degree 64, connects to 18 communities
- [[session_manager.py]] - degree 19, connects to 12 communities
- [[shared_memory.py]] - degree 12, connects to 8 communities
- [[test_session_isolation.py]] - degree 12, connects to 4 communities
- [[webhook_receiver.py]] - degree 7, connects to 4 communities
