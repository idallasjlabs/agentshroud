---
source_file: "gateway/tests/test_anthropic_openai_translator.py"
type: "rationale"
community: "Anthropic Openai Translator"
location: "L301"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Anthropic_Openai_Translator
---

# Failover reply with empty-string content must not return content:[].

## Connections
- [[test_translator_empty_string_content_yields_nonempty_content()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Anthropic_Openai_Translator