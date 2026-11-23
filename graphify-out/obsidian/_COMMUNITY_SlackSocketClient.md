---
type: community
members: 11
---

# SlackSocketClient

**Members:** 11 nodes

## Members
- [[dot-__init__()_38]] - code - gateway/proxy/slack_socket_client.py
- [[dot-_connect_and_handle()]] - code - gateway/proxy/slack_socket_client.py
- [[dot-_get_wss_url()]] - code - gateway/proxy/slack_socket_client.py
- [[dot-run()_1]] - code - gateway/proxy/slack_socket_client.py
- [[dot-stop()_3]] - code - gateway/proxy/slack_socket_client.py
- [[Call apps.connections.open to get a fresh WSS URL.]] - rationale - gateway/proxy/slack_socket_client.py
- [[Main reconnect loop. Runs until stop() is called.]] - rationale - gateway/proxy/slack_socket_client.py
- [[Maintains a persistent Socket Mode WebSocket connection to Slack. Call run() as…]] - rationale - gateway/proxy/slack_socket_client.py
- [[Open the WebSocket and process events until Slack requests disconnect.]] - rationale - gateway/proxy/slack_socket_client.py
- [[Signal the run loop to exit.]] - rationale - gateway/proxy/slack_socket_client.py
- [[SlackSocketClient]] - code - gateway/proxy/slack_socket_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SlackSocketClient
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_slack_socket_client.py]]
- 1 edge to [[_COMMUNITY__make_client]]
- 1 edge to [[_COMMUNITY_compute_backoff]]

## Top bridge nodes
- [[SlackSocketClient]] - degree 9, connects to 2 communities
- [[dot-run()_1]] - degree 5, connects to 1 community
