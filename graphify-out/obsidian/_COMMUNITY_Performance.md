---
type: community
cohesion: 0.29
members: 7
---

# Performance

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.guard()_2]] - code - gateway/tests/test_performance.py
- [[.test_1000_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[.test_detection_accuracy_at_scale()]] - code - gateway/tests/test_performance.py
- [[Injection attempts should be detected even under load.]] - rationale - gateway/tests/test_performance.py
- [[Prompt guard 1000 messages in  5s.]] - rationale - gateway/tests/test_performance.py
- [[Scan 1000 messages in under 5 seconds.]] - rationale - gateway/tests/test_performance.py
- [[TestPromptGuardPerformance]] - code - gateway/tests/test_performance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Performance
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 3 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 1 edge to [[_COMMUNITY_Security Regressions V1 2]]

## Top bridge nodes
- [[TestPromptGuardPerformance]] - degree 12, connects to 3 communities
- [[.guard()_2]] - degree 2, connects to 1 community