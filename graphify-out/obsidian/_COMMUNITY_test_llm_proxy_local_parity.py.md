---
type: community
members: 66
---

# test_llm_proxy_local_parity.py

**Members:** 66 nodes

## Members
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
- [[The shim must not leak onto backends that accept these fields (LM Studio).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Unknown path (not v1messages, not is_openai) returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[When AGENTSHROUD_LOCAL_FAILOVER_ON_OOM=0, OOM passes through without retry.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_anthropic_tool_use_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
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
- [[_fake_forward()_17]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_18]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_19]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_20]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_21]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_22]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_23]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_model strips the provider prefix for a Fieldflare ref, same as it…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for successful responses.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_make_proxy()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_openai_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[asyncio_3]] - code
- [[deepseek-r1 is routed to mlx_lm endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[failover_local_secondary_succeeded stat increments on successful secondary…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[mlx-communitydeepseek-r1 full ID routes to mlx_lm endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[ollama prefix is stripped during proxy_messages dispatch and normalization…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[p99 timeout (TimeoutError on primary local) triggers secondary local model.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[parametrize]] - code
- [[proxy_messages applies the shim only on the Fieldflare route, before forwarding.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_cloud_mode_anthropic_tool_use_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_deepseek_r1_routes_to_mlxlm()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_route_strips_unsupported_fields_non_streaming]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_model_reads_fieldflare_ref()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_hermes_cloud_mode_uses_anthropic_endpoint()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_hermes_openai_path_local_model_routed_correctly()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_returns_false_for_200()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_mode_anthropic_tool_use_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_mode_openai_tool_call_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_failover_disabled_does_not_retry()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_no_secondary_falls_through_to_503()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_triggers_secondary_failover]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_p99_timeout_triggers_secondary_failover()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_anthropic_path()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_exception_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_secondary_non_200_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_unknown_path_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_mlx_community_deepseek_routes_to_mlxlm()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_model_ref_round_trip()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_non_fieldflare_local_route_keeps_fields]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_provider_prefix_stripped_before_normalize()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_stats_local_secondary_failover_succeeded_incremented()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_llm_proxy_local_paritypy
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py (2)]]
- 5 edges to [[_COMMUNITY_LLMProxy]]
- 3 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 2 edges to [[_COMMUNITY__FakeStreamResponse]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]

## Top bridge nodes
- [[_make_proxy()]] - degree 27, connects to 3 communities
- [[asyncio_3]] - degree 23, connects to 3 communities
- [[test_local_oom_triggers_secondary_failover]] - degree 9, connects to 3 communities
- [[test_fieldflare_route_strips_unsupported_fields_non_streaming]] - degree 8, connects to 3 communities
- [[test_non_fieldflare_local_route_keeps_fields]] - degree 8, connects to 3 communities
