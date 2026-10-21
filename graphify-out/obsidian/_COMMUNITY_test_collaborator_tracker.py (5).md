---
type: community
members: 5
---

# test_collaborator_tracker.py (5)

**Members:** 5 nodes

## Members
- [[dot-_make_proxy()_4]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_400_retry_no_loop()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_400_retry_succeeds_when_text_strippable()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[First sendMessage returns 400 'can't parse entities'; retry with plain text succ]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Persistent 400 returns the error after exactly one retry (no infinite loop).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_trackerpy_5
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY__make_sanitizer()]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2)]]

## Top bridge nodes
- [[dot-_make_proxy()_4]] - degree 5, connects to 3 communities
- [[dot-test_400_retry_no_loop()]] - degree 3, connects to 1 community
- [[dot-test_400_retry_succeeds_when_text_strippable()]] - degree 3, connects to 1 community
