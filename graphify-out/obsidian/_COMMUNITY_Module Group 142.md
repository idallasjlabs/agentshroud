---
type: community
cohesion: 0.09
members: 34
---

# Module Group 142

**Cohesion:** 0.09 - loosely connected
**Members:** 34 nodes

## Members
- [[.__init__()_76]] - code - gateway/security/memory_lifecycle.py
- [[.__post_init__()_3]] - code - gateway/security/memory_lifecycle.py
- [[._cleanup_old_actions()]] - code - gateway/security/memory_lifecycle.py
- [[._cleanup_old_threats()]] - code - gateway/security/memory_lifecycle.py
- [[.archive_file()]] - code - gateway/security/memory_lifecycle.py
- [[.enforce_daily_notes_retention()]] - code - gateway/security/memory_lifecycle.py
- [[.enforce_memory_md_size_limit()]] - code - gateway/security/memory_lifecycle.py
- [[.get_lifecycle_status()]] - code - gateway/security/memory_lifecycle.py
- [[.get_recent_actions()]] - code - gateway/security/memory_lifecycle.py
- [[.get_recent_threats()]] - code - gateway/security/memory_lifecycle.py
- [[.run_lifecycle_maintenance()]] - code - gateway/security/memory_lifecycle.py
- [[.setup_method()_9]] - code - gateway/tests/test_memory_lifecycle.py
- [[Action taken during retention policy enforcement.]] - rationale - gateway/security/memory_lifecycle.py
- [[Any_43]] - code - gateway/security/memory_lifecycle.py
- [[Archive a file to the archive directory.]] - rationale - gateway/security/memory_lifecycle.py
- [[Clean up old retention action records.]] - rationale - gateway/security/memory_lifecycle.py
- [[Clean up old threat records.]] - rationale - gateway/security/memory_lifecycle.py
- [[Configuration for memory lifecycle management.]] - rationale - gateway/security/memory_config.py
- [[ContentThreatType]] - code - gateway/security/memory_lifecycle.py
- [[Enforce retention policy for daily notes.]] - rationale - gateway/security/memory_lifecycle.py
- [[Enforce size limit for MEMORY.md file.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get current lifecycle management status.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get retention actions taken in the last N hours.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get threats detected in the last N hours.]] - rationale - gateway/security/memory_lifecycle.py
- [[Manages memory file lifecycle and content security.]] - rationale - gateway/security/memory_lifecycle.py
- [[MemoryLifecycleConfig_1]] - code - gateway/security/memory_lifecycle.py
- [[MemoryLifecycleConfig]] - code - gateway/security/memory_config.py
- [[MemoryLifecycleManager]] - code - gateway/security/memory_lifecycle.py
- [[Path_14]] - code - gateway/security/memory_lifecycle.py
- [[RetentionAction]] - code - gateway/security/memory_lifecycle.py
- [[Run all lifecycle maintenance tasks.]] - rationale - gateway/security/memory_lifecycle.py
- [[Set up test environment._1]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Types of content threats detected in memory files.]] - rationale - gateway/security/memory_lifecycle.py
- [[memory_lifecycle.py]] - code - gateway/security/memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_142
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_Module Group 143]]
- 12 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 7 edges to [[_COMMUNITY_Module Group 355]]
- 4 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 4 edges to [[_COMMUNITY_Module Group 256]]
- 4 edges to [[_COMMUNITY_Module Group 388]]
- 2 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]

## Top bridge nodes
- [[MemoryLifecycleManager]] - degree 36, connects to 6 communities
- [[MemoryLifecycleConfig]] - degree 18, connects to 5 communities
- [[ContentThreatType]] - degree 10, connects to 4 communities
- [[memory_lifecycle.py]] - degree 8, connects to 4 communities
- [[Path_14]] - degree 6, connects to 3 communities
