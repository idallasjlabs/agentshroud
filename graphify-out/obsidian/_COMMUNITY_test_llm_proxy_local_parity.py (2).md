---
type: community
members: 63
---

# test_llm_proxy_local_parity.py (2)

**Members:** 63 nodes

## Members
- [[dot-_flatten_fieldflare_schema()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_is_local_oom()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_merge_object_schemas()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_strip_fieldflare_unsupported_fields()]] - code - gateway/proxy/llm_proxy.py
- [[dot-block_credentials()_1]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[dot-filter_xml_blocks()_1]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[dot-sanitize()_1]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[128k token request at 4 bytestoken KV cache triggers rejection at 4096 MB…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[FIELDFLARE_API_BASE (TurboFieldfare 8238)]] - code - gateway/proxy/llm_proxy.py
- [[Fieldflare representable tool-schema subset (two-branch nullable unions only)]] - rationale - gateway/proxy/llm_proxy.py
- [[Fieldflare tool-schema flatten fix (skill_manage six-branch union 400)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Fieldflare unsupported-fields shim]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Remove OpenAI request fields TurboFieldfare rejects with HTTP 400, in place.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Return True if the response indicates a local-model OOM or backend_unavailable.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Rewrite a tool-parameter JSON schema into the subset Fieldflare's Gemma…]] - rationale - gateway/proxy/llm_proxy.py
- [[Single-branch unions unwrap, null-only unions are left alone, and a union…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Small context request passes VRAM headroom check.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Union several object schemas into one (see _flatten_fieldflare_schema).…]] - rationale - gateway/proxy/llm_proxy.py
- [[VRAM check is skipped when max_vram_headroom_mb=0 (disabled).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[VRAMHeadroomError must be a distinct exception, not a subclass of…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Workstream C — Full local-model parity for both bots. Tests that every cloud-…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_FakeSanitizer_1]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_anthropic_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_24]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_fake_forward()_25]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_secondary_model reads AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_secondary_model returns None if env var is unset.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom detects 'out of memory' in error message string.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom handles raw non-JSON bodies from some backends.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for cloud 429 quota errors (different failover…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for non-OOM raw 500 bodies.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns True for backend_unavailable 503 bodies.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_op()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_openai_tool_use_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_skill_manage_like_request()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[check_vram_headroom raises VRAMHeadroomError when estimated VRAM exceeds budget.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_collapses_type_list_to_one_concrete_type_plus_null()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_degenerate_unions()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_drops_parallel_tool_calls_true_and_false]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_inlines_allof_and_recurses_into_nested_nodes()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_is_noop_without_the_fields()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_keeps_first_branch_of_scalar_union()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_keeps_null_branch_when_merging()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_keeps_two_branch_nullable_union_unchanged()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_leaves_accepted_tool_choice_strings_alone()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_leaves_representable_tool_schemas_alone()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_merges_multi_branch_object_union_into_one_object()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_rewrites_named_tool_choice_object_to_auto]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_rewrites_required_tool_choice_to_auto]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_tolerates_malformed_tool_entries()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_secondary_model_reads_env()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_secondary_model_returns_none_when_unset()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_detects_backend_unavailable()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_detects_oom_in_error_message()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_handles_non_json_body()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_raw_body_false_on_normal_500()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_returns_false_for_quota_429()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_llm_proxy_local_parity.py]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_vram_headroom_error_is_not_resource_warning()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_llm_proxy_local_paritypy_2
SORT file.name ASC
```

## Connections to other communities
- 44 edges to [[_COMMUNITY_LLMProxy]]
- 32 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 4 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 3 edges to [[_COMMUNITY__FakeStreamResponse]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_SecureBrowser Skill (2)]]

## Top bridge nodes
- [[test_llm_proxy_local_parity.py]] - degree 79, connects to 5 communities
- [[dot-_is_local_oom()]] - degree 9, connects to 2 communities
- [[test_fieldflare_shim_drops_parallel_tool_calls_true_and_false]] - degree 4, connects to 2 communities
- [[test_fieldflare_shim_leaves_accepted_tool_choice_strings_alone()]] - degree 4, connects to 2 communities
- [[test_fieldflare_shim_rewrites_named_tool_choice_object_to_auto]] - degree 4, connects to 2 communities
