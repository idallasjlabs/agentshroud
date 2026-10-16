---
type: community
cohesion: 0.50
members: 4
---

# ApprovalHardening

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-_cleanup_old_denied_requests()]] - code - gateway/security/approval_hardening.py
- [[dot-record_denied_request()]] - code - gateway/security/approval_hardening.py
- [[Clean up old denied requests beyond cooldown period.]] - rationale - gateway/security/approval_hardening.py
- [[Record a denied request for cooldown tracking.]] - rationale - gateway/security/approval_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalHardening
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_ApprovalHardening_1]]
- 1 edge to [[_COMMUNITY_ApprovalHardening_3]]

## Top bridge nodes
- [[dot-record_denied_request()]] - degree 5, connects to 2 communities
- [[dot-_cleanup_old_denied_requests()]] - degree 3, connects to 1 community
