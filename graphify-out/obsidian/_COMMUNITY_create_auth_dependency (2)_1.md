---
type: community
members: 15
---

# create_auth_dependency (2)

**Members:** 15 nodes

## Members
- [[dot-_compute_file_hash()]] - code - gateway/security/memory_integrity.py
- [[dot-_detect_modification_source()]] - code - gateway/security/memory_integrity.py
- [[dot-_is_in_write_window()]] - code - gateway/security/memory_integrity.py
- [[dot-_save_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[dot-clear_old_alerts()]] - code - gateway/security/memory_integrity.py
- [[dot-scan_all_monitored_files()]] - code - gateway/security/memory_integrity.py
- [[dot-scan_file()_1]] - code - gateway/security/memory_integrity.py
- [[Attempt to detect the source of a file modification.          Detection strategy]] - rationale - gateway/security/memory_integrity.py
- [[Check if a file is currently in a write grace window.]] - rationale - gateway/security/memory_integrity.py
- [[Clear alerts older than N days.]] - rationale - gateway/security/memory_integrity.py
- [[Compute SHA-256 hash of a file.]] - rationale - gateway/security/memory_integrity.py
- [[Path_55]] - code - gateway/security/memory_integrity.py
- [[Save integrity database to disk.]] - rationale - gateway/security/memory_integrity.py
- [[Scan a single file for integrity changes.]] - rationale - gateway/security/memory_integrity.py
- [[Scan all configured monitored files and directories.]] - rationale - gateway/security/memory_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/create_auth_dependency_2
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 1 edge to [[_COMMUNITY_cmd_start]]

## Top bridge nodes
- [[dot-_save_integrity_database()]] - degree 6, connects to 2 communities
- [[dot-scan_file()_1]] - degree 9, connects to 1 community
- [[dot-_detect_modification_source()]] - degree 6, connects to 1 community
- [[Path_55]] - degree 5, connects to 1 community
- [[dot-_is_in_write_window()]] - degree 5, connects to 1 community
