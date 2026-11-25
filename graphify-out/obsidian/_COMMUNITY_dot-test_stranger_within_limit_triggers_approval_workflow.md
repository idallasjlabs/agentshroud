---
type: community
members: 19
---

# .test_stranger_within_limit_triggers_approval_workflow

**Members:** 19 nodes

## Members
- [[dot-test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_stranger_rate_limit_notice_includes_reset_time()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_stranger_within_limit_triggers_approval_workflow()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[First message from unknown user (within limit) queues approval flow.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Once stranger exhausts rate limit, they get a rate-limit notice; owner is NOT…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Repeated rate-limited messages within the cooldown window send at most one…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestStrangerRateLimit]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknownunapproved users have stricter rate limits than collaborators. After…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[__enter__()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[__exit__()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_send_stranger_rate_limit_notice must include a reset time in HHMM UTC format.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_owner_notice()_19]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_owner_notice()_20]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_pending_notice()_3]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_19]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[read()_3]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_stranger_within_limit_triggers_approval_workflow
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY__wrap_response]]
- 5 edges to [[_COMMUNITY_PassthroughPipeline]]
- 4 edges to [[_COMMUNITY_asyncio]]
- 3 edges to [[_COMMUNITY_fake_owner_notice]]
- 1 edge to [[_COMMUNITY_dot-_make_proxy]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_RateLimiter]]

## Top bridge nodes
- [[dot-test_stranger_within_limit_triggers_approval_workflow()]] - degree 11, connects to 4 communities
- [[dot-test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - degree 10, connects to 4 communities
- [[dot-test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - degree 9, connects to 3 communities
- [[dot-test_stranger_rate_limit_notice_includes_reset_time()]] - degree 7, connects to 3 communities
- [[TestStrangerRateLimit]] - degree 7, connects to 2 communities
