---
type: community
members: 2
---

# .test_outbound_owner_exempt_from_fail_closed

**Members:** 2 nodes

## Members
- [[dot-test_outbound_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, owner messages should still go through.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_outbound_owner_exempt_from_fail_closed
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY__make_sanitizer()]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2)]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]

## Top bridge nodes
- [[dot-test_outbound_owner_exempt_from_fail_closed()]] - degree 4, connects to 3 communities
