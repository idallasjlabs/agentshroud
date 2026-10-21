---
type: community
members: 14
---

# RBACConfig (2)

**Members:** 14 nodes

## Members
- [[dot-_call_slack_api()]] - code - gateway/proxy/slack_proxy.py
- [[dot-_intercept_connections_open()]] - code - gateway/proxy/slack_proxy.py
- [[dot-_is_owner_channel()]] - code - gateway/proxy/slack_proxy.py
- [[dot-invite_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[dot-kick_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[dot-provision_group_channel()]] - code - gateway/proxy/slack_proxy.py
- [[dot-proxy_outbound()]] - code - gateway/proxy/slack_proxy.py
- [[Create a Slack channel for a group. Returns channel_id or None on failure.]] - rationale - gateway/proxy/slack_proxy.py
- [[Intercept apps.connections.open rewrite the returned WSS URL to route         t]] - rationale - gateway/proxy/slack_proxy.py
- [[Invite a Slack user to a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[POST to httpsslack.comapimethod with the bot token.]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxy a bot Slack Web API call through the security pipeline.          For messa]] - rationale - gateway/proxy/slack_proxy.py
- [[Remove a Slack user from a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[Return True if channel is a DM with the configured owner.          In Slack, DM]] - rationale - gateway/proxy/slack_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RBACConfig_2
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_api.py (2)]]

## Top bridge nodes
- [[dot-_call_slack_api()]] - degree 7, connects to 1 community
- [[dot-proxy_outbound()]] - degree 5, connects to 1 community
- [[dot-_intercept_connections_open()]] - degree 4, connects to 1 community
- [[dot-invite_channel_member()]] - degree 3, connects to 1 community
- [[dot-_is_owner_channel()]] - degree 3, connects to 1 community
