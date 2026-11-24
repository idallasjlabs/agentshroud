---
type: community
members: 20
---

# .process_webhook

**Members:** 20 nodes

## Members
- [[dot-_extract_message()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_user_id()_1]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_username()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_prepare_session_payload()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_replace_message()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-get_stats()_15]] - code - gateway/proxy/webhook_receiver.py
- [[dot-process_webhook()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-test_extract_user_id_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_user_id_slack_missing_event()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_user_id_telegram_unchanged()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_username_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_username_slack_fallback_to_user_id()]] - code - gateway/tests/test_slack_proxy.py
- [[Any_71]] - code
- [[Extract display name from webhook payload.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract message text from webhook payload (Telegram format).]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract user ID from webhook payload based on source platform.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Prepare payload with session context injection.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Process an incoming webhook through the security pipeline.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Replace message text in payload with sanitized version.]] - rationale - gateway/proxy/webhook_receiver.py
- [[TestWebhookReceiverSlackExtraction]] - code - gateway/tests/test_slack_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/process_webhook
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY__make_proxy]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[dot-process_webhook()]] - degree 9, connects to 2 communities
- [[TestWebhookReceiverSlackExtraction]] - degree 7, connects to 2 communities
- [[dot-_extract_user_id()_1]] - degree 7, connects to 1 community
- [[dot-_extract_username()]] - degree 6, connects to 1 community
- [[dot-_prepare_session_payload()]] - degree 5, connects to 1 community
