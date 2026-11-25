---
type: community
members: 26
---

# WebhookReceiver

**Members:** 26 nodes

## Members
- [[dot-__init__()_181]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_can_create_directory()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_message()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_user_id()_1]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_username()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_prepare_session_payload()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_replace_message()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-get_stats()_16]] - code - gateway/proxy/webhook_receiver.py
- [[dot-process_webhook()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-test_extract_user_id_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_user_id_slack_missing_event()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_user_id_telegram_unchanged()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_username_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_username_slack_fallback_to_user_id()]] - code - gateway/tests/test_slack_proxy.py
- [[Any_68]] - code
- [[Check if we can create the given directory path.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract display name from webhook payload.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract message text from webhook payload (Telegram format).]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract user ID from webhook payload based on source platform.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Path_63]] - code
- [[Prepare payload with session context injection.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Process an incoming webhook through the security pipeline.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Receives webhooks and routes them through the security pipeline. In production,…]] - rationale - gateway/proxy/webhook_receiver.py
- [[Replace message text in payload with sanitized version.]] - rationale - gateway/proxy/webhook_receiver.py
- [[TestWebhookReceiverSlackExtraction]] - code - gateway/tests/test_slack_proxy.py
- [[WebhookReceiver]] - code - gateway/proxy/webhook_receiver.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/WebhookReceiver
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 4 edges to [[_COMMUNITY_TestMiddlewareSessionEnforcement]]
- 4 edges to [[_COMMUNITY_UserSessionManager]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY__make_proxy]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_test_webhook_receiver_passes_agent_id_as_bot_id]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[WebhookReceiver]] - degree 30, connects to 8 communities
- [[dot-__init__()_181]] - degree 4, connects to 2 communities
- [[dot-process_webhook()]] - degree 9, connects to 1 community
- [[TestWebhookReceiverSlackExtraction]] - degree 7, connects to 1 community
