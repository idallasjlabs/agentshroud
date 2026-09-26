---
type: community
cohesion: 1.00
members: 2
---

# curriculum.md (input requirement)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_proxy_request_allows_distinct_system_notices()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Different system notices should both be forwarded.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/curriculummd_input_requirement
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_proxy_request_allows_distinct_system_notices()]] - degree 4, connects to 3 communities