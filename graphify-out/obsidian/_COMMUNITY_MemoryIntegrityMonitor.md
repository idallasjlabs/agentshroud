---
type: community
members: 24
---

# MemoryIntegrityMonitor

**Members:** 24 nodes

## Members
- [[dot-__init__()_154]] - code - gateway/security/memory_integrity.py
- [[dot-_compute_file_hash()]] - code - gateway/security/memory_integrity.py
- [[dot-_detect_modification_source()]] - code - gateway/security/memory_integrity.py
- [[dot-_is_in_write_window()]] - code - gateway/security/memory_integrity.py
- [[dot-_load_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[dot-_load_write_windows()]] - code - gateway/security/memory_integrity.py
- [[dot-_save_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[dot-_save_write_windows()]] - code - gateway/security/memory_integrity.py
- [[dot-register_expected_write()]] - code - gateway/security/memory_integrity.py
- [[dot-scan_all_monitored_files()]] - code - gateway/security/memory_integrity.py
- [[dot-scan_file()_1]] - code - gateway/security/memory_integrity.py
- [[Attempt to detect the source of a file modification. Detection strategy (in…]] - rationale - gateway/security/memory_integrity.py
- [[Check if a file is currently in a write grace window.]] - rationale - gateway/security/memory_integrity.py
- [[Compute SHA-256 hash of a file.]] - rationale - gateway/security/memory_integrity.py
- [[Load active write windows from disk.]] - rationale - gateway/security/memory_integrity.py
- [[Load integrity database from disk.]] - rationale - gateway/security/memory_integrity.py
- [[MemoryIntegrityMonitor]] - code - gateway/security/memory_integrity.py
- [[Monitors integrity of critical memory files.]] - rationale - gateway/security/memory_integrity.py
- [[Path_56]] - code
- [[Register an expected write to a file to prevent false alerts.]] - rationale - gateway/security/memory_integrity.py
- [[Save active write windows to disk.]] - rationale - gateway/security/memory_integrity.py
- [[Save integrity database to disk.]] - rationale - gateway/security/memory_integrity.py
- [[Scan a single file for integrity changes.]] - rationale - gateway/security/memory_integrity.py
- [[Scan all configured monitored files and directories.]] - rationale - gateway/security/memory_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MemoryIntegrityMonitor
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_memory_lifecycle.py]]
- 4 edges to [[_COMMUNITY_FileIntegrityRecord]]
- 3 edges to [[_COMMUNITY_TestMemoryIntegrityMonitor]]
- 2 edges to [[_COMMUNITY_MemoryLifecycleManager]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[MemoryIntegrityMonitor]] - degree 29, connects to 9 communities
- [[dot-scan_file()_1]] - degree 9, connects to 1 community
- [[dot-_detect_modification_source()]] - degree 6, connects to 1 community
- [[dot-__init__()_154]] - degree 5, connects to 1 community
- [[dot-_load_integrity_database()]] - degree 4, connects to 1 community
