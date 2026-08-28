---
type: community
cohesion: 0.15
members: 17
---

# Community 533

**Cohesion:** 0.15 - loosely connected
**Members:** 17 nodes

## Members
- [[.age_days()]] - code - gateway/security/key_rotation.py
- [[.is_in_grace_period()]] - code - gateway/security/key_rotation.py
- [[.test_age_calculation()]] - code - gateway/tests/test_key_rotation.py
- [[.test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[.test_not_due_without_force_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
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
TABLE source_file, type FROM #community/Community_533
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 226]]
- 8 edges to [[_COMMUNITY_Community 295]]
- 4 edges to [[_COMMUNITY_Community 130]]
- 4 edges to [[_COMMUNITY_Community 432]]
- 4 edges to [[_COMMUNITY_Community 692]]
- 3 edges to [[_COMMUNITY_Community 810]]
- 1 edge to [[_COMMUNITY_Community 1271]]

## Top bridge nodes
- [[CredentialInfo]] - degree 35, connects to 7 communities
- [[TestCredentialInfo]] - degree 12, connects to 4 communities
- [[.test_should_rotate()]] - degree 4, connects to 1 community
- [[.test_should_warn()]] - degree 4, connects to 1 community
- [[.test_not_due_without_force_is_rejected()]] - degree 2, connects to 1 community