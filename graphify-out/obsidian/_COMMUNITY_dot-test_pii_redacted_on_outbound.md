---
type: community
members: 2
---

# .test_pii_redacted_on_outbound

**Members:** 2 nodes

## Members
- [[dot-test_pii_redacted_on_outbound()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Phone numbers in outbound messages must be redacted by PII sanitizer.…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_pii_redacted_on_outbound
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY__make_sanitizer]]
- 1 edge to [[_COMMUNITY_asyncio_5]]

## Top bridge nodes
- [[dot-test_pii_redacted_on_outbound()]] - degree 4, connects to 3 communities
