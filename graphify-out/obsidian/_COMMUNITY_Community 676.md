---
type: community
cohesion: 0.15
members: 14
---

# Community 676

**Cohesion:** 0.15 - loosely connected
**Members:** 14 nodes

## Members
- [[._call_slack_api()]] - code - gateway/proxy/slack_proxy.py
- [[._intercept_connections_open()]] - code - gateway/proxy/slack_proxy.py
- [[._is_owner_channel()]] - code - gateway/proxy/slack_proxy.py
- [[.invite_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[.kick_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[.provision_group_channel()]] - code - gateway/proxy/slack_proxy.py
- [[.proxy_outbound()]] - code - gateway/proxy/slack_proxy.py
- [[Create a Slack channel for a group. Returns channel_id or None on failure.]] - rationale - gateway/proxy/slack_proxy.py
- [[Intercept apps.connections.open rewrite the returned WSS URL to route         t]] - rationale - gateway/proxy/slack_proxy.py
- [[Invite a Slack user to a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[POST to httpsslack.comapimethod with the bot token.]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxy a bot Slack Web API call through the security pipeline.          For messa]] - rationale - gateway/proxy/slack_proxy.py
- [[Remove a Slack user from a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[Return True if channel is a DM with the configured owner.          In Slack, DM]] - rationale - gateway/proxy/slack_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_676
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 24]]

## Top bridge nodes
- [[._call_slack_api()]] - degree 7, connects to 1 community
- [[.proxy_outbound()]] - degree 5, connects to 1 community
- [[._intercept_connections_open()]] - degree 4, connects to 1 community
- [[.invite_channel_member()]] - degree 3, connects to 1 community
- [[._is_owner_channel()]] - degree 3, connects to 1 community