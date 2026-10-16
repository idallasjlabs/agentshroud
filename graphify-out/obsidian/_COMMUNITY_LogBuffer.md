---
type: community
cohesion: 0.40
members: 5
---

# LogBuffer

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[dot-__init__()_43]] - code - gateway/web/dashboard_endpoints.py
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
- 2 edges to [[_COMMUNITY_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_logs_recent]]

## Top bridge nodes
- [[LogBuffer]] - degree 8, connects to 3 communities
- [[test_log_buffer_ring()]] - degree 2, connects to 1 community
- [[test_log_buffer_tail()]] - degree 2, connects to 1 community
