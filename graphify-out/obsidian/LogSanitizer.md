---
source_file: "gateway/ingest_api/middleware.py"
type: "code"
community: "Egress & RBAC Security Core"
location: "L1353"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Egress__RBAC_Security_Core
---

# LogSanitizer

## Connections
- [[.__init__()_13]] - `calls` [EXTRACTED]
- [[.get_log_sanitizer()]] - `references` [EXTRACTED]
- [[.sanitizer()_2]] - `calls` [INFERRED]
- [[.setup_method()_7]] - `calls` [INFERRED]
- [[.test_empty_inputs_everywhere()]] - `calls` [INFERRED]
- [[.test_log_sanitizer_covers_stack_traces()]] - `calls` [INFERRED]
- [[Action_1]] - `uses` [INFERRED]
- [[AgentRegistry]] - `uses` [INFERRED]
- [[AlertDispatcher]] - `uses` [INFERRED]
- [[ApprovalHardening]] - `uses` [INFERRED]
- [[ApprovalHardeningConfig]] - `uses` [INFERRED]
- [[AuditExportConfig_1]] - `uses` [INFERRED]
- [[AuditExporter]] - `uses` [INFERRED]
- [[BrowserSecurityGuard]] - `uses` [INFERRED]
- [[ConsentFramework]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[DNSFilter]] - `uses` [INFERRED]
- [[DNSFilterConfig]] - `uses` [INFERRED]
- [[DriftDetector]] - `uses` [INFERRED]
- [[EgressMonitor]] - `uses` [INFERRED]
- [[EgressMonitorConfig]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[KeyRotationManager]] - `uses` [INFERRED]
- [[KillSwitchMonitor]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MemoryIntegrityMonitor]] - `uses` [INFERRED]
- [[MemoryLifecycleManager]] - `uses` [INFERRED]
- [[MemorySecurityConfig]] - `uses` [INFERRED]
- [[MetadataGuard]] - `uses` [INFERRED]
- [[MultiTurnTracker]] - `uses` [INFERRED]
- [[NetworkValidator]] - `uses` [INFERRED]
- [[OAuthSecurityValidator]] - `uses` [INFERRED]
- [[OutputCanary]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PathIsolationConfig]] - `uses` [INFERRED]
- [[PathIsolationManager]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[ResourceGuard]] - `uses` [INFERRED]
- [[SessionManager]] - `uses` [INFERRED]
- [[SubagentMonitor]] - `uses` [INFERRED]
- [[SubagentMonitorConfig]] - `uses` [INFERRED]
- [[ToolChainAnalyzer]] - `uses` [INFERRED]
- [[ToolResultInjectionScanner]] - `uses` [INFERRED]
- [[ToolResultPIIConfig]] - `uses` [INFERRED]
- [[ToolResultSanitizer_1]] - `uses` [INFERRED]
- [[ToolResultSanitizer]] - `uses` [INFERRED]
- [[ToolResultSanitizerConfig]] - `uses` [INFERRED]
- [[ToolTier_1]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[XMLLeakFilter]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/Egress__RBAC_Security_Core