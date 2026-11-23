---
type: community
members: 61
---

# KeyVault

**Members:** 61 nodes

## Members
- [[dot-__init__()_34]] - code - gateway/security/key_vault.py
- [[dot-__init__()_35]] - code - gateway/security/key_vault.py
- [[dot-__init__()_36]] - code - gateway/security/key_vault.py
- [[dot-_agent_in_scope()]] - code - gateway/security/key_vault.py
- [[dot-_log_audit()]] - code - gateway/security/key_vault.py
- [[dot-check_value_match()]] - code - gateway/security/key_vault.py
- [[dot-delete_key()]] - code - gateway/security/key_vault.py
- [[dot-get_audit_log()]] - code - gateway/security/key_vault.py
- [[dot-get_key()]] - code - gateway/security/key_vault.py
- [[dot-inject_for_request()]] - code - gateway/security/key_vault.py
- [[dot-list_keys()]] - code - gateway/security/key_vault.py
- [[dot-redact()]] - code - gateway/security/key_vault.py
- [[dot-rotate_key()]] - code - gateway/security/key_vault.py
- [[dot-scan_outbound()]] - code - gateway/security/key_vault.py
- [[dot-store_key()]] - code - gateway/security/key_vault.py
- [[dot-test_default_config()_1]] - code - gateway/tests/test_key_vault.py
- [[dot-test_delete_key()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_detect_api_key_patterns()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_detect_key_in_outbound()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_inject_auth_header()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_inject_fails_for_unscoped()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_inject_preserves_existing_headers()]] - code - gateway/tests/test_key_vault.py
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
- [[dot-test_unscoped_agent_denied()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_wildcard_scope_allows_all()]] - code - gateway/tests/test_key_vault.py
- [[Check if any stored key values appear in text. Returns matching key names.]] - rationale - gateway/security/key_vault.py
- [[KeyAuditEvent]] - code - gateway/security/key_vault.py
- [[KeyEntry]] - code - gateway/security/key_vault.py
- [[KeyInjector]] - code - gateway/security/key_vault.py
- [[KeyLeakDetector]] - code - gateway/security/key_vault.py
- [[KeyVault]] - code - gateway/security/key_vault.py
- [[KeyVaultConfig]] - code - gateway/security/key_vault.py
- [[LeakScanResult]] - code - gateway/security/key_vault.py
- [[TestKeyInjection]] - code - gateway/tests/test_key_vault.py
- [[TestKeyLeakDetection]] - code - gateway/tests/test_key_vault.py
- [[TestKeyRedaction]] - code - gateway/tests/test_key_vault.py
- [[TestKeyRotation]] - code - gateway/tests/test_key_vault.py
- [[TestKeyScoping]] - code - gateway/tests/test_key_vault.py
- [[TestKeyStorage]] - code - gateway/tests/test_key_vault.py
- [[TestKeyVaultConfig]] - code - gateway/tests/test_key_vault.py
- [[Tests for API key isolation and vault.]] - rationale - gateway/tests/test_key_vault.py
- [[config()]] - code - gateway/tests/test_key_vault.py
- [[fixture_24]] - code
- [[key_vault.py]] - code - gateway/security/key_vault.py
- [[test_key_vault.py]] - code - gateway/tests/test_key_vault.py
- [[vault()]] - code - gateway/tests/test_key_vault.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyVault
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_asyncio_1]]
- 3 edges to [[_COMMUNITY_EncryptedStore]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_lifespan]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[KeyVault]] - degree 26, connects to 5 communities
- [[KeyVaultConfig]] - degree 14, connects to 5 communities
- [[KeyLeakDetector]] - degree 14, connects to 3 communities
- [[dot-scan_outbound()]] - degree 3, connects to 1 community
- [[dot-test_key_vault_init()]] - degree 3, connects to 1 community
