---
type: community
cohesion: 0.02
members: 140
---

# Encrypted Store & Drift Detector

**Cohesion:** 0.02 - loosely connected
**Members:** 140 nodes

## Members
- [[dot-__init__()_73]] - code - gateway/security/encrypted_store.py
- [[dot-__init__()_74]] - code - gateway/security/prompt_guard.py
- [[dot-_derive_key()]] - code - gateway/security/encrypted_store.py
- [[dot-_resolve_secret()]] - code - gateway/security/encrypted_store.py
- [[dot-check_drift()]] - code - gateway/security/drift_detector.py
- [[dot-config_hash()]] - code - gateway/security/drift_detector.py
- [[dot-decrypt()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_json()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_str()]] - code - gateway/security/encrypted_store.py
- [[dot-encrypt()]] - code - gateway/security/encrypted_store.py
- [[dot-encrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[dot-from_dict()]] - code - gateway/security/drift_detector.py
- [[dot-get_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-get_blob_key_id()]] - code - gateway/security/encrypted_store.py
- [[dot-rotate()]] - code - gateway/security/encrypted_store.py
- [[dot-set_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-setup_method()_10]] - code - gateway/tests/test_security_hardening.py
- [[dot-setup_method()_11]] - code - gateway/tests/test_security_hardening.py
- [[dot-setup_method()_12]] - code - gateway/tests/test_security_hardening.py
- [[dot-setup_method()_13]] - code - gateway/tests/test_security_hardening.py
- [[dot-store()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-teardown_method()_2]] - code - gateway/tests/test_security_hardening.py
- [[dot-teardown_method()_3]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_acknowledge_alert()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_action_allowed_basic()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_action_denied_high_trust()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_action_unknown_agent()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_alerts_persisted()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_b64_roundtrip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_ula()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_localhost_variants()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_hash_changes()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_hash_consistency()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_custom_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_different_encryptions_differ()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_double_base64_injection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_drift_detector_concurrent_writes()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_encrypt_decrypt_bytes()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_dict()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_string()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_env_var_secret()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_event_type_validation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_failure_decreases_score()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_file_secret()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_fullwidth_detection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_blob_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_trust()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_trust_unknown()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_history()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_homoglyph_detection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_image_change()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_invalid_blob_too_short()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_invalid_blob_version()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation_auto_increment()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation_with_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_large_data()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_mixed_case_still_caught()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_new_capability()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_new_env_var()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_new_mount()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_baseline_no_alerts()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_drift()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_secret_raises()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_privileged_escalation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_read_only_disabled()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_register_agent()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_register_idempotent()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_removed_capability()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_rtl_override_detection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_score_never_negative()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_seccomp_drift()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_set_and_get_baseline()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_simultaneous_baseline_and_config_change()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_sqlite_persistence()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_success_increases_score()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_violation_large_decrease()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wrong_key_fails()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_wrong_key_fails()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_zero_width_evasion()]] - code - gateway/tests/test_security_hardening.py
- [[dot-to_dict()_5]] - code - gateway/security/drift_detector.py
- [[AES-256-GCM encrypted storage with key derivation and rotation support.]] - rationale - gateway/security/encrypted_store.py
- [[Args             block_threshold Score at or above which input is blocked.]] - rationale - gateway/security/prompt_guard.py
- [[Best-effort zeroing of key material using ctypes.memset.      Works on bytearray]] - rationale - gateway/security/encrypted_store.py
- [[Compare current config against baseline, return any drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[Concurrent baseline updates — SQLite is single-threaded by default.         This]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[ContainerSnapshot]] - code - gateway/security/drift_detector.py
- [[Decrypt a base64-encoded blob.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt an AES-256-GCM encrypted blob.          Args             blob The encr]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as UTF-8 string.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as parsed JSON dict.]] - rationale - gateway/security/encrypted_store.py
- [[Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256.]] - rationale - gateway/security/encrypted_store.py
- [[Double-encoded base64 injection should be caught.]] - rationale - gateway/tests/test_security_hardening.py
- [[DriftAlert]] - code - gateway/security/drift_detector.py
- [[Encrypt and return as base64-encoded string.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt data using AES-256-GCM.          Args             data String, bytes,]] - rationale - gateway/security/encrypted_store.py
- [[Encrypted Store Module Badge Icon]] - image - branding/icons/modules/encrypted-store-256x256.png
- [[EncryptedStore]] - code - gateway/security/encrypted_store.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[Extract the key_id from an encrypted blob without decrypting.]] - rationale - gateway/security/encrypted_store.py
- [[Fullwidth chars NFKC-normalized — injection defeated.]] - rationale - gateway/tests/test_security_hardening.py
- [[Initialize the encrypted store.          Args             master_secret The ma]] - rationale - gateway/security/encrypted_store.py
- [[Mix of Latin and Cyrillic should trigger homoglyph detection.]] - rationale - gateway/tests/test_security_hardening.py
- [[PatternRule]] - code - gateway/security/prompt_guard.py
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[Resolve master secret from args, file, or environment.]] - rationale - gateway/security/encrypted_store.py
- [[Retrieve baseline snapshot for a container.]] - rationale - gateway/security/drift_detector.py
- [[SHA-256 hash of the config for quick comparison.]] - rationale - gateway/security/drift_detector.py
- [[Same plaintext should produce different blobs (random saltnonce).]] - rationale - gateway/tests/test_security_hardening.py
- [[Store a known-good baseline configuration. Returns config hash.]] - rationale - gateway/security/drift_detector.py
- [[TestDriftDetector]] - code - gateway/tests/test_security_hardening.py
- [[TestDriftDetectorHardened]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[TestEncryptedStore]] - code - gateway/tests/test_security_hardening.py
- [[TestPromptGuardEvasion]] - code - gateway/tests/test_security_hardening.py
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManager]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManagerHardened]] - code - gateway/tests/test_security_hardening.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for drift detector hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for prompt guard evasion techniques.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for trust manager hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Unknown event types should not inject SQL.]] - rationale - gateway/tests/test_security_hardening.py
- [[Verify drift is detected even with rapid changes.]] - rationale - gateway/tests/test_security_hardening.py
- [[Zero-width chars between letters should not bypass detection.]] - rationale - gateway/tests/test_security_hardening.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py
- [[encrypted_store()]] - code - gateway/tests/test_security_integration.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py
- [[test_security_hardening.py]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Encrypted_Store__Drift_Detector
SORT file.name ASC
```

## Connections to other communities
- 40 edges to [[_COMMUNITY_Agent Isolation & Group Config Tests]]
- 33 edges to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 23 edges to [[_COMMUNITY_Alert Dispatcher & RBAC Reliability]]
- 23 edges to [[_COMMUNITY_Session Manager & PIIContext Guard]]
- 20 edges to [[_COMMUNITY_P3 Infrastructure Security Modules]]
- 18 edges to [[_COMMUNITY_Prompt Guard & Context Integrity]]
- 13 edges to [[_COMMUNITY_Community 182]]
- 10 edges to [[_COMMUNITY_Community 185]]
- 9 edges to [[_COMMUNITY_Community 52]]
- 9 edges to [[_COMMUNITY_Signed Instruction Envelopes & Security Pipeline]]
- 9 edges to [[_COMMUNITY_Community 167]]
- 4 edges to [[_COMMUNITY_Community 322]]
- 2 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 2 edges to [[_COMMUNITY_Community 56]]
- 2 edges to [[_COMMUNITY_File Sandbox & Privilege Separation Tests]]
- 2 edges to [[_COMMUNITY_Community 48]]
- 1 edge to [[_COMMUNITY_Ingest API & RBAC Core]]
- 1 edge to [[_COMMUNITY_Proxy Sidecar & Forwarder]]
- 1 edge to [[_COMMUNITY_Community 475]]
- 1 edge to [[_COMMUNITY_Community 44]]
- 1 edge to [[_COMMUNITY_Community 565]]

## Top bridge nodes
- [[ContainerSnapshot]] - degree 64, connects to 11 communities
- [[EncryptedStore]] - degree 65, connects to 10 communities
- [[TestDriftDetector]] - degree 35, connects to 9 communities
- [[TestEncryptedStore]] - degree 35, connects to 9 communities
- [[TestTrustManager]] - degree 35, connects to 9 communities