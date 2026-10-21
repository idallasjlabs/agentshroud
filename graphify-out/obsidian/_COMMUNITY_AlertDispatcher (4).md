---
type: community
members: 7
---

# AlertDispatcher (4)

**Members:** 7 nodes

## Members
- [[dot-export_leakage_report()]] - code - gateway/security/env_guard.py
- [[dot-get_leakage_summary()]] - code - gateway/security/env_guard.py
- [[dot-monitor_environment_access()]] - code - gateway/security/env_guard.py
- [[Any_8]] - code - gateway/security/env_guard.py
- [[Export leakage findings to a report file.]] - rationale - gateway/security/env_guard.py
- [[Get summary of all detected leakages.]] - rationale - gateway/security/env_guard.py
- [[Monitor an agent's environment access attempts.          Args             agent]] - rationale - gateway/security/env_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AlertDispatcher_4
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[dot-get_leakage_summary()]] - degree 4, connects to 1 community
- [[dot-export_leakage_report()]] - degree 3, connects to 1 community
- [[dot-monitor_environment_access()]] - degree 3, connects to 1 community
