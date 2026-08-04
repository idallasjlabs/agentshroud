---
source_file: "gateway/tests/test_llm_proxy_failover.py"
type: "code"
community: "Module Group 183"
location: "L46"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Module_Group_183
---

# make_proxy()

## Connections
- [[LLMProxy_1]] - `references` [EXTRACTED]
- [[LLMProxy]] - `calls` [EXTRACTED]
- [[test_already_local_request_does_not_failover()]] - `calls` [EXTRACTED]
- [[test_failover_notification_cooldown()]] - `calls` [EXTRACTED]
- [[test_failover_notification_distinguishes_translated_vs_not()]] - `calls` [EXTRACTED]
- [[test_failover_routes_qwen3_to_lm_studio_with_normalized_model()]] - `calls` [EXTRACTED]
- [[test_llm_proxy_failover.py]] - `contains` [EXTRACTED]
- [[test_per_request_opt_out_header_skips_failover()]] - `calls` [EXTRACTED]
- [[test_proxy_failover_anthropic_overloaded_529()]] - `calls` [EXTRACTED]
- [[test_proxy_failover_anthropic_overloaded_http200()]] - `calls` [EXTRACTED]
- [[test_proxy_failover_anthropic_quota_success()]] - `calls` [EXTRACTED]
- [[test_proxy_failover_flag_off_returns_429()]] - `calls` [EXTRACTED]
- [[test_proxy_failover_gemini_ollama_down_no_false_notice()]] - `calls` [EXTRACTED]
- [[test_proxy_failover_gemini_quota_success()]] - `calls` [EXTRACTED]
- [[test_proxy_failover_gemini_streaming_passthrough()]] - `calls` [EXTRACTED]
- [[test_proxy_failover_gemini_tools_passthrough()]] - `calls` [EXTRACTED]
- [[test_proxy_failover_ollama_unreachable_returns_original_429()]] - `calls` [EXTRACTED]
- [[test_proxy_failover_openai_quota_dropin()]] - `calls` [EXTRACTED]
- [[test_proxy_normal_200_passthrough_untouched()]] - `calls` [EXTRACTED]
- [[test_proxy_post_retry_429_now_failovers()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Module_Group_183
