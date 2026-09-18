---
type: community
cohesion: 0.02
members: 140
---

# EncryptedStore

**Cohesion:** 0.02 - loosely connected
**Members:** 140 nodes

## Members
- [[.__init__()_73]] - code - gateway/security/encrypted_store.py
- [[._derive_key()]] - code - gateway/security/encrypted_store.py
- [[._resolve_secret()]] - code - gateway/security/encrypted_store.py
- [[.check_drift()]] - code - gateway/security/drift_detector.py
- [[.config_hash()]] - code - gateway/security/drift_detector.py
- [[.decrypt()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_json()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_str()]] - code - gateway/security/encrypted_store.py
- [[.encrypt()]] - code - gateway/security/encrypted_store.py
- [[.encrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.from_dict()]] - code - gateway/security/drift_detector.py
- [[.get_baseline()]] - code - gateway/security/drift_detector.py
- [[.get_blob_key_id()]] - code - gateway/security/encrypted_store.py
- [[.rotate()]] - code - gateway/security/encrypted_store.py
- [[.set_baseline()]] - code - gateway/security/drift_detector.py
- [[.setup_method()_10]] - code - gateway/tests/test_security_hardening.py
- [[.setup_method()_11]] - code - gateway/tests/test_security_hardening.py
- [[.store()_1]] - code - gateway/tests/test_security_audit.py
- [[.teardown_method()_2]] - code - gateway/tests/test_security_hardening.py
- [[.test_acknowledge_alert()]] - code - gateway/tests/test_security_hardening.py
- [[.test_agent_isolation_module()]] - code - gateway/tests/test_security_audit.py
- [[.test_alerts_persisted()]] - code - gateway/tests/test_security_hardening.py
- [[.test_b64_roundtrip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_ciphertext_not_plaintext()]] - code - gateway/tests/test_security_audit.py
- [[.test_clamav_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[.test_clamav_parse_clean()]] - code - gateway/tests/test_security_audit.py
- [[.test_clamav_parse_infected()]] - code - gateway/tests/test_security_audit.py
- [[.test_config_hash_changes()]] - code - gateway/tests/test_security_hardening.py
- [[.test_config_hash_consistency()]] - code - gateway/tests/test_security_hardening.py
- [[.test_custom_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[.test_different_encryptions_differ()]] - code - gateway/tests/test_security_hardening.py
- [[.test_different_plaintexts_different_ciphertexts()]] - code - gateway/tests/test_security_audit.py
- [[.test_encrypt_decrypt_bytes()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_dict()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_roundtrip()]] - code - gateway/tests/test_security_audit.py
- [[.test_encrypt_decrypt_string()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_json()]] - code - gateway/tests/test_security_audit.py
- [[.test_encrypted_store_constant_time()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_encrypted_store_error_no_key_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_env_var_secret()]] - code - gateway/tests/test_security_hardening.py
- [[.test_file_secret()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_blob_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[.test_image_change()]] - code - gateway/tests/test_security_hardening.py
- [[.test_invalid_blob_too_short()]] - code - gateway/tests/test_security_hardening.py
- [[.test_invalid_blob_version()]] - code - gateway/tests/test_security_hardening.py
- [[.test_key_rotation()_1]] - code - gateway/tests/test_security_audit.py
- [[.test_key_rotation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_key_rotation_auto_increment()]] - code - gateway/tests/test_security_hardening.py
- [[.test_large_data()]] - code - gateway/tests/test_security_hardening.py
- [[.test_network_validator_init()]] - code - gateway/tests/test_security_audit.py
- [[.test_new_capability()]] - code - gateway/tests/test_security_hardening.py
- [[.test_new_env_var()]] - code - gateway/tests/test_security_hardening.py
- [[.test_new_mount()]] - code - gateway/tests/test_security_hardening.py
- [[.test_no_baseline_no_alerts()]] - code - gateway/tests/test_security_hardening.py
- [[.test_no_drift()]] - code - gateway/tests/test_security_hardening.py
- [[.test_no_secret_raises()]] - code - gateway/tests/test_security_hardening.py
- [[.test_privileged_escalation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_read_only_disabled()]] - code - gateway/tests/test_security_hardening.py
- [[.test_removed_capability()]] - code - gateway/tests/test_security_hardening.py
- [[.test_seccomp_drift()]] - code - gateway/tests/test_security_hardening.py
- [[.test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[.test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[.test_security_toolchain_clamav()]] - code - gateway/tests/test_security_audit.py
- [[.test_security_toolchain_falco()]] - code - gateway/tests/test_security_audit.py
- [[.test_security_toolchain_trivy()]] - code - gateway/tests/test_security_audit.py
- [[.test_security_toolchain_wazuh()]] - code - gateway/tests/test_security_audit.py
- [[.test_set_and_get_baseline()]] - code - gateway/tests/test_security_hardening.py
- [[.test_simultaneous_baseline_and_config_change()]] - code - gateway/tests/test_security_hardening.py
- [[.test_tampered_ciphertext_fails()]] - code - gateway/tests/test_security_audit.py
- [[.test_wrong_key_fails()]] - code - gateway/tests/test_security_audit.py
- [[.test_wrong_key_fails()_1]] - code - gateway/tests/test_security_hardening.py
- [[.to_dict()_3]] - code - gateway/security/canary.py
- [[.to_dict()_5]] - code - gateway/security/drift_detector.py
- [[AES-256-GCM encrypted storage with key derivation and rotation support.]] - rationale - gateway/security/encrypted_store.py
- [[Any_18]] - code - gateway/security/canary.py
- [[Any_63]] - code - gateway/security/clamav_scanner.py
- [[Best-effort zeroing of key material using ctypes.memset.      Works on bytearray]] - rationale - gateway/security/encrypted_store.py
- [[CanaryCheck]] - code - gateway/security/canary.py
- [[CanaryResult]] - code - gateway/security/canary.py
- [[Compare current config against baseline, return any drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[ContainerSnapshot]] - code - gateway/security/drift_detector.py
- [[Decrypt a base64-encoded blob.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt an AES-256-GCM encrypted blob.          Args             blob The encr]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as UTF-8 string.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as parsed JSON dict.]] - rationale - gateway/security/encrypted_store.py
- [[Decryption errors shouldn't expose the encryption key.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256.]] - rationale - gateway/security/encrypted_store.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[Drift detector catches container config changes during operation.]] - rationale - gateway/tests/test_security_integration.py
- [[DriftAlert]] - code - gateway/security/drift_detector.py
- [[Encrypt and return as base64-encoded string.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt data using AES-256-GCM.          Args             data String, bytes,]] - rationale - gateway/security/encrypted_store.py
- [[EncryptedStore]] - code - gateway/security/encrypted_store.py
- [[Encryptiondecryption time should not leak plaintext length.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[Extract the key_id from an encrypted blob without decrypting.]] - rationale - gateway/security/encrypted_store.py
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[Generate a summary dict suitable for the health report.      Args         alert_1]] - rationale - gateway/security/falco_monitor.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
- [[Individual canary check result.]] - rationale - gateway/security/canary.py
- [[Initialize the encrypted store.          Args             master_secret The ma]] - rationale - gateway/security/encrypted_store.py
- [[IsolationStatus]] - code - gateway/security/agent_isolation.py
- [[Key rotation should re-encrypt all blobs.]] - rationale - gateway/tests/test_security_audit.py
- [[Parse clamscan output into structured results.      Args         output Raw st]] - rationale - gateway/security/clamav_scanner.py
- [[Path_38]] - code - gateway/security/clamav_scanner.py
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[Resolve master secret from args, file, or environment.]] - rationale - gateway/security/encrypted_store.py
- [[Result of running the canary system.]] - rationale - gateway/security/canary.py
- [[Retrieve baseline snapshot for a container.]] - rationale - gateway/security/drift_detector.py
- [[Run ClamAV scan and return parsed results.      Args         target Directory]] - rationale - gateway/security/clamav_scanner.py
- [[SHA-256 hash of the config for quick comparison.]] - rationale - gateway/security/drift_detector.py
- [[Same plaintext encrypted twice should produce different ciphertext (random IV).]] - rationale - gateway/tests/test_security_audit.py
- [[Same plaintext should produce different blobs (random saltnonce).]] - rationale - gateway/tests/test_security_hardening.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[Store a known-good baseline configuration. Returns config hash.]] - rationale - gateway/security/drift_detector.py
- [[Test container hardening and runtime security.]] - rationale - gateway/tests/test_security_audit.py
- [[Test encryption, key management, and secret handling.]] - rationale - gateway/tests/test_security_audit.py
- [[TestContainerSecurity]] - code - gateway/tests/test_security_audit.py
- [[TestCryptography]] - code - gateway/tests/test_security_audit.py
- [[TestDriftDetector]] - code - gateway/tests/test_security_hardening.py
- [[TestEncryptedStore]] - code - gateway/tests/test_security_hardening.py
- [[Update ClamAV virus database using freshclam.      Args         freshclam_bin]] - rationale - gateway/security/clamav_scanner.py
- [[Verify drift is detected even with rapid changes.]] - rationale - gateway/tests/test_security_hardening.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py
- [[agent_isolation.py]] - code - gateway/security/agent_isolation.py
- [[alert_dispatcher.py_2]] - code - gateway/security/alert_dispatcher.py
- [[canary.py]] - code - gateway/security/canary.py
- [[clamav_scanner.py_2]] - code - gateway/security/clamav_scanner.py
- [[drift_detector.py_2]] - code - gateway/security/drift_detector.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py
- [[env_guard.py]] - code - gateway/security/env_guard.py
- [[gateway.security.trust_manager]] - code - gateway/security/trust_manager.py
- [[generate_summary()_1]] - code - gateway/security/clamav_scanner.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[parse_clamscan_output()]] - code - gateway/security/clamav_scanner.py
- [[run_clamscan()]] - code - gateway/security/clamav_scanner.py
- [[save_report()]] - code - gateway/security/clamav_scanner.py
- [[test_drift_detection_in_pipeline()]] - code - gateway/tests/test_security_integration.py
- [[update_virus_db()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EncryptedStore
SORT file.name ASC
```

## Connections to other communities
- 77 edges to [[_COMMUNITY_lifespan.py]]
- 29 edges to [[_COMMUNITY_EgressAction]]
- 27 edges to [[_COMMUNITY_AgentRegistry]]
- 26 edges to [[_COMMUNITY_test_security_audit.py]]
- 14 edges to [[_COMMUNITY_TrustManager]]
- 8 edges to [[_COMMUNITY_EgressFilterConfig]]
- 8 edges to [[_COMMUNITY_TestAuth]]
- 7 edges to [[_COMMUNITY_ResourceGuard]]
- 6 edges to [[_COMMUNITY_Enum]]
- 5 edges to [[_COMMUNITY_DNSFilterConfig]]
- 5 edges to [[_COMMUNITY_KeyVault]]
- 5 edges to [[_COMMUNITY_EgressFilter]]
- 4 edges to [[_COMMUNITY_TrustConfig]]
- 4 edges to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded S]]
- 4 edges to [[_COMMUNITY_KeyVaultConfig]]
- 4 edges to [[_COMMUNITY_test_security_integration.py]]
- 4 edges to [[_COMMUNITY_EgressPolicy]]
- 4 edges to [[_COMMUNITY_FileSandbox]]
- 3 edges to [[_COMMUNITY_TrustLevel]]
- 3 edges to [[_COMMUNITY_check_command()]]
- 3 edges to [[_COMMUNITY_TestFileSandbox]]
- 3 edges to [[_COMMUNITY_test_clamav_pipeline.py]]
- 3 edges to [[_COMMUNITY_falco_monitor.py]]
- 3 edges to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_ConsentFramework]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 2 edges to [[_COMMUNITY_clamav]]
- 1 edge to [[_COMMUNITY__make_tm()]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_cls]]
- 1 edge to [[_COMMUNITY_patch]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_health_report.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_._process_connect()]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_diagramsREADME]]

## Top bridge nodes
- [[TestContainerSecurity]] - degree 45, connects to 13 communities
- [[gateway.security.trust_manager]] - degree 18, connects to 13 communities
- [[TestCryptography]] - degree 44, connects to 12 communities
- [[ContainerSnapshot]] - degree 64, connects to 10 communities
- [[TestDriftDetector]] - degree 35, connects to 10 communities