---
type: community
cohesion: 1.00
members: 2
---

# _PII_PATTERNS (URL PII regex set)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_raw_web_fetch_json_malformed_hyphen_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Malformed domain labels should be rejected before approval queueing.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_PII_PATTERNS_URL_PII_regex_set
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_raw_web_fetch_json_malformed_hyphen_domain_does_not_queue_approval()]] - degree 4, connects to 3 communities