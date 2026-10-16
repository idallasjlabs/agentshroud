---
type: community
cohesion: 1.00
members: 2
---

# .test_form_outbound_fails_closed_for_non_owner

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[dot-test_form_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[If the pipeline crashes on a form payload, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_form_outbound_fails_closed_for_non_owner
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_7]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_5]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[dot-test_form_outbound_fails_closed_for_non_owner()]] - degree 4, connects to 3 communities
