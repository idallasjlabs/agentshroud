---
source_file: "gateway/security/rate_limit_guard.py"
type: "code"
community: "Gateway Test Suite"
location: "L79"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# RateLimitGuard

## Connections
- [[.__init__()_108]] - `method` [EXTRACTED]
- [[._burst_limit()]] - `method` [EXTRACTED]
- [[._sustained_limit()]] - `method` [EXTRACTED]
- [[.check()_6]] - `method` [EXTRACTED]
- [[.get_stats()_19]] - `method` [EXTRACTED]
- [[Adaptive per-agent  per-tool sliding-window rate limiter with burst detection.]] - `rationale_for` [EXTRACTED]
- [[FakeClock]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `conceptually_related_to` [INFERRED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[rate_limit_guard.py]] - `contains` [EXTRACTED]
- [[test_burst_clears_after_burst_window()]] - `calls` [EXTRACTED]
- [[test_burst_detection_blocks()]] - `calls` [EXTRACTED]
- [[test_default_clock_is_monotonic()]] - `calls` [EXTRACTED]
- [[test_disabled_never_blocks()_1]] - `calls` [EXTRACTED]
- [[test_fail_closed_on_internal_error()]] - `calls` [EXTRACTED]
- [[test_limits_are_per_agent()]] - `calls` [EXTRACTED]
- [[test_limits_are_per_tool()]] - `calls` [EXTRACTED]
- [[test_per_tool_override()]] - `calls` [EXTRACTED]
- [[test_pipeline_blocks_and_downstream_not_reached()_1]] - `calls` [EXTRACTED]
- [[test_pipeline_disabled_guard_passthrough()]] - `calls` [EXTRACTED]
- [[test_rate_limit_guard.py]] - `imports` [EXTRACTED]
- [[test_stats_counts_blocks()]] - `calls` [EXTRACTED]
- [[test_sustained_limit_blocks_on_overflow()]] - `calls` [EXTRACTED]
- [[test_under_limit_allows()]] - `calls` [EXTRACTED]
- [[test_window_slides_and_allows_again()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite