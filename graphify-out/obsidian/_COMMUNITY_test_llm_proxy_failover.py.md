---
type: community
members: 62
---

# test_llm_proxy_failover.py

**Members:** 62 nodes

## Members
- [[A healthy 200 message body must NOT be failed over.]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[A real production incident a stalled chunked response from a local model…]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[Failover for a qwen3 local ref must dispatch to LM Studio (not Ollama, which…]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[HTTP 200 with an overloaded_error body must trigger local failover.]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[HTTP 529 with an overloaded_error body must trigger local failover.]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[Same freeze, but on the HTTPError branch's e.read() — also moved off the event…]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[Tests for the cloud→local quota failover orchestrator in LLMProxy.]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[Updated 2026-06-15 a plain 429 that escaped the upstream retry loop NOW…]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[Without the interactive flag the 3-retry loop is unchanged (guards the hermes-…]] - rationale - gateway/tests/test_llm_proxy_failover.py
- [[_call_proxy()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[_no_sleep()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[_slow_read()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[asyncio_20]] - code
- [[canary()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[canary()_1]] - code - gateway/tests/test_llm_proxy_failover.py
- [[close()_1]] - code - gateway/tests/test_llm_proxy_failover.py
- [[fake_urlopen()_16]] - code - gateway/tests/test_llm_proxy_failover.py
- [[fake_urlopen()_17]] - code - gateway/tests/test_llm_proxy_failover.py
- [[fake_urlopen()_18]] - code - gateway/tests/test_llm_proxy_failover.py
- [[fake_urlopen()_19]] - code - gateway/tests/test_llm_proxy_failover.py
- [[make_proxy()_1]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_1]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_2]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_3]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_4]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_5]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_6]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_7]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_8]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_9]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_10]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_11]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_12]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_13]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_14]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_forward()_15]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_urlopen()]] - code - gateway/tests/test_llm_proxy_failover.py
- [[mock_urlopen()_1]] - code - gateway/tests/test_llm_proxy_failover.py
- [[read()_1]] - code - gateway/tests/test_llm_proxy_failover.py
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
- [[x-agentshroud-interactive 1 → the first 429 returns immediately (no 2s4s8s…]] - rationale - gateway/tests/test_llm_proxy_failover.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_llm_proxy_failoverpy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_test_anthropic_openai_translator.py]]

## Top bridge nodes
- [[test_llm_proxy_failover.py]] - degree 27, connects to 2 communities
- [[make_proxy()_1]] - degree 23, connects to 1 community
