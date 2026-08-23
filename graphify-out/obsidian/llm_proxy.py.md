---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "Anthropic Openai Translator"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Anthropic_Openai_Translator
---

# llm_proxy.py

## Connections
- [[AGENTS_1]] - `conceptually_related_to` [INFERRED]
- [[ANTHROPIC_BASE_URL]] - `references` [INFERRED]
- [[CONTINUE-2026-08-17]] - `references` [EXTRACTED]
- [[LLMProxy]] - `contains` [EXTRACTED]
- [[anthropic_to_openai_request()]] - `imports` [EXTRACTED]
- [[anthropic_to_openai_response()]] - `imports` [EXTRACTED]
- [[egress_retry.py]] - `semantically_similar_to` [INFERRED]
- [[gemini_failover_unsupported_reason()]] - `imports` [EXTRACTED]
- [[gemini_to_openai_request()]] - `imports` [EXTRACTED]
- [[gemini_to_openai_response()]] - `imports` [EXTRACTED]
- [[is_overloaded()]] - `imports` [EXTRACTED]
- [[is_quota_exhausted()]] - `imports` [EXTRACTED]
- [[is_rate_limited_post_retry()]] - `imports` [EXTRACTED]
- [[openai_to_anthropic_request()]] - `imports` [EXTRACTED]
- [[openai_to_anthropic_response()]] - `imports` [EXTRACTED]
- [[openai_to_gemini_request()]] - `imports` [EXTRACTED]
- [[openai_to_gemini_response()]] - `imports` [EXTRACTED]
- [[resolve_model.py]] - `shares_data_with` [EXTRACTED]
- [[switch_model.sh]] - `references` [EXTRACTED]
- [[telegram_proxy.py]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `imports_from` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `imports_from` [EXTRACTED]
- [[translate_openai_sse_to_anthropic()]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Anthropic_Openai_Translator