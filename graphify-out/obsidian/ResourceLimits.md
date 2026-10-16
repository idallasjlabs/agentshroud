---
source_file: "gateway/security/resource_guard.py"
type: "code"
community: "ResourceGuard"
location: "L49"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ResourceGuard
---

# ResourceLimits

## Connections
- [[dot-__init__()_37]] - `references` [EXTRACTED]
- [[dot-setup_method()_6]] - `calls` [EXTRACTED]
- [[dot-test_cpu_limit_check()]] - `calls` [EXTRACTED]
- [[dot-test_disk_write_limit()]] - `calls` [EXTRACTED]
- [[dot-test_memory_limit_check()]] - `calls` [EXTRACTED]
- [[dot-test_resource_guard_config()]] - `calls` [EXTRACTED]
- [[dot-test_resource_guard_init()]] - `calls` [EXTRACTED]
- [[dot-test_setup_with_custom_limits_overrides_defaults()]] - `calls` [EXTRACTED]
- [[dot-test_stop_cancels_monitor_task()]] - `calls` [EXTRACTED]
- [[dot-test_usage_stats()]] - `calls` [EXTRACTED]
- [[Any_17]] - `uses` [INFERRED]
- [[Configuration for resource limits.]] - `rationale_for` [EXTRACTED]
- [[LLMProxy_1]] - `uses` [INFERRED]
- [[TestAuditTrail]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard]] - `uses` [INFERRED]
- [[TestCpuMemoryDiskLimits]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestExpiredUsageCleanup]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestGlobalAccessor]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestPIIDetection]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestResourceGuard]] - `uses` [INFERRED]
- [[TestResourceGuardAlertBridge]] - `uses` [INFERRED]
- [[TestResourceGuardLifecycle]] - `uses` [INFERRED]
- [[TestResourceGuardWiring]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSupplyChain]] - `uses` [INFERRED]
- [[TestTempFiles]] - `uses` [INFERRED]
- [[TestUsageStatsAndTracking]] - `uses` [INFERRED]
- [[TestVramHeadroom]] - `uses` [INFERRED]
- [[_FakeSanitizer]] - `uses` [INFERRED]
- [[guard()]] - `calls` [EXTRACTED]
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

#graphify/code #graphify/INFERRED #community/ResourceGuard
