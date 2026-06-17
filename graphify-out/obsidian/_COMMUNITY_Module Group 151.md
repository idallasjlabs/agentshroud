---
type: community
cohesion: 0.07
members: 32
---

# Module Group 151

**Cohesion:** 0.07 - loosely connected
**Members:** 32 nodes

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
- [[._is_connect_error()]] - code - gateway/proxy/llm_proxy.py
- [[._local_backend_unavailable_response()]] - code - gateway/proxy/llm_proxy.py
- [[._local_failover_base()]] - code - gateway/proxy/llm_proxy.py
- [[._normalize_local_model()]] - code - gateway/proxy/llm_proxy.py
- [[._record_failover_event()]] - code - gateway/proxy/llm_proxy.py
- [[.proxy_messages()]] - code - gateway/proxy/llm_proxy.py
- [[Any_11]] - code - gateway/proxy/llm_proxy.py
- [[Apply XML and credential filters to text.]] - rationale - gateway/proxy/llm_proxy.py
- [[Apply outbound text filters to known streaming response formats.          Also e]] - rationale - gateway/proxy/llm_proxy.py
- [[Attempt a cloud→local failover dispatch.          Returns (status, headers, body]] - rationale - gateway/proxy/llm_proxy.py
- [[BaseException]] - code - gateway/proxy/llm_proxy.py
- [[Build a structured 503 for an unreachable local backend.          Logs one WARNI]] - rationale - gateway/proxy/llm_proxy.py
- [[Build provider-compatible timeout fallback message to avoid silent Telegram fail]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter buffered SSE-like streaming responses for XMLcredential leaks and ToolAC]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter outbound LLM response for credential leaks and XML.]] - rationale - gateway/proxy/llm_proxy.py
- [[Forward request to the real LLM API provider.          Retries up to 3 times on]] - rationale - gateway/proxy/llm_proxy.py
- [[Persist a failover event to the audit chain if wired.]] - rationale - gateway/proxy/llm_proxy.py
- [[Proxy an LLM API request.          Returns (status_code, response_headers, respo]] - rationale - gateway/proxy/llm_proxy.py
- [[Resolve the local backend for failover dispatch via LOCAL_MODEL_ROUTES.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan Anthropic tool_use blocks; replace denied tools with a text error block.]] - rationale - gateway/proxy/llm_proxy.py
- [[Send a single Telegram notice per cooldown window when failover activates.]] - rationale - gateway/proxy/llm_proxy.py
- [[True for connection-level failures (refused  unreachable  reset).          Unw]] - rationale - gateway/proxy/llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_151
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Module Group 73]]
- 4 edges to [[_COMMUNITY_Module Group 101]]
- 4 edges to [[_COMMUNITY_Module Group 178]]
- 1 edge to [[_COMMUNITY_Module Group 480]]
- 1 edge to [[_COMMUNITY_Module Group 352]]
- 1 edge to [[_COMMUNITY_Module Group 220]]
- 1 edge to [[_COMMUNITY_Module Group 431]]

## Top bridge nodes
- [[.proxy_messages()]] - degree 20, connects to 7 communities
- [[._failover_request()]] - degree 12, connects to 3 communities
- [[._filter_streaming_event()]] - degree 5, connects to 1 community
- [[._apply_filters()]] - degree 4, connects to 1 community
- [[._emit_failover_notice()]] - degree 4, connects to 1 community