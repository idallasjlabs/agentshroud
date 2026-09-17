---
source_file: "gateway/security/memory_lifecycle.py"
type: "code"
community: "MemoryIntegrityMonitor"
location: "L72"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/MemoryIntegrityMonitor
---

# MemoryLifecycleManager

## Connections
- [[.__init__()_12]] - `calls` [EXTRACTED]
- [[.__init__()_82]] - `method` [EXTRACTED]
- [[._cleanup_old_actions()]] - `method` [EXTRACTED]
- [[._cleanup_old_threats()]] - `method` [EXTRACTED]
- [[.archive_file()]] - `method` [EXTRACTED]
- [[.enforce_daily_notes_retention()]] - `method` [EXTRACTED]
- [[.enforce_memory_md_size_limit()]] - `method` [EXTRACTED]
- [[.get_lifecycle_status()]] - `method` [EXTRACTED]
- [[.get_recent_actions()]] - `method` [EXTRACTED]
- [[.get_recent_threats()]] - `method` [EXTRACTED]
- [[.run_lifecycle_maintenance()]] - `method` [EXTRACTED]
- [[.sanitize_content()]] - `method` [EXTRACTED]
- [[.scan_content_for_threats()]] - `method` [EXTRACTED]
- [[.setup_method()_17]] - `calls` [EXTRACTED]
- [[.setup_method()_18]] - `calls` [EXTRACTED]
- [[.validate_memory_write()]] - `method` [EXTRACTED]
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

#graphify/code #graphify/EXTRACTED #community/MemoryIntegrityMonitor