---
type: community
members: 11
---

# FileIntegrityRecord

**Members:** 11 nodes

## Members
- [[dot-from_dict()_2]] - code - gateway/security/memory_integrity.py
- [[dot-get_integrity_status()]] - code - gateway/security/memory_integrity.py
- [[dot-get_recent_alerts()]] - code - gateway/security/memory_integrity.py
- [[dot-to_dict()_1]] - code - gateway/security/memory_integrity.py
- [[Any_14]] - code
- [[Convert to dictionary for JSON serialization.]] - rationale - gateway/security/memory_integrity.py
- [[Create from dictionary for JSON deserialization.]] - rationale - gateway/security/memory_integrity.py
- [[FileIntegrityRecord]] - code - gateway/security/memory_integrity.py
- [[Get alerts from the last N hours.]] - rationale - gateway/security/memory_integrity.py
- [[Get current integrity monitoring status.]] - rationale - gateway/security/memory_integrity.py
- [[Record of a file's integrity state.]] - rationale - gateway/security/memory_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FileIntegrityRecord
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 2 edges to [[_COMMUNITY_test_memory_lifecycle.py]]

## Top bridge nodes
- [[FileIntegrityRecord]] - degree 5, connects to 2 communities
- [[dot-from_dict()_2]] - degree 5, connects to 2 communities
- [[dot-get_integrity_status()]] - degree 4, connects to 1 community
- [[dot-get_recent_alerts()]] - degree 4, connects to 1 community
