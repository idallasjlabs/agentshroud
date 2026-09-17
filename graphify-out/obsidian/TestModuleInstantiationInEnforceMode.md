---
source_file: "gateway/tests/test_all_modules_enforce.py"
type: "code"
community: "Alert Dispatcher & RBAC Reliability"
location: "L147"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Alert_Dispatcher__RBAC_Reliability
---

# TestModuleInstantiationInEnforceMode

## Connections
- [[dot-test_browser_security_guard_instantiates()]] - `method` [EXTRACTED]
- [[dot-test_context_guard_instantiates()]] - `method` [EXTRACTED]
- [[dot-test_egress_filter_instantiates()]] - `method` [EXTRACTED]
- [[dot-test_file_sandbox_instantiates()]] - `method` [EXTRACTED]
- [[dot-test_git_guard_instantiates()]] - `method` [EXTRACTED]
- [[dot-test_multi_turn_tracker_instantiates()]] - `method` [EXTRACTED]
- [[dot-test_output_canary_instantiates()]] - `method` [EXTRACTED]
- [[dot-test_path_isolation_instantiates()]] - `method` [EXTRACTED]
- [[dot-test_prompt_guard_instantiates()]] - `method` [EXTRACTED]
- [[dot-test_tool_chain_analyzer_instantiates()]] - `method` [EXTRACTED]
- [[BrowserSecurityGuard]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[DNSFilterConfig]] - `uses` [INFERRED]
- [[EgressFilter]] - `uses` [INFERRED]
- [[EgressMonitorConfig]] - `uses` [INFERRED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GatewayConfig_4]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[KillSwitchConfig]] - `uses` [INFERRED]
- [[MultiTurnTracker]] - `uses` [INFERRED]
- [[OutputCanary]] - `uses` [INFERRED]
- [[PathIsolationConfig]] - `uses` [INFERRED]
- [[PathIsolationManager]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityConfig_4]] - `uses` [INFERRED]
- [[SecurityModuleConfig]] - `uses` [INFERRED]
- [[SubagentMonitorConfig]] - `uses` [INFERRED]
- [[ToolChainAnalyzer]] - `uses` [INFERRED]
- [[Verify modules can instantiate and operate in enforce mode.]] - `rationale_for` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Alert_Dispatcher__RBAC_Reliability