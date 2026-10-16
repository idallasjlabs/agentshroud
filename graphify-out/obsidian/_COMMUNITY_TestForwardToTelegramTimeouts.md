---
type: community
cohesion: 0.33
members: 6
---

# TestForwardToTelegramTimeouts

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-_fake_urlopen_factory()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_long_poll_timeout_remains_60s()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_non_long_poll_timeout_is_15s()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Return a urlopen mock that records the timeout kwarg and succeeds.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[getUpdates must use a 60s urlopen timeout so the long-poll is not aborted early.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[sendMessage and similar calls must use a 15s urlopen timeout.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestForwardToTelegramTimeouts
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_5]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy_7]]

## Top bridge nodes
- [[dot-test_long_poll_timeout_remains_60s()]] - degree 5, connects to 3 communities
- [[dot-test_non_long_poll_timeout_is_15s()]] - degree 5, connects to 3 communities
- [[dot-_fake_urlopen_factory()]] - degree 4, connects to 1 community
