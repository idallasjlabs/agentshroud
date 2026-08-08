---
source_file: "gateway/security/data_exfil_volume_guard.py"
type: "code"
community: "Gateway Test Suite"
location: "L83"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# DataExfilVolumeGuard

## Connections
- [[.__init__()_66]] - `method` [EXTRACTED]
- [[._size()]] - `method` [EXTRACTED]
- [[.get_stats()_15]] - `method` [EXTRACTED]
- [[.observe()]] - `method` [EXTRACTED]
- [[.reset_session()]] - `method` [EXTRACTED]
- [[Cumulative + adaptive outbound-volume anomaly detector, per session.]] - `rationale_for` [EXTRACTED]
- [[EgressFilter_1]] - `conceptually_related_to` [EXTRACTED]
- [[data_exfil_volume_guard.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_accepts_str_and_bytes()]] - `calls` [EXTRACTED]
- [[test_adaptive_floor_prevents_noise_blocks()]] - `calls` [EXTRACTED]
- [[test_adaptive_needs_min_samples()]] - `calls` [EXTRACTED]
- [[test_adaptive_spike_blocks()]] - `calls` [EXTRACTED]
- [[test_adaptive_window_bounds_baseline_memory()]] - `calls` [EXTRACTED]
- [[test_blocked_response_does_not_add_to_cumulative()]] - `calls` [EXTRACTED]
- [[test_cumulative_cap_blocks_when_crossed()]] - `calls` [EXTRACTED]
- [[test_cumulative_is_per_session()]] - `calls` [EXTRACTED]
- [[test_data_exfil_volume_guard.py]] - `implements` [EXTRACTED]
- [[test_disabled_never_blocks()]] - `calls` [EXTRACTED]
- [[test_get_stats()]] - `calls` [EXTRACTED]
- [[test_pipeline_allows_small_response()]] - `calls` [EXTRACTED]
- [[test_pipeline_blocks_and_downstream_not_reached()]] - `calls` [EXTRACTED]
- [[test_reset_session_clears_state()]] - `calls` [EXTRACTED]
- [[test_single_response_over_cap_blocks()]] - `calls` [EXTRACTED]
- [[test_under_single_cap_allows()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite