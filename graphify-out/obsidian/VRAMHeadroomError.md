---
source_file: "gateway/security/resource_guard.py"
type: "code"
community: "ResourceGuard"
location: "L25"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ResourceGuard
---

# VRAMHeadroomError

## Connections
- [[.check_vram_headroom()]] - `calls` [EXTRACTED]
- [[Exception_4]] - `inherits` [EXTRACTED]
- [[Raised when a local-model call is rejected because estimated VRAM usage     woul]] - `rationale_for` [EXTRACTED]
- [[TestCpuMemoryDiskLimits]] - `uses` [INFERRED]
- [[TestExpiredUsageCleanup]] - `uses` [INFERRED]
- [[TestGlobalAccessor]] - `uses` [INFERRED]
- [[TestTempFiles]] - `uses` [INFERRED]
- [[TestUsageStatsAndTracking]] - `uses` [INFERRED]
- [[TestVramHeadroom]] - `uses` [INFERRED]
- [[resource_guard.py]] - `contains` [EXTRACTED]
- [[test_resource_guard_limits.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ResourceGuard