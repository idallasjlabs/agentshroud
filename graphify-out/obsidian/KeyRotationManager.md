---
source_file: "gateway/security/key_rotation.py"
type: "code"
community: "KeyRotationManager"
location: "L119"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/KeyRotationManager
---

# KeyRotationManager

## Connections
- [[dot-__init__()]] - `calls` [EXTRACTED]
- [[dot-__init__()_41]] - `method` [EXTRACTED]
- [[dot-_generate_new_credential()]] - `method` [EXTRACTED]
- [[dot-_read_credential_from_1password()]] - `method` [EXTRACTED]
- [[dot-_retire_old_credential_after_grace_period()]] - `method` [EXTRACTED]
- [[dot-_store_credential_in_1password()]] - `method` [EXTRACTED]
- [[dot-_validate_credential()]] - `method` [EXTRACTED]
- [[dot-check_and_rotate_due_credentials()]] - `method` [EXTRACTED]
- [[dot-cleanup_retired_credentials()]] - `method` [EXTRACTED]
- [[dot-emergency_rotate_credential()]] - `method` [EXTRACTED]
- [[dot-get_all_credentials_status()]] - `method` [EXTRACTED]
- [[dot-get_credential_status()]] - `method` [EXTRACTED]
- [[dot-get_health_score()]] - `method` [EXTRACTED]
- [[dot-manager()_2]] - `calls` [EXTRACTED]
- [[dot-register_credential()]] - `method` [EXTRACTED]
- [[dot-register_validator()]] - `method` [EXTRACTED]
- [[dot-rotate_credential()]] - `method` [EXTRACTED]
- [[dot-setup_manager_with_credential()]] - `calls` [EXTRACTED]
- [[dot-test_check_and_rotate_due_credentials()]] - `calls` [EXTRACTED]
- [[KeyRotationConfig]] - `uses` [INFERRED]
- [[Manages automated rotation of credentials with zero downtime.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[TestKeyRotationManager]] - `uses` [INFERRED]
- [[TestKeyRotationWorkflow]] - `uses` [INFERRED]
- [[credentials_health()]] - `uses` [INFERRED]
- [[credentials_status()]] - `uses` [INFERRED]
- [[key_rotation.py]] - `contains` [EXTRACTED]
- [[management.py]] - `imports` [EXTRACTED]
- [[manager()]] - `uses` [INFERRED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[rotate_credential()]] - `uses` [INFERRED]
- [[test_key_rotation.py]] - `imports` [EXTRACTED]
- [[test_key_rotation_internals.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/KeyRotationManager
