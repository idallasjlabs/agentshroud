---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "test_voice_stt_model_ab.py"
location: "L337-L404"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_voice_stt_model_abpy
---

# LLMProxy._local_secondary_failover_request

## Connections
- [[LLMProxy._forward_request]] - `calls` [EXTRACTED]
- [[LLMProxy._get_local_secondary_model]] - `calls` [EXTRACTED]
- [[LLMProxy._local_backend_headers]] - `calls` [EXTRACTED]
- [[LLMProxy._local_failover_base]] - `calls` [EXTRACTED]
- [[LLMProxy._normalize_local_model]] - `calls` [EXTRACTED]
- [[LLMProxy.proxy_messages (non-streaming)]] - `calls` [EXTRACTED]
- [[test_local_oom_triggers_secondary_failover]] - `references` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_voice_stt_model_abpy
