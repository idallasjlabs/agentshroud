---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "Community 49"
location: "L212"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_49
---

# _fake_forward()

## Connections
- [[_openai_ok()]] - `calls` [EXTRACTED]
- [[test_cloud_mode_anthropic_tool_use_shape_passes_through()]] - `indirect_call` [INFERRED]
- [[test_deepseek_r1_routes_to_mlxlm()]] - `indirect_call` [INFERRED]
- [[test_hermes_cloud_mode_uses_anthropic_endpoint()]] - `indirect_call` [INFERRED]
- [[test_hermes_openai_path_local_model_routed_correctly()]] - `indirect_call` [INFERRED]
- [[test_local_mode_anthropic_tool_use_shape_passes_through()]] - `indirect_call` [INFERRED]
- [[test_local_mode_openai_tool_call_shape_passes_through()]] - `indirect_call` [INFERRED]
- [[test_local_oom_failover_disabled_does_not_retry()]] - `indirect_call` [INFERRED]
- [[test_local_oom_no_secondary_falls_through_to_503()]] - `indirect_call` [INFERRED]
- [[test_local_oom_triggers_secondary_failover()]] - `indirect_call` [INFERRED]
- [[test_local_p99_timeout_triggers_secondary_failover()]] - `indirect_call` [INFERRED]
- [[test_local_secondary_failover_anthropic_path()]] - `indirect_call` [INFERRED]
- [[test_local_secondary_failover_exception_returns_none()]] - `indirect_call` [INFERRED]
- [[test_local_secondary_failover_secondary_non_200_returns_none()]] - `indirect_call` [INFERRED]
- [[test_mlx_community_deepseek_routes_to_mlxlm()]] - `indirect_call` [INFERRED]
- [[test_model_ref_round_trip()]] - `indirect_call` [INFERRED]
- [[test_normalize_local_model_provider_prefix_stripped_before_normalize()]] - `indirect_call` [INFERRED]
- [[test_stats_local_secondary_failover_succeeded_incremented()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/INFERRED #community/Community_49