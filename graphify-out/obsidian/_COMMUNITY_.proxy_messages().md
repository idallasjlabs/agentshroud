---
type: community
cohesion: 0.07
members: 41
---

# .proxy_messages()

**Cohesion:** 0.07 - loosely connected
**Members:** 41 nodes

## Members
- [[._build_timeout_fallback_response()_1]] - code - gateway/proxy/llm_proxy.py
- [[._emit_failover_notice()_1]] - code - gateway/proxy/llm_proxy.py
- [[._enforce_tool_acl()_1]] - code - gateway/proxy/llm_proxy.py
- [[._failover_request()_1]] - code - gateway/proxy/llm_proxy.py
- [[._forward_request()_1]] - code - gateway/proxy/llm_proxy.py
- [[._get_local_model()_1]] - code - gateway/proxy/llm_proxy.py
- [[._get_local_secondary_model()_1]] - code - gateway/proxy/llm_proxy.py
- [[._is_connect_error()_1]] - code - gateway/proxy/llm_proxy.py
- [[._local_backend_headers()_1]] - code - gateway/proxy/llm_proxy.py
- [[._local_backend_unavailable_response()]] - code - gateway/proxy/llm_proxy.py
- [[._local_backend_unavailable_response()_1]] - code - gateway/proxy/llm_proxy.py
- [[._local_failover_base()_1]] - code - gateway/proxy/llm_proxy.py
- [[._local_secondary_failover_request()_1]] - code - gateway/proxy/llm_proxy.py
- [[._normalize_local_model()_1]] - code - gateway/proxy/llm_proxy.py
- [[._record_failover_event()_1]] - code - gateway/proxy/llm_proxy.py
- [[._scan_inbound()_1]] - code - gateway/proxy/llm_proxy.py
- [[._scan_request_data()_1]] - code - gateway/proxy/llm_proxy.py
- [[._suppress_qwen3_thinking()_1]] - code - gateway/proxy/llm_proxy.py
- [[._widen_optional_tool_param_types()_1]] - code - gateway/proxy/llm_proxy.py
- [[.proxy_messages()_1]] - code - gateway/proxy/llm_proxy.py
- [[.proxy_messages_streaming()_1]] - code - gateway/proxy/llm_proxy.py
- [[Add 'null' as an accepted type for every non-required tool parameter, in place.]] - rationale - gateway/proxy/llm_proxy.py
- [[Append 'no_think' to the last user message, in place, if not already present.]] - rationale - gateway/proxy/llm_proxy.py
- [[Attempt a cloud→local failover dispatch.          Returns (status, headers, body]] - rationale - gateway/proxy/llm_proxy.py
- [[Attempt a local→local-secondary failover when the primary local model hits OOM.]] - rationale - gateway/proxy/llm_proxy.py
- [[BaseException_1]] - code
- [[Build a structured 503 for an unreachable local backend.          Logs one WARNI]] - rationale - gateway/proxy/llm_proxy.py
- [[Build a structured 503 for an unreachable local backend. Logs one WARNING per…]] - rationale - gateway/proxy/llm_proxy.py
- [[Build provider-compatible timeout fallback message to avoid silent Telegram fail]] - rationale - gateway/proxy/llm_proxy.py
- [[Forward request to the real LLM API provider.          Retries up to 3 times on]] - rationale - gateway/proxy/llm_proxy.py
- [[Inject per-backend auth for local backends that require it.          Unlike LM S]] - rationale - gateway/proxy/llm_proxy.py
- [[Persist a failover event to the audit chain if wired.]] - rationale - gateway/proxy/llm_proxy.py
- [[Proxy a streaming LLM API request, yielding SSE chunks as they arrive.]] - rationale - gateway/proxy/llm_proxy.py
- [[Proxy an LLM API request.          Returns (status_code, response_headers, respo]] - rationale - gateway/proxy/llm_proxy.py
- [[Resolve the local backend for failover dispatch via LOCAL_MODEL_ROUTES.]] - rationale - gateway/proxy/llm_proxy.py
- [[Return the bare secondary local model name, or None if not configured.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan Anthropic tool_use blocks; replace denied tools with a text error block.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan inbound user message text for PII and injection.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan request data for PII and injection across different provider formats.]] - rationale - gateway/proxy/llm_proxy.py
- [[Send a single Telegram notice per cooldown window when failover activates.]] - rationale - gateway/proxy/llm_proxy.py
- [[True for connection-level failures (refused  unreachable  reset).          Unw]] - rationale - gateway/proxy/llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/proxy_messages
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_LLMProxy]]
- 13 edges to [[_COMMUNITY_LLMProxy]]
- 2 edges to [[_COMMUNITY_._filter_streaming_event()]]
- 1 edge to [[_COMMUNITY_._is_local_oom()]]

## Top bridge nodes
- [[.proxy_messages()_1]] - degree 20, connects to 3 communities
- [[._failover_request()_1]] - degree 8, connects to 1 community
- [[._local_secondary_failover_request()_1]] - degree 8, connects to 1 community
- [[.proxy_messages_streaming()_1]] - degree 7, connects to 1 community
- [[._local_backend_headers()_1]] - degree 6, connects to 1 community