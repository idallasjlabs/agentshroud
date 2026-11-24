---
source_file: "gateway/security/rate_limit_guard.py"
type: "code"
community: "RateLimitGuard"
location: "L45"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RateLimitGuard
---

# RateLimitConfig

## Connections
- [[dot-__init__()_97]] - `calls` [EXTRACTED]
- [[Configuration for class`RateLimitGuard`. All windows are per (agent_id, tool)…]] - `rationale_for` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[rate_limit_guard.py]] - `contains` [EXTRACTED]
- [[test_burst_clears_after_burst_window()]] - `calls` [EXTRACTED]
- [[test_burst_detection_blocks()]] - `calls` [EXTRACTED]
- [[test_default_clock_is_monotonic()]] - `calls` [EXTRACTED]
- [[test_disabled_never_blocks()]] - `calls` [EXTRACTED]
- [[test_fail_closed_on_internal_error()]] - `calls` [EXTRACTED]
- [[test_limits_are_per_agent()]] - `calls` [EXTRACTED]
- [[test_limits_are_per_tool()]] - `calls` [EXTRACTED]
- [[test_per_tool_override()]] - `calls` [EXTRACTED]
- [[test_pipeline_blocks_and_downstream_not_reached()]] - `uses` [INFERRED]
- [[test_pipeline_disabled_guard_passthrough()]] - `uses` [INFERRED]
- [[test_rate_limit_guard.py]] - `imports` [EXTRACTED]
- [[test_stats_counts_blocks()]] - `calls` [EXTRACTED]
- [[test_sustained_limit_blocks_on_overflow()]] - `calls` [EXTRACTED]
- [[test_under_limit_allows()]] - `calls` [EXTRACTED]
- [[test_window_slides_and_allows_again()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RateLimitGuard
