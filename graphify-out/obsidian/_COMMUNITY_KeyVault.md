---
type: community
cohesion: 0.04
members: 56
---

# KeyVault

**Cohesion:** 0.04 - loosely connected
**Members:** 56 nodes

## Members
- [[dot-__init__()_25]] - code - gateway/security/log_sanitizer.py
- [[dot-_compile_patterns()]] - code - gateway/security/log_sanitizer.py
- [[dot-_contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[dot-_derive_key()]] - code - gateway/security/encrypted_store.py
- [[dot-_looks_like_credential()]] - code - gateway/security/env_guard.py
- [[dot-_record_leakage()]] - code - gateway/security/env_guard.py
- [[dot-check_command_execution()]] - code - gateway/security/env_guard.py
- [[dot-check_file_access()]] - code - gateway/security/env_guard.py
- [[dot-decrypt()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_json()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_str()]] - code - gateway/security/encrypted_store.py
- [[dot-encrypt()]] - code - gateway/security/encrypted_store.py
- [[dot-encrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[dot-rotate()]] - code - gateway/security/encrypted_store.py
- [[dot-scrub_command_output()]] - code - gateway/security/env_guard.py
- [[dot-store_key()]] - code - gateway/security/key_vault.py
- [[dot-test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation_with_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[Any_3]] - code - gateway/security/log_sanitizer.py
- [[Best-effort zeroing of key material using ctypes.memset.      Works on bytearray]] - rationale - gateway/security/encrypted_store.py
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Decrypt a base64-encoded blob.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt an AES-256-GCM encrypted blob.          Args             blob The encr]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as UTF-8 string.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as parsed JSON dict.]] - rationale - gateway/security/encrypted_store.py
- [[Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256.]] - rationale - gateway/security/encrypted_store.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[Encrypt and return as base64-encoded string.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt data using AES-256-GCM.          Args             data String, bytes,]] - rationale - gateway/security/encrypted_store.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
- [[KeyEntry]] - code - gateway/security/key_vault.py
- [[KeyScope]] - code - gateway/security/key_vault.py
- [[Pattern]] - code - gateway/security/log_sanitizer.py
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[Record a detected environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Scrub environment variables and API keys from command output.          Args]] - rationale - gateway/security/env_guard.py
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py
- [[env_guard.py]] - code - gateway/security/env_guard.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[get_sanitizer_stats()]] - code - gateway/security/log_sanitizer.py
- [[key_vault.py]] - code - gateway/security/key_vault.py
- [[log_sanitizer.py]] - code - gateway/security/log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyVault
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_AlertDispatcher]]
- 8 edges to [[_COMMUNITY_EgressFilterConfig]]
- 8 edges to [[_COMMUNITY_AuditChain]]
- 4 edges to [[_COMMUNITY_check_command]]
- 4 edges to [[_COMMUNITY_AgentRegistry]]
- 3 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]
- 1 edge to [[_COMMUNITY_TestLogSanitizer]]
- 1 edge to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_DataLedger]]
- 1 edge to [[_COMMUNITY_diagramsREADME]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]

## Top bridge nodes
- [[TestSecureZero]] - degree 23, connects to 6 communities
- [[FR4 Data Confidentiality]] - degree 8, connects to 5 communities
- [[env_guard.py]] - degree 10, connects to 4 communities
- [[log_sanitizer.py]] - degree 7, connects to 4 communities
- [[key_vault.py]] - degree 12, connects to 3 communities
