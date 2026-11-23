---
type: community
members: 18
---

# TestReplayBufferOffsetParsing

**Members:** 18 nodes

## Members
- [[dot-_fake_get_updates_urlopen()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-_fake_urlopen_factory()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-_make_proxy_with_mock_buffer()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_body_still_calls_mark_delivered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_long_poll_timeout_remains_60s()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_non_long_poll_timeout_is_15s()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_url_encoded_body_calls_mark_delivered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON getUpdates body must still call mark_delivered (existing behaviour…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Return a urlopen mock that records the timeout kwarg and succeeds.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestForwardToTelegramTimeouts]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestReplayBufferOffsetParsing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests that _forward_to_telegram uses correct urlopen timeouts. Regression guard…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[URL-encoded getUpdates body must call mark_delivered with the correct int…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Verify URL-encoded and JSON getUpdates bodies both trigger mark_delivered…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_fake()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_fake()_1]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[getUpdates must use a 60s urlopen timeout so the long-poll is not aborted early.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[sendMessage and similar calls must use a 15s urlopen timeout.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestReplayBufferOffsetParsing
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY__make_sanitizer]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_PIIConfig]]

## Top bridge nodes
- [[TestReplayBufferOffsetParsing]] - degree 7, connects to 2 communities
- [[TestForwardToTelegramTimeouts]] - degree 6, connects to 2 communities
- [[dot-test_long_poll_timeout_remains_60s()]] - degree 5, connects to 1 community
- [[dot-test_non_long_poll_timeout_is_15s()]] - degree 5, connects to 1 community
- [[dot-test_json_body_still_calls_mark_delivered()]] - degree 5, connects to 1 community
