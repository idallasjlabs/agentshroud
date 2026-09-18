---
type: community
cohesion: 0.15
members: 13
---

# ._is_local_oom()

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[._is_local_oom()]] - code - gateway/proxy/llm_proxy.py
- [[._is_local_oom()_1]] - code - gateway/proxy/llm_proxy.py
- [[Return True if the response indicates a local-model OOM or backend_unavailable.]] - rationale - gateway/proxy/llm_proxy.py
- [[_is_local_oom detects 'out of memory' in error message string.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom handles raw non-JSON bodies from some backends.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for cloud 429 quota errors (different failover…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for non-OOM raw 500 bodies.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns True for backend_unavailable 503 bodies.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_detects_backend_unavailable()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_detects_oom_in_error_message()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_handles_non_json_body()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_raw_body_false_on_normal_500()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_returns_false_for_quota_429()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_is_local_oom
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_LLMProxy]]
- 6 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_.proxy_messages()]]

## Top bridge nodes
- [[._is_local_oom()]] - degree 9, connects to 2 communities
- [[test_is_local_oom_detects_backend_unavailable()]] - degree 4, connects to 2 communities
- [[test_is_local_oom_detects_oom_in_error_message()]] - degree 4, connects to 2 communities
- [[test_is_local_oom_handles_non_json_body()]] - degree 4, connects to 2 communities
- [[test_is_local_oom_raw_body_false_on_normal_500()]] - degree 4, connects to 2 communities