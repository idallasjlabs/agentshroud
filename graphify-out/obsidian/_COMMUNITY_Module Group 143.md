---
type: community
cohesion: 0.09
members: 34
---

# Module Group 143

**Cohesion:** 0.09 - loosely connected
**Members:** 34 nodes

## Members
- [[.from_env()_2]] - code - gateway/security/memory_config.py
- [[.setup_method()_8]] - code - gateway/tests/test_memory_lifecycle.py
- [[.teardown_method()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_config_from_env()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_default_config()_4]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_expected_write_window()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_file_monitoring_new_file()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_hash_computation()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_tampering_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[Clean up test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Combined memory security configuration.]] - rationale - gateway/security/memory_config.py
- [[Configuration for memory file integrity monitoring.]] - rationale - gateway/security/memory_config.py
- [[Create configuration from environment variables.]] - rationale - gateway/security/memory_config.py
- [[FileIntegrityRecord]] - code - gateway/security/memory_integrity.py
- [[MemoryIntegrityConfig_1]] - code - gateway/security/memory_integrity.py
- [[MemoryIntegrityConfig]] - code - gateway/security/memory_config.py
- [[MemorySecurityConfig]] - code - gateway/security/memory_config.py
- [[ModificationSource]] - code - gateway/security/memory_integrity.py
- [[Record of a file's integrity state.]] - rationale - gateway/security/memory_integrity.py
- [[Set up test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Source of a file modification.]] - rationale - gateway/security/memory_integrity.py
- [[Test configuration from environment variables.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test default configuration values._3]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test detection of unauthorized modifications.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test file hash computation.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test memory integrity configuration.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test memory integrity monitoring.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test monitoring a new file.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test write grace window prevents false alerts.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[TestMemoryIntegrityConfig]] - code - gateway/tests/test_memory_lifecycle.py
- [[TestMemoryIntegrityMonitor]] - code - gateway/tests/test_memory_lifecycle.py
- [[memory_config.py]] - code - gateway/security/memory_config.py
- [[memory_integrity.py]] - code - gateway/security/memory_integrity.py
- [[test_memory_lifecycle.py]] - code - gateway/tests/test_memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_143
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_Module Group 142]]
- 14 edges to [[_COMMUNITY_Module Group 168]]
- 9 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 6 edges to [[_COMMUNITY_Module Group 388]]
- 5 edges to [[_COMMUNITY_Module Group 395]]
- 5 edges to [[_COMMUNITY_Module Group 256]]
- 4 edges to [[_COMMUNITY_Module Group 355]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]

## Top bridge nodes
- [[MemorySecurityConfig]] - degree 33, connects to 7 communities
- [[MemoryIntegrityConfig]] - degree 18, connects to 5 communities
- [[ModificationSource]] - degree 13, connects to 5 communities
- [[test_memory_lifecycle.py]] - degree 13, connects to 5 communities
- [[FileIntegrityRecord]] - degree 12, connects to 4 communities
