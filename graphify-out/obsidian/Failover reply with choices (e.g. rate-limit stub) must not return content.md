---
source_file: "gateway/tests/test_anthropic_openai_translator.py"
type: "rationale"
community: "test_anthropic_openai_translator.py"
location: "L311"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_anthropic_openai_translatorpy
---

# Failover reply with choices:[] (e.g. rate-limit stub) must not return content:[]

## Connections
- [[test_translator_empty_choices_yields_nonempty_content()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_anthropic_openai_translatorpy