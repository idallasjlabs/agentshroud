---
type: community
cohesion: 1.00
members: 2
---

# Diagram 18: Runbook

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_raw_web_fetch_json_queues_egress_approval_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw web_fetch JSON should queue interactive egress approval for the destination.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Diagram_18_Runbook
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_raw_web_fetch_json_queues_egress_approval_when_available()]] - degree 4, connects to 3 communities