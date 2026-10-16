---
type: community
cohesion: 0.22
members: 9
---

# MiddlewareManager

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-__init__()_205]] - code - gateway/security/memory_lifecycle.py
- [[dot-sanitize_content()]] - code - gateway/security/memory_lifecycle.py
- [[dot-scan_content_for_threats()]] - code - gateway/security/memory_lifecycle.py
- [[dot-validate_memory_write()]] - code - gateway/security/memory_lifecycle.py
- [[MemoryLifecycleConfig_1]] - code - gateway/security/memory_lifecycle.py
- [[Path_63]] - code - gateway/security/memory_lifecycle.py
- [[Sanitize content by removingredacting threats.]] - rationale - gateway/security/memory_lifecycle.py
- [[Scan memory file content for security threats.]] - rationale - gateway/security/memory_lifecycle.py
- [[Validate content before writing to memory file.]] - rationale - gateway/security/memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_MiddlewareManager_4]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_6]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_8]]

## Top bridge nodes
- [[Path_63]] - degree 5, connects to 3 communities
- [[dot-scan_content_for_threats()]] - degree 5, connects to 1 community
- [[dot-validate_memory_write()]] - degree 5, connects to 1 community
- [[dot-sanitize_content()]] - degree 4, connects to 1 community
- [[dot-__init__()_205]] - degree 3, connects to 1 community
