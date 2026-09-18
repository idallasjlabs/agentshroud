---
type: community
cohesion: 0.06
members: 63
---

# LLMProxy

**Cohesion:** 0.06 - loosely connected
**Members:** 63 nodes

## Members
- [[.__init__()_204]] - code - gateway/proxy/llm_proxy.py
- [[.__init__()_208]] - code - gateway/tests/test_llm_proxy.py
- [[.__init__()_207]] - code - gateway/tests/test_llm_proxy.py
- [[.block_credentials()_3]] - code - gateway/tests/test_llm_proxy.py
- [[.can_use_tool()_3]] - code - gateway/tests/test_llm_proxy.py
- [[.filter_xml_blocks()_3]] - code - gateway/tests/test_llm_proxy.py
- [[.get_stats()_20]] - code - gateway/proxy/llm_proxy.py
- [[.inject_headers()_2]] - code - gateway/tests/test_llm_proxy.py
- [[.sanitize()_5]] - code - gateway/tests/test_llm_proxy.py
- [[A known secret value echoed in a streaming delta must be scrubbed.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Anthropic-bound request with x-api-key injector injects Bearer + beta, strips x]] - rationale - gateway/tests/test_llm_proxy.py
- [[Connect failures to cloud providers keep the existing 502 behavior.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Connect timeout must exceed this host's measured DNS-resolution latency     (~4.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Events from 'unknown' user_id must not be blocked (not authenticated).]] - rationale - gateway/tests/test_llm_proxy.py
- [[LLMProxy_2]] - code - gateway/proxy/llm_proxy.py
- [[LM Studio down → 503 backend_unavailable with LM Studio hint.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Localnon-Anthropic destination injector must NOT be called.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Minimal ToolACLEnforcer stub that denies a named tool.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Ollama down → 503 backend_unavailable with ollama serve hint.]] - rationale - gateway/tests/test_llm_proxy.py
- [[OpenClaw already sends Authorization Bearer — injector must leave it untouched.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Proxies LLM API calls (Anthropic, OpenAI, Google) through the security pipeline.]] - rationale - gateway/proxy/llm_proxy.py
- [[Regression 2026-08-07 a plain (non-Claude, non-Gemini, non-local)     OpenAI-mo]] - rationale - gateway/tests/test_llm_proxy.py
- [[Regression 2026-09-16 openai-local is AgentShroud's own local-model     prov]] - rationale - gateway/tests/test_llm_proxy.py
- [[Repeated connect failures log one WARNING per window, not per request.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Return a monkeypatched urlopen that captures the Request headers.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Same regression as test_proxy_messages_strips_openai_local_prefix_and_routes_to_]] - rationale - gateway/tests/test_llm_proxy.py
- [[Streaming Anthropic request triggers inject_headers before httpx connects.]] - rationale - gateway/tests/test_llm_proxy.py
- [[_FakeSanitizer_2]] - code - gateway/tests/test_llm_proxy.py
- [[_FakeToolACL_1]] - code - gateway/tests/test_llm_proxy.py
- [[_TrackingInjector_1]] - code - gateway/tests/test_llm_proxy.py
- [[_is_connect_error matches connection-level failures only.]] - rationale - gateway/tests/test_llm_proxy.py
- [[_make_fake_urlopen()_1]] - code - gateway/tests/test_llm_proxy.py
- [[_proxy_with_connect_refused()_1]] - code - gateway/tests/test_llm_proxy.py
- [[content_block_start with terminal_tool must be replaced with a text error block.]] - rationale - gateway/tests/test_llm_proxy.py
- [[llm_proxy.py_2]] - code - gateway/proxy/llm_proxy.py
- [[mlx_lm down (connection refused) → 503 backend_unavailable with start hint.]] - rationale - gateway/tests/test_llm_proxy.py
- [[test_backend_unavailable_warning_rate_limited()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_cloud_backend_connect_failure_still_returns_502()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_called_in_streaming_path()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_does_not_overwrite_existing_bearer()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_not_applied_for_non_anthropic_dest()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_filter_outbound_streaming_filters_anthropic_content_text()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_filter_outbound_streaming_filters_openai_delta_content()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_is_connect_error_classification()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_llm_connect_timeout_clears_observed_dns_latency()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_llm_proxy.py_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_lmstudio_connect_failure_returns_structured_503()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_mlxlm_connect_failure_returns_structured_503()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_ollama_connect_failure_returns_structured_503()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_plain_openai_model_substitutes_real_key()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_rewrites_claude_opus_to_local_model()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_streaming_strips_openai_local_prefix_and_routes_to_backend()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_strips_ollama_prefix_for_openai_compat()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_strips_openai_local_prefix_and_routes_to_backend()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_timeout_returns_anthropic_compatible_fallback()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_timeout_returns_openai_compatible_fallback()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_scan_request_data_scans_messages_without_name_error()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_secret_value_redacted()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_tool_acl_allows_permitted_tool()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_tool_acl_blocks_terminal_tool()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_tool_acl_skips_unknown_user()_1]] - code - gateway/tests/test_llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LLMProxy
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_.proxy_messages()]]
- 16 edges to [[_COMMUNITY_test_llm_proxy.py]]
- 4 edges to [[_COMMUNITY_._filter_streaming_event()]]
- 2 edges to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_gateway.proxy.llm_proxy]]
- 1 edge to [[_COMMUNITY_._is_local_oom()]]
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]

## Top bridge nodes
- [[LLMProxy_2]] - degree 55, connects to 3 communities
- [[test_llm_proxy.py_1]] - degree 36, connects to 3 communities
- [[_TrackingInjector_1]] - degree 9, connects to 1 community
- [[test_streaming_tool_acl_allows_permitted_tool()_1]] - degree 5, connects to 1 community
- [[Proxies LLM API calls (Anthropic, OpenAI, Google) through the security pipeline.]] - degree 2, connects to 1 community