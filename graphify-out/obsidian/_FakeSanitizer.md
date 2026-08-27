---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "Community 79"
location: "L14"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_79
---

# _FakeSanitizer

## Connections
- [[.block_credentials()_1]] - `method` [EXTRACTED]
- [[.filter_xml_blocks()_1]] - `method` [EXTRACTED]
- [[.sanitize()_3]] - `method` [EXTRACTED]
- [[LLMProxy]] - `uses` [INFERRED]
- [[test_credential_injector_called_in_streaming_path()]] - `calls` [EXTRACTED]
- [[test_credential_injector_does_not_overwrite_existing_bearer()]] - `calls` [EXTRACTED]
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()]] - `calls` [EXTRACTED]
- [[test_credential_injector_not_applied_for_non_anthropic_dest()]] - `calls` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_anthropic_content_text()]] - `calls` [EXTRACTED]
- [[test_filter_outbound_streaming_filters_openai_delta_content()]] - `calls` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]
- [[test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()]] - `calls` [EXTRACTED]
- [[test_proxy_messages_plain_openai_model_substitutes_real_key()]] - `calls` [EXTRACTED]
- [[test_proxy_messages_rewrites_claude_opus_to_local_model()]] - `calls` [EXTRACTED]
- [[test_proxy_messages_strips_ollama_prefix_for_openai_compat()]] - `calls` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_anthropic_compatible_fallback()]] - `calls` [EXTRACTED]
- [[test_proxy_messages_timeout_returns_openai_compatible_fallback()]] - `calls` [EXTRACTED]
- [[test_scan_request_data_scans_messages_without_name_error()]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_allows_permitted_tool()]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_blocks_terminal_tool()]] - `calls` [EXTRACTED]
- [[test_streaming_tool_acl_skips_unknown_user()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_79