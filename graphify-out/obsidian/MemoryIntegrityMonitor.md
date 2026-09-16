---
source_file: "gateway/security/memory_integrity.py"
type: "code"
community: "Memory Integrity & Lifecycle"
location: "L62"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Memory_Integrity__Lifecycle
---

# MemoryIntegrityMonitor

## Connections
- [[dot-__init__()_12]] - `calls` [EXTRACTED]
- [[dot-__init__()_81]] - `method` [EXTRACTED]
- [[dot-_compute_file_hash()]] - `method` [EXTRACTED]
- [[dot-_detect_modification_source()]] - `method` [EXTRACTED]
- [[dot-_is_in_write_window()]] - `method` [EXTRACTED]
- [[dot-_load_integrity_database()]] - `method` [EXTRACTED]
- [[dot-_load_write_windows()]] - `method` [EXTRACTED]
- [[dot-_save_integrity_database()]] - `method` [EXTRACTED]
- [[dot-_save_write_windows()]] - `method` [EXTRACTED]
- [[dot-clear_old_alerts()]] - `method` [EXTRACTED]
- [[dot-get_integrity_status()]] - `method` [EXTRACTED]
- [[dot-get_recent_alerts()]] - `method` [EXTRACTED]
- [[dot-register_expected_write()]] - `method` [EXTRACTED]
- [[dot-scan_all_monitored_files()]] - `method` [EXTRACTED]
- [[dot-scan_file()]] - `method` [EXTRACTED]
- [[dot-setup_method()_16]] - `calls` [EXTRACTED]
- [[dot-setup_method()_18]] - `calls` [EXTRACTED]
- [[dot-test_integrity_database_persistence()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[FileIntegrityRecord]] - `references` [EXTRACTED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MemoryIntegrityConfig_1]] - `uses` [INFERRED]
- [[MemoryLifecycleManager]] - `semantically_similar_to` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[ModificationSource]] - `references` [EXTRACTED]
- [[Monitors integrity of critical memory files.]] - `rationale_for` [EXTRACTED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestMemoryIntegrityConfig]] - `uses` [INFERRED]
- [[TestMemoryIntegrityMonitor]] - `uses` [INFERRED]
- [[TestMemoryLifecycleManager]] - `uses` [INFERRED]
- [[TestMemorySecurityIntegration]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[memory_integrity.py]] - `contains` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_memory_lifecycle.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Memory_Integrity__Lifecycle