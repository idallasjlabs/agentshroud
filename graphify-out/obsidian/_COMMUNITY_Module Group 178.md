---
type: community
cohesion: 0.13
members: 27
---

# Module Group 178

**Cohesion:** 0.13 - loosely connected
**Members:** 27 nodes

## Members
- [[Extract the system instruction as plain text (camelCase or snake_case key).]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Flatten a Gemini parts list to plain text (text parts only).]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Return a reason string if this Gemini request cannot be failed over.      Return]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Translate a Gemini generateContent request body to OpenAI chat format.      Retu]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Translate an Ollama OpenAI-compat response to Gemini candidates format.      The]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[_parts_to_text()]] - code - gateway/proxy/gemini_openai_translator.py
- [[_system_instruction_text()]] - code - gateway/proxy/gemini_openai_translator.py
- [[gemini_failover_unsupported_reason()]] - code - gateway/proxy/gemini_openai_translator.py
- [[gemini_openai_translator.py]] - code - gateway/proxy/gemini_openai_translator.py
- [[gemini_to_openai_request()]] - code - gateway/proxy/gemini_openai_translator.py
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
- [[test_openai_response_empty_choices_yields_empty_text()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_response_length_maps_to_max_tokens()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_openai_response_to_gemini_candidates()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_unsupported_reason_function_call_parts()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_unsupported_reason_none_for_plain_text()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_unsupported_reason_streaming_path()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_unsupported_reason_tools_in_body()]] - code - gateway/tests/test_gemini_openai_translator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_178
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 151]]
- 3 edges to [[_COMMUNITY_Module Group 101]]

## Top bridge nodes
- [[gemini_to_openai_request()]] - degree 15, connects to 2 communities
- [[gemini_failover_unsupported_reason()]] - degree 10, connects to 2 communities
- [[openai_to_gemini_response()]] - degree 8, connects to 2 communities