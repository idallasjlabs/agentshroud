---
type: community
cohesion: 0.16
members: 16
---

# TestInspectorEdgeCases

**Cohesion:** 0.16 - loosely connected
**Members:** 16 nodes

## Members
- [[.age_days()]] - code - gateway/security/key_rotation.py
- [[.is_in_grace_period()]] - code - gateway/security/key_rotation.py
- [[.test_age_calculation()]] - code - gateway/tests/test_key_rotation.py
- [[.test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[.test_should_rotate()]] - code - gateway/tests/test_key_rotation.py
- [[.test_should_warn()]] - code - gateway/tests/test_key_rotation.py
- [[Age of credential in days.]] - rationale - gateway/security/key_rotation.py
- [[CredentialInfo]] - code - gateway/security/key_rotation.py
- [[Information about a managed credential.]] - rationale - gateway/security/key_rotation.py
- [[Test credential age calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential information tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period status tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test rotation requirement calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test warning threshold calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCredentialInfo]] - code - gateway/tests/test_key_rotation.py
- [[Whether credential is currently in grace period.]] - rationale - gateway/security/key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestInspectorEdgeCases
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Google Services Setup - Calendar, Contacts, Keep]]
- 6 edges to [[_COMMUNITY_3. Security Controls]]
- 4 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 4 edges to [[_COMMUNITY_test_key_rotation.py]]
- 4 edges to [[_COMMUNITY_DOCKER-VPN-NETWORKING]]
- 4 edges to [[_COMMUNITY_4. Environment Variables]]
- 3 edges to [[_COMMUNITY_OpenClaw Bot Container]]
- 2 edges to [[_COMMUNITY_TestOpProxyEndpoint]]

## Top bridge nodes
- [[CredentialInfo]] - degree 35, connects to 8 communities
- [[TestCredentialInfo]] - degree 12, connects to 5 communities
- [[.test_should_rotate()]] - degree 4, connects to 1 community
- [[.test_should_warn()]] - degree 4, connects to 1 community