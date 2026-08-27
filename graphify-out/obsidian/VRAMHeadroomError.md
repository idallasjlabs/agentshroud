---
source_file: "gateway/security/resource_guard.py"
type: "code"
community: "Community 7"
location: "L25"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_7
---

# VRAMHeadroomError

## Connections
- [[.check_vram_headroom()]] - `calls` [EXTRACTED]
- [[Exception]] - `inherits` [EXTRACTED]
- [[LLMProxy_2]] - `uses` [INFERRED]
- [[Raised when a local-model call is rejected because estimated VRAM usage     woul]] - `rationale_for` [EXTRACTED]
- [[TestCpuMemoryDiskLimits]] - `uses` [INFERRED]
- [[TestExpiredUsageCleanup]] - `uses` [INFERRED]
- [[TestGlobalAccessor]] - `uses` [INFERRED]
- [[TestTempFiles]] - `uses` [INFERRED]
- [[TestUsageStatsAndTracking]] - `uses` [INFERRED]
- [[TestVramHeadroom]] - `uses` [INFERRED]
- [[_FakeSanitizer_1]] - `uses` [INFERRED]
- [[resource_guard.py]] - `contains` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `imports` [EXTRACTED]
- [[test_resource_guard_limits.py]] - `imports` [EXTRACTED]
- [[test_vram_headroom_error_is_not_resource_warning()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_7