---
source_file: "gateway/proxy/anthropic_openai_translator.py"
type: "rationale"
community: "test_claude_via_openai_path.py"
location: "L292"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_claude_via_openai_pathpy
---

# Anthropic /v1/messages response → OpenAI /v1/chat/completions envelope.

## Connections
- [[anthropic_to_openai_response()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_claude_via_openai_pathpy