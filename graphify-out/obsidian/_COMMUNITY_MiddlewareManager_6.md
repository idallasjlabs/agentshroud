---
type: community
cohesion: 0.10
members: 22
---

# MiddlewareManager

**Cohesion:** 0.10 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-__post_init__()_4]] - code - gateway/security/memory_lifecycle.py
- [[dot-_cleanup_old_actions()]] - code - gateway/security/memory_lifecycle.py
- [[dot-_cleanup_old_threats()]] - code - gateway/security/memory_lifecycle.py
- [[dot-archive_file()]] - code - gateway/security/memory_lifecycle.py
- [[dot-enforce_daily_notes_retention()]] - code - gateway/security/memory_lifecycle.py
- [[dot-enforce_memory_md_size_limit()]] - code - gateway/security/memory_lifecycle.py
- [[dot-get_lifecycle_status()]] - code - gateway/security/memory_lifecycle.py
- [[dot-get_recent_actions()]] - code - gateway/security/memory_lifecycle.py
- [[dot-get_recent_threats()]] - code - gateway/security/memory_lifecycle.py
- [[dot-run_lifecycle_maintenance()]] - code - gateway/security/memory_lifecycle.py
- [[Action taken during retention policy enforcement.]] - rationale - gateway/security/memory_lifecycle.py
- [[Any_49]] - code - gateway/security/memory_lifecycle.py
- [[Archive a file to the archive directory.]] - rationale - gateway/security/memory_lifecycle.py
- [[Clean up old retention action records.]] - rationale - gateway/security/memory_lifecycle.py
- [[Clean up old threat records.]] - rationale - gateway/security/memory_lifecycle.py
- [[Enforce retention policy for daily notes.]] - rationale - gateway/security/memory_lifecycle.py
- [[Enforce size limit for MEMORY.md file.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get current lifecycle management status.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get retention actions taken in the last N hours.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get threats detected in the last N hours.]] - rationale - gateway/security/memory_lifecycle.py
- [[RetentionAction]] - code - gateway/security/memory_lifecycle.py
- [[Run all lifecycle maintenance tasks.]] - rationale - gateway/security/memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_MiddlewareManager_4]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_9]]

## Top bridge nodes
- [[dot-archive_file()]] - degree 6, connects to 2 communities
- [[RetentionAction]] - degree 8, connects to 1 community
- [[dot-run_lifecycle_maintenance()]] - degree 6, connects to 1 community
- [[dot-enforce_memory_md_size_limit()]] - degree 5, connects to 1 community
- [[dot-get_lifecycle_status()]] - degree 5, connects to 1 community
