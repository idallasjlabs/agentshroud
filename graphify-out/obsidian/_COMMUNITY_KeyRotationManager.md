---
type: community
cohesion: 0.09
members: 38
---

# KeyRotationManager

**Cohesion:** 0.09 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-_generate_new_credential()]] - code - gateway/security/key_rotation.py
- [[dot-_read_credential_from_1password()]] - code - gateway/security/key_rotation.py
- [[dot-_retire_old_credential_after_grace_period()]] - code - gateway/security/key_rotation.py
- [[dot-_store_credential_in_1password()]] - code - gateway/security/key_rotation.py
- [[dot-_validate_credential()]] - code - gateway/security/key_rotation.py
- [[dot-check_and_rotate_due_credentials()]] - code - gateway/security/key_rotation.py
- [[dot-cleanup_retired_credentials()]] - code - gateway/security/key_rotation.py
- [[dot-emergency_rotate_credential()]] - code - gateway/security/key_rotation.py
- [[dot-get_all_credentials_status()]] - code - gateway/security/key_rotation.py
- [[dot-get_credential_status()]] - code - gateway/security/key_rotation.py
- [[dot-get_health_score()]] - code - gateway/security/key_rotation.py
- [[dot-register_credential()]] - code - gateway/security/key_rotation.py
- [[dot-register_validator()]] - code - gateway/security/key_rotation.py
- [[dot-rotate_credential()]] - code - gateway/security/key_rotation.py
- [[dot-should_rotate()]] - code - gateway/security/key_rotation.py
- [[dot-should_warn()]] - code - gateway/security/key_rotation.py
- [[dot-validate()]] - code - gateway/security/key_rotation.py
- [[Any_11]] - code - gateway/security/key_rotation.py
- [[Calculate overall credential health score.]] - rationale - gateway/security/key_rotation.py
- [[Check all credentials and rotate those that are due.]] - rationale - gateway/security/key_rotation.py
- [[Clean up any credentials past their grace period.]] - rationale - gateway/security/key_rotation.py
- [[CredentialRotationPolicy]] - code - gateway/security/key_rotation.py
- [[Get detailed status for a credential.]] - rationale - gateway/security/key_rotation.py
- [[Get status for all managed credentials.]] - rationale - gateway/security/key_rotation.py
- [[KeyRotationManager]] - code - gateway/security/key_rotation.py
- [[Manages automated rotation of credentials with zero downtime.]] - rationale - gateway/security/key_rotation.py
- [[Perform emergency rotation of a credential.]] - rationale - gateway/security/key_rotation.py
- [[Register a credential for rotation management.]] - rationale - gateway/security/key_rotation.py
- [[Register a validator for a credential type.]] - rationale - gateway/security/key_rotation.py
- [[Retire old credential after grace period ends.]] - rationale - gateway/security/key_rotation.py
- [[Rotate a single credential with zero downtime.          Workflow generate new →]] - rationale - gateway/security/key_rotation.py
- [[Safely read a credential from 1Password using op CLI.]] - rationale - gateway/security/key_rotation.py
- [[Store a new credential in 1Password.]] - rationale - gateway/security/key_rotation.py
- [[Validate a credential using registered validator.]] - rationale - gateway/security/key_rotation.py
- [[Validate a credential.          Returns             tuple (is_valid, message)]] - rationale - gateway/security/key_rotation.py
- [[Whether credential age warrants a warning.]] - rationale - gateway/security/key_rotation.py
- [[Whether credential needs rotation based on age.]] - rationale - gateway/security/key_rotation.py
- [[EXPERIMENTAL Generate a new credential value.          WARNING This method ge]] - rationale - gateway/security/key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyRotationManager
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_CredentialValidator]]
- 11 edges to [[_COMMUNITY_MiddlewareManager]]
- 10 edges to [[_COMMUNITY_KeyRotationConfig]]
- 6 edges to [[_COMMUNITY_CredentialInfo]]
- 6 edges to [[_COMMUNITY_management.py]]
- 4 edges to [[_COMMUNITY_MockValidator]]
- 2 edges to [[_COMMUNITY_test_key_rotation.py]]

## Top bridge nodes
- [[KeyRotationManager]] - degree 55, connects to 7 communities
- [[dot-register_credential()]] - degree 5, connects to 2 communities
- [[Any_11]] - degree 13, connects to 1 community
- [[dot-should_rotate()]] - degree 7, connects to 1 community
- [[dot-should_warn()]] - degree 6, connects to 1 community
