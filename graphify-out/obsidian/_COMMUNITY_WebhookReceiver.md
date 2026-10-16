---
type: community
cohesion: 0.07
members: 36
---

# WebhookReceiver

**Cohesion:** 0.07 - loosely connected
**Members:** 36 nodes

## Members
- [[dot-_extract_message()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_user_id()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_username()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_prepare_session_payload()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_replace_message()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-get_stats()_8]] - code - gateway/proxy/webhook_receiver.py
- [[dot-process_webhook()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-test_extract_user_id_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_user_id_slack_missing_event()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_user_id_telegram_unchanged()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_username_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_username_slack_fallback_to_user_id()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[dot-validate_signature()]] - code - gateway/proxy/webhook_receiver.py
- [[Collaborator Tracker Tests]] - code - gateway/tests/test_collaborator_tracker.py
- [[Extract display name from webhook payload.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract message text from webhook payload (Telegram format).]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract user ID from webhook payload based on source platform.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Prepare payload with session context injection.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Process an incoming webhook through the security pipeline.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Receives webhooks and routes them through the security pipeline.      In product]] - rationale - gateway/proxy/webhook_receiver.py
- [[Replace message text in payload with sanitized version.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Test that conversations are logged per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is injected into forwarded requests.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user IDs are properly extracted from webhook payloads.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestWebhookReceiverSlackExtraction]] - code - gateway/tests/test_slack_proxy.py
- [[Validate the X-Telegram-Bot-Api-Secret-Token header.          Uses constant-time]] - rationale - gateway/proxy/webhook_receiver.py
- [[Verify webhook receiver blocks prompt injection.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver routes through pipeline.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver strips PII.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[WebhookReceiver]] - code - gateway/proxy/webhook_receiver.py
- [[test_webhook_blocks_injection()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_receiver_processes()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_strips_pii()]] - code - gateway/tests/test_e2e_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/WebhookReceiver
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_UserSessionManager]]
- 7 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 6 edges to [[_COMMUNITY__make_proxy]]
- 3 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_test_forward_stream.py]]
- 2 edges to [[_COMMUNITY_TestHandleEvent]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[WebhookReceiver]] - degree 44, connects to 8 communities
- [[TestWebhookReceiverSlackExtraction]] - degree 8, connects to 2 communities
- [[dot-process_webhook()]] - degree 8, connects to 1 community
- [[dot-_prepare_session_payload()]] - degree 5, connects to 1 community
- [[dot-_replace_message()]] - degree 5, connects to 1 community
