---
type: community
cohesion: 1.00
members: 2
---

# TelegramAPIProxy

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[dot-test_ssn_redacted_on_outbound()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[SSN in outbound messages must be redacted.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TelegramAPIProxy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_7]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_5]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[dot-test_ssn_redacted_on_outbound()]] - degree 4, connects to 3 communities
