---
type: community
members: 29
---

# Community 506

**Members:** 29 nodes

## Members
- [[Cloud mode Anthropic tool_use responses are unmodified (baseline parity).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Exception during secondary dispatch increments failed stat and returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Full round-trip each model ref is normalized and dispatched to the correct back]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Hermes sends OpenAI-compat requests; local qwen3 model routes to LM Studio.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[In cloud mode, Hermes Claude model routes to Anthropic endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[OpenAI-format tool_calls response returns the same shape in local mode.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[The shim must not leak onto backends that accept these fields (LM Studio).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Unknown path (not v1messages, not is_openai) returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[When AGENTSHROUD_LOCAL_FAILOVER_ON_OOM=0, OOM passes through without retry.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_model strips the provider prefix for a Fieldflare ref, same     as it]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_secondary_model returns None if env var is unset.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_make_proxy()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[deepseek-r1 is routed to mlx_lm endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[failover_local_secondary_succeeded stat increments on successful secondary dispa]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[ollama prefix is stripped during proxy_messages dispatch and normalization foll]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_cloud_mode_anthropic_tool_use_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_deepseek_r1_routes_to_mlxlm()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_model_reads_fieldflare_ref()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_secondary_model_returns_none_when_unset()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_hermes_cloud_mode_uses_anthropic_endpoint()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_hermes_openai_path_local_model_routed_correctly()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_mode_openai_tool_call_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_failover_disabled_does_not_retry()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_exception_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_unknown_path_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_model_ref_round_trip()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_non_fieldflare_local_route_keeps_fields()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_provider_prefix_stripped_before_normalize()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_stats_local_secondary_failover_succeeded_incremented()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_506
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 208]]
- 3 edges to [[_COMMUNITY_Community 1969]]
- 2 edges to [[_COMMUNITY_Community 5]]
- 1 edge to [[_COMMUNITY_Community 1278]]
- 1 edge to [[_COMMUNITY_Community 2316]]
- 1 edge to [[_COMMUNITY_Community 2004]]
- 1 edge to [[_COMMUNITY_Community 2325]]
- 1 edge to [[_COMMUNITY_Community 2322]]
- 1 edge to [[_COMMUNITY_Community 2323]]
- 1 edge to [[_COMMUNITY_Community 2336]]
- 1 edge to [[_COMMUNITY_Community 2332]]

## Top bridge nodes
- [[_make_proxy()]] - degree 28, connects to 11 communities
- [[test_normalize_local_model_provider_prefix_stripped_before_normalize()]] - degree 3, connects to 1 community
- [[test_local_mode_openai_tool_call_shape_passes_through()]] - degree 3, connects to 1 community
- [[test_cloud_mode_anthropic_tool_use_shape_passes_through()]] - degree 3, connects to 1 community
- [[test_local_oom_failover_disabled_does_not_retry()]] - degree 3, connects to 1 community