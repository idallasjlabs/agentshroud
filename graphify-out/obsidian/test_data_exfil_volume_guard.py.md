---
source_file: "gateway/tests/test_data_exfil_volume_guard.py"
type: "code"
community: "Gateway Test Suite"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# test_data_exfil_volume_guard.py

## Connections
- [[DataExfilVolumeConfig]] - `imports` [EXTRACTED]
- [[DataExfilVolumeGuard]] - `implements` [EXTRACTED]
- [[SecurityPipeline]] - `imports` [EXTRACTED]
- [[_make_pipeline()_1]] - `contains` [EXTRACTED]
- [[test_accepts_str_and_bytes()]] - `contains` [EXTRACTED]
- [[test_adaptive_floor_prevents_noise_blocks()]] - `contains` [EXTRACTED]
- [[test_adaptive_needs_min_samples()]] - `contains` [EXTRACTED]
- [[test_adaptive_spike_blocks()]] - `contains` [EXTRACTED]
- [[test_adaptive_window_bounds_baseline_memory()]] - `contains` [EXTRACTED]
- [[test_blocked_response_does_not_add_to_cumulative()]] - `contains` [EXTRACTED]
- [[test_cumulative_cap_blocks_when_crossed()]] - `contains` [EXTRACTED]
- [[test_cumulative_is_per_session()]] - `contains` [EXTRACTED]
- [[test_disabled_never_blocks()]] - `contains` [EXTRACTED]
- [[test_get_stats()]] - `contains` [EXTRACTED]
- [[test_pipeline_allows_small_response()]] - `contains` [EXTRACTED]
- [[test_pipeline_blocks_and_downstream_not_reached()]] - `contains` [EXTRACTED]
- [[test_pipeline_fail_closed_for_non_owner_on_error()]] - `contains` [EXTRACTED]
- [[test_pipeline_no_guard_is_unchanged()]] - `contains` [EXTRACTED]
- [[test_reset_session_clears_state()]] - `contains` [EXTRACTED]
- [[test_single_response_over_cap_blocks()]] - `contains` [EXTRACTED]
- [[test_under_single_cap_allows()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite