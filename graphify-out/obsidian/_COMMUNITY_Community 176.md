---
type: community
members: 38
---

# Community 176

**Members:** 38 nodes

## Members
- [[.__init__()_69]] - code - gateway/security/data_exfil_volume_guard.py
- [[._size()]] - code - gateway/security/data_exfil_volume_guard.py
- [[.get_stats()_15]] - code - gateway/security/data_exfil_volume_guard.py
- [[.observe()]] - code - gateway/security/data_exfil_volume_guard.py
- [[.reset_session()]] - code - gateway/security/data_exfil_volume_guard.py
- [[A blocked (undelivered) response must not consume the session budget,     otherw]] - rationale - gateway/tests/test_data_exfil_volume_guard.py
- [[Clear cumulative + baseline state for a session (e.g. on new session).]] - rationale - gateway/security/data_exfil_volume_guard.py
- [[Configuration for class`DataExfilVolumeGuard`.]] - rationale - gateway/security/data_exfil_volume_guard.py
- [[Cumulative + adaptive outbound-volume anomaly detector, per session.]] - rationale - gateway/security/data_exfil_volume_guard.py
- [[DataExfilVolumeConfig]] - code - gateway/security/data_exfil_volume_guard.py
- [[DataExfilVolumeGuard]] - code - gateway/security/data_exfil_volume_guard.py
- [[If the guard raises, non-owner outbound is blocked (fail-closed).]] - rationale - gateway/tests/test_data_exfil_volume_guard.py
- [[Observe one outbound response and decide allowblock.          A blocked respons]] - rationale - gateway/security/data_exfil_volume_guard.py
- [[Structured verdict returned by meth`DataExfilVolumeGuard.observe`.]] - rationale - gateway/security/data_exfil_volume_guard.py
- [[The rolling baseline deque is trimmed to adaptive_window; old samples drop.]] - rationale - gateway/tests/test_data_exfil_volume_guard.py
- [[Tiny baselines must not turn ordinary small growth into spikes.]] - rationale - gateway/tests/test_data_exfil_volume_guard.py
- [[VolumeVerdict]] - code - gateway/security/data_exfil_volume_guard.py
- [[_SessionState]] - code - gateway/security/data_exfil_volume_guard.py
- [[_make_pipeline()_1]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[data_exfil_volume_guard.py]] - code - gateway/security/data_exfil_volume_guard.py
- [[test_accepts_str_and_bytes()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_adaptive_floor_prevents_noise_blocks()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_adaptive_needs_min_samples()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_adaptive_spike_blocks()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_adaptive_window_bounds_baseline_memory()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_blocked_response_does_not_add_to_cumulative()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_cumulative_cap_blocks_when_crossed()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_cumulative_is_per_session()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_data_exfil_volume_guard.py]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_disabled_never_blocks()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_get_stats()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_pipeline_allows_small_response()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_pipeline_blocks_and_downstream_not_reached()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_pipeline_fail_closed_for_non_owner_on_error()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_pipeline_no_guard_is_unchanged()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_reset_session_clears_state()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_single_response_over_cap_blocks()]] - code - gateway/tests/test_data_exfil_volume_guard.py
- [[test_under_single_cap_allows()]] - code - gateway/tests/test_data_exfil_volume_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_176
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 6]]
- 3 edges to [[_COMMUNITY_Community 22]]
- 3 edges to [[_COMMUNITY_Community 109]]
- 1 edge to [[_COMMUNITY_Community 251]]
- 1 edge to [[_COMMUNITY_Community 282]]

## Top bridge nodes
- [[DataExfilVolumeGuard]] - degree 26, connects to 2 communities
- [[_make_pipeline()_1]] - degree 6, connects to 2 communities
- [[test_pipeline_no_guard_is_unchanged()]] - degree 3, connects to 2 communities
- [[DataExfilVolumeConfig]] - degree 21, connects to 1 community
- [[test_data_exfil_volume_guard.py]] - degree 21, connects to 1 community