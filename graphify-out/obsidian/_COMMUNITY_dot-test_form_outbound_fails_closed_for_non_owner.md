---
type: community
members: 3
---

# .test_form_outbound_fails_closed_for_non_owner

**Members:** 3 nodes

## Members
- [[dot-test_form_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[If the pipeline crashes on a form payload, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[process_outbound()_19]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_form_outbound_fails_closed_for_non_owner
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY__make_sanitizer]]
- 1 edge to [[_COMMUNITY_asyncio_5]]

## Top bridge nodes
- [[dot-test_form_outbound_fails_closed_for_non_owner()]] - degree 5, connects to 3 communities
