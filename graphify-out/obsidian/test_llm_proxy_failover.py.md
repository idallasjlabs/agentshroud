---
source_file: "gateway/tests/test_llm_proxy_failover.py"
type: "code"
community: "Architecture Docs"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Architecture_Docs
---

# test_llm_proxy_failover.py

## Connections
- [[LLMProxy]] - `imports` [EXTRACTED]
- [[_call_proxy()]] - `contains` [EXTRACTED]
- [[make_proxy()]] - `contains` [EXTRACTED]
- [[test_already_local_request_does_not_failover()]] - `contains` [EXTRACTED]
- [[test_failover_notification_cooldown()]] - `contains` [EXTRACTED]
- [[test_failover_notification_distinguishes_translated_vs_not()]] - `contains` [EXTRACTED]
- [[test_failover_routes_qwen3_to_lm_studio_with_normalized_model()]] - `contains` [EXTRACTED]
- [[test_forward_request_default_still_retries_429()]] - `contains` [EXTRACTED]
- [[test_forward_request_interactive_header_skips_retries()]] - `contains` [EXTRACTED]
- [[test_per_request_opt_out_header_skips_failover()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_anthropic_overloaded_529()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_anthropic_overloaded_http200()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_anthropic_quota_success()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_flag_off_returns_429()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_gemini_ollama_down_no_false_notice()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_gemini_quota_success()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_gemini_streaming_passthrough()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_gemini_tools_passthrough()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_ollama_unreachable_returns_original_429()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_openai_quota_dropin()]] - `contains` [EXTRACTED]
- [[test_proxy_normal_200_passthrough_untouched()]] - `contains` [EXTRACTED]
- [[test_proxy_post_retry_429_now_failovers()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Architecture_Docs