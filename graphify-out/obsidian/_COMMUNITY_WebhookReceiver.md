---
type: community
cohesion: 0.07
members: 42
---

# WebhookReceiver

**Cohesion:** 0.07 - loosely connected
**Members:** 42 nodes

## Members
- [[dot-__init__()_34]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_can_create_directory()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_message()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_user_id()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_username()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_prepare_session_payload()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_replace_message()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-get_stats()_5]] - code - gateway/proxy/webhook_receiver.py
- [[dot-process_webhook()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-session_manager()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[dot-validate_signature()]] - code - gateway/proxy/webhook_receiver.py
- [[Any_14]] - code - gateway/proxy/webhook_receiver.py
- [[Check if we can create the given directory path.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Collaborator Tracker Tests]] - code - gateway/tests/test_collaborator_tracker.py
- [[Create a session manager.]] - rationale - gateway/tests/test_session_isolation.py
- [[Extract display name from webhook payload.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract message text from webhook payload (Telegram format).]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract user ID from webhook payload based on source platform.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Path_9]] - code - gateway/proxy/webhook_receiver.py
- [[Prepare payload with session context injection.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Process an incoming webhook through the security pipeline.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Receives webhooks and routes them through the security pipeline.      In product]] - rationale - gateway/proxy/webhook_receiver.py
- [[Replace message text in payload with sanitized version.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Test WebhookReceiver integration with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that conversations are logged per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is injected into forwarded requests.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user IDs are properly extracted from webhook payloads.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestWebhookReceiverIntegration]] - code - gateway/tests/test_session_isolation.py
- [[Validate the X-Telegram-Bot-Api-Secret-Token header.          Uses constant-time]] - rationale - gateway/proxy/webhook_receiver.py
- [[Verify webhook receiver blocks prompt injection.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver routes through pipeline.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver strips PII.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[WebhookReceiver]] - code - gateway/proxy/webhook_receiver.py
- [[process_webhook passes agent_id as bot_id to record_activity.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[test_webhook_blocks_injection()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_webhook_receiver_processes()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_strips_pii()]] - code - gateway/tests/test_e2e_proxy.py
- [[webhook_receiver.py]] - code - gateway/proxy/webhook_receiver.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/WebhookReceiver
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 7 edges to [[_COMMUNITY_UserSessionManager]]
- 6 edges to [[_COMMUNITY__make_proxy]]
- 5 edges to [[_COMMUNITY_RBACConfig]]
- 4 edges to [[_COMMUNITY_TestMiddlewareSessionEnforcement]]
- 3 edges to [[_COMMUNITY_forward.py]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_TestHandleEvent]]
- 2 edges to [[_COMMUNITY_TestUserSessionManager]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY__get_gmail_app_password]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_Role]]
- 1 edge to [[_COMMUNITY_CollaboratorActivityTracker]]

## Top bridge nodes
- [[WebhookReceiver]] - degree 44, connects to 10 communities
- [[TestWebhookReceiverIntegration]] - degree 13, connects to 6 communities
- [[Path_9]] - degree 5, connects to 3 communities
- [[webhook_receiver.py]] - degree 4, connects to 3 communities
- [[Any_14]] - degree 9, connects to 2 communities
