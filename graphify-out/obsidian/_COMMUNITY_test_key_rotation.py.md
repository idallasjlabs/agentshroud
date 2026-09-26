---
type: community
cohesion: 0.25
members: 11
---

# test_key_rotation.py

**Cohesion:** 0.25 - loosely connected
**Members:** 11 nodes

## Members
- [[.test_emergency_disabled_trigger_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_in_progress_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_max_attempts_exceeded_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_not_due_without_force_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_retire_clears_old_reference_when_grace_expired()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_retire_noop_when_no_grace_period()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_failure_marks_failed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_unknown_credential_returns_error()]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestEmergencyAndRetire]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestRotateGuardBranches]] - code - gateway/tests/test_key_rotation_internals.py
- [[_old_cred()]] - code - gateway/tests/test_key_rotation_internals.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_key_rotationpy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Google Services Setup - Calendar, Contacts, Keep]]
- 4 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 2 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 2 edges to [[_COMMUNITY_OpenClaw Bot Container]]

## Top bridge nodes
- [[TestRotateGuardBranches]] - degree 11, connects to 4 communities
- [[TestEmergencyAndRetire]] - degree 9, connects to 4 communities
- [[_old_cred()]] - degree 9, connects to 2 communities
- [[.test_not_due_without_force_is_rejected()]] - degree 2, connects to 1 community