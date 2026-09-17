---
type: community
cohesion: 0.06
members: 62
---

# test_llm_proxy.py

**Cohesion:** 0.06 - loosely connected
**Members:** 62 nodes

## Members
- [[.__init__()_5]] - code - gateway/tests/test_llm_proxy.py
- [[.__init__()_6]] - code - gateway/tests/test_llm_proxy.py
- [[.block_credentials()_1]] - code - gateway/tests/test_llm_proxy.py
- [[.can_use_tool()]] - code - gateway/tests/test_llm_proxy.py
- [[.filter_xml_blocks()_1]] - code - gateway/tests/test_llm_proxy.py
- [[.inject_headers()_1]] - code - gateway/tests/test_llm_proxy.py
- [[.sanitize()_1]] - code - gateway/tests/test_llm_proxy.py
- [[Allowed tool blocks must pass through unchanged.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Anthropic-bound request with x-api-key injector injects Bearer + beta, strips…]] - rationale - gateway/tests/test_llm_proxy.py
- [[Connect timeout must exceed this host's measured DNS-resolution latency…]] - rationale - gateway/tests/test_llm_proxy.py
- [[Fake CredentialInjector that records inject_headers calls and applies Anthropic]] - rationale - gateway/tests/test_llm_proxy.py
- [[No streaming call site may hardcode its own connect timeout literal.      Guards]] - rationale - gateway/tests/test_llm_proxy.py
- [[Regression 2026-08-07 a plain (non-Claude, non-Gemini, non-local) OpenAI-model…]] - rationale - gateway/tests/test_llm_proxy.py
- [[Regression 2026-09-16 openai-local is AgentShroud's own local-model…]] - rationale - gateway/tests/test_llm_proxy.py
- [[Same regression as…]] - rationale - gateway/tests/test_llm_proxy.py
- [[_FakeSanitizer_1]] - code - gateway/tests/test_llm_proxy.py
- [[_FakeToolACL]] - code - gateway/tests/test_llm_proxy.py
- [[_TrackingInjector]] - code - gateway/tests/test_llm_proxy.py
- [[_fake_forward()_17]] - code - gateway/tests/test_llm_proxy.py
- [[_fake_forward()_18]] - code - gateway/tests/test_llm_proxy.py
- [[_fake_forward()_19]] - code - gateway/tests/test_llm_proxy.py
- [[_fake_forward()_20]] - code - gateway/tests/test_llm_proxy.py
- [[_fake_forward()_21]] - code - gateway/tests/test_llm_proxy.py
- [[_fake_forward()_22]] - code - gateway/tests/test_llm_proxy.py
- [[_fake_forward()_23]] - code - gateway/tests/test_llm_proxy.py
- [[_make_fake_urlopen()]] - code - gateway/tests/test_llm_proxy.py
- [[_proxy_with_connect_refused()]] - code - gateway/tests/test_llm_proxy.py
- [[asyncio_3]] - code
- [[block_credentials()]] - code - gateway/tests/test_llm_proxy.py
- [[fake_open()]] - code - gateway/tests/test_llm_proxy.py
- [[fake_urlopen()]] - code - gateway/tests/test_llm_proxy.py
- [[mock_forward()]] - code - gateway/tests/test_llm_proxy.py
- [[mock_forward()_1]] - code - gateway/tests/test_llm_proxy.py
- [[mock_forward()_2]] - code - gateway/tests/test_llm_proxy.py
- [[test_all_streaming_clients_use_the_shared_connect_timeout_constant()]] - code - gateway/tests/test_llm_proxy.py
- [[test_all_streaming_clients_use_the_shared_connect_timeout_constant()_1]] - code - gateway/tests/test_llm_proxy.py
- [[test_backend_unavailable_warning_rate_limited()]] - code - gateway/tests/test_llm_proxy.py
- [[test_cloud_backend_connect_failure_still_returns_502()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_called_in_streaming_path()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_does_not_overwrite_existing_bearer()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_not_applied_for_non_anthropic_dest()]] - code - gateway/tests/test_llm_proxy.py
- [[test_filter_outbound_streaming_filters_anthropic_content_text()]] - code - gateway/tests/test_llm_proxy.py
- [[test_filter_outbound_streaming_filters_openai_delta_content()]] - code - gateway/tests/test_llm_proxy.py
- [[test_llm_connect_timeout_clears_observed_dns_latency()]] - code - gateway/tests/test_llm_proxy.py
- [[test_llm_proxy.py]] - code - gateway/tests/test_llm_proxy.py
- [[test_lmstudio_connect_failure_returns_structured_503()]] - code - gateway/tests/test_llm_proxy.py
- [[test_mlxlm_connect_failure_returns_structured_503()]] - code - gateway/tests/test_llm_proxy.py
- [[test_ollama_connect_failure_returns_structured_503()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_plain_openai_model_substitutes_real_key()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_rewrites_claude_opus_to_local_model()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_streaming_strips_openai_local_prefix_and_routes_to_backend()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_strips_ollama_prefix_for_openai_compat()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_strips_openai_local_prefix_and_routes_to_backend()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_timeout_returns_anthropic_compatible_fallback()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_timeout_returns_openai_compatible_fallback()]] - code - gateway/tests/test_llm_proxy.py
- [[test_scan_request_data_scans_messages_without_name_error()]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_secret_value_redacted()]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_tool_acl_allows_permitted_tool()]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_tool_acl_blocks_terminal_tool()]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_tool_acl_skips_unknown_user()]] - code - gateway/tests/test_llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_llm_proxypy
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_LLMProxy]]
- 16 edges to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_gateway.proxy.llm_proxy]]

## Top bridge nodes
- [[test_llm_proxy.py]] - degree 34, connects to 2 communities
- [[test_credential_injector_does_not_overwrite_existing_bearer()]] - degree 7, connects to 2 communities
- [[test_credential_injector_not_applied_for_non_anthropic_dest()]] - degree 7, connects to 2 communities
- [[test_backend_unavailable_warning_rate_limited()]] - degree 6, connects to 2 communities
- [[test_cloud_backend_connect_failure_still_returns_502()]] - degree 6, connects to 2 communities