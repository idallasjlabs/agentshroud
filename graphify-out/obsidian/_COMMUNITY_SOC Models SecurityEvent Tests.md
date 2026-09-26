---
type: community
cohesion: 1.00
members: 2
---

# SOC Models SecurityEvent Tests

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_raw_web_fetch_json_overlong_url_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Overly long URLs should be rejected before approval queueing.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SOC_Models_SecurityEvent_Tests
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_raw_web_fetch_json_overlong_url_does_not_queue_approval()]] - degree 4, connects to 3 communities