---
type: community
members: 8
---

# TestForwardToTelegramTimeouts

**Members:** 8 nodes

## Members
- [[dot-_fake_urlopen_factory()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_long_poll_timeout_remains_60s()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_non_long_poll_timeout_is_15s()]] - code - gateway/tests/test_telegram_proxy_outbound.py
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
- 4 edges to [[_COMMUNITY_TelegramAPIProxy (2)]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py (2)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py (3)]]

## Top bridge nodes
- [[TestForwardToTelegramTimeouts]] - degree 9, connects to 4 communities
- [[dot-test_long_poll_timeout_remains_60s()]] - degree 5, connects to 1 community
- [[dot-test_non_long_poll_timeout_is_15s()]] - degree 5, connects to 1 community
