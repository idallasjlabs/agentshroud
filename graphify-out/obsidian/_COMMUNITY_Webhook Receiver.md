---
type: community
cohesion: 0.03
members: 87
---

# Webhook Receiver

**Cohesion:** 0.03 - loosely connected
**Members:** 87 nodes

## Members
- [[._extract_message()]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_user_id()_1]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_username()]] - code - gateway/proxy/webhook_receiver.py
- [[._prepare_session_payload()]] - code - gateway/proxy/webhook_receiver.py
- [[._replace_message()]] - code - gateway/proxy/webhook_receiver.py
- [[.get_stats()_11]] - code - gateway/proxy/webhook_receiver.py
- [[.mock_forwarder()]] - code - gateway/tests/test_session_isolation.py
- [[.mock_pipeline()]] - code - gateway/tests/test_session_isolation.py
- [[.process_webhook()]] - code - gateway/proxy/webhook_receiver.py
- [[.temp_workspace()_2]] - code - gateway/tests/test_session_isolation.py
- [[.temp_workspace()_3]] - code - gateway/tests/test_session_isolation.py
- [[.temp_workspace()]] - code - gateway/tests/test_session_isolation.py
- [[.temp_workspace()_1]] - code - gateway/tests/test_session_isolation.py
- [[.test_conversation_history_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[.test_memory_file_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_cross_session_blocking()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_file_path_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_normalizes_invisible_unicode()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_own_workspace_allowed()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_owner_bypass()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[.test_middleware_user_identification()]] - code - gateway/tests/test_session_isolation.py
- [[.test_multi_turn_block_reason_hides_score()]] - code - gateway/tests/test_session_isolation.py
- [[.test_owner_access_control()]] - code - gateway/tests/test_session_isolation.py
- [[.test_session_context_generation()]] - code - gateway/tests/test_session_isolation.py
- [[.test_session_creation()]] - code - gateway/tests/test_session_isolation.py
- [[.test_session_isolation_directories()]] - code - gateway/tests/test_session_isolation.py
- [[.test_session_listing_authorization()]] - code - gateway/tests/test_session_isolation.py
- [[.test_session_prompt_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[.test_trust_level_per_user()]] - code - gateway/tests/test_session_isolation.py
- [[.test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[.test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[.test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[.validate_signature()]] - code - gateway/proxy/webhook_receiver.py
- [[A single message in a conversation.]] - rationale - gateway/security/session_manager.py
- [[Any_21]] - code - gateway/proxy/webhook_receiver.py
- [[Blocked multi-turn sessions should not disclose scoring details.]] - rationale - gateway/tests/test_session_isolation.py
- [[ConversationMessage]] - code - gateway/security/session_manager.py
- [[Create a mock forwarder.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a mock security pipeline.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace for testing._1]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace for testing.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace._1]] - rationale - gateway/tests/test_session_isolation.py
- [[End-to-end integration tests for session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Extract display name from webhook payload.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract message text from webhook payload (Telegram format).]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract user ID from webhook payload based on source platform.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Input normalization should strip zero-width obfuscation before guards run.]] - rationale - gateway/tests/test_session_isolation.py
- [[Prepare payload with session context injection.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Process an incoming webhook through the security pipeline.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Receives webhooks and routes them through the security pipeline.      In product]] - rationale - gateway/proxy/webhook_receiver.py
- [[Replace message text in payload with sanitized version.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Test WebhookReceiver integration with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
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
- [[Test that session context is injected into forwarded requests.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is properly generated.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session listing respects authorization.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session prompts include isolation instructions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that trust levels are tracked per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user IDs are properly extracted from webhook payloads.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user sessions are created properly.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that users can access their own workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test the UserSessionManager for per-user isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestMiddlewareSessionEnforcement]] - code - gateway/tests/test_session_isolation.py
- [[TestSessionIsolationEndToEnd]] - code - gateway/tests/test_session_isolation.py
- [[TestUserSessionManager]] - code - gateway/tests/test_session_isolation.py
- [[TestWebhookReceiverIntegration]] - code - gateway/tests/test_session_isolation.py
- [[Validate the X-Telegram-Bot-Api-Secret-Token header.          Uses constant-time]] - rationale - gateway/proxy/webhook_receiver.py
- [[Verify webhook receiver blocks prompt injection.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver routes through pipeline.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver strips PII.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[WebhookReceiver]] - code - gateway/proxy/webhook_receiver.py
- [[test_session_isolation.py]] - code - gateway/tests/test_session_isolation.py
- [[test_webhook_blocks_injection()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_receiver_processes()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_strips_pii()]] - code - gateway/tests/test_e2e_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Webhook_Receiver
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Session Manager & Webhook]]
- 14 edges to [[_COMMUNITY_Module Group 111]]
- 8 edges to [[_COMMUNITY_Sidecar Security Scanner]]
- 5 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 5 edges to [[_COMMUNITY_Slack Proxy Tests]]
- 5 edges to [[_COMMUNITY_RBAC Configuration]]
- 2 edges to [[_COMMUNITY_Module Group 195]]
- 2 edges to [[_COMMUNITY_Module Group 289]]
- 2 edges to [[_COMMUNITY_Module Group 196]]
- 2 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 2 edges to [[_COMMUNITY_Module Group 104]]
- 2 edges to [[_COMMUNITY_Module Group 74]]
- 1 edge to [[_COMMUNITY_Module Group 496]]
- 1 edge to [[_COMMUNITY_Module Group 189]]
- 1 edge to [[_COMMUNITY_Module Group 259]]

## Top bridge nodes
- [[WebhookReceiver]] - degree 42, connects to 9 communities
- [[ConversationMessage]] - degree 19, connects to 4 communities
- [[TestUserSessionManager]] - degree 19, connects to 4 communities
- [[TestMiddlewareSessionEnforcement]] - degree 18, connects to 4 communities
- [[TestWebhookReceiverIntegration]] - degree 15, connects to 4 communities