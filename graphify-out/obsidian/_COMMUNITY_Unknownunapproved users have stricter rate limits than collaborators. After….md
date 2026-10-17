---
type: community
members: 27
---

# Unknown/unapproved users have stricter rate limits than collaborators. After…

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
- [[__enter__()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[__exit__()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_send_stranger_rate_limit_notice must include a reset time in HHMM UTC format.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_owner_notice()_19]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_owner_notice()_20]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_pending_notice()_3]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_send()_16]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_60]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[read()]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_FakeRBAC]]
- 8 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]
- 7 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 3 edges to [[_COMMUNITY_Owner approve should fail closed when target has no pending request.]]

## Top bridge nodes
- [[dot-test_stranger_within_limit_triggers_approval_workflow()]] - degree 11, connects to 4 communities
- [[dot-test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - degree 10, connects to 4 communities
- [[dot-test_collaborator_rate_limit_resets_after_window()]] - degree 9, connects to 3 communities
- [[dot-test_owner_unaffected_by_collaborator_rate_limiter()]] - degree 9, connects to 3 communities
- [[dot-test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - degree 9, connects to 3 communities
