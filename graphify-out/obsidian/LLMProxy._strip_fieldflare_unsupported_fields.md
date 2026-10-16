---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "test_llm_proxy_local_parity.py"
location: "L550-L575"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxy_local_paritypy
---

# LLMProxy._strip_fieldflare_unsupported_fields

## Connections
- [[LLMProxy._suppress_qwen3_thinking]] - `semantically_similar_to` [INFERRED]
- [[LLMProxy._widen_optional_tool_param_types]] - `semantically_similar_to` [INFERRED]
- [[LLMProxy.proxy_messages (non-streaming)]] - `calls` [EXTRACTED]
- [[LLMProxy.proxy_messages_streaming]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_drops_parallel_tool_calls_true_and_false]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_rewrites_named_tool_choice_object_to_auto]] - `calls` [EXTRACTED]
- [[test_fieldflare_shim_rewrites_required_tool_choice_to_auto]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxy_local_paritypy
