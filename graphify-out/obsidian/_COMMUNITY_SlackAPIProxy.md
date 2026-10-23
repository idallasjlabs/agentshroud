---
type: community
cohesion: 0.09
members: 30
---

# SlackAPIProxy

**Cohesion:** 0.09 - loosely connected
**Members:** 30 nodes

## Members
- [[dot-__init__()_116]] - code - gateway/proxy/slack_proxy.py
- [[dot-__init__()_117]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-_call_slack_api()]] - code - gateway/proxy/slack_proxy.py
- [[dot-_intercept_connections_open()]] - code - gateway/proxy/slack_proxy.py
- [[dot-_is_owner_channel()]] - code - gateway/proxy/slack_proxy.py
- [[dot-consume_relay_token()]] - code - gateway/proxy/slack_proxy.py
- [[dot-get_stats()_10]] - code - gateway/proxy/slack_proxy.py
- [[dot-handle_event()]] - code - gateway/proxy/slack_proxy.py
- [[dot-info_filter_redaction_count()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-invite_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[dot-kick_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[dot-provision_group_channel()]] - code - gateway/proxy/slack_proxy.py
- [[dot-proxy_outbound()]] - code - gateway/proxy/slack_proxy.py
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
- [[_RaisingRedactionResult]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[slack_proxy.py]] - code - gateway/proxy/slack_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SlackAPIProxy
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_api.py (2)]]
- 6 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_Request (2)]]
- 2 edges to [[_COMMUNITY_test_anthropic_openai_translator.py (2)]]
- 1 edge to [[_COMMUNITY_WebhookReceiver]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_SecurityPipeline (2)]]

## Top bridge nodes
- [[SlackAPIProxy]] - degree 37, connects to 7 communities
- [[slack_proxy.py]] - degree 3, connects to 2 communities
- [[_RaisingRedactionResult]] - degree 6, connects to 1 community
- [[dot-test_redaction_count_access_error_is_non_fatal()]] - degree 5, connects to 1 community
- [[TestRedactionCountErrorSwallow]] - degree 3, connects to 1 community
