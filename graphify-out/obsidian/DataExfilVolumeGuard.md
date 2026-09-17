---
source_file: "gateway/security/data_exfil_volume_guard.py"
type: "code"
community: "Community 189"
location: "L83"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_189
---

# DataExfilVolumeGuard

## Connections
- [[dot-__init__()_80]] - `method` [EXTRACTED]
- [[dot-_size()]] - `method` [EXTRACTED]
- [[dot-get_stats()_13]] - `method` [EXTRACTED]
- [[dot-observe()]] - `method` [EXTRACTED]
- [[dot-reset_session()_1]] - `method` [EXTRACTED]
- [[Cumulative + adaptive outbound-volume anomaly detector, per session.]] - `rationale_for` [EXTRACTED]
- [[EgressFilter]] - `conceptually_related_to` [EXTRACTED]
- [[data_exfil_volume_guard.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_accepts_str_and_bytes()]] - `calls` [EXTRACTED]
- [[test_adaptive_floor_prevents_noise_blocks()]] - `calls` [EXTRACTED]
- [[test_adaptive_needs_min_samples()]] - `calls` [EXTRACTED]
- [[test_adaptive_spike_blocks()]] - `calls` [EXTRACTED]
- [[test_adaptive_window_bounds_baseline_memory()]] - `calls` [EXTRACTED]
- [[test_blocked_response_does_not_add_to_cumulative()]] - `calls` [EXTRACTED]
- [[test_cumulative_cap_blocks_when_crossed()]] - `calls` [EXTRACTED]
- [[test_cumulative_is_per_session()]] - `calls` [EXTRACTED]
- [[test_data_exfil_volume_guard.py]] - `imports` [EXTRACTED]
- [[test_disabled_never_blocks()]] - `calls` [EXTRACTED]
- [[test_get_stats()_2]] - `calls` [EXTRACTED]
- [[test_pipeline_allows_small_response()]] - `calls` [EXTRACTED]
- [[test_pipeline_blocks_and_downstream_not_reached()]] - `calls` [EXTRACTED]
- [[test_reset_session_clears_state()]] - `calls` [EXTRACTED]
- [[test_single_response_over_cap_blocks()]] - `calls` [EXTRACTED]
- [[test_under_single_cap_allows()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_189