---
type: community
cohesion: 0.06
members: 69
---

# Key Vault

**Cohesion:** 0.06 - loosely connected
**Members:** 69 nodes

## Members
- [[.__init__()_90]] - code - gateway/security/key_vault.py
- [[.__init__()_91]] - code - gateway/security/key_vault.py
- [[.__init__()_89]] - code - gateway/security/key_vault.py
- [[._agent_in_scope()]] - code - gateway/security/key_vault.py
- [[._log_audit()]] - code - gateway/security/key_vault.py
- [[._make_vault_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[.check_value_match()]] - code - gateway/security/key_vault.py
- [[.delete_key()]] - code - gateway/security/key_vault.py
- [[.get_audit_log()_5]] - code - gateway/security/key_vault.py
- [[.get_key()]] - code - gateway/security/key_vault.py
- [[.inject_for_request()]] - code - gateway/security/key_vault.py
- [[.list_keys()]] - code - gateway/security/key_vault.py
- [[.redact()]] - code - gateway/security/key_vault.py
- [[.rotate_key()]] - code - gateway/security/key_vault.py
- [[.scan_outbound()]] - code - gateway/security/key_vault.py
- [[.store_key()]] - code - gateway/security/key_vault.py
- [[.test_clean_response_passes_unchanged()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_default_config()_2]] - code - gateway/tests/test_key_vault.py
- [[.test_delete_key()]] - code - gateway/tests/test_key_vault.py
- [[.test_detect_api_key_patterns()]] - code - gateway/tests/test_key_vault.py
- [[.test_detect_key_in_outbound()]] - code - gateway/tests/test_key_vault.py
- [[.test_detector_failure_fails_closed_for_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_generic_key_pattern_audited_but_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_inject_auth_header()]] - code - gateway/tests/test_key_vault.py
- [[.test_inject_fails_for_unscoped()]] - code - gateway/tests/test_key_vault.py
- [[.test_inject_preserves_existing_headers()]] - code - gateway/tests/test_key_vault.py
- [[.test_key_leak_increments_sanitized_stat_and_audits()]] - code - gateway/tests/test_pipeline_unit.py
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
- [[.test_stored_key_value_redacted_from_outbound()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_unscoped_agent_denied()]] - code - gateway/tests/test_key_vault.py
- [[.test_wildcard_scope_allows_all()]] - code - gateway/tests/test_key_vault.py
- [[Check if any stored key values appear in text. Returns matching key names.]] - rationale - gateway/security/key_vault.py
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
- [[config()]] - code - gateway/tests/test_key_vault.py
- [[key_vault.py]] - code - gateway/security/key_vault.py
- [[test_key_vault.py]] - code - gateway/tests/test_key_vault.py
- [[vault()]] - code - gateway/tests/test_key_vault.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Key_Vault
SORT file.name ASC
```

## Connections to other communities
- 38 edges to [[_COMMUNITY_Pipeline Unit]]
- 15 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 12 edges to [[_COMMUNITY_OAuth & Metadata Guard]]
- 7 edges to [[_COMMUNITY_Pipeline Unit]]
- 3 edges to [[_COMMUNITY_Git Guard (security)]]
- 3 edges to [[_COMMUNITY_Security Hardening]]
- 2 edges to [[_COMMUNITY_Egress Monitor]]
- 2 edges to [[_COMMUNITY_Privilege Separation & File Sandbox]]
- 2 edges to [[_COMMUNITY_Security Audit]]
- 2 edges to [[_COMMUNITY_Resource Guard & Local Model Parity]]
- 1 edge to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Outbound Filter]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Cross Bot Trust Ledger]]
- 1 edge to [[_COMMUNITY_Security Regressions V1 2]]
- 1 edge to [[_COMMUNITY_Slack Proxy Coverage]]

## Top bridge nodes
- [[KeyVault]] - degree 55, connects to 9 communities
- [[KeyVaultConfig]] - degree 42, connects to 9 communities
- [[TestKeyLeakDetection_1]] - degree 24, connects to 8 communities
- [[key_vault.py]] - degree 13, connects to 4 communities
- [[KeyLeakDetector]] - degree 31, connects to 3 communities