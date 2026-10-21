---
type: community
members: 70
---

# ApprovalQueueConfig (3)

**Members:** 70 nodes

## Members
- [[dot-__init__()_183]] - code - gateway/security/key_vault.py
- [[dot-__init__()_184]] - code - gateway/security/key_vault.py
- [[dot-__init__()_185]] - code - gateway/security/key_vault.py
- [[dot-_agent_in_scope()]] - code - gateway/security/key_vault.py
- [[dot-_log_audit()]] - code - gateway/security/key_vault.py
- [[dot-_make_vault_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-check_value_match()]] - code - gateway/security/key_vault.py
- [[dot-delete_key()]] - code - gateway/security/key_vault.py
- [[dot-get_audit_log()_7]] - code - gateway/security/key_vault.py
- [[dot-get_key()_1]] - code - gateway/security/key_vault.py
- [[dot-inject_for_request()]] - code - gateway/security/key_vault.py
- [[dot-list_keys()]] - code - gateway/security/key_vault.py
- [[dot-redact()]] - code - gateway/security/key_vault.py
- [[dot-rotate_key()]] - code - gateway/security/key_vault.py
- [[dot-scan_outbound()]] - code - gateway/security/key_vault.py
- [[dot-store_key()]] - code - gateway/security/key_vault.py
- [[dot-test_clean_response_passes_unchanged()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_default_config()_8]] - code - gateway/tests/test_key_vault.py
- [[dot-test_delete_key()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_detect_api_key_patterns()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_detect_key_in_outbound()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_detector_failure_fails_closed_for_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_generic_key_pattern_audited_but_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_inject_auth_header()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_inject_fails_for_unscoped()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_inject_preserves_existing_headers()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_key_leak_increments_sanitized_stat_and_audits()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_key_not_found()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_key_redacted_from_string()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_key_vault_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_leak_detection_logged()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_list_keys_no_values()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_multiple_keys_redacted()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_no_keys_unchanged()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_no_leak_clean_message()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_old_key_in_redaction_after_rotation()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_partial_key_redacted()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_rotate_key()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_rotate_nonexistent_raises()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_rotation_logged()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_scope_enforcement_logged()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_scoped_agent_can_access()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_store_and_retrieve()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_stored_key_value_redacted_from_outbound()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_unscoped_agent_denied()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_wildcard_scope_allows_all()]] - code - gateway/tests/test_key_vault.py
- [[Check if any stored key values appear in text. Returns matching key names.]] - rationale - gateway/security/key_vault.py
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[KeyAuditEvent]] - code - gateway/security/key_vault.py
- [[KeyEntry]] - code - gateway/security/key_vault.py
- [[KeyInjector]] - code - gateway/security/key_vault.py
- [[KeyLeakDetector]] - code - gateway/security/key_vault.py
- [[KeyLeakDetector wiring — stored credential values must never leave the gateway.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[KeyScope]] - code - gateway/security/key_vault.py
- [[KeyVault]] - code - gateway/security/key_vault.py
- [[KeyVaultConfig]] - code - gateway/security/key_vault.py
- [[LeakScanResult]] - code - gateway/security/key_vault.py
- [[Per-agent API key scoping, redaction, leak detection, and rotation]] - concept - gateway/tests/test_key_vault.py
- [[TestKeyInjection]] - code - gateway/tests/test_key_vault.py
- [[TestKeyLeakDetection]] - code - gateway/tests/test_key_vault.py
- [[TestKeyLeakDetection_1]] - code - gateway/tests/test_pipeline_unit.py
- [[TestKeyRedaction]] - code - gateway/tests/test_key_vault.py
- [[TestKeyRotation]] - code - gateway/tests/test_key_vault.py
- [[TestKeyScoping]] - code - gateway/tests/test_key_vault.py
- [[TestKeyStorage]] - code - gateway/tests/test_key_vault.py
- [[TestKeyVaultConfig]] - code - gateway/tests/test_key_vault.py
- [[config()_4]] - code - gateway/tests/test_key_vault.py
- [[key_vault.py_2]] - code - gateway/security/key_vault.py
- [[test_key_vault.py]] - code - gateway/tests/test_key_vault.py
- [[vault()]] - code - gateway/tests/test_key_vault.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig_3
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 17 edges to [[_COMMUNITY_ApprovalQueueConfig (2)_1]]
- 13 edges to [[_COMMUNITY__wrap_response()]]
- 6 edges to [[_COMMUNITY_ApprovalQueueConfig (4)]]
- 4 edges to [[_COMMUNITY_test_playback_state.c]]
- 3 edges to [[_COMMUNITY__wrap_response() (4)]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 2 edges to [[_COMMUNITY_Common Queries]]
- 2 edges to [[_COMMUNITY__wrap_response() (2)_1]]
- 2 edges to [[_COMMUNITY__wrap_response() (5)]]
- 2 edges to [[_COMMUNITY_FetchOutcome]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy (2)_1]]
- 1 edge to [[_COMMUNITY__make_proxy()]]
- 1 edge to [[_COMMUNITY_api.py (2)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY__wrap_response() (3)_1]]
- 1 edge to [[_COMMUNITY_Daedalus — Concept Illustrator (3)]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_Distributed OpenClaw Node Architecture — Raspberry Pi 4]]

## Top bridge nodes
- [[KeyVault]] - degree 53, connects to 11 communities
- [[KeyVaultConfig]] - degree 40, connects to 11 communities
- [[TestKeyLeakDetection_1]] - degree 24, connects to 8 communities
- [[FR4 Data Confidentiality]] - degree 8, connects to 7 communities
- [[KeyLeakDetector]] - degree 29, connects to 3 communities
