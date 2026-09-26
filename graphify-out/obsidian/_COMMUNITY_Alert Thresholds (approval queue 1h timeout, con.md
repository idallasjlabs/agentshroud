---
type: community
cohesion: 1.00
members: 2
---

# Alert Thresholds (approval queue 1h timeout, con

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Repeated identical web_fetch leaks should not spam approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Alert_Thresholds_approval_queue_1h_timeout_con
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - degree 4, connects to 3 communities