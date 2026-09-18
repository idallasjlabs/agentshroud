---
type: community
cohesion: 0.23
members: 14
---

# gateway.proxy.llm_proxy

**Cohesion:** 0.23 - loosely connected
**Members:** 14 nodes

## Members
- [[Any_67]] - code - gateway/security/egress_retry.py
- [[Calculate delay with exponential backoff and jitter.]] - rationale - gateway/security/egress_retry.py
- [[Configuration for egress retry behavior.]] - rationale - gateway/security/egress_retry.py
- [[Execute a request with exponential backoff retry on transient failures.      Arg]] - rationale - gateway/security/egress_retry.py
- [[LLM API Reverse Proxy — intercepts all OpenClaw ↔ (AnthropicOpenAIGoogle)…]] - rationale - gateway/proxy/llm_proxy.py
- [[Result of a retried operation.]] - rationale - gateway/security/egress_retry.py
- [[RetryConfig]] - code - gateway/security/egress_retry.py
- [[RetryResult]] - code - gateway/security/egress_retry.py
- [[Synchronous version of retry_request for non-async contexts.]] - rationale - gateway/security/egress_retry.py
- [[calculate_delay()]] - code - gateway/security/egress_retry.py
- [[egress_retry.py]] - code - gateway/security/egress_retry.py
- [[gateway.proxy.llm_proxy]] - code - gateway/proxy/llm_proxy.py
- [[retry_request()]] - code - gateway/security/egress_retry.py
- [[retry_request_sync()]] - code - gateway/security/egress_retry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gatewayproxyllm_proxy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_ANTHROPIC_BASE_URL]]
- 1 edge to [[_COMMUNITY_test_hermes_model_resolver.py]]
- 1 edge to [[_COMMUNITY_AgentShroud™ — OpenClaw Local-Model Tool-Use Ins]]
- 1 edge to [[_COMMUNITY_LLMProxy]]

## Top bridge nodes
- [[gateway.proxy.llm_proxy]] - degree 11, connects to 9 communities
- [[egress_retry.py]] - degree 7, connects to 1 community