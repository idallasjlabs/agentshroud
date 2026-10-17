---
type: community
members: 35
---

# AsyncMock (2)

**Members:** 35 nodes

## Members
- [[dot-__init__()_95]] - code - gateway/proxy/slack_proxy.py
- [[dot-__init__()_96]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-_call_slack_api()]] - code - gateway/proxy/slack_proxy.py
- [[dot-_intercept_connections_open()]] - code - gateway/proxy/slack_proxy.py
- [[dot-_is_owner_channel()]] - code - gateway/proxy/slack_proxy.py
- [[dot-consume_relay_token()]] - code - gateway/proxy/slack_proxy.py
- [[dot-get_stats()_9]] - code - gateway/proxy/slack_proxy.py
- [[dot-handle_event()]] - code - gateway/proxy/slack_proxy.py
- [[dot-info_filter_redaction_count()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-invite_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[dot-kick_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[dot-provision_group_channel()]] - code - gateway/proxy/slack_proxy.py
- [[dot-proxy_outbound()]] - code - gateway/proxy/slack_proxy.py
- [[dot-test_extract_user_id_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_user_id_slack_missing_event()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_user_id_telegram_unchanged()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_username_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_extract_username_slack_fallback_to_user_id()]] - code - gateway/tests/test_slack_proxy.py
- [[dot-test_redaction_count_access_error_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[Create a Slack channel for a group. Returns channel_id or None on failure.]] - rationale - gateway/proxy/slack_proxy.py
- [[Handle an inbound Slack event payload received via Socket Mode.          Called]] - rationale - gateway/proxy/slack_proxy.py
- [[Intercept apps.connections.open rewrite the returned WSS URL to route         t]] - rationale - gateway/proxy/slack_proxy.py
- [[Invite a Slack user to a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[Non-owner channel error reading info_filter_redaction_count is swallowed]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[POST to httpsslack.comapimethod with the bot token.]] - rationale - gateway/proxy/slack_proxy.py
- [[Pipeline result whose redaction-count attribute raises on access.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Pop and return the real WSS URL for a relay token (one-time use).          Retur]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxies bot Slack Web API calls through SecurityPipeline.      Outbound flow (bo]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxy a bot Slack Web API call through the security pipeline.          For messa]] - rationale - gateway/proxy/slack_proxy.py
- [[Remove a Slack user from a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[Return True if channel is a DM with the configured owner.          In Slack, DM]] - rationale - gateway/proxy/slack_proxy.py
- [[SlackAPIProxy]] - code - gateway/proxy/slack_proxy.py
- [[TestRedactionCountErrorSwallow]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestWebhookReceiverSlackExtraction]] - code - gateway/tests/test_slack_proxy.py
- [[_RaisingRedactionResult]] - code - gateway/tests/test_slack_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AsyncMock_2
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_AsyncMock]]
- 7 edges to [[_COMMUNITY__make_proxy]]
- 2 edges to [[_COMMUNITY_SlackSocketClient]]
- 2 edges to [[_COMMUNITY_TestHandleEvent]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_test_dashboard_endpoints.py]]

## Top bridge nodes
- [[SlackAPIProxy]] - degree 37, connects to 7 communities
- [[TestWebhookReceiverSlackExtraction]] - degree 8, connects to 2 communities
- [[_RaisingRedactionResult]] - degree 6, connects to 1 community
- [[dot-test_redaction_count_access_error_is_non_fatal()]] - degree 5, connects to 1 community
- [[TestRedactionCountErrorSwallow]] - degree 3, connects to 1 community
