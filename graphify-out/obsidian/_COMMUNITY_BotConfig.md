---
type: community
cohesion: 0.14
members: 25
---

# BotConfig

**Cohesion:** 0.14 - loosely connected
**Members:** 25 nodes

## Members
- [[Return a reason string if this Gemini request cannot be failed over.      Return]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Translate a Gemini generateContent request body to OpenAI chat format.      Retu]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Translate an OpenAI chatcompletions request body to Gemini's     generateConten]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[gemini_failover_unsupported_reason()]] - code - gateway/proxy/gemini_openai_translator.py
- [[gemini_to_openai_request()]] - code - gateway/proxy/gemini_openai_translator.py
- [[openai_to_gemini_request()]] - code - gateway/proxy/gemini_openai_translator.py
- [[test_gemini_basic_text_request()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_generation_config_top_p_and_stop_sequences()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_missing_role_defaults_to_user()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_missing_system_instruction_omits_system_message()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_multi_part_contents_joined()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_non_text_parts_skipped()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_openai_translator.py]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_role_mapping_model_to_assistant()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_system_instruction_snake_case_and_string()]] - code - gateway/tests/test_gemini_openai_translator.py
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
TABLE source_file, type FROM #community/BotConfig
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Post-v1.0.0 — Deferred]]
- 5 edges to [[_COMMUNITY_DELIVERABLE 3 — v0.8.0 Implementation Items]]
- 1 edge to [[_COMMUNITY_agentshroud-gateway service (proxy mode) (2)]]
- 1 edge to [[_COMMUNITY_TestFabricatedSecurityNotice]]

## Top bridge nodes
- [[test_gemini_openai_translator.py]] - degree 30, connects to 2 communities
- [[gemini_to_openai_request()]] - degree 14, connects to 2 communities
- [[openai_to_gemini_request()]] - degree 11, connects to 2 communities
- [[gemini_failover_unsupported_reason()]] - degree 7, connects to 1 community
