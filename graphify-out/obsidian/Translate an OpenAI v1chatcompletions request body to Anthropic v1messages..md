---
source_file: "gateway/proxy/anthropic_openai_translator.py"
type: "rationale"
community: "AgentShroud Security Hardening Plan"
location: "L242"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AgentShroud_Security_Hardening_Plan
---

# Translate an OpenAI /v1/chat/completions request body to Anthropic /v1/messages.

## Connections
- [[openai_to_anthropic_request()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AgentShroud_Security_Hardening_Plan