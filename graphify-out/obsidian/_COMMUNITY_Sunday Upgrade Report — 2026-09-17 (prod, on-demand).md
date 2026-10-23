---
type: community
cohesion: 0.08
members: 27
---

# Sunday Upgrade Report — 2026-09-17 (prod, on-demand)

**Cohesion:** 0.08 - loosely connected
**Members:** 27 nodes

## Members
- [[dot-test_collaborator_rate_limit_resets_after_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_owner_unaffected_by_collaborator_rate_limiter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_stranger_rate_limit_notice_includes_reset_time()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_stranger_within_limit_triggers_approval_workflow()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[After the rate-limit window expires, collaborator messages go through normally.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[First message from unknown user (within limit) queues approval flow.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Messages within the window are blocked; after the window passes they succeed.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Once stranger exhausts rate limit, they get a rate-limit notice; owner is NOT…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner messages are never rate-limited by the collaborator limiter.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Repeated rate-limited messages within the cooldown window send at most one…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestCollaboratorRateLimitRecovery]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestStrangerRateLimit]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknownunapproved users have stricter rate limits than collaborators. After…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[__enter__()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[__exit__()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_send_stranger_rate_limit_notice must include a reset time in HHMM UTC format.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_owner_notice()_19]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_owner_notice()_20]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_pending_notice()_3]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_send()_21]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_64]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[read()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Sunday_Upgrade_Report__2026-09-17_prod_on-demand
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 6 edges to [[_COMMUNITY_asyncio]]
- 3 edges to [[_COMMUNITY_SecurityPipeline]]
- 3 edges to [[_COMMUNITY_fake_owner_notice()]]
- 1 edge to [[_COMMUNITY_TestInboundPipelineOnGetUpdates]]

## Top bridge nodes
- [[dot-test_stranger_within_limit_triggers_approval_workflow()]] - degree 11, connects to 3 communities
- [[dot-test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - degree 10, connects to 3 communities
- [[dot-test_owner_unaffected_by_collaborator_rate_limiter()]] - degree 9, connects to 3 communities
- [[dot-test_stranger_rate_limit_notice_includes_reset_time()]] - degree 7, connects to 3 communities
- [[dot-test_collaborator_rate_limit_resets_after_window()]] - degree 9, connects to 2 communities
