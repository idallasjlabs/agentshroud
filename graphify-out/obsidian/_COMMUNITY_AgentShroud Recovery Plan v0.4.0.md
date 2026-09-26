---
type: community
cohesion: 0.18
members: 11
---

# AgentShroud Recovery Plan v0.4.0

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[.test_demotion_on_violations()]] - code - gateway/tests/test_trust_manager.py
- [[.test_failure_decreases_score()_1]] - code - gateway/tests/test_trust_manager.py
- [[.test_promotion_on_threshold()]] - code - gateway/tests/test_trust_manager.py
- [[.test_score_floor_at_zero()]] - code - gateway/tests/test_trust_manager.py
- [[.test_success_increases_score()_1]] - code - gateway/tests/test_trust_manager.py
- [[.test_violation_severe_penalty()]] - code - gateway/tests/test_trust_manager.py
- [[Agent should be demoted on violations.]] - rationale - gateway/tests/test_trust_manager.py
- [[Agent should be promoted when score crosses threshold.]] - rationale - gateway/tests/test_trust_manager.py
- [[Score should not go below 0.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test earning and losing trust.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestTrustProgression]] - code - gateway/tests/test_trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Recovery_Plan_v040
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 2 edges to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[TestTrustProgression]] - degree 11, connects to 2 communities