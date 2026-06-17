---
type: community
cohesion: 0.25
members: 8
---

# Module Group 419

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[.__init__()_74]] - code - gateway/security/log_sanitizer.py
- [[._compile_patterns()]] - code - gateway/security/log_sanitizer.py
- [[Any_41]] - code - gateway/security/log_sanitizer.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Pattern_1]] - code - gateway/security/log_sanitizer.py
- [[get_sanitizer_stats()]] - code - gateway/security/log_sanitizer.py
- [[log_sanitizer.py]] - code - gateway/security/log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_419
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 1 edge to [[_COMMUNITY_Module Group 244]]

## Top bridge nodes
- [[log_sanitizer.py]] - degree 3, connects to 2 communities
- [[get_sanitizer_stats()]] - degree 5, connects to 1 community
- [[._compile_patterns()]] - degree 5, connects to 1 community
- [[.__init__()_74]] - degree 2, connects to 1 community