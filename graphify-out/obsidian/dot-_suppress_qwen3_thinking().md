---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "LLMProxy"
location: "L448"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxy
---

# ._suppress_qwen3_thinking()

## Connections
- [[dot-proxy_messages()]] - `calls` [EXTRACTED]
- [[dot-proxy_messages_streaming()]] - `calls` [EXTRACTED]
- [[Append 'no_think' to the last user message, in place, if not already present.…]] - `rationale_for` [EXTRACTED]
- [[LLMProxy]] - `method` [EXTRACTED]
- [[Nemotron + Qwen-only no_think suffix root cause]] - `rationale_for` [EXTRACTED]
- [[test_missing_model_treated_as_non_qwen()]] - `calls` [EXTRACTED]
- [[test_nemotron_alias_gets_reasoning_effort_none_and_text_untouched()]] - `calls` [EXTRACTED]
- [[test_nemotron_normalized_full_path_gets_reasoning_effort_none()]] - `calls` [EXTRACTED]
- [[test_non_qwen_caller_supplied_effort_is_overridden_to_none()]] - `calls` [EXTRACTED]
- [[test_non_qwen_reasoning_effort_already_none_is_noop()]] - `calls` [EXTRACTED]
- [[test_qwen_list_content_gets_suffix_on_last_text_part()]] - `calls` [EXTRACTED]
- [[test_qwen_model_gets_no_think_suffix()]] - `calls` [EXTRACTED]
- [[test_qwen_model_suffix_already_present_is_noop()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxy
