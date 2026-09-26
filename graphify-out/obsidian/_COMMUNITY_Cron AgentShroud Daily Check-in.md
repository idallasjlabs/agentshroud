---
type: community
cohesion: 1.00
members: 2
---

# Cron: AgentShroud Daily Check-in

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_collaborator_access_not_configured_user_id_leakage_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should not receive telegram user-id enrollment leakage text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Cron_AgentShroud_Daily_Check-in
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_collaborator_access_not_configured_user_id_leakage_is_redacted_json()]] - degree 4, connects to 3 communities