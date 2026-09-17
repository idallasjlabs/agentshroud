---
type: community
cohesion: 0.05
members: 42
---

# test_trust_manager.py

**Cohesion:** 0.05 - loosely connected
**Members:** 42 nodes

## Members
- [[.test_basic_can_read()]] - code - gateway/tests/test_trust_manager.py
- [[.test_default_config()_7]] - code - gateway/tests/test_trust_manager.py
- [[.test_demotion_on_violations()]] - code - gateway/tests/test_trust_manager.py
- [[.test_failure_decreases_score()_1]] - code - gateway/tests/test_trust_manager.py
- [[.test_get_trust_registered()]] - code - gateway/tests/test_trust_manager.py
- [[.test_get_trust_unregistered()]] - code - gateway/tests/test_trust_manager.py
- [[.test_history_empty_for_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[.test_history_recorded()]] - code - gateway/tests/test_trust_manager.py
- [[.test_persistence_across_instances()]] - code - gateway/tests/test_trust_manager.py
- [[.test_promotion_on_threshold()]] - code - gateway/tests/test_trust_manager.py
- [[.test_register_idempotent()_1]] - code - gateway/tests/test_trust_manager.py
- [[.test_register_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[.test_score_floor_at_zero()]] - code - gateway/tests/test_trust_manager.py
- [[.test_success_increases_score()_1]] - code - gateway/tests/test_trust_manager.py
- [[.test_trust_level_ordering()]] - code - gateway/tests/test_trust_manager.py
- [[.test_unregistered_denied()]] - code - gateway/tests/test_trust_manager.py
- [[.test_untrusted_limited()]] - code - gateway/tests/test_trust_manager.py
- [[.test_violation_severe_penalty()]] - code - gateway/tests/test_trust_manager.py
- [[Agent should be demoted on violations.]] - rationale - gateway/tests/test_trust_manager.py
- [[Agent should be promoted when score crosses threshold.]] - rationale - gateway/tests/test_trust_manager.py
- [[Config with strict thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[Create a temporary trust database.]] - rationale - gateway/tests/test_trust_manager.py
- [[Create a trust manager with temp DB.]] - rationale - gateway/tests/test_trust_manager.py
- [[Score should not go below 0.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test agent registration and initial trust.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test earning and losing trust.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test that actions are gated by trust level.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust history tracking.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust level hierarchy and thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust survives restart.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestActionGating]] - code - gateway/tests/test_trust_manager.py
- [[TestAgentRegistration]] - code - gateway/tests/test_trust_manager.py
- [[TestHistory]] - code - gateway/tests/test_trust_manager.py
- [[TestPersistence_1]] - code - gateway/tests/test_trust_manager.py
- [[TestTrustLevels]] - code - gateway/tests/test_trust_manager.py
- [[TestTrustProgression]] - code - gateway/tests/test_trust_manager.py
- [[Trust manager starting at untrusted.]] - rationale - gateway/tests/test_trust_manager.py
- [[manager()_3]] - code - gateway/tests/test_trust_manager.py
- [[strict_config()_2]] - code - gateway/tests/test_trust_manager.py
- [[strict_manager()]] - code - gateway/tests/test_trust_manager.py
- [[test_trust_manager.py]] - code - gateway/tests/test_trust_manager.py
- [[trust_db()]] - code - gateway/tests/test_trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_trust_managerpy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_TrustManager]]
- 10 edges to [[_COMMUNITY_TrustConfig]]
- 7 edges to [[_COMMUNITY_TrustLevel]]

## Top bridge nodes
- [[test_trust_manager.py]] - degree 14, connects to 3 communities
- [[TestTrustProgression]] - degree 11, connects to 3 communities
- [[TestAgentRegistration]] - degree 9, connects to 3 communities
- [[TestActionGating]] - degree 8, connects to 3 communities
- [[TestHistory]] - degree 7, connects to 3 communities