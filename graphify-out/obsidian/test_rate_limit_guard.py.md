---
source_file: "gateway/tests/test_rate_limit_guard.py"
type: "code"
community: "RateLimitGuard"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RateLimitGuard
---

# test_rate_limit_guard.py

## Connections
- [[FakeClock_1]] - `contains` [EXTRACTED]
- [[RateLimitConfig]] - `imports` [EXTRACTED]
- [[RateLimitGuard]] - `imports` [EXTRACTED]
- [[SecurityPipeline]] - `imports` [EXTRACTED]
- [[Tests for RateLimitGuard — SCRUM-68 WS-B.1 deep-hardening module. Adaptive per-…]] - `rationale_for` [EXTRACTED]
- [[_make_pipeline()_2]] - `contains` [EXTRACTED]
- [[clock()]] - `contains` [EXTRACTED]
- [[rate_limit_guard.py]] - `imports_from` [EXTRACTED]
- [[test_burst_clears_after_burst_window()]] - `contains` [EXTRACTED]
- [[test_burst_detection_blocks()]] - `contains` [EXTRACTED]
- [[test_default_clock_is_monotonic()]] - `contains` [EXTRACTED]
- [[test_disabled_never_blocks()]] - `contains` [EXTRACTED]
- [[test_fail_closed_on_internal_error()]] - `contains` [EXTRACTED]
- [[test_limits_are_per_agent()]] - `contains` [EXTRACTED]
- [[test_limits_are_per_tool()]] - `contains` [EXTRACTED]
- [[test_per_tool_override()]] - `contains` [EXTRACTED]
- [[test_pipeline_blocks_and_downstream_not_reached()]] - `contains` [EXTRACTED]
- [[test_pipeline_disabled_guard_passthrough()]] - `contains` [EXTRACTED]
- [[test_pipeline_no_guard_is_unchanged()]] - `contains` [EXTRACTED]
- [[test_stats_counts_blocks()]] - `contains` [EXTRACTED]
- [[test_sustained_limit_blocks_on_overflow()]] - `contains` [EXTRACTED]
- [[test_under_limit_allows()]] - `contains` [EXTRACTED]
- [[test_window_slides_and_allows_again()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RateLimitGuard
