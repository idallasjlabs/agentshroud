---
type: community
cohesion: 0.23
members: 16
---

# gateway/tests/test_llm_proxy_thinking_suppression.py (8 cases)

**Cohesion:** 0.23 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-_suppress_qwen3_thinking()]] - code - gateway/proxy/llm_proxy.py
- [[Append 'no_think' to the last user message, in place, if not already present.…]] - rationale - gateway/proxy/llm_proxy.py
- [[LLM API Reverse Proxy — intercepts all OpenClaw ↔ (AnthropicOpenAIGoogle)…]] - rationale - gateway/proxy/llm_proxy.py
- [[Regression tests for LLMProxy._suppress_qwen3_thinking. 2026-10-16 incident…]] - rationale - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[_req()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[asyncio_2]] - code
- [[gatewayteststest_llm_proxy_thinking_suppression.py (8 cases)]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[llm_proxy.py_2]] - code - gateway/proxy/llm_proxy.py
- [[test_missing_model_treated_as_non_qwen()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_nemotron_alias_gets_reasoning_effort_none_and_text_untouched()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_nemotron_normalized_full_path_gets_reasoning_effort_none()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_non_qwen_caller_supplied_effort_is_overridden_to_none()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_non_qwen_reasoning_effort_already_none_is_noop()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_qwen_list_content_gets_suffix_on_last_text_part()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_qwen_model_gets_no_think_suffix()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_qwen_model_suffix_already_present_is_noop()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gateway/tests/test_llm_proxy_thinking_suppressionpy_8_cases
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_LLMProxy]]
- 2 edges to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_local_parity.py]]

## Top bridge nodes
- [[llm_proxy.py_2]] - degree 7, connects to 3 communities
- [[gatewayteststest_llm_proxy_thinking_suppression.py (8 cases)]] - degree 13, connects to 2 communities
- [[dot-_suppress_qwen3_thinking()]] - degree 12, connects to 1 community
- [[test_nemotron_alias_gets_reasoning_effort_none_and_text_untouched()]] - degree 4, connects to 1 community
- [[test_nemotron_normalized_full_path_gets_reasoning_effort_none()]] - degree 4, connects to 1 community
