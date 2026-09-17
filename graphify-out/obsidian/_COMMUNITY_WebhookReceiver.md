---
type: community
cohesion: 0.08
members: 35
---

# WebhookReceiver

**Cohesion:** 0.08 - loosely connected
**Members:** 35 nodes

## Members
- [[.__init__()_141]] - code - gateway/proxy/webhook_receiver.py
- [[._can_create_directory()]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_message()]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_user_id()_1]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_username()]] - code - gateway/proxy/webhook_receiver.py
- [[._prepare_session_payload()]] - code - gateway/proxy/webhook_receiver.py
- [[._replace_message()]] - code - gateway/proxy/webhook_receiver.py
- [[.get_stats()_7]] - code - gateway/proxy/webhook_receiver.py
- [[.process_webhook()]] - code - gateway/proxy/webhook_receiver.py
- [[.test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[.test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[.test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[.validate_signature()]] - code - gateway/proxy/webhook_receiver.py
- [[Any_51]] - code - gateway/proxy/webhook_receiver.py
- [[Check if we can create the given directory path.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Collaborator Tracker Tests]] - code - gateway/tests/test_collaborator_tracker.py
- [[Extract display name from webhook payload.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract message text from webhook payload (Telegram format).]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract user ID from webhook payload based on source platform.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Path_28]] - code - gateway/proxy/webhook_receiver.py
- [[Prepare payload with session context injection.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Process an incoming webhook through the security pipeline.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Receives webhooks and routes them through the security pipeline.      In product]] - rationale - gateway/proxy/webhook_receiver.py
- [[Replace message text in payload with sanitized version.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Test that conversations are logged per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is injected into forwarded requests.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user IDs are properly extracted from webhook payloads.]] - rationale - gateway/tests/test_session_isolation.py
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
- 12 edges to [[_COMMUNITY_MiddlewareManager]]
- 8 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 5 edges to [[_COMMUNITY__make_proxy()]]
- 4 edges to [[_COMMUNITY_RBACConfig]]
- 3 edges to [[_COMMUNITY_CollaboratorActivityTracker]]
- 3 edges to [[_COMMUNITY_forward.py]]
- 2 edges to [[_COMMUNITY_TestHandleEvent]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_TestWebhookReceiverSlackExtraction]]
- 1 edge to [[_COMMUNITY__get_gmail_app_password()]]

## Top bridge nodes
- [[WebhookReceiver]] - degree 44, connects to 9 communities
- [[Path_28]] - degree 5, connects to 3 communities
- [[Any_51]] - degree 9, connects to 2 communities
- [[.__init__()_141]] - degree 5, connects to 2 communities
- [[test_webhook_blocks_injection()]] - degree 3, connects to 1 community