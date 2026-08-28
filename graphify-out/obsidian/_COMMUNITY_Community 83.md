---
type: community
cohesion: 0.06
members: 64
---

# Community 83

**Cohesion:** 0.06 - loosely connected
**Members:** 64 nodes

## Members
- [[.__init__()_24]] - code - gateway/proxy/llm_proxy.py
- [[.__init__()_171]] - code - gateway/tests/test_llm_proxy.py
- [[.__init__()_170]] - code - gateway/tests/test_llm_proxy.py
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
- [[Connect timeout must exceed this host's measured DNS-resolution latency     (~4.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Events from 'unknown' user_id must not be blocked (not authenticated).]] - rationale - gateway/tests/test_llm_proxy.py
- [[Fake CredentialInjector that records inject_headers calls and applies Anthropic]] - rationale - gateway/tests/test_llm_proxy.py
- [[LLMProxy]] - code - gateway/proxy/llm_proxy.py
- [[LM Studio down → 503 backend_unavailable with LM Studio hint.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Localnon-Anthropic destination injector must NOT be called.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Minimal ToolACLEnforcer stub that denies a named tool.]] - rationale - gateway/tests/test_llm_proxy.py
- [[No streaming call site may hardcode its own connect timeout literal.      Guards]] - rationale - gateway/tests/test_llm_proxy.py
- [[Ollama down → 503 backend_unavailable with ollama serve hint.]] - rationale - gateway/tests/test_llm_proxy.py
- [[OpenClaw already sends Authorization Bearer — injector must leave it untouched.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Post-Retry Rate Limit Failover Tests]] - code - gateway/tests/test_rate_limit_failover.py
- [[Proxies LLM API calls (Anthropic, OpenAI, Google) through the security pipeline.]] - rationale - gateway/proxy/llm_proxy.py
- [[Regression 2026-08-07 a plain (non-Claude, non-Gemini, non-local)     OpenAI-mo]] - rationale - gateway/tests/test_llm_proxy.py
- [[Repeated connect failures log one WARNING per window, not per request.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Return a monkeypatched urlopen that captures the Request headers.]] - rationale - gateway/tests/test_llm_proxy.py
- [[Round 2 Security Hardening Tests]] - code - gateway/tests/test_round2_hardening.py
- [[Streaming Anthropic request triggers inject_headers before httpx connects.]] - rationale - gateway/tests/test_llm_proxy.py
- [[_FakeSanitizer]] - code - gateway/tests/test_llm_proxy.py
- [[_FakeToolACL]] - code - gateway/tests/test_llm_proxy.py
- [[_TrackingInjector]] - code - gateway/tests/test_llm_proxy.py
- [[_is_connect_error matches connection-level failures only.]] - rationale - gateway/tests/test_llm_proxy.py
- [[_make_fake_urlopen()]] - code - gateway/tests/test_llm_proxy.py
- [[_proxy_with_connect_refused()]] - code - gateway/tests/test_llm_proxy.py
- [[content_block_start with terminal_tool must be replaced with a text error block.]] - rationale - gateway/tests/test_llm_proxy.py
- [[mlx_lm down (connection refused) → 503 backend_unavailable with start hint.]] - rationale - gateway/tests/test_llm_proxy.py
- [[test_all_streaming_clients_use_the_shared_connect_timeout_constant()]] - code - gateway/tests/test_llm_proxy.py
- [[test_backend_unavailable_warning_rate_limited()]] - code - gateway/tests/test_llm_proxy.py
- [[test_cloud_backend_connect_failure_still_returns_502()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_called_in_streaming_path()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_does_not_overwrite_existing_bearer()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()]] - code - gateway/tests/test_llm_proxy.py
- [[test_credential_injector_not_applied_for_non_anthropic_dest()]] - code - gateway/tests/test_llm_proxy.py
- [[test_filter_outbound_streaming_filters_anthropic_content_text()]] - code - gateway/tests/test_llm_proxy.py
- [[test_filter_outbound_streaming_filters_openai_delta_content()]] - code - gateway/tests/test_llm_proxy.py
- [[test_is_connect_error_classification()]] - code - gateway/tests/test_llm_proxy.py
- [[test_llm_connect_timeout_clears_observed_dns_latency()]] - code - gateway/tests/test_llm_proxy.py
- [[test_llm_proxy.py]] - code - gateway/tests/test_llm_proxy.py
- [[test_lmstudio_connect_failure_returns_structured_503()]] - code - gateway/tests/test_llm_proxy.py
- [[test_mlxlm_connect_failure_returns_structured_503()]] - code - gateway/tests/test_llm_proxy.py
- [[test_ollama_connect_failure_returns_structured_503()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic()]] - code - gateway/tests/test_llm_proxy.py
- [[test_proxy_messages_plain_openai_model_substitutes_real_key()]] - code - gateway/tests/test_llm_proxy.py
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
TABLE source_file, type FROM #community/Community_83
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_Community 129]]
- 7 edges to [[_COMMUNITY_Community 450]]
- 3 edges to [[_COMMUNITY_Community 224]]
- 3 edges to [[_COMMUNITY_Community 54]]
- 2 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 2 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 2 edges to [[_COMMUNITY_Community 126]]
- 2 edges to [[_COMMUNITY_Community 225]]
- 2 edges to [[_COMMUNITY_Community 1076]]
- 2 edges to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Ingest API & Approval Routes]]
- 1 edge to [[_COMMUNITY_Community 39]]
- 1 edge to [[_COMMUNITY_Community 65]]
- 1 edge to [[_COMMUNITY_Community 28]]
- 1 edge to [[_COMMUNITY_Security Audit & Drift Detection]]
- 1 edge to [[_COMMUNITY_Community 24]]

## Top bridge nodes
- [[LLMProxy]] - degree 80, connects to 14 communities
- [[test_llm_proxy.py]] - degree 32, connects to 1 community
- [[test_scan_request_data_scans_messages_without_name_error()]] - degree 4, connects to 1 community
- [[Round 2 Security Hardening Tests]] - degree 2, connects to 1 community