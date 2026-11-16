---
type: community
members: 35
---

# Community 381

**Members:** 35 nodes

## Members
- [[.__init__()_50]] - code - gateway/proxy/slack_proxy.py
- [[.__init__()_208]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[._call_slack_api()]] - code - gateway/proxy/slack_proxy.py
- [[._intercept_connections_open()]] - code - gateway/proxy/slack_proxy.py
- [[._is_owner_channel()]] - code - gateway/proxy/slack_proxy.py
- [[.consume_relay_token()]] - code - gateway/proxy/slack_proxy.py
- [[.get_stats()_8]] - code - gateway/proxy/slack_proxy.py
- [[.handle_event()]] - code - gateway/proxy/slack_proxy.py
- [[.info_filter_redaction_count()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.invite_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[.kick_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[.provision_group_channel()]] - code - gateway/proxy/slack_proxy.py
- [[.proxy_outbound()]] - code - gateway/proxy/slack_proxy.py
- [[.test_extract_user_id_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_extract_user_id_slack_missing_event()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_extract_user_id_telegram_unchanged()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_extract_username_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_extract_username_slack_fallback_to_user_id()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_redaction_count_access_error_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
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
TABLE source_file, type FROM #community/Community_381
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Community 37]]
- 7 edges to [[_COMMUNITY_Community 100]]
- 2 edges to [[_COMMUNITY_Community 660]]
- 2 edges to [[_COMMUNITY_Community 176]]
- 1 edge to [[_COMMUNITY_Community 68]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 84]]
- 1 edge to [[_COMMUNITY_Community 18]]
- 1 edge to [[_COMMUNITY_Community 14]]
- 1 edge to [[_COMMUNITY_Community 114]]

## Top bridge nodes
- [[SlackAPIProxy]] - degree 38, connects to 8 communities
- [[TestWebhookReceiverSlackExtraction]] - degree 8, connects to 2 communities
- [[_RaisingRedactionResult]] - degree 6, connects to 1 community
- [[.test_redaction_count_access_error_is_non_fatal()]] - degree 5, connects to 1 community
- [[TestRedactionCountErrorSwallow]] - degree 3, connects to 1 community