---
source_file: "gateway/security/key_rotation.py"
type: "code"
community: "Community 133"
location: "L119"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_133
---

# KeyRotationManager

## Connections
- [[dot-__init__()_12]] - `calls` [EXTRACTED]
- [[dot-__init__()_124]] - `method` [EXTRACTED]
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
- [[dot-manager()_1]] - `calls` [EXTRACTED]
- [[dot-register_credential()]] - `method` [EXTRACTED]
- [[dot-register_validator()]] - `method` [EXTRACTED]
- [[dot-rotate_credential()]] - `method` [EXTRACTED]
- [[dot-setup_manager_with_credential()]] - `calls` [EXTRACTED]
- [[dot-test_check_and_rotate_due_credentials()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[CredentialRotationPolicy_1]] - `uses` [INFERRED]
- [[EgressAllowlistResponse]] - `uses` [INFERRED]
- [[EgressAllowlistUpdate]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[KeyRotationConfig_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[Manages automated rotation of credentials with zero downtime.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[MockValidator]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestCheckAndRotateDisabled]] - `uses` [INFERRED]
- [[TestCredentialInfo]] - `uses` [INFERRED]
- [[TestCredentialRotationPolicy]] - `uses` [INFERRED]
- [[TestEmergencyAndRetire]] - `uses` [INFERRED]
- [[TestGenerateAndValidate]] - `uses` [INFERRED]
- [[TestKeyRotationConfig]] - `uses` [INFERRED]
- [[TestKeyRotationManager]] - `uses` [INFERRED]
- [[TestKeyRotationWorkflow]] - `uses` [INFERRED]
- [[TestReadFrom1Password]] - `uses` [INFERRED]
- [[TestRotateGuardBranches]] - `uses` [INFERRED]
- [[TestStatusHelpers]] - `uses` [INFERRED]
- [[TestStoreIn1Password]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[credentials_health()]] - `calls` [EXTRACTED]
- [[credentials_status()]] - `calls` [EXTRACTED]
- [[key_rotation.py]] - `contains` [EXTRACTED]
- [[management.py]] - `imports` [EXTRACTED]
- [[manager()]] - `calls` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[rotate_credential()]] - `calls` [EXTRACTED]
- [[test_key_rotation.py]] - `imports` [EXTRACTED]
- [[test_key_rotation_internals.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_133