---
source_file: "gateway/proxy/anthropic_openai_translator.py"
type: "rationale"
community: "AgentShroud Security Hardening Plan"
location: "L292"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AgentShroud_Security_Hardening_Plan
---

# Anthropic /v1/messages response → OpenAI /v1/chat/completions envelope.

## Connections
- [[anthropic_to_openai_response()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AgentShroud_Security_Hardening_Plan