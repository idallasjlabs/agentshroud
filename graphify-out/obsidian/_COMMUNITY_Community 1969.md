---
type: community
members: 9
---

# Community 1969

**Members:** 9 nodes

## Members
- [[OOM (503 backend_unavailable from primary local) triggers secondary local failov]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Secondary failover for Anthropic-format (v1messages) path translates and retur]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for successful responses.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_openai_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[p99 timeout (TimeoutError on primary local) triggers secondary local model.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_returns_false_for_200()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_triggers_secondary_failover()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_p99_timeout_triggers_secondary_failover()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_anthropic_path()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1969
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 208]]
- 3 edges to [[_COMMUNITY_Community 506]]

## Top bridge nodes
- [[test_local_oom_triggers_secondary_failover()]] - degree 4, connects to 2 communities
- [[test_local_p99_timeout_triggers_secondary_failover()]] - degree 4, connects to 2 communities
- [[test_local_secondary_failover_anthropic_path()]] - degree 4, connects to 2 communities
- [[_openai_ok()]] - degree 5, connects to 1 community
- [[test_is_local_oom_returns_false_for_200()]] - degree 3, connects to 1 community