---
type: community
members: 11
---

# TestTrustProgression

**Members:** 11 nodes

## Members
- [[dot-test_demotion_on_violations()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_failure_decreases_score()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_promotion_on_threshold()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_score_floor_at_zero()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_success_increases_score()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_violation_severe_penalty()]] - code - gateway/tests/test_trust_manager.py
- [[Agent should be demoted on violations.]] - rationale - gateway/tests/test_trust_manager.py
- [[Agent should be promoted when score crosses threshold.]] - rationale - gateway/tests/test_trust_manager.py
- [[Score should not go below 0.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test earning and losing trust.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestTrustProgression]] - code - gateway/tests/test_trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestTrustProgression
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[TestTrustProgression]] - degree 9, connects to 2 communities
