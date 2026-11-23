---
type: community
members: 12
---

# compute_backoff

**Members:** 12 nodes

## Members
- [[dot-test_capped_at_cap_for_large_attempts()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_first_attempt_uses_base()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_grows_exponentially_with_attempt()]] - code - gateway/tests/test_slack_socket_client.py
- [[dot-test_jitter_stays_within_half_to_full_ceiling()]] - code - gateway/tests/test_slack_socket_client.py
- [[Attempt 0 waits at most the base interval (1s default).]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Backoff never exceeds the cap, even for huge attempt counts.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[Capped exponential backoff with jitter for reconnect attempts. Returns a wait…]] - rationale - gateway/proxy/slack_socket_client.py
- [[Jitter scales the wait between 50% and 100% of the ceiling.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[TestComputeBackoff]] - code - gateway/tests/test_slack_socket_client.py
- [[Unit tests for the reconnect backoff calculation.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[With jitter pinned to max, backoff doubles per attempt until the cap.]] - rationale - gateway/tests/test_slack_socket_client.py
- [[compute_backoff()]] - code - gateway/proxy/slack_socket_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/compute_backoff
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_slack_socket_client.py]]
- 1 edge to [[_COMMUNITY_dot-test_run_resets_backoff_after_successful_connect]]
- 1 edge to [[_COMMUNITY_SlackSocketClient]]

## Top bridge nodes
- [[compute_backoff()]] - degree 8, connects to 2 communities
- [[TestComputeBackoff]] - degree 7, connects to 2 communities
