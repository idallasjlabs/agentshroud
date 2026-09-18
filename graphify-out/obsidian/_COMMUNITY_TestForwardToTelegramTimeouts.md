---
type: community
cohesion: 0.32
members: 8
---

# TestForwardToTelegramTimeouts

**Cohesion:** 0.32 - loosely connected
**Members:** 8 nodes

## Members
- [[._fake_urlopen_factory()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_long_poll_timeout_remains_60s()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_non_long_poll_timeout_is_15s()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Return a urlopen mock that records the timeout kwarg and succeeds.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestForwardToTelegramTimeouts]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests that _forward_to_telegram uses correct urlopen timeouts.      Regression g]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[getUpdates must use a 60s urlopen timeout so the long-poll is not aborted early.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[sendMessage and similar calls must use a 15s urlopen timeout.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestForwardToTelegramTimeouts
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_CollaboratorActivityTracker]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[TestForwardToTelegramTimeouts]] - degree 9, connects to 4 communities
- [[.test_long_poll_timeout_remains_60s()]] - degree 5, connects to 1 community
- [[.test_non_long_poll_timeout_is_15s()]] - degree 5, connects to 1 community