---
source_file: "gateway/tests/test_all_modules_enforce.py"
type: "code"
community: "PathIsolationManager"
location: "L98"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PathIsolationManager
---

# TestGetModuleModeEnforceDefault

## Connections
- [[dot-test_get_module_mode_no_env_override()]] - `method` [EXTRACTED]
- [[dot-test_global_monitor_override_downgrades_all()]] - `method` [EXTRACTED]
- [[BrowserSecurityGuard]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[DNSFilterConfig]] - `uses` [INFERRED]
- [[EgressFilter]] - `uses` [INFERRED]
- [[EgressMonitorConfig]] - `uses` [INFERRED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GatewayConfig_3]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[KillSwitchConfig_1]] - `uses` [INFERRED]
- [[MultiTurnTracker]] - `uses` [INFERRED]
- [[OutputCanary]] - `uses` [INFERRED]
- [[PathIsolationConfig]] - `uses` [INFERRED]
- [[PathIsolationManager]] - `uses` [INFERRED]
- [[PromptGuard_1]] - `uses` [INFERRED]
- [[SecurityConfig_4]] - `uses` [INFERRED]
- [[SecurityModuleConfig]] - `uses` [INFERRED]
- [[SubagentMonitorConfig]] - `uses` [INFERRED]
- [[ToolChainAnalyzer]] - `uses` [INFERRED]
- [[Verify get_module_mode returns enforce when no override is set.]] - `rationale_for` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PathIsolationManager
