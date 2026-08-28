---
type: community
cohesion: 0.11
members: 38
---

# Community 182

**Cohesion:** 0.11 - loosely connected
**Members:** 38 nodes

## Members
- [[.__call__()_9]] - code - gateway/tests/test_rate_limit_guard.py
- [[.__init__()_111]] - code - gateway/security/rate_limit_guard.py
- [[.__init__()_178]] - code - gateway/tests/test_rate_limit_guard.py
- [[._burst_limit()]] - code - gateway/security/rate_limit_guard.py
- [[._sustained_limit()]] - code - gateway/security/rate_limit_guard.py
- [[.advance()]] - code - gateway/tests/test_rate_limit_guard.py
- [[.check()_6]] - code - gateway/security/rate_limit_guard.py
- [[.get_stats()_19]] - code - gateway/security/rate_limit_guard.py
- [[Adaptive per-agent  per-tool sliding-window rate limiter with burst detection.]] - rationale - gateway/security/rate_limit_guard.py
- [[Build a SecurityPipeline with only the guards needed to exercise the     RateLim]] - rationale - gateway/tests/test_rate_limit_guard.py
- [[Configuration for class`RateLimitGuard`.      All windows are per (agent_id, t]] - rationale - gateway/security/rate_limit_guard.py
- [[FakeClock]] - code - gateway/tests/test_rate_limit_guard.py
- [[No injected clock the guard falls back to time.monotonic and still works.]] - rationale - gateway/tests/test_rate_limit_guard.py
- [[RateLimitConfig]] - code - gateway/security/rate_limit_guard.py
- [[RateLimitDecision]] - code - gateway/security/rate_limit_guard.py
- [[RateLimitGuard]] - code - gateway/security/rate_limit_guard.py
- [[Record one request for (agent_id, tool) and decide allowblock.          Fail-cl]] - rationale - gateway/security/rate_limit_guard.py
- [[Structured verdict returned by meth`RateLimitGuard.check`.]] - rationale - gateway/security/rate_limit_guard.py
- [[_make_pipeline()_3]] - code - gateway/tests/test_rate_limit_guard.py
- [[clock()]] - code - gateway/tests/test_rate_limit_guard.py
- [[config-off equivalence absent guard leaves inbound behaviour identical.]] - rationale - gateway/tests/test_rate_limit_guard.py
- [[rate_limit_guard.py]] - code - gateway/security/rate_limit_guard.py
- [[test_burst_clears_after_burst_window()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_burst_detection_blocks()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_default_clock_is_monotonic()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_disabled_never_blocks()_1]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_fail_closed_on_internal_error()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_limits_are_per_agent()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_limits_are_per_tool()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_per_tool_override()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_pipeline_blocks_and_downstream_not_reached()_1]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_pipeline_disabled_guard_passthrough()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_pipeline_no_guard_is_unchanged()_1]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_rate_limit_guard.py]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_stats_counts_blocks()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_sustained_limit_blocks_on_overflow()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_under_limit_allows()]] - code - gateway/tests/test_rate_limit_guard.py
- [[test_window_slides_and_allows_again()]] - code - gateway/tests/test_rate_limit_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_182
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 4 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Progressive Trust]]

## Top bridge nodes
- [[RateLimitGuard]] - degree 26, connects to 2 communities
- [[_make_pipeline()_3]] - degree 6, connects to 2 communities
- [[test_pipeline_no_guard_is_unchanged()_1]] - degree 4, connects to 2 communities
- [[test_rate_limit_guard.py]] - degree 22, connects to 1 community
- [[RateLimitConfig]] - degree 21, connects to 1 community