---
type: community
members: 14
---

# FODL — Fluence Operational Data Lakehouse

**Members:** 14 nodes

## Members
- [[dot-manager()_2]] - code - gateway/tests/test_key_rotation.py
- [[dot-sample_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_credential_status()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_health_score_all_healthy()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_health_score_mixed_states()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_register_credential()]] - code - gateway/tests/test_key_rotation.py
- [[Create a manager with test configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Create a sample credential for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential registration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential status reporting.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score calculation with all healthy credentials.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score with mixed credential states.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation manager functionality.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestKeyRotationManager]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FODL__Fluence_Operational_Data_Lakehouse
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_A2AMethod]]
- 4 edges to [[_COMMUNITY_AgentShroud Documentation]]
- 2 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 1 edge to [[_COMMUNITY_env_guard.py]]

## Top bridge nodes
- [[TestKeyRotationManager]] - degree 15, connects to 4 communities
- [[dot-manager()_2]] - degree 4, connects to 2 communities
- [[dot-sample_credential()]] - degree 3, connects to 1 community
- [[dot-test_get_health_score_all_healthy()]] - degree 3, connects to 1 community
- [[dot-test_get_health_score_mixed_states()]] - degree 3, connects to 1 community
