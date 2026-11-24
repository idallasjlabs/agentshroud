---
type: community
members: 2
---

# .test_long_outbound_message_quarantined

**Members:** 2 nodes

## Members
- [[dot-test_long_outbound_message_quarantined()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Blocked outbound messages should be stored in outbound quarantine.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_long_outbound_message_quarantined
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY__make_sanitizer]]
- 1 edge to [[_COMMUNITY_asyncio_5]]

## Top bridge nodes
- [[dot-test_long_outbound_message_quarantined()]] - degree 4, connects to 3 communities
