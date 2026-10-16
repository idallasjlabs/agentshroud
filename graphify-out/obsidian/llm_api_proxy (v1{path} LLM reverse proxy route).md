---
source_file: "gateway/ingest_api/main.py"
type: "code"
community: "LLMProxy.proxy_messages (non-streaming)"
location: "L4319-L4449"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxyproxy_messages_non-streaming
---

# llm_api_proxy (/v1/{path} LLM reverse proxy route)

## Connections
- [[LLMProxy.proxy_messages (non-streaming)]] - `calls` [EXTRACTED]
- [[LLMProxy.proxy_messages_streaming]] - `calls` [EXTRACTED]
- [[Proxy Anthropic API calls through security pipeline.]] - `rationale_for` [EXTRACTED]
- [[Request]] - `references` [EXTRACTED]
- [[StreamHead]] - `shares_data_with` [EXTRACTED]
- [[Streaming route masked upstream 4xx as 200 event stream]] - `rationale_for` [EXTRACTED]
- [[TestStreamingProxyStatusPropagation]] - `calls` [INFERRED]
- [[api_route]] - `references` [EXTRACTED]
- [[cmd_start]] - `references` [AMBIGUOUS]
- [[cmd_up]] - `references` [INFERRED]
- [[google_api_proxy]] - `semantically_similar_to` [INFERRED]
- [[ingest_apimain.py]] - `contains` [EXTRACTED]
- [[llm_api_v1_prefix_alias]] - `calls` [EXTRACTED]
- [[llm_openai_chat_alias]] - `calls` [EXTRACTED]
- [[telegram_api_proxy (telegram-api{path})]] - `semantically_similar_to` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/LLMProxyproxy_messages_non-streaming
