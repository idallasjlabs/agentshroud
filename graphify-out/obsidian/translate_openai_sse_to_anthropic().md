---
source_file: "gateway/proxy/anthropic_openai_sse_translator.py"
type: "code"
community: "translate_openai_sse_to_anthropic()"
location: "L52"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/translate_openai_sse_to_anthropic
---

# translate_openai_sse_to_anthropic()

## Connections
- [[LLMProxy.proxy_messages_streaming]] - `calls` [EXTRACTED]
- [[Translate an OpenAI-compat SSE byte stream to Anthropic SSE byte events.      Yi]] - `rationale_for` [EXTRACTED]
- [[_collect_sse()]] - `calls` [EXTRACTED]
- [[_random_msg_id()]] - `calls` [EXTRACTED]
- [[_sse()]] - `calls` [EXTRACTED]
- [[anthropic_openai_sse_translator.py]] - `contains` [EXTRACTED]
- [[test_anthropic_openai_translator.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/translate_openai_sse_to_anthropic