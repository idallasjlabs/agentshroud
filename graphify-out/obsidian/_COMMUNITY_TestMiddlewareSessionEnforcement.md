---
type: community
members: 42
---

# TestMiddlewareSessionEnforcement

**Members:** 42 nodes

## Members
- [[dot-middleware_manager()]] - code - gateway/tests/test_session_isolation.py
- [[dot-mock_forwarder()]] - code - gateway/tests/test_session_isolation.py
- [[dot-mock_pipeline()]] - code - gateway/tests/test_session_isolation.py
- [[dot-session_manager()_1]] - code - gateway/tests/test_session_isolation.py
- [[dot-temp_workspace()_1]] - code - gateway/tests/test_session_isolation.py
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
- [[dot-test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[Blocked multi-turn sessions should not disclose scoring details.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a mock forwarder.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a mock security pipeline.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a session manager.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace for testing._1]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace._1]] - rationale - gateway/tests/test_session_isolation.py
- [[Create middleware manager with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Input normalization should strip zero-width obfuscation before guards run.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test WebhookReceiver integration with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test middleware enforcement of session boundaries.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that conversations are logged per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware blocks access to sensitive system files.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware blocks cross-session access attempts.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware injects session context.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that middleware requires user identification.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owner can perform cross-session actions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is injected into forwarded requests.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user IDs are properly extracted from webhook payloads.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that users can access their own workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestMiddlewareSessionEnforcement]] - code - gateway/tests/test_session_isolation.py
- [[TestWebhookReceiverIntegration]] - code - gateway/tests/test_session_isolation.py
- [[asyncio_3]] - code
- [[fixture_15]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMiddlewareSessionEnforcement
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_UserSessionManager]]
- 4 edges to [[_COMMUNITY_WebhookReceiver]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_TestUserSessionManager]]
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[TestMiddlewareSessionEnforcement]] - degree 15, connects to 3 communities
- [[TestWebhookReceiverIntegration]] - degree 11, connects to 2 communities
- [[dot-middleware_manager()]] - degree 5, connects to 2 communities
- [[asyncio_3]] - degree 13, connects to 1 community
- [[fixture_15]] - degree 9, connects to 1 community
