---
type: community
cohesion: 0.50
members: 4
---

# ContextSegment

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-record_segment()]] - code - gateway/security/context_guard.py
- [[dot-tag_segment()]] - code - gateway/security/context_guard.py
- [[Create a provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Tag a segment and append it to the session's provenance log.]] - rationale - gateway/security/context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContextSegment
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_ContextSegment]]

## Top bridge nodes
- [[dot-record_segment()]] - degree 4, connects to 2 communities
- [[dot-tag_segment()]] - degree 4, connects to 2 communities
