---
type: community
cohesion: 0.13
members: 25
---

# LLMProxy.proxy_messages

**Cohesion:** 0.13 - loosely connected
**Members:** 25 nodes

## Members
- [[CredentialInjector.inject_headers]] - code - gateway/security/credential_injector.py
- [[LLMProxy._apply_filters]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._build_timeout_fallback_response]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._emit_failover_notice]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._failover_request]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._filter_outbound]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._filter_outbound_streaming]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._filter_streaming_event]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._forward_request]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._get_local_model]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._get_local_secondary_model]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._is_connect_error]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._is_local_oom]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_backend_headers]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_backend_unavailable_response]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_failover_base]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_secondary_failover_request]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._normalize_local_model]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._record_failover_event]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._scan_inbound]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._scan_request_data]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._suppress_qwen3_thinking]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._widen_optional_tool_param_types]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy.proxy_messages]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy.proxy_messages_streaming]] - code - gateway/proxy/llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LLMProxyproxy_messages
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_gemini_openai_translator.py]]
- 4 edges to [[_COMMUNITY_test_anthropic_openai_translator.py]]
- 2 edges to [[_COMMUNITY_is_overloaded()]]
- 2 edges to [[_COMMUNITY_is_quota_exhausted()]]
- 2 edges to [[_COMMUNITY_test_claude_via_openai_path.py]]
- 1 edge to [[_COMMUNITY_is_rate_limited_post_retry()]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_translate_openai_sse_to_anthropic()]]
- 1 edge to [[_COMMUNITY_Local-Model Job Quality Matrix]]
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]

## Top bridge nodes
- [[LLMProxy.proxy_messages]] - degree 24, connects to 6 communities
- [[LLMProxy.proxy_messages_streaming]] - degree 12, connects to 4 communities
- [[LLMProxy._failover_request]] - degree 11, connects to 2 communities
- [[LLMProxy._local_secondary_failover_request]] - degree 7, connects to 1 community
- [[LLMProxy._forward_request]] - degree 4, connects to 1 community