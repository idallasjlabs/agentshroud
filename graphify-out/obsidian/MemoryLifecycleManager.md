---
source_file: "gateway/security/memory_lifecycle.py"
type: "code"
community: "Memory Lifecycle & Integrity"
location: "L72"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Memory_Lifecycle__Integrity
---

# MemoryLifecycleManager

## Connections
- [[.__init__()_14]] - `calls` [EXTRACTED]
- [[.__init__()_96]] - `method` [EXTRACTED]
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
- [[.setup_method()_10]] - `calls` [EXTRACTED]
- [[.setup_method()_11]] - `calls` [EXTRACTED]
- [[.validate_memory_write()]] - `method` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[ContentThreat]] - `references` [EXTRACTED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[Manages memory file lifecycle and content security.]] - `rationale_for` [EXTRACTED]
- [[MemoryIntegrityMonitor]] - `semantically_similar_to` [INFERRED]
- [[MemoryLifecycleConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[RetentionAction]] - `references` [EXTRACTED]
- [[TestMemoryIntegrityConfig]] - `uses` [INFERRED]
- [[TestMemoryIntegrityMonitor]] - `uses` [INFERRED]
- [[TestMemoryLifecycleManager]] - `uses` [INFERRED]
- [[TestMemorySecurityIntegration]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[memory_lifecycle.py]] - `contains` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_memory_lifecycle.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Memory_Lifecycle__Integrity