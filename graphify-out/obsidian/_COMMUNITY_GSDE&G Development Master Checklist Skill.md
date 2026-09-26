---
type: community
cohesion: 0.10
members: 22
---

# GSDE&G Development Master Checklist Skill

**Cohesion:** 0.10 - loosely connected
**Members:** 22 nodes

## Members
- [[.__post_init__()_7]] - code - gateway/security/memory_lifecycle.py
- [[._cleanup_old_actions()]] - code - gateway/security/memory_lifecycle.py
- [[._cleanup_old_threats()]] - code - gateway/security/memory_lifecycle.py
- [[.archive_file()]] - code - gateway/security/memory_lifecycle.py
- [[.enforce_daily_notes_retention()]] - code - gateway/security/memory_lifecycle.py
- [[.enforce_memory_md_size_limit()]] - code - gateway/security/memory_lifecycle.py
- [[.get_lifecycle_status()]] - code - gateway/security/memory_lifecycle.py
- [[.get_recent_actions()]] - code - gateway/security/memory_lifecycle.py
- [[.get_recent_threats()]] - code - gateway/security/memory_lifecycle.py
- [[.run_lifecycle_maintenance()]] - code - gateway/security/memory_lifecycle.py
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
TABLE source_file, type FROM #community/GSDEG_Development_Master_Checklist_Skill
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 1 edge to [[_COMMUNITY_3. AWS API MCP Authentication Reset]]

## Top bridge nodes
- [[.archive_file()]] - degree 6, connects to 2 communities
- [[RetentionAction]] - degree 8, connects to 1 community
- [[.run_lifecycle_maintenance()]] - degree 6, connects to 1 community
- [[.enforce_memory_md_size_limit()]] - degree 5, connects to 1 community
- [[.get_lifecycle_status()]] - degree 5, connects to 1 community