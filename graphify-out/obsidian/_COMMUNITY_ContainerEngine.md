---
type: community
cohesion: 0.08
members: 36
---

# ContainerEngine

**Cohesion:** 0.08 - loosely connected
**Members:** 36 nodes

## Members
- [[.__init__()_95]] - code - gateway/security/memory_integrity.py
- [[._load_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[._load_write_windows()]] - code - gateway/security/memory_integrity.py
- [[._save_write_windows()]] - code - gateway/security/memory_integrity.py
- [[.from_dict()_8]] - code - gateway/security/memory_integrity.py
- [[.register_expected_write()]] - code - gateway/security/memory_integrity.py
- [[.setup_method()_9]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_expected_write_window()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_file_monitoring_new_file()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_hash_computation()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_integrity_database_persistence()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_tampering_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[Configuration for memory file integrity monitoring.]] - rationale - gateway/security/memory_config.py
- [[Create from dictionary for JSON deserialization.]] - rationale - gateway/security/memory_integrity.py
- [[FileIntegrityRecord]] - code - gateway/security/memory_integrity.py
- [[Load active write windows from disk.]] - rationale - gateway/security/memory_integrity.py
- [[Load integrity database from disk.]] - rationale - gateway/security/memory_integrity.py
- [[MemoryIntegrityConfig_1]] - code - gateway/security/memory_integrity.py
- [[MemoryIntegrityConfig]] - code - gateway/security/memory_config.py
- [[MemoryIntegrityMonitor]] - code - gateway/security/memory_integrity.py
- [[ModificationSource]] - code - gateway/security/memory_integrity.py
- [[Monitors integrity of critical memory files.]] - rationale - gateway/security/memory_integrity.py
- [[Record of a file's integrity state.]] - rationale - gateway/security/memory_integrity.py
- [[Register an expected write to a file to prevent false alerts.]] - rationale - gateway/security/memory_integrity.py
- [[Save active write windows to disk.]] - rationale - gateway/security/memory_integrity.py
- [[Set up test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Source of a file modification.]] - rationale - gateway/security/memory_integrity.py
- [[Test detection of unauthorized modifications.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test file hash computation.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test integrity database saves and loads correctly.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test memory integrity monitoring.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test monitoring a new file.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test write grace window prevents false alerts.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[TestMemoryIntegrityMonitor]] - code - gateway/tests/test_memory_lifecycle.py
- [[memory_config.py]] - code - gateway/security/memory_config.py
- [[memory_integrity.py]] - code - gateway/security/memory_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContainerEngine
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 13 edges to [[_COMMUNITY_TrustManager]]
- 12 edges to [[_COMMUNITY_falco_monitor.py]]
- 5 edges to [[_COMMUNITY_TestTail]]
- 4 edges to [[_COMMUNITY__wrap_response()]]
- 2 edges to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]
- 1 edge to [[_COMMUNITY_run_targeted_tests.sh]]
- 1 edge to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_Hermes Podcast Production Orchestrator README]]

## Top bridge nodes
- [[MemoryIntegrityMonitor]] - degree 41, connects to 5 communities
- [[MemoryIntegrityConfig]] - degree 18, connects to 5 communities
- [[TestMemoryIntegrityMonitor]] - degree 17, connects to 3 communities
- [[ModificationSource]] - degree 13, connects to 3 communities
- [[FileIntegrityRecord]] - degree 7, connects to 2 communities