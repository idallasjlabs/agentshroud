---
type: community
cohesion: 0.11
members: 28
---

# Module Group 168

**Cohesion:** 0.11 - loosely connected
**Members:** 28 nodes

## Members
- [[.__init__()_75]] - code - gateway/security/memory_integrity.py
- [[._compute_file_hash()]] - code - gateway/security/memory_integrity.py
- [[._detect_modification_source()]] - code - gateway/security/memory_integrity.py
- [[._is_in_write_window()]] - code - gateway/security/memory_integrity.py
- [[._load_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[._load_write_windows()]] - code - gateway/security/memory_integrity.py
- [[._save_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[._save_write_windows()]] - code - gateway/security/memory_integrity.py
- [[.clear_old_alerts()]] - code - gateway/security/memory_integrity.py
- [[.register_expected_write()]] - code - gateway/security/memory_integrity.py
- [[.scan_all_monitored_files()]] - code - gateway/security/memory_integrity.py
- [[.scan_file()]] - code - gateway/security/memory_integrity.py
- [[.test_integrity_database_persistence()]] - code - gateway/tests/test_memory_lifecycle.py
- [[Attempt to detect the source of a file modification.          Detection strategy]] - rationale - gateway/security/memory_integrity.py
- [[Check if a file is currently in a write grace window.]] - rationale - gateway/security/memory_integrity.py
- [[Clear alerts older than N days.]] - rationale - gateway/security/memory_integrity.py
- [[Compute SHA-256 hash of a file.]] - rationale - gateway/security/memory_integrity.py
- [[Load active write windows from disk.]] - rationale - gateway/security/memory_integrity.py
- [[Load integrity database from disk.]] - rationale - gateway/security/memory_integrity.py
- [[MemoryIntegrityMonitor]] - code - gateway/security/memory_integrity.py
- [[Monitors integrity of critical memory files.]] - rationale - gateway/security/memory_integrity.py
- [[Path_13]] - code - gateway/security/memory_integrity.py
- [[Register an expected write to a file to prevent false alerts.]] - rationale - gateway/security/memory_integrity.py
- [[Save active write windows to disk.]] - rationale - gateway/security/memory_integrity.py
- [[Save integrity database to disk.]] - rationale - gateway/security/memory_integrity.py
- [[Scan a single file for integrity changes.]] - rationale - gateway/security/memory_integrity.py
- [[Scan all configured monitored files and directories.]] - rationale - gateway/security/memory_integrity.py
- [[Test integrity database saves and loads correctly.]] - rationale - gateway/tests/test_memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_168
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_Module Group 143]]
- 10 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 4 edges to [[_COMMUNITY_Module Group 395]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 388]]
- 1 edge to [[_COMMUNITY_Module Group 256]]

## Top bridge nodes
- [[MemoryIntegrityMonitor]] - degree 38, connects to 6 communities
- [[.scan_file()]] - degree 9, connects to 1 community
- [[Path_13]] - degree 6, connects to 1 community
- [[._detect_modification_source()]] - degree 6, connects to 1 community
- [[._save_integrity_database()]] - degree 6, connects to 1 community