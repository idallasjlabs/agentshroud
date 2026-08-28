---
source_file: "gateway/ingest_api/middleware.py"
type: "code"
community: "Memory Lifecycle & Egress Filtering"
location: "L496"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Memory_Lifecycle__Egress_Filtering
---

# Any

## Connections
- [[._analyze_request_for_rbac()]] - `references` [EXTRACTED]
- [[._check_cross_session_access()]] - `references` [EXTRACTED]
- [[._check_rbac_permissions()]] - `references` [EXTRACTED]
- [[._enforce_session_isolation()]] - `references` [EXTRACTED]
- [[._extract_user_id()]] - `references` [EXTRACTED]
- [[._is_tool_call_request()]] - `references` [EXTRACTED]
- [[.process_request()]] - `references` [EXTRACTED]
- [[.process_tool_result()]] - `references` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[AgentRegistry]] - `uses` [INFERRED]
- [[AlertDispatcher]] - `uses` [INFERRED]
- [[ApprovalHardening]] - `uses` [INFERRED]
- [[ApprovalHardeningConfig]] - `uses` [INFERRED]
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

#graphify/code #graphify/INFERRED #community/Memory_Lifecycle__Egress_Filtering