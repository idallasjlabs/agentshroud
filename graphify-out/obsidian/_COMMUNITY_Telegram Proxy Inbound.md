---
type: community
cohesion: 0.50
members: 4
---

# Telegram Proxy Inbound

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_collaborator_approval_action_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_system_prompt_probe_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator attempts to approvedeny requests should be blocked.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[System promptinstruction leakage probes should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Telegram_Proxy_Inbound
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Telegram Inbound Proxy Tests]]
- 2 edges to [[_COMMUNITY_Telegram Proxy Inbound]]

## Top bridge nodes
- [[.test_collaborator_approval_action_request_is_blocked_and_quarantined()]] - degree 9, connects to 2 communities
- [[.test_collaborator_system_prompt_probe_is_blocked_and_quarantined()]] - degree 8, connects to 2 communities