---
source_file: "gateway/tests/test_all_modules_enforce.py"
type: "code"
community: "RBAC Middleware & Ingest API"
location: "L151"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/RBAC_Middleware__Ingest_API
---

# TestModuleInstantiationInEnforceMode

## Connections
- [[.test_browser_security_guard_instantiates()]] - `method` [EXTRACTED]
- [[.test_context_guard_instantiates()]] - `method` [EXTRACTED]
- [[.test_egress_filter_instantiates()]] - `method` [EXTRACTED]
- [[.test_file_sandbox_instantiates()]] - `method` [EXTRACTED]
- [[.test_git_guard_instantiates()]] - `method` [EXTRACTED]
- [[.test_multi_turn_tracker_instantiates()]] - `method` [EXTRACTED]
- [[.test_output_canary_instantiates()]] - `method` [EXTRACTED]
- [[.test_path_isolation_instantiates()]] - `method` [EXTRACTED]
- [[.test_prompt_guard_instantiates()]] - `method` [EXTRACTED]
- [[.test_tool_chain_analyzer_instantiates()]] - `method` [EXTRACTED]
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
- [[Verify modules can instantiate and operate in enforce mode.]] - `rationale_for` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/RBAC_Middleware__Ingest_API
