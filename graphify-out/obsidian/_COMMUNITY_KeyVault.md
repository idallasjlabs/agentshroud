---
type: community
cohesion: 0.04
members: 82
---

# KeyVault

**Cohesion:** 0.04 - loosely connected
**Members:** 82 nodes

## Members
- [[dot-__init__()_159]] - code - gateway/security/key_vault.py
- [[dot-__init__()_160]] - code - gateway/security/key_vault.py
- [[dot-__init__()_161]] - code - gateway/security/log_sanitizer.py
- [[dot-_agent_in_scope()]] - code - gateway/security/key_vault.py
- [[dot-_compile_patterns()_1]] - code - gateway/security/log_sanitizer.py
- [[dot-_contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[dot-_log_audit()]] - code - gateway/security/key_vault.py
- [[dot-_looks_like_credential()]] - code - gateway/security/env_guard.py
- [[dot-_record_leakage()]] - code - gateway/security/env_guard.py
- [[dot-check_command_execution()]] - code - gateway/security/env_guard.py
- [[dot-check_file_access()]] - code - gateway/security/env_guard.py
- [[dot-check_value_match()]] - code - gateway/security/key_vault.py
- [[dot-delete_key()]] - code - gateway/security/key_vault.py
- [[dot-get_audit_log()_5]] - code - gateway/security/key_vault.py
- [[dot-get_key()_1]] - code - gateway/security/key_vault.py
- [[dot-inject_for_request()]] - code - gateway/security/key_vault.py
- [[dot-list_keys()]] - code - gateway/security/key_vault.py
- [[dot-redact()]] - code - gateway/security/key_vault.py
- [[dot-rotate_key()]] - code - gateway/security/key_vault.py
- [[dot-scan_outbound()]] - code - gateway/security/key_vault.py
- [[dot-scrub_command_output()]] - code - gateway/security/env_guard.py
- [[dot-store_key()]] - code - gateway/security/key_vault.py
- [[dot-test_default_config()_5]] - code - gateway/tests/test_key_vault.py
- [[dot-test_delete_key()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_inject_auth_header()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_inject_fails_for_unscoped()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_inject_preserves_existing_headers()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_key_not_found()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_key_redacted_from_string()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_key_vault_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_list_keys_no_values()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_multiple_keys_redacted()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_no_keys_unchanged()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_old_key_in_redaction_after_rotation()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_partial_key_redacted()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_rotate_key()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_rotate_nonexistent_raises()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_rotation_logged()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_scope_enforcement_logged()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_scoped_agent_can_access()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_store_and_retrieve()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_unscoped_agent_denied()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_wildcard_scope_allows_all()]] - code - gateway/tests/test_key_vault.py
- [[Any_61]] - code - gateway/security/log_sanitizer.py
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if any stored key values appear in text. Returns matching key names.]] - rationale - gateway/security/key_vault.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[Encrypted Store Module Badge Icon]] - image - branding/icons/modules/encrypted-store-256x256.png
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
- [[KeyAuditEvent]] - code - gateway/security/key_vault.py
- [[KeyEntry]] - code - gateway/security/key_vault.py
- [[KeyInjector]] - code - gateway/security/key_vault.py
- [[KeyScope]] - code - gateway/security/key_vault.py
- [[KeyVault]] - code - gateway/security/key_vault.py
- [[KeyVaultConfig]] - code - gateway/security/key_vault.py
- [[LeakScanResult]] - code - gateway/security/key_vault.py
- [[Pattern_2]] - code - gateway/security/log_sanitizer.py
- [[Per-agent API key scoping, redaction, leak detection, and rotation]] - concept - gateway/tests/test_key_vault.py
- [[Record a detected environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Scrub environment variables and API keys from command output.          Args]] - rationale - gateway/security/env_guard.py
- [[TestKeyInjection]] - code - gateway/tests/test_key_vault.py
- [[TestKeyRedaction]] - code - gateway/tests/test_key_vault.py
- [[TestKeyRotation]] - code - gateway/tests/test_key_vault.py
- [[TestKeyScoping]] - code - gateway/tests/test_key_vault.py
- [[TestKeyStorage]] - code - gateway/tests/test_key_vault.py
- [[TestKeyVaultConfig]] - code - gateway/tests/test_key_vault.py
- [[config()_2]] - code - gateway/tests/test_key_vault.py
- [[encrypted_store.py_2]] - code - gateway/security/encrypted_store.py
- [[env_guard.py_2]] - code - gateway/security/env_guard.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[get_sanitizer_stats()]] - code - gateway/security/log_sanitizer.py
- [[key_vault.py_2]] - code - gateway/security/key_vault.py
- [[log_sanitizer.py]] - code - gateway/security/log_sanitizer.py
- [[test_key_vault.py]] - code - gateway/tests/test_key_vault.py
- [[vault()]] - code - gateway/tests/test_key_vault.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyVault
SORT file.name ASC
```

## Connections to other communities
- 45 edges to [[_COMMUNITY_AuditChain]]
- 40 edges to [[_COMMUNITY_AlertDispatcher]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_check_command]]
- 2 edges to [[_COMMUNITY_AlertDispatcher_1]]
- 2 edges to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_SessionError]]
- 1 edge to [[_COMMUNITY_AgentRegistry_1]]
- 1 edge to [[_COMMUNITY_TestLogSanitizer]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_diagramsREADME]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]

## Top bridge nodes
- [[FR4 Data Confidentiality]] - degree 8, connects to 5 communities
- [[env_guard.py_2]] - degree 10, connects to 4 communities
- [[log_sanitizer.py]] - degree 7, connects to 4 communities
- [[KeyVault]] - degree 55, connects to 3 communities
- [[KeyVaultConfig]] - degree 42, connects to 3 communities
