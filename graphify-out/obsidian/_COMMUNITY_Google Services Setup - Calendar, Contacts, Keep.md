---
type: community
cohesion: 0.09
members: 30
---

# Google Services Setup - Calendar, Contacts, Keep

**Cohesion:** 0.09 - loosely connected
**Members:** 30 nodes

## Members
- [[.register_validator()]] - code - gateway/security/key_rotation.py
- [[.test_generate_returns_typed_token()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_get_all_credentials_status_lists_registered()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_get_credential_status_none_for_unknown()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_health_score_empty_is_perfect()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_generic_exception_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_nonzero_returncode_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_success_strips_whitespace()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_timeout_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_scheduled_rotation_disabled_short_circuits()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_nonzero_returncode_is_false()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_rejects_malformed_reference()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_success()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_timeout_is_false()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_validate_with_validator_that_raises_fails_closed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_validate_without_registered_validator_passes()]] - code - gateway/tests/test_key_rotation_internals.py
- [[Base class for credential validators.]] - rationale - gateway/security/key_rotation.py
- [[CredentialValidator]] - code - gateway/security/key_rotation.py
- [[Register a validator for a credential type.]] - rationale - gateway/security/key_rotation.py
- [[RotationStatus]] - code - gateway/security/key_rotation.py
- [[Status of a credential rotation.]] - rationale - gateway/security/key_rotation.py
- [[TestCheckAndRotateDisabled]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestGenerateAndValidate]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestReadFrom1Password]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestStatusHelpers]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestStoreIn1Password]] - code - gateway/tests/test_key_rotation_internals.py
- [[key_rotation.py (KeyRotationManager)]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py (KeyRotationConfig)]] - code - gateway/security/key_rotation_config.py
- [[manager()_2]] - code - gateway/tests/test_key_rotation_internals.py
- [[test_key_rotation_internals.py]] - code - gateway/tests/test_key_rotation_internals.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Google_Services_Setup_-_Calendar_Contacts_Keep
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_OpenClaw Bot Container]]
- 9 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 8 edges to [[_COMMUNITY_test_key_rotation.py]]
- 8 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 6 edges to [[_COMMUNITY_3. Security Controls]]
- 4 edges to [[_COMMUNITY_DOCKER-VPN-NETWORKING]]
- 3 edges to [[_COMMUNITY_TestOpProxyEndpoint]]
- 2 edges to [[_COMMUNITY_4. Environment Variables]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]

## Top bridge nodes
- [[CredentialValidator]] - degree 21, connects to 8 communities
- [[RotationStatus]] - degree 20, connects to 8 communities
- [[test_key_rotation_internals.py]] - degree 17, connects to 5 communities
- [[TestReadFrom1Password]] - degree 10, connects to 3 communities
- [[TestStoreIn1Password]] - degree 10, connects to 3 communities