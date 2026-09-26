---
type: community
cohesion: 0.17
members: 15
---

# falco_monitor.py

**Cohesion:** 0.17 - loosely connected
**Members:** 15 nodes

## Members
- [[._compute_file_hash()]] - code - gateway/security/memory_integrity.py
- [[._detect_modification_source()]] - code - gateway/security/memory_integrity.py
- [[._is_in_write_window()]] - code - gateway/security/memory_integrity.py
- [[._save_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[.clear_old_alerts()]] - code - gateway/security/memory_integrity.py
- [[.scan_all_monitored_files()]] - code - gateway/security/memory_integrity.py
- [[.scan_file()]] - code - gateway/security/memory_integrity.py
- [[Attempt to detect the source of a file modification.          Detection strategy]] - rationale - gateway/security/memory_integrity.py
- [[Check if a file is currently in a write grace window.]] - rationale - gateway/security/memory_integrity.py
- [[Clear alerts older than N days.]] - rationale - gateway/security/memory_integrity.py
- [[Compute SHA-256 hash of a file.]] - rationale - gateway/security/memory_integrity.py
- [[Path_15]] - code - gateway/security/memory_integrity.py
- [[Save integrity database to disk.]] - rationale - gateway/security/memory_integrity.py
- [[Scan a single file for integrity changes.]] - rationale - gateway/security/memory_integrity.py
- [[Scan all configured monitored files and directories.]] - rationale - gateway/security/memory_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/falco_monitorpy
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_ContainerEngine]]
- 1 edge to [[_COMMUNITY_TestTail]]

## Top bridge nodes
- [[._save_integrity_database()]] - degree 6, connects to 2 communities
- [[.scan_file()]] - degree 9, connects to 1 community
- [[._detect_modification_source()]] - degree 6, connects to 1 community
- [[Path_15]] - degree 5, connects to 1 community
- [[._is_in_write_window()]] - degree 5, connects to 1 community