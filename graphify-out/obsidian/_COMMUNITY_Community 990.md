---
type: community
cohesion: 0.21
members: 8
---

# Community 990

**Cohesion:** 0.21 - loosely connected
**Members:** 8 nodes

## Members
- [[Turbo Fieldflare's exact model ID must win over the generic 'gemma' LM     Studi]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for non-OOM raw 500 bodies.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns True for backend_unavailable 503 bodies.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's DeepSeek-R1-0528-Qwen3-8B must win over the generic     'deepseek-r1' -]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_detects_backend_unavailable()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_raw_body_false_on_normal_500()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_failover_base_routes_fieldflare_gemma_before_generic_gemma()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_failover_base_routes_omlx_deepseek_r1_qwen3_8b()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_990
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 54]]

## Top bridge nodes
- [[test_is_local_oom_raw_body_false_on_normal_500()]] - degree 3, connects to 1 community
- [[test_local_failover_base_routes_omlx_deepseek_r1_qwen3_8b()]] - degree 3, connects to 1 community
- [[test_is_local_oom_detects_backend_unavailable()]] - degree 2, connects to 1 community
- [[test_local_failover_base_routes_fieldflare_gemma_before_generic_gemma()]] - degree 2, connects to 1 community