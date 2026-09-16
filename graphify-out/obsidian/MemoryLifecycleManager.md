---
source_file: "gateway/security/memory_lifecycle.py"
type: "code"
community: "Memory Integrity & Lifecycle"
location: "L72"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Memory_Integrity__Lifecycle
---

# MemoryLifecycleManager

## Connections
- [[dot-__init__()_12]] - `calls` [EXTRACTED]
- [[dot-__init__()_82]] - `method` [EXTRACTED]
- [[dot-_cleanup_old_actions()]] - `method` [EXTRACTED]
- [[dot-_cleanup_old_threats()]] - `method` [EXTRACTED]
- [[dot-archive_file()]] - `method` [EXTRACTED]
- [[dot-enforce_daily_notes_retention()]] - `method` [EXTRACTED]
- [[dot-enforce_memory_md_size_limit()]] - `method` [EXTRACTED]
- [[dot-get_lifecycle_status()]] - `method` [EXTRACTED]
- [[dot-get_recent_actions()]] - `method` [EXTRACTED]
- [[dot-get_recent_threats()]] - `method` [EXTRACTED]
- [[dot-run_lifecycle_maintenance()]] - `method` [EXTRACTED]
- [[dot-sanitize_content()]] - `method` [EXTRACTED]
- [[dot-scan_content_for_threats()]] - `method` [EXTRACTED]
- [[dot-setup_method()_17]] - `calls` [EXTRACTED]
- [[dot-setup_method()_18]] - `calls` [EXTRACTED]
- [[dot-validate_memory_write()]] - `method` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[ContentThreat]] - `references` [EXTRACTED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[Manages memory file lifecycle and content security.]] - `rationale_for` [EXTRACTED]
- [[MemoryIntegrityMonitor]] - `semantically_similar_to` [INFERRED]
- [[MemoryLifecycleConfig_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[RetentionAction]] - `references` [EXTRACTED]
- [[TestMemoryIntegrityConfig]] - `uses` [INFERRED]
- [[TestMemoryIntegrityMonitor]] - `uses` [INFERRED]
- [[TestMemoryLifecycleManager]] - `uses` [INFERRED]
- [[TestMemorySecurityIntegration]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[memory_lifecycle.py]] - `contains` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_memory_lifecycle.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Memory_Integrity__Lifecycle