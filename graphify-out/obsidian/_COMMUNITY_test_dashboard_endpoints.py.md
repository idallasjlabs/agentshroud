---
type: community
cohesion: 0.07
members: 38
---

# test_dashboard_endpoints.py

**Cohesion:** 0.07 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-__init__()_132]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_can_create_directory()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_message()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_user_id()_1]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_extract_username()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_prepare_session_payload()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_replace_message()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-get_stats()_12]] - code - gateway/proxy/webhook_receiver.py
- [[dot-process_webhook()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[dot-validate_signature()]] - code - gateway/proxy/webhook_receiver.py
- [[Any_50]] - code - gateway/proxy/webhook_receiver.py
- [[Check if we can create the given directory path.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Collaborator Tracker Tests]] - code - gateway/tests/test_collaborator_tracker.py
- [[Extract display name from webhook payload.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract message text from webhook payload (Telegram format).]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract user ID from webhook payload based on source platform.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Path_37]] - code - gateway/proxy/webhook_receiver.py
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
- [[process_webhook passes agent_id as bot_id to record_activity.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[test_webhook_blocks_injection()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_webhook_receiver_processes()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_strips_pii()]] - code - gateway/tests/test_e2e_proxy.py
- [[webhook_receiver.py]] - code - gateway/proxy/webhook_receiver.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_dashboard_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_TestFabricatedSecurityNotice]]
- 8 edges to [[_COMMUNITY_EgressFilterConfig_2]]
- 6 edges to [[_COMMUNITY__make_proxy]]
- 5 edges to [[_COMMUNITY_MiddlewareManager]]
- 5 edges to [[_COMMUNITY_UserSessionManager_3]]
- 3 edges to [[_COMMUNITY_test_forward_stream.py]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py_1]]
- 2 edges to [[_COMMUNITY_TestHandleEvent]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_PipelineAction]]
- 1 edge to [[_COMMUNITY__get_gmail_app_password]]

## Top bridge nodes
- [[WebhookReceiver]] - degree 44, connects to 9 communities
- [[Path_37]] - degree 5, connects to 3 communities
- [[webhook_receiver.py]] - degree 4, connects to 3 communities
- [[Any_50]] - degree 9, connects to 2 communities
- [[dot-__init__()_132]] - degree 5, connects to 2 communities
