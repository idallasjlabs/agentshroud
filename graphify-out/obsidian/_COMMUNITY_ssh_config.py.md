---
type: community
cohesion: 0.29
members: 12
---

# ssh_config.py

**Cohesion:** 0.29 - loosely connected
**Members:** 12 nodes

## Members
- [[Any_38]] - code - gateway/security/egress_retry.py
- [[Calculate delay with exponential backoff and jitter.]] - rationale - gateway/security/egress_retry.py
- [[Configuration for egress retry behavior.]] - rationale - gateway/security/egress_retry.py
- [[Execute a request with exponential backoff retry on transient failures.      Arg]] - rationale - gateway/security/egress_retry.py
- [[Result of a retried operation.]] - rationale - gateway/security/egress_retry.py
- [[RetryConfig]] - code - gateway/security/egress_retry.py
- [[RetryResult]] - code - gateway/security/egress_retry.py
- [[Synchronous version of retry_request for non-async contexts.]] - rationale - gateway/security/egress_retry.py
- [[calculate_delay()]] - code - gateway/security/egress_retry.py
- [[egress_retry.py]] - code - gateway/security/egress_retry.py
- [[retry_request()]] - code - gateway/security/egress_retry.py
- [[retry_request_sync()]] - code - gateway/security/egress_retry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ssh_configpy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_StdioConnection]]

## Top bridge nodes
- [[egress_retry.py]] - degree 6, connects to 1 community