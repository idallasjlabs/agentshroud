---
type: community
members: 2
---

# TelegramAPIProxy (16)

**Members:** 2 nodes

## Members
- [[dot-test_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TelegramAPIProxy_16
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY__req]]
- 1 edge to [[_COMMUNITY_CronStateMonitor]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2)]]

## Top bridge nodes
- [[dot-test_outbound_fails_closed_for_non_owner()]] - degree 4, connects to 3 communities
