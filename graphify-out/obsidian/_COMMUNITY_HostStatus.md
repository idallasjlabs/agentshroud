---
type: community
cohesion: 0.29
members: 7
---

# HostStatus

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.export_leakage_report()]] - code - gateway/security/env_guard.py
- [[.get_leakage_summary()]] - code - gateway/security/env_guard.py
- [[.monitor_environment_access()]] - code - gateway/security/env_guard.py
- [[Any_39]] - code - gateway/security/env_guard.py
- [[Export leakage findings to a report file.]] - rationale - gateway/security/env_guard.py
- [[Get summary of all detected leakages.]] - rationale - gateway/security/env_guard.py
- [[Monitor an agent's environment access attempts.          Args             agent]] - rationale - gateway/security/env_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/HostStatus
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[.get_leakage_summary()]] - degree 4, connects to 1 community
- [[.export_leakage_report()]] - degree 3, connects to 1 community
- [[.monitor_environment_access()]] - degree 3, connects to 1 community