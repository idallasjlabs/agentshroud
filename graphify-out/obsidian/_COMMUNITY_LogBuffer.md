---
type: community
members: 9
---

# LogBuffer

**Members:** 9 nodes

## Members
- [[dot-__init__()_174]] - code - gateway/web/dashboard_endpoints.py
- [[dot-append()]] - code - gateway/web/dashboard_endpoints.py
- [[dot-recent()]] - code - gateway/web/dashboard_endpoints.py
- [[dot-tail()]] - code - gateway/web/dashboard_endpoints.py
- [[Any_68]] - code
- [[LogBuffer]] - code - gateway/web/dashboard_endpoints.py
- [[Ring buffer for recent logaudit entries.]] - rationale - gateway/web/dashboard_endpoints.py
- [[test_log_buffer_ring()]] - code - gateway/tests/test_dashboard_endpoints.py
- [[test_log_buffer_tail()]] - code - gateway/tests/test_dashboard_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LogBuffer
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 3 edges to [[_COMMUNITY_dashboard_endpoints.py]]

## Top bridge nodes
- [[LogBuffer]] - degree 8, connects to 2 communities
- [[Any_68]] - degree 3, connects to 1 community
- [[test_log_buffer_ring()]] - degree 2, connects to 1 community
- [[test_log_buffer_tail()]] - degree 2, connects to 1 community
- [[dot-recent()]] - degree 2, connects to 1 community
