---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "Gateway Test Suite"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# test_llm_proxy.py

## Connections
- [[LLMProxy]] - `imports` [EXTRACTED]
- [[_FakeSanitizer]] - `contains` [EXTRACTED]
- [[_FakeToolACL]] - `contains` [EXTRACTED]
- [[_TrackingInjector]] - `contains` [EXTRACTED]
- [[_make_fake_urlopen()]] - `contains` [EXTRACTED]
- [[_proxy_with_connect_refused()]] - `contains` [EXTRACTED]
- [[llm_proxy.py]] - `imports_from` [EXTRACTED]
- [[test_all_streaming_clients_use_the_shared_connect_timeout_constant()]] - `contains` [EXTRACTED]
- [[test_backend_unavailable_warning_rate_limited()]] - `contains` [EXTRACTED]
- [[test_cloud_backend_connect_failure_still_returns_502()]] - `contains` [EXTRACTED]
- [[test_credential_injector_called_in_streaming_path()]] - `contains` [EXTRACTED]
- [[test_credential_injector_does_not_overwrite_existing_bearer()]] - `contains` [EXTRACTED]
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()]] - `contains` [EXTRACTED]
- [[test_credential_injector_not_applied_for_non_anthropic_dest()]] - `contains` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_anthropic_content_text()]] - `contains` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_openai_delta_content()]] - `contains` [EXTRACTED]
- [[test_is_connect_error_classification()]] - `contains` [EXTRACTED]
- [[test_llm_connect_timeout_clears_observed_dns_latency()]] - `contains` [EXTRACTED]
- [[test_lmstudio_connect_failure_returns_structured_503()]] - `contains` [EXTRACTED]
- [[test_mlxlm_connect_failure_returns_structured_503()]] - `contains` [EXTRACTED]
- [[test_ollama_connect_failure_returns_structured_503()]] - `contains` [EXTRACTED]
- [[test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()]] - `contains` [EXTRACTED]
- [[test_proxy_messages_plain_openai_model_substitutes_real_key()]] - `contains` [EXTRACTED]
- [[test_proxy_messages_rewrites_claude_opus_to_local_model()]] - `contains` [EXTRACTED]
- [[test_proxy_messages_strips_ollama_prefix_for_openai_compat()]] - `contains` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_anthropic_compatible_fallback()]] - `contains` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_openai_compatible_fallback()]] - `contains` [EXTRACTED]
- [[test_scan_request_data_scans_messages_without_name_error()]] - `contains` [EXTRACTED]
- [[test_streaming_secret_value_redacted()]] - `contains` [EXTRACTED]
- [[test_streaming_tool_acl_allows_permitted_tool()]] - `contains` [EXTRACTED]
- [[test_streaming_tool_acl_blocks_terminal_tool()]] - `contains` [EXTRACTED]
- [[test_streaming_tool_acl_skips_unknown_user()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite