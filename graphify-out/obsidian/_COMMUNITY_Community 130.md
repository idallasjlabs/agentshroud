---
type: community
cohesion: 0.07
members: 45
---

# Community 130

**Cohesion:** 0.07 - loosely connected
**Members:** 45 nodes

## Members
- [[.__init__()_88]] - code - gateway/security/key_rotation.py
- [[._generate_new_credential()]] - code - gateway/security/key_rotation.py
- [[._read_credential_from_1password()]] - code - gateway/security/key_rotation.py
- [[._retire_old_credential_after_grace_period()]] - code - gateway/security/key_rotation.py
- [[._store_credential_in_1password()]] - code - gateway/security/key_rotation.py
- [[._validate_credential()]] - code - gateway/security/key_rotation.py
- [[.check_and_rotate_due_credentials()]] - code - gateway/security/key_rotation.py
- [[.cleanup_retired_credentials()]] - code - gateway/security/key_rotation.py
- [[.emergency_rotate_credential()]] - code - gateway/security/key_rotation.py
- [[.get_all_credentials_status()]] - code - gateway/security/key_rotation.py
- [[.get_credential_status()]] - code - gateway/security/key_rotation.py
- [[.get_health_score()]] - code - gateway/security/key_rotation.py
- [[.register_credential()]] - code - gateway/security/key_rotation.py
- [[.register_validator()]] - code - gateway/security/key_rotation.py
- [[.rotate_credential()]] - code - gateway/security/key_rotation.py
- [[.should_rotate()]] - code - gateway/security/key_rotation.py
- [[.should_warn()]] - code - gateway/security/key_rotation.py
- [[.validate()]] - code - gateway/security/key_rotation.py
- [[Any_43]] - code - gateway/security/key_rotation.py
- [[Calculate overall credential health score.]] - rationale - gateway/security/key_rotation.py
- [[Check all credentials and rotate those that are due.]] - rationale - gateway/security/key_rotation.py
- [[Clean up any credentials past their grace period.]] - rationale - gateway/security/key_rotation.py
- [[Get detailed status for a credential.]] - rationale - gateway/security/key_rotation.py
- [[Get overall credential health score and status summary.]] - rationale - gateway/web/management.py
- [[Get status for all managed credentials.]] - rationale - gateway/security/key_rotation.py
- [[Get status of all managed credentials including age and rotation schedule.]] - rationale - gateway/web/management.py
- [[Initialize the key rotation manager.]] - rationale - gateway/security/key_rotation.py
- [[KeyRotationManager]] - code - gateway/security/key_rotation.py
- [[Manages automated rotation of credentials with zero downtime.]] - rationale - gateway/security/key_rotation.py
- [[Perform emergency rotation of a credential.]] - rationale - gateway/security/key_rotation.py
- [[Register a credential for rotation management.]] - rationale - gateway/security/key_rotation.py
- [[Register a validator for a credential type.]] - rationale - gateway/security/key_rotation.py
- [[Retire old credential after grace period ends.]] - rationale - gateway/security/key_rotation.py
- [[Rotate a single credential with zero downtime.          Workflow generate new →]] - rationale - gateway/security/key_rotation.py
- [[Safely read a credential from 1Password using op CLI.]] - rationale - gateway/security/key_rotation.py
- [[Store a new credential in 1Password.]] - rationale - gateway/security/key_rotation.py
- [[Trigger manual rotation for a specific credential (owner only).]] - rationale - gateway/web/management.py
- [[Validate a credential using registered validator.]] - rationale - gateway/security/key_rotation.py
- [[Validate a credential.          Returns             tuple (is_valid, message)]] - rationale - gateway/security/key_rotation.py
- [[Whether credential age warrants a warning.]] - rationale - gateway/security/key_rotation.py
- [[Whether credential needs rotation based on age.]] - rationale - gateway/security/key_rotation.py
- [[EXPERIMENTAL Generate a new credential value.          WARNING This method ge]] - rationale - gateway/security/key_rotation.py
- [[credentials_health()]] - code - gateway/web/management.py
- [[credentials_status()]] - code - gateway/web/management.py
- [[rotate_credential()]] - code - gateway/web/management.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_130
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Community 295]]
- 10 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 10 edges to [[_COMMUNITY_Community 226]]
- 6 edges to [[_COMMUNITY_Community 174]]
- 4 edges to [[_COMMUNITY_Community 533]]
- 4 edges to [[_COMMUNITY_Community 432]]
- 2 edges to [[_COMMUNITY_Community 810]]
- 2 edges to [[_COMMUNITY_Community 692]]
- 1 edge to [[_COMMUNITY_Middleware & Lifespan]]
- 1 edge to [[_COMMUNITY_Community 1271]]

## Top bridge nodes
- [[KeyRotationManager]] - degree 55, connects to 10 communities
- [[.should_rotate()]] - degree 7, connects to 2 communities
- [[.should_warn()]] - degree 6, connects to 2 communities
- [[.register_credential()]] - degree 5, connects to 2 communities
- [[credentials_health()]] - degree 4, connects to 2 communities