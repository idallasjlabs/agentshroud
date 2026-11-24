---
type: community
members: 67
---

# .test_events_api_envelope_dispatches_handle_event

**Members:** 67 nodes

## Members
- [[dot-__init__()_32]] - code - gateway/proxy/slack_socket_client.py
- [[dot-_connect_and_handle()]] - code - gateway/proxy/slack_socket_client.py
- [[dot-_get_wss_url()]] - code - gateway/proxy/slack_socket_client.py
- [[dot-run()_1]] - code - gateway/proxy/slack_socket_client.py
- [[dot-stop()_2]] - code - gateway/proxy/slack_socket_client.py
- [[dot-test_capped_at_cap_for_large_attempts()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_events_api_envelope_dispatches_handle_event()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_first_attempt_uses_base()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_get_wss_url_raises_on_api_error()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_get_wss_url_returns_url_on_success()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_grows_exponentially_with_attempt()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_hello_message_not_dispatched()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_jitter_stays_within_half_to_full_ceiling()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_run_resets_backoff_after_successful_connect()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_stop_sets_running_false()]] - code - gateway/tests/test_slack_socket_client.py
- [[A successful WSS connection resets the attempt counter to 0.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Attempt 0 waits at most the base interval (1s default).]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Backoff never exceeds the cap, even for huge attempt counts.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Call apps.connections.open to get a fresh WSS URL.]] - rationale - gateway/proxy/slack_socket_client.py
- [[Capped exponential backoff with jitter for reconnect attempts. Returns a wait…]] - rationale - gateway/proxy/slack_socket_client.py
- [[Jitter scales the wait between 50% and 100% of the ceiling.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Main reconnect loop. Runs until stop() is called.]] - rationale - gateway/proxy/slack_socket_client.py
- [[Maintains a persistent Socket Mode WebSocket connection to Slack. Call run() as…]] - rationale - gateway/proxy/slack_socket_client.py
- [[Open the WebSocket and process events until Slack requests disconnect.]] - rationale - gateway/proxy/slack_socket_client.py
- [[Signal the run loop to exit.]] - rationale - gateway/proxy/slack_socket_client.py
- [[Slack API Proxy — secures outbound bot → Slack traffic. Outbound Bot Slack API…]] - rationale - gateway/proxy/slack_proxy.py
- [[Slack Socket Mode client — receives Slack events via outbound WebSocket. No…]] - rationale - gateway/proxy/slack_socket_client.py
- [[SlackSocketClient]] - code - gateway/proxy/slack_socket_client.py
- [[TestComputeBackoff]] - code - gateway/tests/test_slack_socket_client.py
- [[TestSlackSocketClient]] - code - gateway/tests/test_slack_socket_client.py
- [[Tests for SlackSocketClient — gateway-side Slack Socket Mode listener. Verifies…]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Unit tests for SlackSocketClient.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Unit tests for the reconnect backoff calculation.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[With jitter pinned to max, backoff doubles per attempt until the cap.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[__aenter__()]] - code - gateway/tests/test_slack_socket_client.py
- [[__aenter__()_1]] - code - gateway/tests/test_slack_socket_client.py
- [[__aenter__()_2]] - code - gateway/tests/test_slack_socket_client.py
- [[__aenter__()_3]] - code - gateway/tests/test_slack_socket_client.py
- [[__aexit__()]] - code - gateway/tests/test_slack_socket_client.py
- [[__aexit__()_1]] - code - gateway/tests/test_slack_socket_client.py
- [[__aexit__()_2]] - code - gateway/tests/test_slack_socket_client.py
- [[__aexit__()_3]] - code - gateway/tests/test_slack_socket_client.py
- [[__aiter__()]] - code - gateway/tests/test_slack_socket_client.py
- [[__aiter__()_1]] - code - gateway/tests/test_slack_socket_client.py
- [[__anext__()]] - code - gateway/tests/test_slack_socket_client.py
- [[__anext__()_1]] - code - gateway/tests/test_slack_socket_client.py
- [[__init__()_5]] - code - gateway/tests/test_slack_socket_client.py
- [[__init__()_6]] - code - gateway/tests/test_slack_socket_client.py
- [[_get_wss_url raises RuntimeError when apps.connections.open fails.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[_get_wss_url returns the WSS URL from apps.connections.open.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[_make_client()]] - code - gateway/tests/test_slack_socket_client.py
- [[asyncio_19]] - code
- [[compute_backoff()]] - code - gateway/proxy/slack_socket_client.py
- [[events_api envelopes call proxy.handle_event with the payload.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[fake_backoff()]] - code - gateway/tests/test_slack_socket_client.py
- [[fake_connect_and_handle()]] - code - gateway/tests/test_slack_socket_client.py
- [[fake_get_wss_url()]] - code - gateway/tests/test_slack_socket_client.py
- [[fake_sleep()_1]] - code - gateway/tests/test_slack_socket_client.py
- [[hello messages are silently consumed without calling handle_event.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[post()]] - code - gateway/tests/test_slack_socket_client.py
- [[post()_1]] - code - gateway/tests/test_slack_socket_client.py
- [[send()_1]] - code - gateway/tests/test_slack_socket_client.py
- [[send()_2]] - code - gateway/tests/test_slack_socket_client.py
- [[slack_proxy.py]] - code - gateway/proxy/slack_proxy.py
- [[slack_socket_client.py]] - code - gateway/proxy/slack_socket_client.py
- [[stop() signals the run loop to exit.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[test_slack_socket_client.py]] - code - gateway/tests/test_slack_socket_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_events_api_envelope_dispatches_handle_event
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_SlackAPIProxy]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_read_secret]]
- 1 edge to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY__make_proxy]]

## Top bridge nodes
- [[slack_proxy.py]] - degree 9, connects to 7 communities
- [[dot-test_events_api_envelope_dispatches_handle_event()]] - degree 11, connects to 1 community
- [[dot-test_hello_message_not_dispatched()]] - degree 11, connects to 1 community
- [[_make_client()]] - degree 9, connects to 1 community
- [[slack_socket_client.py]] - degree 6, connects to 1 community
