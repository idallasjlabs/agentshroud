---
type: community
members: 50
---

# Community 108

**Members:** 50 nodes

## Members
- [[._apply_filters()]] - code - gateway/proxy/llm_proxy.py
- [[._build_timeout_fallback_response()]] - code - gateway/proxy/llm_proxy.py
- [[._emit_failover_notice()]] - code - gateway/proxy/llm_proxy.py
- [[._enforce_tool_acl()]] - code - gateway/proxy/llm_proxy.py
- [[._failover_request()]] - code - gateway/proxy/llm_proxy.py
- [[._filter_outbound()]] - code - gateway/proxy/llm_proxy.py
- [[._filter_outbound_streaming()]] - code - gateway/proxy/llm_proxy.py
- [[._filter_streaming_event()]] - code - gateway/proxy/llm_proxy.py
- [[._forward_request()]] - code - gateway/proxy/llm_proxy.py
- [[._get_local_model()]] - code - gateway/proxy/llm_proxy.py
- [[._get_local_secondary_model()]] - code - gateway/proxy/llm_proxy.py
- [[._is_connect_error()]] - code - gateway/proxy/llm_proxy.py
- [[._is_local_oom()]] - code - gateway/proxy/llm_proxy.py
- [[._local_backend_headers()]] - code - gateway/proxy/llm_proxy.py
- [[._local_backend_unavailable_response()]] - code - gateway/proxy/llm_proxy.py
- [[._local_failover_base()]] - code - gateway/proxy/llm_proxy.py
- [[._local_secondary_failover_request()]] - code - gateway/proxy/llm_proxy.py
- [[._normalize_local_model()]] - code - gateway/proxy/llm_proxy.py
- [[._record_failover_event()]] - code - gateway/proxy/llm_proxy.py
- [[._scan_inbound()]] - code - gateway/proxy/llm_proxy.py
- [[._scan_request_data()]] - code - gateway/proxy/llm_proxy.py
- [[._suppress_qwen3_thinking()]] - code - gateway/proxy/llm_proxy.py
- [[._widen_optional_tool_param_types()]] - code - gateway/proxy/llm_proxy.py
- [[.proxy_messages()]] - code - gateway/proxy/llm_proxy.py
- [[.proxy_messages_streaming()]] - code - gateway/proxy/llm_proxy.py
- [[Add 'null' as an accepted type for every non-required tool parameter, in place.]] - rationale - gateway/proxy/llm_proxy.py
- [[Any_14]] - code - gateway/proxy/llm_proxy.py
- [[Append 'no_think' to the last user message, in place, if not already present.]] - rationale - gateway/proxy/llm_proxy.py
- [[Apply XML and credential filters to text.]] - rationale - gateway/proxy/llm_proxy.py
- [[Apply outbound text filters to known streaming response formats.          Also e]] - rationale - gateway/proxy/llm_proxy.py
- [[Attempt a cloud→local failover dispatch.          Returns (status, headers, body]] - rationale - gateway/proxy/llm_proxy.py
- [[Attempt a local→local-secondary failover when the primary local model hits OOM.]] - rationale - gateway/proxy/llm_proxy.py
- [[BaseException]] - code - gateway/proxy/llm_proxy.py
- [[Build a structured 503 for an unreachable local backend.          Logs one WARNI]] - rationale - gateway/proxy/llm_proxy.py
- [[Build provider-compatible timeout fallback message to avoid silent Telegram fail]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter buffered SSE-like streaming responses for XMLcredential leaks and ToolAC]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter outbound LLM response for credential leaks and XML.]] - rationale - gateway/proxy/llm_proxy.py
- [[Forward request to the real LLM API provider.          Retries up to 3 times on]] - rationale - gateway/proxy/llm_proxy.py
- [[Inject per-backend auth for local backends that require it.          Unlike LM S]] - rationale - gateway/proxy/llm_proxy.py
- [[Persist a failover event to the audit chain if wired.]] - rationale - gateway/proxy/llm_proxy.py
- [[Proxy a streaming LLM API request, yielding SSE chunks as they arrive.]] - rationale - gateway/proxy/llm_proxy.py
- [[Proxy an LLM API request.          Returns (status_code, response_headers, respo]] - rationale - gateway/proxy/llm_proxy.py
- [[Resolve the local backend for failover dispatch via LOCAL_MODEL_ROUTES.]] - rationale - gateway/proxy/llm_proxy.py
- [[Return True if the response indicates a local-model OOM or backend_unavailable.]] - rationale - gateway/proxy/llm_proxy.py
- [[Return the bare secondary local model name, or None if not configured.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan Anthropic tool_use blocks; replace denied tools with a text error block.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan inbound user message text for PII and injection.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan request data for PII and injection across different provider formats.]] - rationale - gateway/proxy/llm_proxy.py
- [[Send a single Telegram notice per cooldown window when failover activates.]] - rationale - gateway/proxy/llm_proxy.py
- [[True for connection-level failures (refused  unreachable  reset).          Unw]] - rationale - gateway/proxy/llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_108
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_Community 79]]
- 6 edges to [[_COMMUNITY_Community 142]]
- 3 edges to [[_COMMUNITY_Community 126]]
- 2 edges to [[_COMMUNITY_Community 117]]
- 1 edge to [[_COMMUNITY_Community 308]]
- 1 edge to [[_COMMUNITY_Community 419]]
- 1 edge to [[_COMMUNITY_Community 979]]

## Top bridge nodes
- [[.proxy_messages()]] - degree 28, connects to 6 communities
- [[._failover_request()]] - degree 13, connects to 3 communities
- [[._local_secondary_failover_request()]] - degree 9, connects to 2 communities
- [[.proxy_messages_streaming()]] - degree 8, connects to 1 community
- [[._local_backend_headers()]] - degree 6, connects to 1 community