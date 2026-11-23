---
type: community
members: 16
---

# TestMemoryIntegrityMonitor

**Members:** 16 nodes

## Members
- [[dot-setup_method()_2]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-teardown_method()_1]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_expected_write_window()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_file_monitoring_new_file()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_hash_computation()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_integrity_database_persistence()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_tampering_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[Clean up test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Set up test environment._2]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test detection of unauthorized modifications.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test file hash computation.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test integrity database saves and loads correctly.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test memory integrity monitoring.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test monitoring a new file.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test write grace window prevents false alerts.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[TestMemoryIntegrityMonitor]] - code - gateway/tests/test_memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMemoryIntegrityMonitor
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_memory_lifecycle.py]]
- 3 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]

## Top bridge nodes
- [[TestMemoryIntegrityMonitor]] - degree 12, connects to 2 communities
- [[dot-setup_method()_2]] - degree 4, connects to 2 communities
- [[dot-test_integrity_database_persistence()]] - degree 3, connects to 1 community
