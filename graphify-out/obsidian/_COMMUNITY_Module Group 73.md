---
type: community
cohesion: 0.07
members: 54
---

# Module Group 73

**Cohesion:** 0.07 - loosely connected
**Members:** 54 nodes

## Members
- [[.__init__()_16]] - code - gateway/proxy/llm_proxy.py
- [[.__init__()_125]] - code - gateway/tests/test_llm_proxy.py
- [[.__init__()_124]] - code - gateway/tests/test_llm_proxy.py
- [[.block_credentials()_1]] - code - gateway/tests/test_llm_proxy.py
- [[.can_use_tool()_1]] - code - gateway/tests/test_llm_proxy.py
- [[.filter_xml_blocks()_1]] - code - gateway/tests/test_llm_proxy.py
- [[.get_stats()_4]] - code - gateway/proxy/llm_proxy.py
- [[.inject_headers()]] - code - gateway/tests/test_llm_proxy.py
- [[.sanitize()_3]] - code - gateway/tests/test_llm_proxy.py
- [[A known secret value echoed in a streaming delta must be scrubbed.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Allowed tool blocks must pass through unchanged.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Anthropic-bound request with x-api-key injector injects Bearer + beta, strips x]] - rationale - gateway/tests/test_llm_proxy.py
- [[Connect failures to cloud providers keep the existing 502 behavior.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Events from 'unknown' user_id must not be blocked (not authenticated).]] - rationale - gateway/tests/test_llm_proxy.py
- [[Fake CredentialInjector that records inject_headers calls and applies Anthropic]] - rationale - gateway/tests/test_llm_proxy.py
- [[LLMProxy]] - code - gateway/proxy/llm_proxy.py
- [[LM Studio down → 503 backend_unavailable with LM Studio hint.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Localnon-Anthropic destination injector must NOT be called.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Minimal ToolACLEnforcer stub that denies a named tool.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Ollama down → 503 backend_unavailable with ollama serve hint.]] - rationale - gateway/tests/test_llm_proxy.py
- [[OpenClaw already sends Authorization Bearer — injector must leave it untouched.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Proxies LLM API calls (Anthropic, OpenAI, Google) through the security pipeline.]] - rationale - gateway/proxy/llm_proxy.py
- [[Repeated connect failures log one WARNING per window, not per request.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Return a monkeypatched urlopen that captures the Request headers.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Streaming Anthropic request triggers inject_headers before httpx connects.]] - rationale - gateway/tests/test_llm_proxy.py
- [[_FakeSanitizer]] - code - gateway/tests/test_llm_proxy.py
- [[_FakeToolACL]] - code - gateway/tests/test_llm_proxy.py
- [[_TrackingInjector]] - code - gateway/tests/test_llm_proxy.py
- [[_make_fake_urlopen()]] - code - gateway/tests/test_llm_proxy.py
- [[_proxy_with_connect_refused()]] - code - gateway/tests/test_llm_proxy.py
- [[content_block_start with terminal_tool must be replaced with a text error block.]] - rationale - gateway/tests/test_llm_proxy.py
- [[mlx_lm down (connection refused) → 503 backend_unavailable with start hint.]] - rationale - gateway/tests/test_llm_proxy.py
- [[test_backend_unavailable_warning_rate_limited()]] - code - gateway/tests/test_llm_proxy.py
- [[test_cloud_backend_connect_failure_still_returns_502()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_called_in_streaming_path()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_does_not_overwrite_existing_bearer()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_not_applied_for_non_anthropic_dest()]] - code - gateway/tests/test_llm_proxy.py
- [[test_filter_outbound_streaming_filters_anthropic_content_text()]] - code - gateway/tests/test_llm_proxy.py
- [[test_filter_outbound_streaming_filters_openai_delta_content()]] - code - gateway/tests/test_llm_proxy.py
- [[test_llm_proxy.py]] - code - gateway/tests/test_llm_proxy.py
- [[test_lmstudio_connect_failure_returns_structured_503()]] - code - gateway/tests/test_llm_proxy.py
- [[test_mlxlm_connect_failure_returns_structured_503()]] - code - gateway/tests/test_llm_proxy.py
- [[test_ollama_connect_failure_returns_structured_503()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_rewrites_claude_opus_to_local_model()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_strips_ollama_prefix_for_openai_compat()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_timeout_returns_anthropic_compatible_fallback()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_timeout_returns_openai_compatible_fallback()]] - code - gateway/tests/test_llm_proxy.py
- [[test_scan_request_data_scans_messages_without_name_error()]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_secret_value_redacted()]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_tool_acl_allows_permitted_tool()]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_tool_acl_blocks_terminal_tool()]] - code - gateway/tests/test_llm_proxy.py
- [[test_streaming_tool_acl_skips_unknown_user()]] - code - gateway/tests/test_llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_73
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Module Group 151]]
- 4 edges to [[_COMMUNITY_Module Group 101]]
- 3 edges to [[_COMMUNITY_Module Group 183]]
- 3 edges to [[_COMMUNITY_Module Group 480]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 431]]
- 1 edge to [[_COMMUNITY_Module Group 189]]
- 1 edge to [[_COMMUNITY_Module Group 74]]

## Top bridge nodes
- [[LLMProxy]] - degree 55, connects to 6 communities
- [[test_llm_proxy.py]] - degree 29, connects to 2 communities
- [[test_scan_request_data_scans_messages_without_name_error()]] - degree 4, connects to 1 community