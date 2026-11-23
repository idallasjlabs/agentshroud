---
type: community
members: 10
---

# _make_client

**Members:** 10 nodes

## Members
- [[dot-test_get_wss_url_raises_on_api_error()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_stop_sets_running_false()]] - code - gateway/tests/test_slack_socket_client.py
- [[TestSlackSocketClient]] - code - gateway/tests/test_slack_socket_client.py
- [[Unit tests for SlackSocketClient.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[__aenter__()]] - code - gateway/tests/test_slack_socket_client.py
- [[__aexit__()]] - code - gateway/tests/test_slack_socket_client.py
- [[_get_wss_url raises RuntimeError when apps.connections.open fails.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[_make_client()]] - code - gateway/tests/test_slack_socket_client.py
- [[post()]] - code - gateway/tests/test_slack_socket_client.py
- [[stop() signals the run loop to exit.]] - rationale - gateway/tests/test_slack_socket_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_client
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_slack_socket_client.py]]
- 2 edges to [[_COMMUNITY_dot-test_get_wss_url_returns_url_on_success]]
- 2 edges to [[_COMMUNITY_dot-test_events_api_envelope_dispatches_handle_event]]
- 2 edges to [[_COMMUNITY_dot-test_hello_message_not_dispatched]]
- 1 edge to [[_COMMUNITY_SlackSocketClient]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_dot-test_run_resets_backoff_after_successful_connect]]

## Top bridge nodes
- [[_make_client()]] - degree 9, connects to 7 communities
- [[TestSlackSocketClient]] - degree 7, connects to 4 communities
- [[dot-test_get_wss_url_raises_on_api_error()]] - degree 7, connects to 1 community
