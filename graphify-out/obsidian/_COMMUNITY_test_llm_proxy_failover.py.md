---
type: community
members: 36
---

# test_llm_proxy_failover.py

**Members:** 36 nodes

## Members
- [[dot-__init__()_89]] - code - gateway/security/memory_integrity.py
- [[dot-_load_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[dot-_load_write_windows()]] - code - gateway/security/memory_integrity.py
- [[dot-_save_write_windows()]] - code - gateway/security/memory_integrity.py
- [[dot-from_dict()_1]] - code - gateway/security/memory_integrity.py
- [[dot-register_expected_write()]] - code - gateway/security/memory_integrity.py
- [[dot-setup_method()_16]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_expected_write_window()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_file_monitoring_new_file()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_hash_computation()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_integrity_database_persistence()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_tampering_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[Configuration for memory file integrity monitoring.]] - rationale - gateway/security/memory_config.py
- [[Create from dictionary for JSON deserialization.]] - rationale - gateway/security/memory_integrity.py
- [[FileIntegrityRecord]] - code - gateway/security/memory_integrity.py
- [[Load active write windows from disk.]] - rationale - gateway/security/memory_integrity.py
- [[Load integrity database from disk.]] - rationale - gateway/security/memory_integrity.py
- [[MemoryIntegrityConfig]] - code - gateway/security/memory_integrity.py
- [[MemoryIntegrityConfig_1]] - code - gateway/security/memory_config.py
- [[MemoryIntegrityMonitor]] - code - gateway/security/memory_integrity.py
- [[ModificationSource]] - code - gateway/security/memory_integrity.py
- [[Monitors integrity of critical memory files.]] - rationale - gateway/security/memory_integrity.py
- [[Record of a file's integrity state.]] - rationale - gateway/security/memory_integrity.py
- [[Register an expected write to a file to prevent false alerts.]] - rationale - gateway/security/memory_integrity.py
- [[Save active write windows to disk.]] - rationale - gateway/security/memory_integrity.py
- [[Set up test environment._1]] - rationale - gateway/tests/test_memory_lifecycle.py
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
TABLE source_file, type FROM #community/test_llm_proxy_failoverpy
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_gatewayteststest_llm_proxy_thinking_suppression.py (8 cases)]]
- 13 edges to [[_COMMUNITY_MiddlewareManager]]
- 12 edges to [[_COMMUNITY_create_auth_dependency (2)_1]]
- 5 edges to [[_COMMUNITY_cmd_start]]
- 2 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_gatewayteststest_llm_proxy_thinking_suppression.py (8 cases) (2)]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_failover.py (2)]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]

## Top bridge nodes
- [[MemoryIntegrityMonitor]] - degree 39, connects to 4 communities
- [[MemoryIntegrityConfig_1]] - degree 16, connects to 4 communities
- [[TestMemoryIntegrityMonitor]] - degree 17, connects to 3 communities
- [[ModificationSource]] - degree 13, connects to 3 communities
- [[FileIntegrityRecord]] - degree 7, connects to 2 communities
