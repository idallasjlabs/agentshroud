---
type: community
members: 12
---

# test_telegram_proxy_inbound.py (2)

**Members:** 12 nodes

## Members
- [[dot-test_collaborator_always_gets_response_for_generic_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_blocked_command_always_gets_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_unknown_user_always_gets_pending_or_rate_limit_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[A blocked slash command must always produce a protected notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Even a generic message triggers _send_collaborator_safe_info_response…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Every collaborator message must produce a response — never a silent drop.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestNoResponseGuarantee]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknown users must always receive either a pending notice or a rate-limit…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_owner_notice()_21]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_send()_22]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_send()_23]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_send()_24]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_telegram_proxy_inboundpy_2
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 4 edges to [[_COMMUNITY_SecurityPipeline]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig (2) (2)]]
- 1 edge to [[_COMMUNITY_fake_owner_notice()]]

## Top bridge nodes
- [[dot-test_unknown_user_always_gets_pending_or_rate_limit_notice()]] - degree 11, connects to 4 communities
- [[dot-test_collaborator_always_gets_response_for_generic_message()]] - degree 9, connects to 3 communities
- [[dot-test_collaborator_blocked_command_always_gets_notice()]] - degree 9, connects to 3 communities
- [[TestNoResponseGuarantee]] - degree 5, connects to 1 community
