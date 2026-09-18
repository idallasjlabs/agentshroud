---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "LLMProxy"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxy
---

# test_llm_proxy.py

## Connections
- [[LLMProxy_2]] - `references` [EXTRACTED]
- [[ToolACLEnforcer_1]] - `conceptually_related_to` [INFERRED]
- [[_FakeSanitizer_2]] - `contains` [EXTRACTED]
- [[_FakeToolACL_1]] - `contains` [EXTRACTED]
- [[_TrackingInjector_1]] - `contains` [EXTRACTED]
- [[_make_fake_urlopen()_1]] - `contains` [EXTRACTED]
- [[_proxy_with_connect_refused()_1]] - `contains` [EXTRACTED]
- [[gateway.proxy.llm_proxy]] - `imports_from` [EXTRACTED]
- [[llm_proxy.py_2]] - `imports_from` [EXTRACTED]
- [[test_all_streaming_clients_use_the_shared_connect_timeout_constant()_1]] - `contains` [EXTRACTED]
- [[test_backend_unavailable_warning_rate_limited()_1]] - `contains` [EXTRACTED]
- [[test_cloud_backend_connect_failure_still_returns_502()_1]] - `contains` [EXTRACTED]
- [[test_credential_injector_called_in_streaming_path()_1]] - `contains` [EXTRACTED]
- [[test_credential_injector_does_not_overwrite_existing_bearer()_1]] - `contains` [EXTRACTED]
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()_1]] - `contains` [EXTRACTED]
- [[test_credential_injector_not_applied_for_non_anthropic_dest()_1]] - `contains` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_anthropic_content_text()_1]] - `contains` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_openai_delta_content()_1]] - `contains` [EXTRACTED]
- [[test_is_connect_error_classification()_1]] - `contains` [EXTRACTED]
- [[test_llm_connect_timeout_clears_observed_dns_latency()_1]] - `contains` [EXTRACTED]
- [[test_lmstudio_connect_failure_returns_structured_503()_1]] - `contains` [EXTRACTED]
- [[test_mlxlm_connect_failure_returns_structured_503()_1]] - `contains` [EXTRACTED]
- [[test_ollama_connect_failure_returns_structured_503()_1]] - `contains` [EXTRACTED]
- [[test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()_1]] - `contains` [EXTRACTED]
- [[test_proxy_messages_plain_openai_model_substitutes_real_key()_1]] - `contains` [EXTRACTED]
- [[test_proxy_messages_rewrites_claude_opus_to_local_model()_1]] - `contains` [EXTRACTED]
- [[test_proxy_messages_streaming_strips_openai_local_prefix_and_routes_to_backend()_1]] - `contains` [EXTRACTED]
- [[test_proxy_messages_strips_ollama_prefix_for_openai_compat()_1]] - `contains` [EXTRACTED]
- [[test_proxy_messages_strips_openai_local_prefix_and_routes_to_backend()_1]] - `contains` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_anthropic_compatible_fallback()_1]] - `contains` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_openai_compatible_fallback()_1]] - `contains` [EXTRACTED]
- [[test_scan_request_data_scans_messages_without_name_error()_1]] - `contains` [EXTRACTED]
- [[test_streaming_secret_value_redacted()_1]] - `contains` [EXTRACTED]
- [[test_streaming_tool_acl_allows_permitted_tool()_1]] - `contains` [EXTRACTED]
- [[test_streaming_tool_acl_blocks_terminal_tool()_1]] - `contains` [EXTRACTED]
- [[test_streaming_tool_acl_skips_unknown_user()_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxy