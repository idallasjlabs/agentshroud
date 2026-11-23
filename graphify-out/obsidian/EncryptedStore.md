---
source_file: "gateway/security/encrypted_store.py"
type: "code"
community: "EncryptedStore"
location: "L58"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EncryptedStore
---

# EncryptedStore

## Connections
- [[dot-__init__()_12]] - `method` [EXTRACTED]
- [[dot-_derive_key()]] - `method` [EXTRACTED]
- [[dot-_resolve_secret()]] - `method` [EXTRACTED]
- [[dot-decrypt()]] - `method` [EXTRACTED]
- [[dot-decrypt_b64()]] - `method` [EXTRACTED]
- [[dot-decrypt_json()]] - `method` [EXTRACTED]
- [[dot-decrypt_str()]] - `method` [EXTRACTED]
- [[dot-encrypt()]] - `method` [EXTRACTED]
- [[dot-encrypt_b64()]] - `method` [EXTRACTED]
- [[dot-get_blob_key_id()]] - `method` [EXTRACTED]
- [[dot-rotate()]] - `calls` [EXTRACTED]
- [[dot-setup_method()_5]] - `calls` [EXTRACTED]
- [[dot-store()]] - `calls` [EXTRACTED]
- [[dot-test_custom_key_id()]] - `calls` [EXTRACTED]
- [[dot-test_encrypt_decrypt_still_works_after_zeroing()]] - `calls` [EXTRACTED]
- [[dot-test_encrypted_store_constant_time()]] - `calls` [INFERRED]
- [[dot-test_encrypted_store_error_no_key_leak()]] - `calls` [INFERRED]
- [[dot-test_env_var_secret()]] - `calls` [EXTRACTED]
- [[dot-test_file_secret()]] - `calls` [EXTRACTED]
- [[dot-test_key_rotation_auto_increment()]] - `calls` [EXTRACTED]
- [[dot-test_key_rotation_with_zeroing()]] - `calls` [EXTRACTED]
- [[dot-test_no_secret_raises()]] - `calls` [EXTRACTED]
- [[dot-test_wrong_key_fails()]] - `calls` [EXTRACTED]
- [[dot-test_wrong_key_fails()_1]] - `calls` [EXTRACTED]
- [[AES-256-GCM encrypted storage with key derivation and rotation support.]] - `rationale_for` [EXTRACTED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestEncryptedStore]] - `uses` [INFERRED]
- [[TestInfoLeakage]] - `uses` [INFERRED]
- [[TestSecureZero]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[encrypted_store()]] - `uses` [INFERRED]
- [[encrypted_store.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EncryptedStore
