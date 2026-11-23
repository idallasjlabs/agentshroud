---
type: community
members: 7
---

# TestLLMProxyEndpoints

**Members:** 7 nodes

## Members
- [[dot-test_llm_stats_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_v1_endpoint_handles_non_json_upstream_bodies()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_v1_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[Proxy endpoint must not crash if upstream returns non-JSON body.]] - rationale - gateway/tests/test_round2_hardening.py
- [[TestLLMProxyEndpoints]] - code - gateway/tests/test_round2_hardening.py
- [[The llm-proxystats endpoint must exist.]] - rationale - gateway/tests/test_round2_hardening.py
- [[The v1{path} endpoint must exist (enabled in v0.9.0).]] - rationale - gateway/tests/test_round2_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestLLMProxyEndpoints
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[TestLLMProxyEndpoints]] - degree 4, connects to 1 community
