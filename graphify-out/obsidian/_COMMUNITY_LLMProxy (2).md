---
type: community
members: 17
---

# LLMProxy (2)

**Members:** 17 nodes

## Members
- [[Local model defaults nemotron-3.5-lightning-rapid anchor, qwen3-coder coding, deepseek-r1 reasoning]] - concept - docker/docker-compose.yml
- [[Rapid-MLX host.docker.internal trusted-hosts fix (local-llms repo)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Regression tests for LLMProxy._suppress_qwen3_thinking. 2026-10-16 incident…]] - rationale - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[Root cause Nemotron in-band reasoning + Qwen-only no_think suffix]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[VT_AGENTS table (directhermesopenclaw)]] - code - firmware/voice-terminal/main/app_main.c
- [[Voice Interface (STTTTS, wake word)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[_req()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_llm_proxy_thinking_suppression.py]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_missing_model_treated_as_non_qwen()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_nemotron_alias_gets_reasoning_effort_none_and_text_untouched()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_nemotron_normalized_full_path_gets_reasoning_effort_none()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_non_qwen_caller_supplied_effort_is_overridden_to_none()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_non_qwen_reasoning_effort_already_none_is_noop()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_qwen_list_content_gets_suffix_on_last_text_part()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_qwen_model_gets_no_think_suffix()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[test_qwen_model_suffix_already_present_is_noop()]] - code - gateway/tests/test_llm_proxy_thinking_suppression.py
- [[voice-gateway service (ESP32-S3-BOX-3 STTTTS bridge, cpu_shares 4096, cpuset 0-3)]] - code - docker/docker-compose.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LLMProxy_2
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_local_parity.py (2)_1]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]

## Top bridge nodes
- [[test_llm_proxy_thinking_suppression.py]] - degree 12, connects to 1 community
- [[voice-gateway service (ESP32-S3-BOX-3 STTTTS bridge, cpu_shares 4096, cpuset 0-3)]] - degree 4, connects to 1 community
- [[Root cause Nemotron in-band reasoning + Qwen-only no_think suffix]] - degree 4, connects to 1 community
- [[Local model defaults nemotron-3.5-lightning-rapid anchor, qwen3-coder coding, deepseek-r1 reasoning]] - degree 3, connects to 1 community
