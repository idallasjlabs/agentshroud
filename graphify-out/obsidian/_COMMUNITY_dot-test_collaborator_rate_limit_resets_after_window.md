---
type: community
members: 10
---

# .test_collaborator_rate_limit_resets_after_window

**Members:** 10 nodes

## Members
- [[dot-test_collaborator_rate_limit_resets_after_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Messages within the window are blocked; after the window passes they succeed.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Once stranger exhausts rate limit, they get a rate-limit notice; owner is NOT…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Repeated rate-limited messages within the cooldown window send at most one…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_owner_notice()_20]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_rate_limit_resets_after_window
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_FakeRBAC]]
- 3 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]
- 3 edges to [[_COMMUNITY__wrap_response]]
- 3 edges to [[_COMMUNITY_asyncio_7]]
- 1 edge to [[_COMMUNITY_fastapi]]
- 1 edge to [[_COMMUNITY_fake_owner_notice]]

## Top bridge nodes
- [[dot-test_collaborator_rate_limit_resets_after_window()]] - degree 10, connects to 5 communities
- [[dot-test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - degree 10, connects to 5 communities
- [[dot-test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - degree 9, connects to 4 communities
