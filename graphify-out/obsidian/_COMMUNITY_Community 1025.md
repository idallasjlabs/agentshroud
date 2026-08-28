---
type: community
cohesion: 0.29
members: 7
---

# Community 1025

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.export_attack_report()]] - code - gateway/security/context_guard.py
- [[.get_attack_summary()]] - code - gateway/security/context_guard.py
- [[.get_session_risk_level()]] - code - gateway/security/context_guard.py
- [[Any_35]] - code - gateway/security/context_guard.py
- [[Export attack detection report.]] - rationale - gateway/security/context_guard.py
- [[Get risk level for a session based on detected attacks.]] - rationale - gateway/security/context_guard.py
- [[Get summary of detected attacks.]] - rationale - gateway/security/context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1025
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Security Audit & Drift Detection]]

## Top bridge nodes
- [[.get_attack_summary()]] - degree 5, connects to 1 community
- [[.export_attack_report()]] - degree 3, connects to 1 community
- [[.get_session_risk_level()]] - degree 3, connects to 1 community