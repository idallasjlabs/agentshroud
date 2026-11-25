---
type: community
members: 29
---

# RateLimiter

**Members:** 29 nodes

## Members
- [[dot-__init__()_58]] - code - gateway/ingest_api/auth.py
- [[dot-check()_2]] - code - gateway/ingest_api/auth.py
- [[dot-test_collaborator_rate_limit_notice_falls_back_without_markdown()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_rate_limit_notice_includes_retry_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_rate_limit_resets_after_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_owner_unaffected_by_collaborator_rate_limiter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[After the rate-limit window expires, collaborator messages go through normally.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Args max_requests Maximum requests allowed in the time window window_seconds…]] - rationale - gateway/ingest_api/auth.py
- [[Check if client is within rate limit Args client_id Usually client IP address…]] - rationale - gateway/ingest_api/auth.py
- [[If notice send fails, cooldown should not suppress the next retry attempt.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Messages within the window are blocked; after the window passes they succeed.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner messages are never rate-limited by the collaborator limiter.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limit notice path should key retry window by user_id, not chat_id.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limit notice should retry without Markdown when parse-mode send fails.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limited collaborators should receive a deterministic retry-window notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[RateLimiter]] - code - gateway/ingest_api/auth.py
- [[Repeated rate-limited messages should each receive a deterministic notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Simple token-bucket rate limiter Limits requests per client IP to prevent…]] - rationale - gateway/ingest_api/auth.py
- [[TestCollaboratorRateLimitRecovery]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rate_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rate_notice()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rate_notice()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rl_notice()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_send()_24]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_20]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_21]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RateLimiter
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY__wrap_response]]
- 9 edges to [[_COMMUNITY_PassthroughPipeline]]
- 7 edges to [[_COMMUNITY_asyncio]]
- 6 edges to [[_COMMUNITY_fastapi]]
- 4 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY_dot-_make_proxy]]
- 2 edges to [[_COMMUNITY_test_security.py]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_dot-test_stranger_within_limit_triggers_approval_workflow]]

## Top bridge nodes
- [[RateLimiter]] - degree 25, connects to 7 communities
- [[dot-test_collaborator_rate_limit_resets_after_window()]] - degree 10, connects to 4 communities
- [[dot-test_owner_unaffected_by_collaborator_rate_limiter()]] - degree 9, connects to 4 communities
- [[dot-test_collaborator_rate_limit_notice_includes_retry_window()]] - degree 10, connects to 3 communities
- [[dot-test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - degree 10, connects to 3 communities
