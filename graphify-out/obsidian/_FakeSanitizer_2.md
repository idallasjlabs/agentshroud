---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "LLMProxy"
location: "L14"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxy
---

# _FakeSanitizer

## Connections
- [[.block_credentials()_3]] - `method` [EXTRACTED]
- [[.filter_xml_blocks()_3]] - `method` [EXTRACTED]
- [[.sanitize()_5]] - `method` [EXTRACTED]
- [[LLMProxy_2]] - `uses` [INFERRED]
- [[test_credential_injector_called_in_streaming_path()_1]] - `calls` [EXTRACTED]
- [[test_credential_injector_does_not_overwrite_existing_bearer()_1]] - `calls` [EXTRACTED]
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()_1]] - `calls` [EXTRACTED]
- [[test_credential_injector_not_applied_for_non_anthropic_dest()_1]] - `calls` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_anthropic_content_text()_1]] - `calls` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_openai_delta_content()_1]] - `calls` [EXTRACTED]
- [[test_llm_proxy.py_1]] - `contains` [EXTRACTED]
- [[test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_plain_openai_model_substitutes_real_key()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_rewrites_claude_opus_to_local_model()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_strips_ollama_prefix_for_openai_compat()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_strips_openai_local_prefix_and_routes_to_backend()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_anthropic_compatible_fallback()_1]] - `calls` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_openai_compatible_fallback()_1]] - `calls` [EXTRACTED]
- [[test_scan_request_data_scans_messages_without_name_error()_1]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_allows_permitted_tool()_1]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_blocks_terminal_tool()_1]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_skips_unknown_user()_1]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxy