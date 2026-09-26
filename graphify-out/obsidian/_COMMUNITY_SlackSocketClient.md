---
type: community
cohesion: 0.06
members: 41
---

# SlackSocketClient

**Cohesion:** 0.06 - loosely connected
**Members:** 41 nodes

## Members
- [[.check_vram_headroom()]] - code - gateway/security/resource_guard.py
- [[.test_cleanup_keeps_fresh_agents()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cleanup_removes_stale_agents()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cleanup_tolerates_missing_file()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cleanup_unlinks_existing_and_clears_registry()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cpu_limit_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cpu_limit_fails_closed_on_psutil_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cpu_limit_ok_when_under()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_disabled_when_threshold_zero()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_disk_write_limit_allows_when_no_baseline()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_disk_write_limit_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_disk_write_limit_under_threshold()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_get_resource_guard_is_lazy_singleton()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_get_usage_stats_for_agent()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_get_usage_stats_system_wide()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_memory_limit_fails_closed_on_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_memory_limit_ok_and_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_passes_with_sufficient_headroom()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_register_blocks_over_limit()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_register_under_limit()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_rejects_insufficient_headroom()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_start_request_tracking_records_baseline()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_start_request_tracking_survives_psutil_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[Current resource usage metrics.]] - rationale - gateway/security/resource_guard.py
- [[Get the global resource guard instance, creating it lazily on first call.]] - rationale - gateway/security/resource_guard.py
- [[Pre-flight VRAM headroom check before dispatching a long-context local-model cal]] - rationale - gateway/security/resource_guard.py
- [[Raised when a local-model call is rejected because estimated VRAM usage     woul]] - rationale - gateway/security/resource_guard.py
- [[ResourceUsage]] - code - gateway/security/resource_guard.py
- [[TestCpuMemoryDiskLimits]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestExpiredUsageCleanup]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestGlobalAccessor]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestTempFiles]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestUsageStatsAndTracking]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestVramHeadroom]] - code - gateway/tests/test_resource_guard_limits.py
- [[VRAMHeadroomError]] - code - gateway/security/resource_guard.py
- [[VRAMHeadroomError must be a distinct exception, not a subclass of ResourceWarnin]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[get_resource_guard()]] - code - gateway/security/resource_guard.py
- [[guard()_3]] - code - gateway/tests/test_resource_guard_limits.py
- [[resource_guard.py]] - code - gateway/security/resource_guard.py
- [[test_resource_guard_limits.py]] - code - gateway/tests/test_resource_guard_limits.py
- [[test_vram_headroom_error_is_not_resource_warning()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SlackSocketClient
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_rbac_config.py]]
- 10 edges to [[_COMMUNITY_voice_task]]
- 3 edges to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_test_scorecard_integrity.py]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_GroupApprovalRouter]]
- 1 edge to [[_COMMUNITY_climain.py]]
- 1 edge to [[_COMMUNITY_Mode B — Comprehensive review sweep]]

## Top bridge nodes
- [[resource_guard.py]] - degree 10, connects to 5 communities
- [[VRAMHeadroomError]] - degree 15, connects to 3 communities
- [[test_resource_guard_limits.py]] - degree 12, connects to 2 communities
- [[TestCpuMemoryDiskLimits]] - degree 12, connects to 2 communities
- [[TestTempFiles]] - degree 8, connects to 2 communities