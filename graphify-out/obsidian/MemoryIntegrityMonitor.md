---
source_file: "gateway/security/memory_integrity.py"
type: "code"
community: "MemoryIntegrityMonitor"
location: "L62"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/MemoryIntegrityMonitor
---

# MemoryIntegrityMonitor

## Connections
- [[.__init__()_12]] - `calls` [EXTRACTED]
- [[.__init__()_81]] - `method` [EXTRACTED]
- [[._compute_file_hash()]] - `method` [EXTRACTED]
- [[._detect_modification_source()]] - `method` [EXTRACTED]
- [[._is_in_write_window()]] - `method` [EXTRACTED]
- [[._load_integrity_database()]] - `method` [EXTRACTED]
- [[._load_write_windows()]] - `method` [EXTRACTED]
- [[._save_integrity_database()]] - `method` [EXTRACTED]
- [[._save_write_windows()]] - `method` [EXTRACTED]
- [[.clear_old_alerts()]] - `method` [EXTRACTED]
- [[.get_integrity_status()]] - `method` [EXTRACTED]
- [[.get_recent_alerts()]] - `method` [EXTRACTED]
- [[.register_expected_write()]] - `method` [EXTRACTED]
- [[.scan_all_monitored_files()]] - `method` [EXTRACTED]
- [[.scan_file()]] - `method` [EXTRACTED]
- [[.setup_method()_16]] - `calls` [EXTRACTED]
- [[.setup_method()_18]] - `calls` [EXTRACTED]
- [[.test_integrity_database_persistence()]] - `calls` [EXTRACTED]
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

#graphify/code #graphify/EXTRACTED #community/MemoryIntegrityMonitor