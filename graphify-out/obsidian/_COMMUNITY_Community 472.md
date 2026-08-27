---
type: community
members: 18
---

# Community 472

**Members:** 18 nodes

## Members
- [[._send_collaborator_pending_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_help_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_model_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_notice_with_fallback()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_start_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_whoami_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_owner_activity_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_owner_collabs_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_owner_pending_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[Send deterministic help command list without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic start notice without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic identityrole notice to simplify approval workflows.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic model status without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic owner pending-approval snapshot.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic pending-approval notice to unknownrevoked users.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send local command response with deterministic fallback text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send owner a summary of recent collaborator activity (last hour).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send owner-friendly collaborator roster with known labels.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_472
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_Community 4]]
- 2 edges to [[_COMMUNITY_Community 260]]

## Top bridge nodes
- [[._send_local_notice_with_fallback()]] - degree 13, connects to 2 communities
- [[._send_local_model_notice()]] - degree 4, connects to 1 community
- [[._send_owner_pending_notice()]] - degree 4, connects to 1 community
- [[._send_owner_collabs_notice()]] - degree 4, connects to 1 community
- [[._send_collaborator_pending_notice()]] - degree 4, connects to 1 community