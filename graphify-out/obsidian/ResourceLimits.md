---
source_file: "gateway/security/resource_guard.py"
type: "code"
community: "Community 225"
location: "L49"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_225
---

# ResourceLimits

## Connections
- [[.__init__()_114]] - `references` [EXTRACTED]
- [[.setup_method()_22]] - `calls` [EXTRACTED]
- [[.test_cpu_limit_check()]] - `calls` [EXTRACTED]
- [[.test_disk_write_limit()]] - `calls` [EXTRACTED]
- [[.test_memory_limit_check()]] - `calls` [EXTRACTED]
- [[.test_resource_guard_config()]] - `calls` [EXTRACTED]
- [[.test_resource_guard_init()]] - `calls` [EXTRACTED]
- [[.test_setup_with_custom_limits_overrides_defaults()]] - `calls` [EXTRACTED]
- [[.test_stop_cancels_monitor_task()]] - `calls` [EXTRACTED]
- [[.test_usage_stats()]] - `calls` [EXTRACTED]
- [[Any_69]] - `uses` [INFERRED]
- [[Configuration for resource limits.]] - `rationale_for` [EXTRACTED]
- [[LLMProxy_2]] - `uses` [INFERRED]
- [[TestAuditTrail_1]] - `uses` [INFERRED]
- [[TestAuth_1]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard_1]] - `uses` [INFERRED]
- [[TestCpuMemoryDiskLimits]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestExpiredUsageCleanup]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestGlobalAccessor]] - `uses` [INFERRED]
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
- [[TestTempFiles]] - `uses` [INFERRED]
- [[TestUsageStatsAndTracking]] - `uses` [INFERRED]
- [[TestVramHeadroom]] - `uses` [INFERRED]
- [[_FakeSanitizer_1]] - `uses` [INFERRED]
- [[guard()_3]] - `calls` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[resource_guard.py]] - `contains` [EXTRACTED]
- [[setup_resource_guard()]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `imports` [EXTRACTED]
- [[test_resource_guard.py]] - `imports` [EXTRACTED]
- [[test_resource_guard_limits.py]] - `imports` [EXTRACTED]
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - `calls` [EXTRACTED]
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - `calls` [EXTRACTED]
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - `calls` [EXTRACTED]
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - `calls` [EXTRACTED]
- [[test_resource_guard_wiring.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_225