---
type: community
cohesion: 0.09
members: 33
---

# Community 225

**Cohesion:** 0.09 - loosely connected
**Members:** 33 nodes

## Members
- [[.block_credentials()_2]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.filter_xml_blocks()_2]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.sanitize()_4]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.test_cleanup_keeps_fresh_agents()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cleanup_removes_stale_agents()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cleanup_tolerates_missing_file()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cleanup_unlinks_existing_and_clears_registry()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_disabled_when_threshold_zero()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_get_resource_guard_is_lazy_singleton()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_get_usage_stats_for_agent()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_get_usage_stats_system_wide()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_passes_with_sufficient_headroom()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_register_blocks_over_limit()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_register_under_limit()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_rejects_insufficient_headroom()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_start_request_tracking_records_baseline()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_start_request_tracking_survives_psutil_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[Configuration for resource limits.]] - rationale - gateway/security/resource_guard.py
- [[Get the global resource guard instance, creating it lazily on first call.]] - rationale - gateway/security/resource_guard.py
- [[LLMProxy_2]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[Raised when a local-model call is rejected because estimated VRAM usage     woul]] - rationale - gateway/security/resource_guard.py
- [[ResourceLimits]] - code - gateway/security/resource_guard.py
- [[TestExpiredUsageCleanup]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestGlobalAccessor]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestTempFiles]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestUsageStatsAndTracking]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestVramHeadroom]] - code - gateway/tests/test_resource_guard_limits.py
- [[VRAMHeadroomError]] - code - gateway/security/resource_guard.py
- [[_FakeSanitizer_1]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[get_resource_guard()]] - code - gateway/security/resource_guard.py
- [[guard()_3]] - code - gateway/tests/test_resource_guard_limits.py
- [[resource_guard.py]] - code - gateway/security/resource_guard.py
- [[test_resource_guard_limits.py]] - code - gateway/tests/test_resource_guard_limits.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_225
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_Community 88]]
- 12 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 7 edges to [[_COMMUNITY_Community 807]]
- 6 edges to [[_COMMUNITY_Community 54]]
- 4 edges to [[_COMMUNITY_Community 351]]
- 3 edges to [[_COMMUNITY_Community 918]]
- 2 edges to [[_COMMUNITY_Community 83]]
- 2 edges to [[_COMMUNITY_Community 850]]
- 1 edge to [[_COMMUNITY_Community 165]]
- 1 edge to [[_COMMUNITY_Ingest API & Approval Routes]]
- 1 edge to [[_COMMUNITY_Community 95]]
- 1 edge to [[_COMMUNITY_Community 347]]
- 1 edge to [[_COMMUNITY_Community 97]]
- 1 edge to [[_COMMUNITY_Community 18]]

## Top bridge nodes
- [[ResourceLimits]] - degree 49, connects to 9 communities
- [[resource_guard.py]] - degree 10, connects to 5 communities
- [[VRAMHeadroomError]] - degree 15, connects to 4 communities
- [[_FakeSanitizer_1]] - degree 9, connects to 3 communities
- [[LLMProxy_2]] - degree 5, connects to 3 communities