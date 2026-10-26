---
type: community
members: 8
---

# Community 2006

**Members:** 8 nodes

## Members
- [[.test_collaborator_always_gets_response_for_generic_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_blocked_command_always_gets_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unknown_user_always_gets_pending_or_rate_limit_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[A blocked slash command must always produce a protected notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Even a generic message triggers _send_collaborator_safe_info_response (local_inf]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Every collaborator message must produce a response — never a silent drop.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestNoResponseGuarantee]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknown users must always receive either a pending notice or a rate-limit notice]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2006
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Community 4]]
- 4 edges to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 138]]
- 1 edge to [[_COMMUNITY_Community 72]]
- 1 edge to [[_COMMUNITY_Community 14]]

## Top bridge nodes
- [[TestNoResponseGuarantee]] - degree 8, connects to 4 communities
- [[.test_collaborator_always_gets_response_for_generic_message()]] - degree 7, connects to 2 communities
- [[.test_collaborator_blocked_command_always_gets_notice()]] - degree 7, connects to 2 communities
- [[.test_unknown_user_always_gets_pending_or_rate_limit_notice()]] - degree 7, connects to 2 communities