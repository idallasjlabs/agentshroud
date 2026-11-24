---
type: community
members: 2
---

# .test_monitor_mode

**Members:** 2 nodes

## Members
- [[dot-test_monitor_mode()]] - code - gateway/tests/test_outbound_filter.py
- [[Test that monitor mode logs but doesn't redact.]] - rationale - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_monitor_mode
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]

## Top bridge nodes
- [[dot-test_monitor_mode()]] - degree 3, connects to 2 communities
