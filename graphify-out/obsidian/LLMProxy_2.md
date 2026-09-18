---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "LLMProxy"
location: "L229"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxy
---

# LLMProxy

## Connections
- [[.__init__()_204]] - `method` [EXTRACTED]
- [[._apply_filters()_1]] - `method` [EXTRACTED]
- [[._build_timeout_fallback_response()_1]] - `method` [EXTRACTED]
- [[._emit_failover_notice()_1]] - `method` [EXTRACTED]
- [[._enforce_tool_acl()_1]] - `method` [EXTRACTED]
- [[._failover_request()_1]] - `method` [EXTRACTED]
- [[._filter_outbound()_2]] - `method` [EXTRACTED]
- [[._filter_outbound_streaming()_1]] - `method` [EXTRACTED]
- [[._filter_streaming_event()_1]] - `method` [EXTRACTED]
- [[._forward_request()_1]] - `method` [EXTRACTED]
- [[._get_local_model()_1]] - `method` [EXTRACTED]
- [[._get_local_secondary_model()_1]] - `method` [EXTRACTED]
- [[._is_connect_error()_1]] - `method` [EXTRACTED]
- [[._is_local_oom()_1]] - `method` [EXTRACTED]
- [[._local_backend_headers()_1]] - `method` [EXTRACTED]
- [[._local_backend_unavailable_response()_1]] - `method` [EXTRACTED]
- [[._local_failover_base()_1]] - `method` [EXTRACTED]
- [[._local_secondary_failover_request()_1]] - `method` [EXTRACTED]
- [[._normalize_local_model()_1]] - `method` [EXTRACTED]
- [[._record_failover_event()_1]] - `method` [EXTRACTED]
- [[._scan_inbound()_1]] - `method` [EXTRACTED]
- [[._scan_request_data()_1]] - `method` [EXTRACTED]
- [[._suppress_qwen3_thinking()_1]] - `method` [EXTRACTED]
- [[._widen_optional_tool_param_types()_1]] - `method` [EXTRACTED]
- [[.get_stats()_20]] - `method` [EXTRACTED]
- [[.proxy_messages()_1]] - `method` [EXTRACTED]
- [[.proxy_messages_streaming()_1]] - `method` [EXTRACTED]
- [[Proxies LLM API calls (Anthropic, OpenAI, Google) through the security pipeline.]] - `rationale_for` [EXTRACTED]
- [[_FakeSanitizer_2]] - `uses` [INFERRED]
- [[_FakeToolACL_1]] - `uses` [INFERRED]
- [[_TrackingInjector_1]] - `uses` [INFERRED]
- [[_proxy_with_connect_refused()_1]] - `calls` [EXTRACTED]
- [[llm_proxy.py_2]] - `contains` [EXTRACTED]
- [[test_backend_unavailable_warning_rate_limited()_1]] - `calls` [EXTRACTED]
- [[test_cloud_backend_connect_failure_still_returns_502()_1]] - `calls` [EXTRACTED]
- [[test_credential_injector_called_in_streaming_path()_1]] - `calls` [EXTRACTED]
- [[test_credential_injector_does_not_overwrite_existing_bearer()_1]] - `calls` [EXTRACTED]
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()_1]] - `calls` [EXTRACTED]
- [[test_credential_injector_not_applied_for_non_anthropic_dest()_1]] - `calls` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_anthropic_content_text()_1]] - `calls` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_openai_delta_content()_1]] - `calls` [EXTRACTED]
- [[test_llm_proxy.py_1]] - `references` [EXTRACTED]
- [[test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_plain_openai_model_substitutes_real_key()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_rewrites_claude_opus_to_local_model()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_streaming_strips_openai_local_prefix_and_routes_to_backend()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_strips_ollama_prefix_for_openai_compat()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_strips_openai_local_prefix_and_routes_to_backend()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_anthropic_compatible_fallback()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_openai_compatible_fallback()_1]] - `calls` [EXTRACTED]
- [[test_scan_request_data_scans_messages_without_name_error()_1]] - `calls` [EXTRACTED]
- [[test_streaming_secret_value_redacted()_1]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_allows_permitted_tool()_1]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_blocks_terminal_tool()_1]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_skips_unknown_user()_1]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxy