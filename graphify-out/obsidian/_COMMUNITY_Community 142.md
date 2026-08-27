---
type: community
members: 44
---

# Community 142

**Members:** 44 nodes

## Members
- [[Extract the system instruction as plain text (camelCase or snake_case key).]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Flatten a Gemini parts list to plain text (text parts only).]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Flatten an OpenAI message's content (string or content-block list) to     Gemini]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Return a reason string if this Gemini request cannot be failed over.      Return]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Translate a Gemini generateContent request body to OpenAI chat format.      Retu]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Translate a Gemini generateContent response to OpenAI chatcompletions     shape]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Translate an Ollama OpenAI-compat response to Gemini candidates format.      The]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Translate an OpenAI chatcompletions request body to Gemini's     generateConten]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[_openai_content_to_parts()]] - code - gateway/proxy/gemini_openai_translator.py
- [[_parts_to_text()]] - code - gateway/proxy/gemini_openai_translator.py
- [[_system_instruction_text()]] - code - gateway/proxy/gemini_openai_translator.py
- [[gemini_failover_unsupported_reason()]] - code - gateway/proxy/gemini_openai_translator.py
- [[gemini_openai_translator.py]] - code - gateway/proxy/gemini_openai_translator.py
- [[gemini_to_openai_request()]] - code - gateway/proxy/gemini_openai_translator.py
- [[gemini_to_openai_response()]] - code - gateway/proxy/gemini_openai_translator.py
- [[openai_to_gemini_request()]] - code - gateway/proxy/gemini_openai_translator.py
- [[openai_to_gemini_response (existing failover direction) and     gemini_to_openai]] - rationale - gateway/tests/test_gemini_openai_translator.py
- [[openai_to_gemini_response()]] - code - gateway/proxy/gemini_openai_translator.py
- [[test_gemini_basic_text_request()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_generation_config_top_p_and_stop_sequences()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_missing_role_defaults_to_user()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_missing_system_instruction_omits_system_message()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_multi_part_contents_joined()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_non_text_parts_skipped()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_openai_translator.py]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_role_mapping_model_to_assistant()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_system_instruction_snake_case_and_string()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_to_openai_response_empty_candidates_yields_empty_text()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_to_openai_response_envelope()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_to_openai_response_max_tokens_finish_reason()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_to_openai_roundtrip_with_openai_to_gemini_response()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_response_empty_choices_yields_empty_text()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_response_length_maps_to_max_tokens()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_response_to_gemini_candidates()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_to_gemini_assistant_role_becomes_model()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_to_gemini_basic_request()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_to_gemini_content_block_list_flattened()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_to_gemini_no_generation_config_keys_omits_block()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_to_gemini_no_system_message_omits_system_instruction()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_to_gemini_stop_sequences_normalized_to_list()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_unsupported_reason_function_call_parts()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_unsupported_reason_none_for_plain_text()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_unsupported_reason_streaming_path()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_unsupported_reason_tools_in_body()]] - code - gateway/tests/test_gemini_openai_translator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_142
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 126]]
- 6 edges to [[_COMMUNITY_Community 108]]
- 1 edge to [[_COMMUNITY_Community 117]]

## Top bridge nodes
- [[openai_to_gemini_request()]] - degree 13, connects to 3 communities
- [[gemini_to_openai_request()]] - degree 16, connects to 2 communities
- [[gemini_failover_unsupported_reason()]] - degree 10, connects to 2 communities
- [[gemini_to_openai_response()]] - degree 10, connects to 2 communities
- [[openai_to_gemini_response()]] - degree 10, connects to 2 communities