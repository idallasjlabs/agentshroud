---
type: community
cohesion: 0.04
members: 84
---

# test_llm_proxy_local_parity.py

**Cohesion:** 0.04 - loosely connected
**Members:** 84 nodes

## Members
- [[.block_credentials()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.filter_xml_blocks()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.sanitize()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[128k token request at 4 bytestoken KV cache triggers rejection at 4096 MB…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Anthropic-format tool_use response returns the same shape in local mode.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Cloud mode Anthropic tool_use responses are unmodified (baseline parity).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Exception during secondary dispatch increments failed stat and returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Full round-trip each model ref is normalized and dispatched to the correct…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Hermes sends OpenAI-compat requests; local qwen3 model routes to LM Studio.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[If no secondary is configured and primary hits OOM, 503 is returned.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[In cloud mode, Hermes Claude model routes to Anthropic endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[OOM (503 backend_unavailable from primary local) triggers secondary local…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[OpenAI-format tool_calls response returns the same shape in local mode.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Secondary failover for Anthropic-format (v1messages) path translates and…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Secondary model returning non-200 increments failed stat and returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Small context request passes VRAM headroom check.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Unknown path (not v1messages, not is_openai) returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[VRAM check is skipped when max_vram_headroom_mb=0 (disabled).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[VRAMHeadroomError must be a distinct exception, not a subclass of…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[When AGENTSHROUD_LOCAL_FAILOVER_ON_OOM=0, OOM passes through without retry.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Workstream C — Full local-model parity for both bots. Tests that every cloud-…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_FakeSanitizer]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_anthropic_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_anthropic_tool_use_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_1]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_2]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_3]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_4]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_5]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_6]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_7]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_8]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_9]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_10]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_11]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_12]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_13]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_14]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_15]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_16]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_model strips the provider prefix for a Fieldflare ref, same as it…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_secondary_model reads AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_secondary_model returns None if env var is unset.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for successful responses.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_make_proxy()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_openai_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_openai_tool_use_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[asyncio_2]] - code
- [[check_vram_headroom raises VRAMHeadroomError when estimated VRAM exceeds budget.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[deepseek-r1 is routed to mlx_lm endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[failover_local_secondary_succeeded stat increments on successful secondary…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[mlx-communitydeepseek-r1 full ID routes to mlx_lm endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[ollama prefix is stripped during proxy_messages dispatch and normalization…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[p99 timeout (TimeoutError on primary local) triggers secondary local model.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[parametrize_2]] - code
- [[test_cloud_mode_anthropic_tool_use_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_deepseek_r1_routes_to_mlxlm()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_model_reads_fieldflare_ref()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_secondary_model_reads_env()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_secondary_model_returns_none_when_unset()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_hermes_cloud_mode_uses_anthropic_endpoint()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_hermes_openai_path_local_model_routed_correctly()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_returns_false_for_200()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_llm_proxy_local_parity.py]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_mode_anthropic_tool_use_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_mode_openai_tool_call_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_failover_disabled_does_not_retry()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_no_secondary_falls_through_to_503()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_triggers_secondary_failover()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_p99_timeout_triggers_secondary_failover()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_anthropic_path()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_exception_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_secondary_non_200_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_unknown_path_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_mlx_community_deepseek_routes_to_mlxlm()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_model_ref_round_trip()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_provider_prefix_stripped_before_normalize()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_stats_local_secondary_failover_succeeded_incremented()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_vram_headroom_error_is_not_resource_warning()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_llm_proxy_local_paritypy
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_LLMProxy]]
- 6 edges to [[_COMMUNITY_._is_local_oom()]]
- 1 edge to [[_COMMUNITY_gateway.proxy.llm_proxy]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]

## Top bridge nodes
- [[test_llm_proxy_local_parity.py]] - degree 59, connects to 4 communities
- [[test_is_local_oom_returns_false_for_200()]] - degree 5, connects to 2 communities
- [[_make_proxy()]] - degree 24, connects to 1 community