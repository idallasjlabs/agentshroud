---
type: community
members: 34
---

# Community 221

**Members:** 34 nodes

## Members
- [[A healthy 200 message body must NOT be failed over.]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[A real production incident a stalled chunked response from a local     model ba]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[Failover for a qwen3 local ref must dispatch to LM Studio (not Ollama,     which]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[HTTP 200 with an overloaded_error body must trigger local failover.]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[HTTP 529 with an overloaded_error body must trigger local failover.]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[LLMProxy_1]] - code - gateway/tests/test_llm_proxy_failover.py
- [[Same freeze, but on the HTTPError branch's e.read() — also moved off     the eve]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[Updated 2026-06-15 a plain 429 that escaped the upstream retry loop     NOW tri]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[Without the interactive flag the 3-retry loop is unchanged (guards the     herme]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[_call_proxy()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[make_proxy()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_already_local_request_does_not_failover()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_failover_notification_cooldown()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_failover_notification_distinguishes_translated_vs_not()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_failover_routes_qwen3_to_lm_studio_with_normalized_model()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_forward_request_default_still_retries_429()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_forward_request_interactive_header_skips_retries()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_forward_request_slow_http_error_read_does_not_block_event_loop()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_forward_request_slow_read_does_not_block_event_loop()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_llm_proxy_failover.py]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_per_request_opt_out_header_skips_failover()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_failover_anthropic_overloaded_529()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_failover_anthropic_overloaded_http200()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_failover_anthropic_quota_success()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_failover_flag_off_returns_429()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_failover_gemini_ollama_down_no_false_notice()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_failover_gemini_quota_success()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_failover_gemini_streaming_passthrough()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_failover_gemini_tools_passthrough()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_failover_ollama_unreachable_returns_original_429()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_failover_openai_quota_dropin()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_normal_200_passthrough_untouched()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[test_proxy_post_retry_429_now_failovers()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[x-agentshroud-interactive 1 → the first 429 returns immediately (no     2s4s8]] - rationale - gateway/tests/test_llm_proxy_failover.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_221
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 79]]
- 1 edge to [[_COMMUNITY_Community 38]]

## Top bridge nodes
- [[test_llm_proxy_failover.py]] - degree 25, connects to 2 communities
- [[make_proxy()]] - degree 24, connects to 1 community
- [[LLMProxy_1]] - degree 2, connects to 1 community