---
type: community
cohesion: 1.00
members: 2
---

# soc/router.py

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[Query GitHub releases API. Returns {tag_name ..., html_url ...} or {error]] - rationale - gateway/soc/router.py
- [[_fetch_latest_release()]] - code - gateway/soc/router.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/soc/routerpy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[_fetch_latest_release()]] - degree 2, connects to 1 community
