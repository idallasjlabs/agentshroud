---
type: community
members: 27
---

# MemoryLifecycleManager

**Members:** 27 nodes

## Members
- [[dot-__init__()_47]] - code - gateway/security/memory_lifecycle.py
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
- [[Any_17]] - code
- [[Archive a file to the archive directory.]] - rationale - gateway/security/memory_lifecycle.py
- [[Clean up old retention action records.]] - rationale - gateway/security/memory_lifecycle.py
- [[Clean up old threat records.]] - rationale - gateway/security/memory_lifecycle.py
- [[Enforce retention policy for daily notes.]] - rationale - gateway/security/memory_lifecycle.py
- [[Enforce size limit for MEMORY.md file.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get current lifecycle management status.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get retention actions taken in the last N hours.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get threats detected in the last N hours.]] - rationale - gateway/security/memory_lifecycle.py
- [[Manages memory file lifecycle and content security.]] - rationale - gateway/security/memory_lifecycle.py
- [[MemoryLifecycleManager]] - code - gateway/security/memory_lifecycle.py
- [[Path_19]] - code
- [[RetentionAction]] - code - gateway/security/memory_lifecycle.py
- [[Run all lifecycle maintenance tasks.]] - rationale - gateway/security/memory_lifecycle.py
- [[Test Memory Lifecycle and Integrity]] - code - gateway/tests/test_memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MemoryLifecycleManager
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_ContentThreat]]
- 5 edges to [[_COMMUNITY_MemoryLifecycleConfig]]
- 3 edges to [[_COMMUNITY_test_memory_lifecycle.py]]
- 2 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_TestMemoryLifecycleManager]]

## Top bridge nodes
- [[MemoryLifecycleManager]] - degree 28, connects to 9 communities
- [[RetentionAction]] - degree 6, connects to 1 community
- [[dot-get_recent_threats()]] - degree 4, connects to 1 community
- [[dot-__init__()_47]] - degree 3, connects to 1 community
- [[Path_19]] - degree 3, connects to 1 community
