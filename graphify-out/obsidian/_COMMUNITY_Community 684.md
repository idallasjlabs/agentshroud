---
type: community
members: 83
---

# Community 684

**Members:** 83 nodes

## Members
- [[.__init__()_89]] - code - gateway/security/key_vault.py
- [[.__init__()_90]] - code - gateway/security/key_vault.py
- [[.__init__()_93]] - code - gateway/security/log_sanitizer.py
- [[._agent_in_scope()]] - code - gateway/security/key_vault.py
- [[._compile_patterns()]] - code - gateway/security/log_sanitizer.py
- [[._contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[._log_audit()]] - code - gateway/security/key_vault.py
- [[._looks_like_credential()]] - code - gateway/security/env_guard.py
- [[._record_leakage()]] - code - gateway/security/env_guard.py
- [[.check_command_execution()]] - code - gateway/security/env_guard.py
- [[.check_file_access()]] - code - gateway/security/env_guard.py
- [[.check_value_match()]] - code - gateway/security/key_vault.py
- [[.delete_key()]] - code - gateway/security/key_vault.py
- [[.get_audit_log()_5]] - code - gateway/security/key_vault.py
- [[.get_key()]] - code - gateway/security/key_vault.py
- [[.inject_for_request()]] - code - gateway/security/key_vault.py
- [[.list_keys()]] - code - gateway/security/key_vault.py
- [[.redact()]] - code - gateway/security/key_vault.py
- [[.rotate_key()]] - code - gateway/security/key_vault.py
- [[.scan_outbound()]] - code - gateway/security/key_vault.py
- [[.scrub_command_output()]] - code - gateway/security/env_guard.py
- [[.store_key()]] - code - gateway/security/key_vault.py
- [[.test_default_config()_2]] - code - gateway/tests/test_key_vault.py
- [[.test_delete_key()]] - code - gateway/tests/test_key_vault.py
- [[.test_detect_api_key_patterns()]] - code - gateway/tests/test_key_vault.py
- [[.test_detect_key_in_outbound()]] - code - gateway/tests/test_key_vault.py
- [[.test_inject_auth_header()]] - code - gateway/tests/test_key_vault.py
- [[.test_inject_fails_for_unscoped()]] - code - gateway/tests/test_key_vault.py
- [[.test_inject_preserves_existing_headers()]] - code - gateway/tests/test_key_vault.py
- [[.test_key_not_found()]] - code - gateway/tests/test_key_vault.py
- [[.test_key_redacted_from_string()]] - code - gateway/tests/test_key_vault.py
- [[.test_leak_detection_logged()]] - code - gateway/tests/test_key_vault.py
- [[.test_list_keys_no_values()]] - code - gateway/tests/test_key_vault.py
- [[.test_multiple_keys_redacted()]] - code - gateway/tests/test_key_vault.py
- [[.test_no_keys_unchanged()]] - code - gateway/tests/test_key_vault.py
- [[.test_no_leak_clean_message()]] - code - gateway/tests/test_key_vault.py
- [[.test_old_key_in_redaction_after_rotation()]] - code - gateway/tests/test_key_vault.py
- [[.test_partial_key_redacted()]] - code - gateway/tests/test_key_vault.py
- [[.test_rotate_key()]] - code - gateway/tests/test_key_vault.py
- [[.test_rotate_nonexistent_raises()]] - code - gateway/tests/test_key_vault.py
- [[.test_rotation_logged()]] - code - gateway/tests/test_key_vault.py
- [[.test_scope_enforcement_logged()]] - code - gateway/tests/test_key_vault.py
- [[.test_scoped_agent_can_access()]] - code - gateway/tests/test_key_vault.py
- [[.test_store_and_retrieve()]] - code - gateway/tests/test_key_vault.py
- [[.test_unscoped_agent_denied()]] - code - gateway/tests/test_key_vault.py
- [[.test_wildcard_scope_allows_all()]] - code - gateway/tests/test_key_vault.py
- [[Any_46]] - code - gateway/security/log_sanitizer.py
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if any stored key values appear in text. Returns matching key names.]] - rationale - gateway/security/key_vault.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
- [[KeyAuditEvent]] - code - gateway/security/key_vault.py
- [[KeyEntry]] - code - gateway/security/key_vault.py
- [[KeyInjector]] - code - gateway/security/key_vault.py
- [[KeyScope]] - code - gateway/security/key_vault.py
- [[KeyVault]] - code - gateway/security/key_vault.py
- [[LeakScanResult]] - code - gateway/security/key_vault.py
- [[Pattern_1]] - code - gateway/security/log_sanitizer.py
- [[Per-agent API key scoping, redaction, leak detection, and rotation]] - concept - gateway/tests/test_key_vault.py
- [[Record a detected environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Scrub environment variables and API keys from command output.          Args]] - rationale - gateway/security/env_guard.py
- [[TestKeyInjection]] - code - gateway/tests/test_key_vault.py
- [[TestKeyLeakDetection]] - code - gateway/tests/test_key_vault.py
- [[TestKeyRedaction]] - code - gateway/tests/test_key_vault.py
- [[TestKeyRotation]] - code - gateway/tests/test_key_vault.py
- [[TestKeyScoping]] - code - gateway/tests/test_key_vault.py
- [[TestKeyStorage]] - code - gateway/tests/test_key_vault.py
- [[TestKeyVaultConfig]] - code - gateway/tests/test_key_vault.py
- [[agent_isolation.py]] - code - gateway/security/agent_isolation.py
- [[config()]] - code - gateway/tests/test_key_vault.py
- [[env_guard.py]] - code - gateway/security/env_guard.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[get_sanitizer_stats()]] - code - gateway/security/log_sanitizer.py
- [[key_vault.py]] - code - gateway/security/key_vault.py
- [[log_sanitizer.py]] - code - gateway/security/log_sanitizer.py
- [[test_key_vault.py]] - code - gateway/tests/test_key_vault.py
- [[vault()]] - code - gateway/tests/test_key_vault.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_684
SORT file.name ASC
```

## Connections to other communities
- 40 edges to [[_COMMUNITY_Community 0]]
- 29 edges to [[_COMMUNITY_Community 24]]
- 6 edges to [[_COMMUNITY_Community 162]]
- 5 edges to [[_COMMUNITY_Community 72]]
- 4 edges to [[_COMMUNITY_Community 362]]
- 3 edges to [[_COMMUNITY_Community 52]]
- 1 edge to [[_COMMUNITY_Community 8]]
- 1 edge to [[_COMMUNITY_Community 1148]]
- 1 edge to [[_COMMUNITY_Community 809]]
- 1 edge to [[_COMMUNITY_Community 76]]

## Top bridge nodes
- [[agent_isolation.py]] - degree 12, connects to 6 communities
- [[key_vault.py]] - degree 12, connects to 4 communities
- [[log_sanitizer.py]] - degree 7, connects to 4 communities
- [[KeyVault]] - degree 55, connects to 3 communities
- [[env_guard.py]] - degree 10, connects to 3 communities