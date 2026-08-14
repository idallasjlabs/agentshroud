---
source_file: "gateway/security/key_rotation.py"
type: "code"
community: "Gateway Test Suite"
location: "L119"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# KeyRotationManager

## Connections
- [[.__init__()_13]] - `calls` [EXTRACTED]
- [[.__init__()_85]] - `method` [EXTRACTED]
- [[._generate_new_credential()]] - `method` [EXTRACTED]
- [[._read_credential_from_1password()]] - `method` [EXTRACTED]
- [[._retire_old_credential_after_grace_period()]] - `method` [EXTRACTED]
- [[._store_credential_in_1password()]] - `method` [EXTRACTED]
- [[._validate_credential()]] - `method` [EXTRACTED]
- [[.check_and_rotate_due_credentials()]] - `method` [EXTRACTED]
- [[.cleanup_retired_credentials()]] - `method` [EXTRACTED]
- [[.emergency_rotate_credential()]] - `method` [EXTRACTED]
- [[.get_all_credentials_status()]] - `method` [EXTRACTED]
- [[.get_credential_status()]] - `method` [EXTRACTED]
- [[.get_health_score()]] - `method` [EXTRACTED]
- [[.manager()]] - `calls` [EXTRACTED]
- [[.register_credential()]] - `method` [EXTRACTED]
- [[.register_validator()]] - `method` [EXTRACTED]
- [[.rotate_credential()]] - `method` [EXTRACTED]
- [[.setup_manager_with_credential()]] - `calls` [EXTRACTED]
- [[.test_check_and_rotate_due_credentials()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[CredentialRotationPolicy_1]] - `uses` [INFERRED]
- [[EgressAllowlistResponse]] - `uses` [INFERRED]
- [[EgressAllowlistUpdate]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[KeyRotationConfig_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[Manages automated rotation of credentials with zero downtime.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[MockValidator]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
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
- [[ToolTier]] - `uses` [INFERRED]
- [[credentials_health()]] - `calls` [EXTRACTED]
- [[key_rotation.py]] - `contains` [EXTRACTED]
- [[management.py]] - `imports` [EXTRACTED]
- [[manager()_2]] - `calls` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[rotate_credential()]] - `calls` [EXTRACTED]
- [[test_key_rotation.py]] - `imports` [EXTRACTED]
- [[test_key_rotation_internals.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite