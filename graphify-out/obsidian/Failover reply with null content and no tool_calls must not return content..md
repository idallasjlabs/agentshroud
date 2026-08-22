---
source_file: "gateway/tests/test_anthropic_openai_translator.py"
type: "rationale"
community: "Anthropic Openai Translator"
location: "L290"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Anthropic_Openai_Translator
---

# Failover reply with null content and no tool_calls must not return content:[].

## Connections
- [[test_translator_null_content_no_tool_calls_yields_nonempty_content()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Anthropic_Openai_Translator