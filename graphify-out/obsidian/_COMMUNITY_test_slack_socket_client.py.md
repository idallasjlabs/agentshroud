---
type: community
members: 5
---

# test_slack_socket_client.py

**Members:** 5 nodes

## Members
- [[Slack Socket Mode client — receives Slack events via outbound WebSocket. No…]] - rationale - gateway/proxy/slack_socket_client.py
- [[Tests for SlackSocketClient — gateway-side Slack Socket Mode listener. Verifies…]] - rationale - gateway/tests/test_slack_socket_client.py
- [[asyncio_34]] - code
- [[slack_socket_client.py]] - code - gateway/proxy/slack_socket_client.py
- [[test_slack_socket_client.py]] - code - gateway/tests/test_slack_socket_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_slack_socket_clientpy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_compute_backoff]]
- 3 edges to [[_COMMUNITY__make_client]]
- 2 edges to [[_COMMUNITY_SlackSocketClient]]
- 1 edge to [[_COMMUNITY_SlackAPIProxy]]
- 1 edge to [[_COMMUNITY_dot-test_events_api_envelope_dispatches_handle_event]]
- 1 edge to [[_COMMUNITY_dot-test_hello_message_not_dispatched]]
- 1 edge to [[_COMMUNITY_dot-test_run_resets_backoff_after_successful_connect]]
- 1 edge to [[_COMMUNITY_dot-test_get_wss_url_returns_url_on_success]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[asyncio_34]] - degree 6, connects to 5 communities
- [[slack_socket_client.py]] - degree 6, connects to 4 communities
- [[test_slack_socket_client.py]] - degree 8, connects to 3 communities
