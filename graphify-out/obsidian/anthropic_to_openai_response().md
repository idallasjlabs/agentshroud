---
source_file: "gateway/proxy/anthropic_openai_translator.py"
type: "code"
community: "AgentShroud Security Hardening Plan"
location: "L291"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentShroud_Security_Hardening_Plan
---

# anthropic_to_openai_response()

## Connections
- [[.proxy_messages()]] - `calls` [EXTRACTED]
- [[Anthropic v1messages response → OpenAI v1chatcompletions envelope.]] - `rationale_for` [EXTRACTED]
- [[LLMProxy.proxy_messages]] - `calls` [EXTRACTED]
- [[_random_msg_id()_1]] - `calls` [EXTRACTED]
- [[anthropic_openai_translator.py]] - `contains` [EXTRACTED]
- [[llm_proxy.py]] - `imports` [EXTRACTED]
- [[test_anthropic_to_openai_response_envelope()]] - `calls` [EXTRACTED]
- [[test_claude_via_openai_path.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AgentShroud_Security_Hardening_Plan