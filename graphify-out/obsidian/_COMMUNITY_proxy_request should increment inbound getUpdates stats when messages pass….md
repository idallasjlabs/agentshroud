---
type: community
members: 10
---

# proxy_request should increment inbound getUpdates stats when messages pass…

**Members:** 10 nodes

## Members
- [[dot-test_proxy_request_returns_ack_only_updates_when_all_dropped()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_tracks_getupdates_stats_for_dropped_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_tracks_getupdates_stats_for_forwarded_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[When all getUpdates items are locally handleddropped, return ack-only…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_forward()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_forward()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_forward()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_start_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request should increment inbound getUpdates stats when messages pass…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request should track dropped updates (e.g. collaborator blocked command).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/proxy_request_should_increment_inbound_getUpdates_stats_when_messages_pass
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_FakeRBAC]]
- 3 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]
- 3 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]

## Top bridge nodes
- [[dot-test_proxy_request_returns_ack_only_updates_when_all_dropped()]] - degree 8, connects to 2 communities
- [[dot-test_proxy_request_tracks_getupdates_stats_for_dropped_message()]] - degree 7, connects to 2 communities
- [[dot-test_proxy_request_tracks_getupdates_stats_for_forwarded_message()]] - degree 6, connects to 2 communities
- [[fake_forward()_2]] - degree 5, connects to 2 communities
- [[fake_forward()]] - degree 3, connects to 2 communities
