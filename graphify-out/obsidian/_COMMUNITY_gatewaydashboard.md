---
type: community
members: 2
---

# gateway/dashboard

**Members:** 2 nodes

## Members
- [[.test_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gateway/dashboard
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ESP32 Firmware]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_docsvault]]

## Top bridge nodes
- [[.test_outbound_fails_closed_for_non_owner()]] - degree 4, connects to 3 communities