---
type: community
cohesion: 0.36
members: 8
---

# Module Group 431

**Cohesion:** 0.36 - loosely connected
**Members:** 8 nodes

## Members
- [[A 429 that escaped the retry loop must trigger local failover.]] - rationale - gateway/tests/test_rate_limit_failover.py
- [[Return (True, anthropic_rate_limitopenai_rate_limit...) for a     persiste]] - rationale - gateway/proxy/llm_quota_detector.py
- [[is_rate_limited_post_retry()]] - code - gateway/proxy/llm_quota_detector.py
- [[test_detector_empty_body_still_fires_as_generic_cloud()]] - code - gateway/tests/test_rate_limit_failover.py
- [[test_detector_fires_on_plain_429()]] - code - gateway/tests/test_rate_limit_failover.py
- [[test_detector_skips_non_429()]] - code - gateway/tests/test_rate_limit_failover.py
- [[test_proxy_failover_on_post_retry_429()]] - code - gateway/tests/test_rate_limit_failover.py
- [[test_rate_limit_failover.py]] - code - gateway/tests/test_rate_limit_failover.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_431
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Module Group 73]]
- 1 edge to [[_COMMUNITY_Module Group 101]]
- 1 edge to [[_COMMUNITY_Module Group 151]]
- 1 edge to [[_COMMUNITY_Module Group 220]]

## Top bridge nodes
- [[is_rate_limited_post_retry()]] - degree 8, connects to 3 communities
- [[test_rate_limit_failover.py]] - degree 6, connects to 1 community
- [[test_proxy_failover_on_post_retry_429()]] - degree 3, connects to 1 community
