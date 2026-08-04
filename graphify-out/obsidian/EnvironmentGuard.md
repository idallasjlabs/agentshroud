---
source_file: "gateway/security/env_guard.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L33"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Environment_Guard__Leak_Detection
---

# EnvironmentGuard

## Connections
- [[.__init__()_8]] - `calls` [EXTRACTED]
- [[.__init__()_63]] - `method` [EXTRACTED]
- [[._contains_env_access_patterns()]] - `method` [EXTRACTED]
- [[._looks_like_credential()]] - `method` [EXTRACTED]
- [[._record_leakage()]] - `method` [EXTRACTED]
- [[.check_command_execution()]] - `method` [EXTRACTED]
- [[.check_file_access()]] - `method` [EXTRACTED]
- [[.clear_detected_leakages()]] - `method` [EXTRACTED]
- [[.export_leakage_report()]] - `method` [EXTRACTED]
- [[.get_leakage_summary()]] - `method` [EXTRACTED]
- [[.monitor_environment_access()]] - `method` [EXTRACTED]
- [[.scrub_command_output()]] - `method` [EXTRACTED]
- [[.test_env_guard_command_check()]] - `calls` [EXTRACTED]
- [[.test_env_guard_detects_data_access()]] - `calls` [INFERRED]
- [[.test_env_guard_monitoring()]] - `calls` [EXTRACTED]
- [[.test_env_guard_scrub_output()]] - `calls` [EXTRACTED]
- [[.test_env_guard_scrubs_output()]] - `calls` [INFERRED]
- [[.test_natural_language_question_is_allowed()]] - `calls` [EXTRACTED]
- [[.test_unparseable_text_is_allowed()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_6]] - `uses` [INFERRED]
- [[Guard against environment variable leakage and unauthorized access.]] - `rationale_for` [EXTRACTED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestAuditTrail_1]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard_1]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestDRYOwnerChatID]] - `uses` [INFERRED]
- [[TestDependencySecurity]] - `uses` [INFERRED]
- [[TestDoSPrevention]] - `uses` [INFERRED]
- [[TestEgressConfigDefaultEnforce]] - `uses` [INFERRED]
- [[TestEnvGuardFailOpen]] - `uses` [INFERRED]
- [[TestExfiltrationDetection]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestFileSandboxDefaultEnforce]] - `uses` [INFERRED]
- [[TestGitGuardDefaultEnforce]] - `uses` [INFERRED]
- [[TestHTTPSecurity]] - `uses` [INFERRED]
- [[TestInfoLeakage]] - `uses` [INFERRED]
- [[TestKeyVaultWired]] - `uses` [INFERRED]
- [[TestLLMProxyEndpoints]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestMCPSecurity]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestNotifyUserBlockedSanitization]] - `uses` [INFERRED]
- [[TestPIIDetection_1]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestResourceGuardFailClosed]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSupplyChain_1]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[env_guard.py]] - `contains` [EXTRACTED]
- [[get_env_guard()]] - `references` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_round2_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Environment_Guard__Leak_Detection
