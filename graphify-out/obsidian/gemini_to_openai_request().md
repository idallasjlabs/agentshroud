---
source_file: "gateway/proxy/gemini_openai_translator.py"
type: "code"
community: "Community 142"
location: "L98"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_142
---

# gemini_to_openai_request()

## Connections
- [[._failover_request()]] - `calls` [EXTRACTED]
- [[Translate a Gemini generateContent request body to OpenAI chat format.      Retu]] - `rationale_for` [EXTRACTED]
- [[_parts_to_text()]] - `calls` [EXTRACTED]
- [[_system_instruction_text()]] - `calls` [EXTRACTED]
- [[anthropic_to_openai_request()]] - `semantically_similar_to` [INFERRED]
- [[gemini_openai_translator.py]] - `contains` [EXTRACTED]
- [[llm_proxy.py]] - `imports` [EXTRACTED]
- [[test_gemini_basic_text_request()]] - `calls` [EXTRACTED]
- [[test_gemini_generation_config_top_p_and_stop_sequences()]] - `calls` [EXTRACTED]
- [[test_gemini_missing_role_defaults_to_user()]] - `calls` [EXTRACTED]
- [[test_gemini_missing_system_instruction_omits_system_message()]] - `calls` [EXTRACTED]
- [[test_gemini_multi_part_contents_joined()]] - `calls` [EXTRACTED]
- [[test_gemini_non_text_parts_skipped()]] - `calls` [EXTRACTED]
- [[test_gemini_openai_translator.py]] - `imports` [EXTRACTED]
- [[test_gemini_role_mapping_model_to_assistant()]] - `calls` [EXTRACTED]
- [[test_gemini_system_instruction_snake_case_and_string()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_142