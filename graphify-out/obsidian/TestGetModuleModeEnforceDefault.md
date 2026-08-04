---
source_file: "gateway/tests/test_all_modules_enforce.py"
type: "code"
community: "RBAC Middleware & Ingest API"
location: "L102"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/RBAC_Middleware__Ingest_API
---

# TestGetModuleModeEnforceDefault

## Connections
- [[.test_get_module_mode_no_env_override()]] - `method` [EXTRACTED]
- [[.test_global_monitor_override_downgrades_all()]] - `method` [EXTRACTED]
- [[BrowserSecurityGuard]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[DNSFilterConfig]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressMonitorConfig]] - `uses` [INFERRED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GatewayConfig_1]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[KillSwitchConfig]] - `uses` [INFERRED]
- [[MultiTurnTracker]] - `uses` [INFERRED]
- [[OutputCanary]] - `uses` [INFERRED]
- [[PathIsolationConfig]] - `uses` [INFERRED]
- [[PathIsolationManager]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityConfig]] - `uses` [INFERRED]
- [[SecurityModuleConfig]] - `uses` [INFERRED]
- [[SubagentMonitorConfig]] - `uses` [INFERRED]
- [[ToolChainAnalyzer]] - `uses` [INFERRED]
- [[Verify get_module_mode returns enforce when no override is set.]] - `rationale_for` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/RBAC_Middleware__Ingest_API
