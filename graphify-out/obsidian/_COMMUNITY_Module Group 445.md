---
type: community
cohesion: 0.25
members: 8
---

# Module Group 445

**Cohesion:** 0.25 - loosely connected
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
TABLE source_file, type FROM #community/Module_Group_445
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Telegram Proxy Inbound Tests]]
- 3 edges to [[_COMMUNITY_Module Group 64]]
- 2 edges to [[_COMMUNITY_Authentication & Rate Limiting]]
- 1 edge to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]

## Top bridge nodes
- [[TestNoResponseGuarantee]] - degree 8, connects to 3 communities
- [[.test_collaborator_always_gets_response_for_generic_message()]] - degree 7, connects to 2 communities
- [[.test_collaborator_blocked_command_always_gets_notice()]] - degree 7, connects to 2 communities
- [[.test_unknown_user_always_gets_pending_or_rate_limit_notice()]] - degree 7, connects to 2 communities
