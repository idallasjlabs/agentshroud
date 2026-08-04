---
type: community
cohesion: 0.38
members: 7
---

# Module Group 472

**Cohesion:** 0.38 - loosely connected
**Members:** 7 nodes

## Members
- [[._make_proxy()_3]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_400_retry_no_loop()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_400_retry_succeeds_when_text_strippable()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[B1 one-shot 400-retry for unbalanced HTML parse errors.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[First sendMessage returns 400 'can't parse entities'; retry with plain text succ]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Persistent 400 returns the error after exactly one retry (no infinite loop).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestTelegram400Retry]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_472
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Module Group 140]]
- 1 edge to [[_COMMUNITY_Telegram Outbound Test Coverage]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound Tests]]

## Top bridge nodes
- [[TestTelegram400Retry]] - degree 9, connects to 3 communities
- [[._make_proxy()_3]] - degree 5, connects to 2 communities
