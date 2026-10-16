---
type: community
cohesion: 0.04
members: 66
---

# KillSwitchMonitor

**Cohesion:** 0.04 - loosely connected
**Members:** 66 nodes

## Members
- [[dot-__init__()_29]] - code - gateway/security/encrypted_store.py
- [[dot-_derive_key()]] - code - gateway/security/encrypted_store.py
- [[dot-_resolve_secret()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_json()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_str()]] - code - gateway/security/encrypted_store.py
- [[dot-encrypt()]] - code - gateway/security/encrypted_store.py
- [[dot-encrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[dot-get_blob_key_id()]] - code - gateway/security/encrypted_store.py
- [[dot-rotate()]] - code - gateway/security/encrypted_store.py
- [[dot-setup_method()_3]] - code - gateway/tests/test_security_hardening.py
- [[dot-store()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_b64_roundtrip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_ciphertext_not_plaintext()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_custom_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_different_encryptions_differ()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_different_plaintexts_different_ciphertexts()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_encrypt_decrypt_bytes()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_dict()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_roundtrip()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_encrypt_decrypt_string()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_json()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_encrypted_store_constant_time()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_encrypted_store_error_no_key_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_env_var_secret()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_file_secret()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_blob_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_invalid_blob_too_short()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_invalid_blob_version()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_key_rotation()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation_auto_increment()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_large_data()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_secret_raises()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_tampered_ciphertext_fails()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_wrong_key_fails()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_wrong_key_fails()_1]] - code - gateway/tests/test_security_hardening.py
- [[AES-256-GCM encrypted storage with key derivation and rotation support.]] - rationale - gateway/security/encrypted_store.py
- [[Best-effort zeroing of key material using ctypes.memset.      Works on bytearray]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt a base64-encoded blob.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt an AES-256-GCM encrypted blob.          Args             blob The encr]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as UTF-8 string.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as parsed JSON dict.]] - rationale - gateway/security/encrypted_store.py
- [[Decryption errors shouldn't expose the encryption key.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt and return as base64-encoded string.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt data using AES-256-GCM.          Args             data String, bytes,]] - rationale - gateway/security/encrypted_store.py
- [[EncryptedStore]] - code - gateway/security/encrypted_store.py
- [[Encryptiondecryption time should not leak plaintext length.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Extract the key_id from an encrypted blob without decrypting.]] - rationale - gateway/security/encrypted_store.py
- [[Initialize the encrypted store.          Args             master_secret The ma]] - rationale - gateway/security/encrypted_store.py
- [[Key rotation should re-encrypt all blobs.]] - rationale - gateway/tests/test_security_audit.py
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[Resolve master secret from args, file, or environment.]] - rationale - gateway/security/encrypted_store.py
- [[Same plaintext encrypted twice should produce different ciphertext (random IV).]] - rationale - gateway/tests/test_security_audit.py
- [[Same plaintext should produce different blobs (random saltnonce).]] - rationale - gateway/tests/test_security_hardening.py
- [[Test encryption, key management, and secret handling.]] - rationale - gateway/tests/test_security_audit.py
- [[TestCryptography]] - code - gateway/tests/test_security_audit.py
- [[TestEncryptedStore]] - code - gateway/tests/test_security_hardening.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py
- [[alert_dispatcher.py]] - code - gateway/security/alert_dispatcher.py
- [[canary.py]] - code - gateway/security/canary.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KillSwitchMonitor
SORT file.name ASC
```

## Connections to other communities
- 38 edges to [[_COMMUNITY_AlertDispatcher]]
- 16 edges to [[_COMMUNITY_EgressFilterConfig]]
- 4 edges to [[_COMMUNITY_PIIConfig]]
- 4 edges to [[_COMMUNITY_test_telegram_proxy_outbound.py_1]]
- 4 edges to [[_COMMUNITY_AlertDispatcher_1]]
- 4 edges to [[_COMMUNITY_AgentRegistry]]
- 4 edges to [[_COMMUNITY_TrustConfig]]
- 3 edges to [[_COMMUNITY_AgentTarget_2]]
- 3 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 3 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_egress_filter.py]]
- 2 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 2 edges to [[_COMMUNITY_TrustConfig_1]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig_1]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_ResourceGuard_1]]
- 1 edge to [[_COMMUNITY_parse_clamscan_output]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_ClamAV]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_6]]
- 1 edge to [[_COMMUNITY_TestPathIsolationManager]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)_1]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger_1]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_3]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_1]]
- 1 edge to [[_COMMUNITY_ConsentFramework_1]]
- 1 edge to [[_COMMUNITY_validate_network_security]]
- 1 edge to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[TestCryptography]] - degree 44, connects to 16 communities
- [[EncryptedStore]] - degree 65, connects to 12 communities
- [[TestEncryptedStore]] - degree 35, connects to 8 communities
- [[alert_dispatcher.py]] - degree 10, connects to 8 communities
- [[encrypted_store.py]] - degree 6, connects to 3 communities
