---
source_file: "gateway/security/memory_integrity.py"
type: "code"
community: "Progressive Trust Config"
location: "L62"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Progressive_Trust_Config
---

# MemoryIntegrityMonitor

## Connections
- [[.__init__()_13]] - `calls` [EXTRACTED]
- [[.__init__()_92]] - `method` [EXTRACTED]
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
- [[.setup_method()_9]] - `calls` [EXTRACTED]
- [[.setup_method()_11]] - `calls` [EXTRACTED]
- [[.test_integrity_database_persistence()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MemoryIntegrityConfig]] - `uses` [INFERRED]
- [[MemorySecurityConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[Monitors integrity of critical memory files.]] - `rationale_for` [EXTRACTED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestMemoryIntegrityConfig]] - `uses` [INFERRED]
- [[TestMemoryIntegrityMonitor]] - `uses` [INFERRED]
- [[TestMemoryLifecycleManager]] - `uses` [INFERRED]
- [[TestMemorySecurityIntegration]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[memory_integrity.py]] - `contains` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_memory_lifecycle.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Progressive_Trust_Config