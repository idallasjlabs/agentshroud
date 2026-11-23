---
type: community
members: 6
---

# .test_run_resets_backoff_after_successful_connect

**Members:** 6 nodes

## Members
- [[dot-test_run_resets_backoff_after_successful_connect()]] - code - gateway/tests/test_slack_socket_client.py
- [[A successful WSS connection resets the attempt counter to 0.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[fake_backoff()]] - code - gateway/tests/test_slack_socket_client.py
- [[fake_connect_and_handle()]] - code - gateway/tests/test_slack_socket_client.py
- [[fake_get_wss_url()]] - code - gateway/tests/test_slack_socket_client.py
- [[fake_sleep()]] - code - gateway/tests/test_slack_socket_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_run_resets_backoff_after_successful_connect
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_compute_backoff]]
- 1 edge to [[_COMMUNITY__make_client]]
- 1 edge to [[_COMMUNITY_test_slack_socket_client.py]]

## Top bridge nodes
- [[dot-test_run_resets_backoff_after_successful_connect()]] - degree 8, connects to 3 communities
