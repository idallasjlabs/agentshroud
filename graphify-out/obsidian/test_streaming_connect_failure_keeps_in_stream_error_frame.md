---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_llm_proxy.py"
location: "L905-L928"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# test_streaming_connect_failure_keeps_in_stream_error_frame

## Connections
- [[Backend-down stays an in-stream SSE error frame under a 200 head (unchanged…]] - `rationale_for` [EXTRACTED]
- [[LLMProxy]] - `uses` [INFERRED]
- [[LLMProxy.proxy_messages_streaming]] - `calls` [EXTRACTED]
- [[StreamHead]] - `uses` [INFERRED]
- [[_FakeSanitizer]] - `calls` [EXTRACTED]
- [[asyncio_2]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxypy
