---
type: community
cohesion: 0.10
members: 21
---

# MockValidator

**Cohesion:** 0.10 - loosely connected
**Members:** 21 nodes

## Members
- [[.__init__()_148]] - code - gateway/tests/test_key_rotation.py
- [[.setup_manager_with_credential()]] - code - gateway/tests/test_key_rotation.py
- [[.test_check_and_rotate_due_credentials()]] - code - gateway/tests/test_key_rotation.py
- [[.test_emergency_rotation()]] - code - gateway/tests/test_key_rotation.py
- [[.test_grace_period_cleanup()]] - code - gateway/tests/test_key_rotation.py
- [[.test_register_validator()]] - code - gateway/tests/test_key_rotation.py
- [[.test_rotation_with_validation_failure()]] - code - gateway/tests/test_key_rotation.py
- [[.test_successful_rotation_workflow()]] - code - gateway/tests/test_key_rotation.py
- [[.validate()_3]] - code - gateway/tests/test_key_rotation.py
- [[Mock validation that can be controlled.]] - rationale - gateway/tests/test_key_rotation.py
- [[Mock validator for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[MockValidator]] - code - gateway/tests/test_key_rotation.py
- [[Set up manager with a credential that needs rotation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test bulk rotation check and execution.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test complete successful rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test emergency rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period and old credential cleanup.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test rotation workflow with validation failure and rollback.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the complete rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test validator registration.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestKeyRotationWorkflow]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MockValidator
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_KeyRotationConfig]]
- 4 edges to [[_COMMUNITY_KeyRotationManager]]
- 4 edges to [[_COMMUNITY_CredentialValidator]]
- 4 edges to [[_COMMUNITY_CredentialInfo]]
- 2 edges to [[_COMMUNITY_test_key_rotation.py]]
- 1 edge to [[_COMMUNITY_TestKeyRotationManager]]

## Top bridge nodes
- [[MockValidator]] - degree 14, connects to 5 communities
- [[TestKeyRotationWorkflow]] - degree 14, connects to 5 communities
- [[.setup_manager_with_credential()]] - degree 6, connects to 3 communities
- [[.test_check_and_rotate_due_credentials()]] - degree 6, connects to 3 communities
- [[.test_register_validator()]] - degree 3, connects to 1 community