---
type: community
members: 26
---

# SlackAPIProxy

**Members:** 26 nodes

## Members
- [[dot-__init__()_198]] - code - gateway/proxy/slack_proxy.py
- [[dot-__init__()_199]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-_call_slack_api()]] - code - gateway/proxy/slack_proxy.py
- [[dot-_intercept_connections_open()]] - code - gateway/proxy/slack_proxy.py
- [[dot-_is_owner_channel()]] - code - gateway/proxy/slack_proxy.py
- [[dot-consume_relay_token()]] - code - gateway/proxy/slack_proxy.py
- [[dot-get_stats()_17]] - code - gateway/proxy/slack_proxy.py
- [[dot-handle_event()]] - code - gateway/proxy/slack_proxy.py
- [[dot-info_filter_redaction_count()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-invite_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[dot-kick_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[dot-provision_group_channel()]] - code - gateway/proxy/slack_proxy.py
- [[dot-proxy_outbound()]] - code - gateway/proxy/slack_proxy.py
- [[Create a Slack channel for a group. Returns channel_id or None on failure.…]] - rationale - gateway/proxy/slack_proxy.py
- [[Handle an inbound Slack event payload received via Socket Mode. Called by…]] - rationale - gateway/proxy/slack_proxy.py
- [[Intercept apps.connections.open rewrite the returned WSS URL to route the…]] - rationale - gateway/proxy/slack_proxy.py
- [[Invite a Slack user to a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[POST to httpsslack.comapimethod with the bot token.]] - rationale - gateway/proxy/slack_proxy.py
- [[Pipeline result whose redaction-count attribute raises on access.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Pop and return the real WSS URL for a relay token (one-time use). Returns None…]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxies bot Slack Web API calls through SecurityPipeline. Outbound flow (bot-…]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxy a bot Slack Web API call through the security pipeline. For message-…]] - rationale - gateway/proxy/slack_proxy.py
- [[Remove a Slack user from a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[Return True if channel is a DM with the configured owner. In Slack, DM channels…]] - rationale - gateway/proxy/slack_proxy.py
- [[SlackAPIProxy]] - code - gateway/proxy/slack_proxy.py
- [[_RaisingRedactionResult]] - code - gateway/tests/test_slack_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SlackAPIProxy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY__make_proxy]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_dot-test_events_api_envelope_dispatches_handle_event]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[SlackAPIProxy]] - degree 21, connects to 5 communities
- [[_RaisingRedactionResult]] - degree 5, connects to 1 community
- [[dot-info_filter_redaction_count()]] - degree 3, connects to 1 community
