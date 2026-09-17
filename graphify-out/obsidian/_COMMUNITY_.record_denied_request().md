---
type: community
cohesion: 0.50
members: 4
---

# .record_denied_request()

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[._cleanup_old_denied_requests()]] - code - gateway/security/approval_hardening.py
- [[.record_denied_request()]] - code - gateway/security/approval_hardening.py
- [[Clean up old denied requests beyond cooldown period.]] - rationale - gateway/security/approval_hardening.py
- [[Record a denied request for cooldown tracking.]] - rationale - gateway/security/approval_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/record_denied_request
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_DeniedRequest]]

## Top bridge nodes
- [[.record_denied_request()]] - degree 5, connects to 3 communities
- [[._cleanup_old_denied_requests()]] - degree 3, connects to 1 community