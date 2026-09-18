---
type: community
cohesion: 0.14
members: 14
---

# TestNoResponseGuarantee

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[.test_collaborator_always_gets_response_for_generic_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_blocked_command_always_gets_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_resets_after_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_owner_unaffected_by_collaborator_rate_limiter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unknown_user_always_gets_pending_or_rate_limit_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[A blocked slash command must always produce a protected notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[After the rate-limit window expires, collaborator messages go through normally.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Even a generic message triggers _send_collaborator_safe_info_response (local_inf]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Every collaborator message must produce a response — never a silent drop.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Messages within the window are blocked; after the window passes they succeed.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner messages are never rate-limited by the collaborator limiter.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestCollaboratorRateLimitRecovery]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestNoResponseGuarantee]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknown users must always receive either a pending notice or a rate-limit notice]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestNoResponseGuarantee
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 7 edges to [[_COMMUNITY__wrap_response()]]
- 3 edges to [[_COMMUNITY_RateLimiter]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[TestNoResponseGuarantee]] - degree 9, connects to 4 communities
- [[TestCollaboratorRateLimitRecovery]] - degree 7, connects to 4 communities
- [[.test_collaborator_rate_limit_resets_after_window()]] - degree 8, connects to 3 communities
- [[.test_owner_unaffected_by_collaborator_rate_limiter()]] - degree 7, connects to 2 communities
- [[.test_collaborator_always_gets_response_for_generic_message()]] - degree 7, connects to 2 communities