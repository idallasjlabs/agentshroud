---
source_file: "gateway/security/key_rotation.py"
type: "code"
community: "Community 533"
location: "L42"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_533
---

# CredentialInfo

## Connections
- [[.age_days()]] - `method` [EXTRACTED]
- [[.is_in_grace_period()]] - `method` [EXTRACTED]
- [[.register_credential()]] - `calls` [EXTRACTED]
- [[.sample_credential()]] - `calls` [EXTRACTED]
- [[.setup_manager_with_credential()]] - `calls` [EXTRACTED]
- [[.should_rotate()]] - `method` [EXTRACTED]
- [[.should_warn()]] - `method` [EXTRACTED]
- [[.test_age_calculation()]] - `calls` [EXTRACTED]
- [[.test_check_and_rotate_due_credentials()]] - `calls` [EXTRACTED]
- [[.test_get_health_score_all_healthy()]] - `calls` [EXTRACTED]
- [[.test_get_health_score_mixed_states()]] - `calls` [EXTRACTED]
- [[.test_grace_period_tracking()]] - `calls` [EXTRACTED]
- [[.test_not_due_without_force_is_rejected()]] - `calls` [EXTRACTED]
- [[.test_should_rotate()]] - `calls` [EXTRACTED]
- [[.test_should_warn()]] - `calls` [EXTRACTED]
- [[CredentialRotationPolicy_1]] - `uses` [INFERRED]
- [[Information about a managed credential.]] - `rationale_for` [EXTRACTED]
- [[KeyRotationConfig_1]] - `uses` [INFERRED]
- [[MockValidator]] - `uses` [INFERRED]
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
- [[_old_cred()]] - `calls` [EXTRACTED]
- [[key_rotation.py]] - `contains` [EXTRACTED]
- [[test_key_rotation.py]] - `imports` [EXTRACTED]
- [[test_key_rotation_internals.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_533