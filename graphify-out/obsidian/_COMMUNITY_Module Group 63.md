---
type: community
cohesion: 0.07
members: 60
---

# Module Group 63

**Cohesion:** 0.07 - loosely connected
**Members:** 60 nodes

## Members
- [[.__init__()_71]] - code - gateway/security/key_vault.py
- [[.__init__()_72]] - code - gateway/security/key_vault.py
- [[.__init__()_70]] - code - gateway/security/key_vault.py
- [[._agent_in_scope()]] - code - gateway/security/key_vault.py
- [[._log_audit()]] - code - gateway/security/key_vault.py
- [[.check_value_match()]] - code - gateway/security/key_vault.py
- [[.delete_key()]] - code - gateway/security/key_vault.py
- [[.get_audit_log()_2]] - code - gateway/security/key_vault.py
- [[.get_key()]] - code - gateway/security/key_vault.py
- [[.inject_for_request()]] - code - gateway/security/key_vault.py
- [[.list_keys()]] - code - gateway/security/key_vault.py
- [[.redact()]] - code - gateway/security/key_vault.py
- [[.rotate_key()]] - code - gateway/security/key_vault.py
- [[.scan_outbound()]] - code - gateway/security/key_vault.py
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
- [[.test_key_vault_init()]] - code - gateway/tests/test_security_audit.py
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
- [[Check if any stored key values appear in text. Returns matching key names.]] - rationale - gateway/security/key_vault.py
- [[KeyAuditEvent]] - code - gateway/security/key_vault.py
- [[KeyEntry]] - code - gateway/security/key_vault.py
- [[KeyInjector]] - code - gateway/security/key_vault.py
- [[KeyLeakDetector]] - code - gateway/security/key_vault.py
- [[KeyScope]] - code - gateway/security/key_vault.py
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
- [[config()]] - code - gateway/tests/test_key_vault.py
- [[key_vault.py]] - code - gateway/security/key_vault.py
- [[test_key_vault.py]] - code - gateway/tests/test_key_vault.py
- [[vault()]] - code - gateway/tests/test_key_vault.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_63
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_Pipeline Action & Instruction Envelope]]
- 19 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 6 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 6 edges to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 2 edges to [[_COMMUNITY_Alert Dispatcher]]
- 2 edges to [[_COMMUNITY_Module Group 137]]
- 2 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 2 edges to [[_COMMUNITY_Module Group 110]]

## Top bridge nodes
- [[KeyVault]] - degree 50, connects to 8 communities
- [[KeyVaultConfig]] - degree 38, connects to 8 communities
- [[KeyLeakDetector]] - degree 27, connects to 3 communities
- [[.test_key_vault_init()]] - degree 3, connects to 1 community