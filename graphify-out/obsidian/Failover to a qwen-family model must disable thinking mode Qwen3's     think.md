---
source_file: "gateway/tests/test_anthropic_openai_translator.py"
type: "rationale"
community: "Anthropic Openai Translator"
location: "L340"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Anthropic_Openai_Translator
---

# Failover to a qwen-family model must disable thinking mode: Qwen3's     <think>

## Connections
- [[test_translator_qwen_target_injects_no_think()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Anthropic_Openai_Translator