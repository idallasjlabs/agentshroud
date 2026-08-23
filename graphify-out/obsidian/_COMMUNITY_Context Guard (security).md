---
type: community
cohesion: 0.50
members: 4
---

# Context Guard (security)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.record_segment()]] - code - gateway/security/context_guard.py
- [[.tag_segment()]] - code - gateway/security/context_guard.py
- [[Create a provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Tag a segment and append it to the session's provenance log.]] - rationale - gateway/security/context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Context_Guard_security
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Context Integrity]]
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]

## Top bridge nodes
- [[.record_segment()]] - degree 4, connects to 2 communities
- [[.tag_segment()]] - degree 4, connects to 2 communities