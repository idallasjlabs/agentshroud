---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "ModeRequest"
location: "L551"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ModeRequest
---

# ._strip_fieldflare_unsupported_fields()

## Connections
- [[dot-_flatten_fieldflare_schema()]] - `calls` [EXTRACTED]
- [[dot-proxy_messages()]] - `calls` [EXTRACTED]
- [[dot-proxy_messages_streaming()]] - `calls` [EXTRACTED]
- [[FIELDFLARE_API_BASE (TurboFieldfare 8238)]] - `shares_data_with` [INFERRED]
- [[LLMProxy]] - `method` [EXTRACTED]
- [[Remove OpenAI request fields TurboFieldfare rejects with HTTP 400, in place.…]] - `rationale_for` [EXTRACTED]
- [[test_fieldflare_shim_collapses_type_list_to_one_concrete_type_plus_null()]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_degenerate_unions()]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_drops_parallel_tool_calls_true_and_false]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_inlines_allof_and_recurses_into_nested_nodes()]] - `calls` [INFERRED]
- [[test_fieldflare_shim_is_noop_without_the_fields()]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_keeps_first_branch_of_scalar_union()]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_keeps_null_branch_when_merging()]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_keeps_two_branch_nullable_union_unchanged()]] - `calls` [INFERRED]
- [[test_fieldflare_shim_leaves_accepted_tool_choice_strings_alone()]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_leaves_representable_tool_schemas_alone()]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_merges_multi_branch_object_union_into_one_object()]] - `calls` [INFERRED]
- [[test_fieldflare_shim_rewrites_named_tool_choice_object_to_auto]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_rewrites_required_tool_choice_to_auto]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_tolerates_malformed_tool_entries()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ModeRequest
