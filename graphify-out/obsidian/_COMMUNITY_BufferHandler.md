---
type: community
members: 4
---

# BufferHandler

**Members:** 4 nodes

## Members
- [[dot-emit()]] - code - gateway/web/dashboard_endpoints.py
- [[BufferHandler]] - code - gateway/web/dashboard_endpoints.py
- [[LogRecord_2]] - code
- [[Logging handler that pushes records into the LogBuffer.]] - rationale - gateway/web/dashboard_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/BufferHandler
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_dashboard_endpoints.py]]

## Top bridge nodes
- [[BufferHandler]] - degree 4, connects to 2 communities
