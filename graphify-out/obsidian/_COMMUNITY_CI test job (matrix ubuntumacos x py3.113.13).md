---
type: community
cohesion: 0.40
members: 5
---

# CI test job (matrix ubuntu/macos x py3.11/3.13)

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[._make_proxy()_5]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_400_retry_no_loop()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_400_retry_succeeds_when_text_strippable()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[First sendMessage returns 400 'can't parse entities'; retry with plain text succ]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Persistent 400 returns the error after exactly one retry (no infinite loop).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CI_test_job_matrix_ubuntu/macos_x_py311/313
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[._make_proxy()_5]] - degree 5, connects to 3 communities
- [[.test_400_retry_no_loop()]] - degree 3, connects to 1 community
- [[.test_400_retry_succeeds_when_text_strippable()]] - degree 3, connects to 1 community