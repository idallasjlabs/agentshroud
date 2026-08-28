---
type: community
cohesion: 0.22
members: 10
---

# Community 871

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_stranger_rate_limit_notice_includes_reset_time()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_stranger_within_limit_triggers_approval_workflow()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[First message from unknown user (within limit) queues approval flow.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Once stranger exhausts rate limit, they get a rate-limit notice; owner is NOT no]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Repeated rate-limited messages within the cooldown window send at most one notic]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestStrangerRateLimit]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknownunapproved users have stricter rate limits than collaborators.      Afte]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_send_stranger_rate_limit_notice must include a reset time in HHMM UTC format.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_871
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Telegram Proxy Inbound]]
- 4 edges to [[_COMMUNITY_Community 31]]
- 1 edge to [[_COMMUNITY_Community 115]]
- 1 edge to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Adversarial Injection Guards]]

## Top bridge nodes
- [[TestStrangerRateLimit]] - degree 9, connects to 4 communities
- [[.test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - degree 7, connects to 2 communities
- [[.test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - degree 7, connects to 2 communities
- [[.test_stranger_within_limit_triggers_approval_workflow()]] - degree 7, connects to 2 communities
- [[.test_stranger_rate_limit_notice_includes_reset_time()]] - degree 6, connects to 1 community