---
type: community
cohesion: 0.50
members: 4
---

# Approval Hardening (security)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[._format_parameters_with_highlighting()]] - code - gateway/security/approval_hardening.py
- [[.format_hardened_message()]] - code - gateway/security/approval_hardening.py
- [[Format an approval message with hardening measures applied.]] - rationale - gateway/security/approval_hardening.py
- [[Format parameters with risk highlighting.]] - rationale - gateway/security/approval_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Approval_Hardening_security
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 2 edges to [[_COMMUNITY_Approval Hardening (security)]]
- 1 edge to [[_COMMUNITY_Approval Hardening]]

## Top bridge nodes
- [[.format_hardened_message()]] - degree 5, connects to 3 communities
- [[._format_parameters_with_highlighting()]] - degree 4, connects to 2 communities