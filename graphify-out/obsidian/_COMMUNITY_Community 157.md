---
type: community
members: 41
---

# Community 157

**Members:** 41 nodes

## Members
- [[.__init__()_36]] - code - gateway/proxy/slack_socket_client.py
- [[._connect_and_handle()]] - code - gateway/proxy/slack_socket_client.py
- [[._get_wss_url()]] - code - gateway/proxy/slack_socket_client.py
- [[.run()]] - code - gateway/proxy/slack_socket_client.py
- [[.stop()_4]] - code - gateway/proxy/slack_socket_client.py
- [[.test_capped_at_cap_for_large_attempts()]] - code - gateway/tests/test_slack_socket_client.py
- [[.test_events_api_envelope_dispatches_handle_event()]] - code - gateway/tests/test_slack_socket_client.py
- [[.test_first_attempt_uses_base()]] - code - gateway/tests/test_slack_socket_client.py
- [[.test_get_wss_url_raises_on_api_error()]] - code - gateway/tests/test_slack_socket_client.py
- [[.test_get_wss_url_returns_url_on_success()]] - code - gateway/tests/test_slack_socket_client.py
- [[.test_grows_exponentially_with_attempt()]] - code - gateway/tests/test_slack_socket_client.py
- [[.test_hello_message_not_dispatched()]] - code - gateway/tests/test_slack_socket_client.py
- [[.test_jitter_stays_within_half_to_full_ceiling()]] - code - gateway/tests/test_slack_socket_client.py
- [[.test_run_resets_backoff_after_successful_connect()]] - code - gateway/tests/test_slack_socket_client.py
- [[.test_stop_sets_running_false()]] - code - gateway/tests/test_slack_socket_client.py
- [[A successful WSS connection resets the attempt counter to 0.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Attempt 0 waits at most the base interval (1s default).]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Backoff never exceeds the cap, even for huge attempt counts.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Call apps.connections.open to get a fresh WSS URL.]] - rationale - gateway/proxy/slack_socket_client.py
- [[Capped exponential backoff with jitter for reconnect attempts.      Returns a wa]] - rationale - gateway/proxy/slack_socket_client.py
- [[Jitter scales the wait between 50% and 100% of the ceiling.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Main reconnect loop. Runs until stop() is called.]] - rationale - gateway/proxy/slack_socket_client.py
- [[Maintains a persistent Socket Mode WebSocket connection to Slack.      Call run(]] - rationale - gateway/proxy/slack_socket_client.py
- [[Open the WebSocket and process events until Slack requests disconnect.]] - rationale - gateway/proxy/slack_socket_client.py
- [[Signal the run loop to exit.]] - rationale - gateway/proxy/slack_socket_client.py
- [[SlackSocketClient]] - code - gateway/proxy/slack_socket_client.py
- [[SlackSocketClient_1]] - code - gateway/tests/test_slack_socket_client.py
- [[TestComputeBackoff]] - code - gateway/tests/test_slack_socket_client.py
- [[TestSlackSocketClient]] - code - gateway/tests/test_slack_socket_client.py
- [[Unit tests for SlackSocketClient.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Unit tests for the reconnect backoff calculation.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[With jitter pinned to max, backoff doubles per attempt until the cap.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[_get_wss_url raises RuntimeError when apps.connections.open fails.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[_get_wss_url returns the WSS URL from apps.connections.open.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[_make_client()]] - code - gateway/tests/test_slack_socket_client.py
- [[compute_backoff()]] - code - gateway/proxy/slack_socket_client.py
- [[events_api envelopes call proxy.handle_event with the payload.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[hello messages are silently consumed without calling handle_event.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[slack_socket_client.py]] - code - gateway/proxy/slack_socket_client.py
- [[stop() signals the run loop to exit.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[test_slack_socket_client.py]] - code - gateway/tests/test_slack_socket_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_157
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 109]]
- 2 edges to [[_COMMUNITY_Community 25]]

## Top bridge nodes
- [[SlackSocketClient]] - degree 13, connects to 1 community
- [[_make_client()]] - degree 10, connects to 1 community
- [[.test_events_api_envelope_dispatches_handle_event()]] - degree 4, connects to 1 community
- [[.test_hello_message_not_dispatched()]] - degree 4, connects to 1 community
- [[slack_socket_client.py]] - degree 3, connects to 1 community