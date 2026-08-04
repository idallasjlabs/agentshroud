---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "Module Group 73"
location: "L92"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Module_Group_73
---

# LLMProxy

## Connections
- [[.__init__()_16]] - `method` [EXTRACTED]
- [[._apply_filters()]] - `method` [EXTRACTED]
- [[._build_timeout_fallback_response()]] - `method` [EXTRACTED]
- [[._emit_failover_notice()]] - `method` [EXTRACTED]
- [[._enforce_tool_acl()]] - `method` [EXTRACTED]
- [[._failover_request()]] - `method` [EXTRACTED]
- [[._filter_outbound()]] - `method` [EXTRACTED]
- [[._filter_outbound_streaming()]] - `method` [EXTRACTED]
- [[._filter_streaming_event()]] - `method` [EXTRACTED]
- [[._forward_request()]] - `method` [EXTRACTED]
- [[._get_local_model()]] - `method` [EXTRACTED]
- [[._is_connect_error()]] - `method` [EXTRACTED]
- [[._local_backend_unavailable_response()]] - `method` [EXTRACTED]
- [[._local_failover_base()]] - `method` [EXTRACTED]
- [[._normalize_local_model()]] - `method` [EXTRACTED]
- [[._record_failover_event()]] - `method` [EXTRACTED]
- [[._scan_inbound()]] - `method` [EXTRACTED]
- [[._scan_request_data()]] - `method` [EXTRACTED]
- [[.get_stats()_4]] - `method` [EXTRACTED]
- [[.proxy_messages()]] - `method` [EXTRACTED]
- [[.proxy_messages_streaming()]] - `method` [EXTRACTED]
- [[LLMProxy_1]] - `uses` [INFERRED]
- [[Proxies LLM API calls (Anthropic, OpenAI, Google) through the security pipeline.]] - `rationale_for` [EXTRACTED]
- [[_FakeSanitizer]] - `uses` [INFERRED]
- [[_FakeToolACL]] - `uses` [INFERRED]
- [[_TrackingInjector]] - `uses` [INFERRED]
- [[_proxy_with_connect_refused()]] - `calls` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[llm_proxy.py]] - `contains` [EXTRACTED]
- [[make_proxy()]] - `calls` [EXTRACTED]
- [[test_backend_unavailable_warning_rate_limited()]] - `calls` [EXTRACTED]
- [[test_claude_via_openai_path.py]] - `imports` [EXTRACTED]
- [[test_cloud_backend_connect_failure_still_returns_502()]] - `calls` [EXTRACTED]
- [[test_credential_injector_called_in_streaming_path()]] - `calls` [EXTRACTED]
- [[test_credential_injector_does_not_overwrite_existing_bearer()]] - `calls` [EXTRACTED]
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()]] - `calls` [EXTRACTED]
- [[test_credential_injector_not_applied_for_non_anthropic_dest()]] - `calls` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_anthropic_content_text()]] - `calls` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_openai_delta_content()]] - `calls` [EXTRACTED]
- [[test_llm_proxy.py]] - `imports` [EXTRACTED]
- [[test_llm_proxy_failover.py]] - `imports` [EXTRACTED]
- [[test_proxy_failover_on_post_retry_429()]] - `calls` [EXTRACTED]
- [[test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()]] - `calls` [EXTRACTED]
- [[test_proxy_messages_rewrites_claude_opus_to_local_model()]] - `calls` [EXTRACTED]
- [[test_proxy_messages_strips_ollama_prefix_for_openai_compat()]] - `calls` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_anthropic_compatible_fallback()]] - `calls` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_openai_compatible_fallback()]] - `calls` [EXTRACTED]
- [[test_proxy_rewrites_claude_via_openai_path()]] - `calls` [EXTRACTED]
- [[test_rate_limit_failover.py]] - `imports` [EXTRACTED]
- [[test_scan_request_data_scans_messages_without_name_error()]] - `calls` [EXTRACTED]
- [[test_streaming_secret_value_redacted()]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_allows_permitted_tool()]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_blocks_terminal_tool()]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_skips_unknown_user()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Module_Group_73
