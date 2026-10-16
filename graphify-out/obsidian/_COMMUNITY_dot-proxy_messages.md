---
type: community
cohesion: 0.07
members: 42
---

# .proxy_messages

**Cohesion:** 0.07 - loosely connected
**Members:** 42 nodes

## Members
- [[dot-_build_timeout_fallback_response()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_emit_failover_notice()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_enforce_tool_acl()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_failover_request()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_forward_request()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_get_local_model()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_get_local_secondary_model()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_is_connect_error()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_is_local_oom()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_local_backend_headers()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_local_backend_unavailable_response()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_local_failover_base()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_local_secondary_failover_request()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_normalize_local_model()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_record_failover_event()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_scan_inbound()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_scan_request_data()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_widen_optional_tool_param_types()]] - code - gateway/proxy/llm_proxy.py
- [[dot-proxy_messages()]] - code - gateway/proxy/llm_proxy.py
- [[dot-proxy_messages_streaming()]] - code - gateway/proxy/llm_proxy.py
- [[Add 'null' as an accepted type for every non-required tool parameter, in place.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Attempt a cloud→local failover dispatch. Returns (status, headers, body) from…]] - rationale - gateway/proxy/llm_proxy.py
- [[Attempt a local→local-secondary failover when the primary local model hits OOM.…]] - rationale - gateway/proxy/llm_proxy.py
- [[BaseException_1]] - code
- [[Build a structured 503 for an unreachable local backend. Logs one WARNING per…]] - rationale - gateway/proxy/llm_proxy.py
- [[Build provider-compatible timeout fallback message to avoid silent Telegram…]] - rationale - gateway/proxy/llm_proxy.py
- [[Forward request to the real LLM API provider. Retries up to 3 times on…]] - rationale - gateway/proxy/llm_proxy.py
- [[Inject per-backend auth for local backends that require it. Unlike LM Studio …]] - rationale - gateway/proxy/llm_proxy.py
- [[Persist a failover event to the audit chain if wired.]] - rationale - gateway/proxy/llm_proxy.py
- [[Proxy a streaming LLM API request, yielding SSE chunks as they arrive. Used…]] - rationale - gateway/proxy/llm_proxy.py
- [[Proxy an LLM API request. Returns (status_code, response_headers,…]] - rationale - gateway/proxy/llm_proxy.py
- [[Resolve the local backend for failover dispatch via LOCAL_MODEL_ROUTES.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Return True if the response indicates a local-model OOM or backend_unavailable.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Return the bare secondary local model name, or None if not configured. Reads…]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan Anthropic tool_use blocks; replace denied tools with a text error block.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan inbound user message text for PII and injection.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan request data for PII and injection across different provider formats.]] - rationale - gateway/proxy/llm_proxy.py
- [[Send a single Telegram notice per cooldown window when failover activates.]] - rationale - gateway/proxy/llm_proxy.py
- [[True for connection-level failures (refused  unreachable  reset). Unwraps…]] - rationale - gateway/proxy/llm_proxy.py
- [[_read_error_body()]] - code - gateway/proxy/llm_proxy.py
- [[_stream()]] - code - gateway/proxy/llm_proxy.py
- [[_urlopen_and_read()]] - code - gateway/proxy/llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/proxy_messages
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_LLMProxy]]
- 2 edges to [[_COMMUNITY_dot-_filter_streaming_event]]
- 2 edges to [[_COMMUNITY_gatewayteststest_llm_proxy_thinking_suppression.py (8 cases)]]

## Top bridge nodes
- [[dot-proxy_messages()]] - degree 20, connects to 3 communities
- [[dot-proxy_messages_streaming()]] - degree 8, connects to 2 communities
- [[dot-_failover_request()]] - degree 8, connects to 1 community
- [[dot-_local_secondary_failover_request()]] - degree 8, connects to 1 community
- [[dot-_forward_request()]] - degree 7, connects to 1 community
