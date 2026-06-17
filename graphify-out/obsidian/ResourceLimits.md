---
source_file: "gateway/security/resource_guard.py"
type: "code"
community: "PII Sanitizer & Resource Guard"
location: "L26"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer__Resource_Guard
---

# ResourceLimits

## Connections
- [[.__init__()_90]] - `references` [EXTRACTED]
- [[.setup_method()_19]] - `calls` [EXTRACTED]
- [[.test_cpu_limit_check()]] - `calls` [EXTRACTED]
- [[.test_disk_write_limit()]] - `calls` [EXTRACTED]
- [[.test_memory_limit_check()]] - `calls` [EXTRACTED]
- [[.test_resource_guard_config()]] - `calls` [EXTRACTED]
- [[.test_resource_guard_init()]] - `calls` [EXTRACTED]
- [[.test_setup_with_custom_limits_overrides_defaults()]] - `calls` [EXTRACTED]
- [[.test_stop_cancels_monitor_task()]] - `calls` [EXTRACTED]
- [[.test_usage_stats()]] - `calls` [EXTRACTED]
- [[Any_62]] - `uses` [INFERRED]
- [[Configuration for resource limits.]] - `rationale_for` [EXTRACTED]
- [[TestAuditTrail_1]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard_1]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestPIIDetection_1]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestResourceGuard]] - `uses` [INFERRED]
- [[TestResourceGuardAlertBridge]] - `uses` [INFERRED]
- [[TestResourceGuardLifecycle]] - `uses` [INFERRED]
- [[TestResourceGuardWiring]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSupplyChain_1]] - `uses` [INFERRED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[resource_guard.py]] - `contains` [EXTRACTED]
- [[setup_resource_guard()]] - `references` [EXTRACTED]
- [[test_resource_guard.py]] - `imports` [EXTRACTED]
- [[test_resource_guard_wiring.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer__Resource_Guard