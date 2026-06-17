---
type: community
cohesion: 0.39
members: 8
---

# Module Group 446

**Cohesion:** 0.39 - loosely connected
**Members:** 8 nodes

## Members
- [[._fake_get_updates_urlopen()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[._make_proxy_with_mock_buffer()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_body_still_calls_mark_delivered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_url_encoded_body_calls_mark_delivered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON getUpdates body must still call mark_delivered (existing behaviour preserve]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestReplayBufferOffsetParsing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[URL-encoded getUpdates body must call mark_delivered with the correct int offset]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Verify URL-encoded and JSON getUpdates bodies both trigger mark_delivered correc]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_446
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Module Group 140]]
- 1 edge to [[_COMMUNITY_Telegram Outbound Test Coverage]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound Tests]]

## Top bridge nodes
- [[TestReplayBufferOffsetParsing]] - degree 10, connects to 3 communities
- [[._make_proxy_with_mock_buffer()]] - degree 5, connects to 2 communities