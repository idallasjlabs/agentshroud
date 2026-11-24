---
type: community
members: 14
---

# KeyVaultConfig

**Members:** 14 nodes

## Members
- [[dot-__init__()_36]] - code - gateway/security/key_vault.py
- [[dot-test_ciphertext_not_plaintext()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_different_plaintexts_different_ciphertexts()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_encrypt_decrypt_roundtrip()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_encrypt_json()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_key_rotation()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-test_key_vault_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_tampered_ciphertext_fails()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_wrong_key_fails()_1]] - code - gateway/tests/test_security_audit.py
- [[Key rotation should re-encrypt all blobs.]] - rationale - gateway/tests/test_security_audit.py
- [[KeyVaultConfig]] - code - gateway/security/key_vault.py
- [[Same plaintext encrypted twice should produce different ciphertext (random IV).]] - rationale - gateway/tests/test_security_audit.py
- [[Test encryption, key management, and secret handling.]] - rationale - gateway/tests/test_security_audit.py
- [[TestCryptography]] - code - gateway/tests/test_security_audit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyVaultConfig
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_KeyVault]]
- 2 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_KeyLeakDetector]]
- 2 edges to [[_COMMUNITY_TestKeyLeakDetection]]
- 2 edges to [[_COMMUNITY_test_key_vault.py]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_FileSandbox]]

## Top bridge nodes
- [[KeyVaultConfig]] - degree 14, connects to 8 communities
- [[TestCryptography]] - degree 14, connects to 4 communities
- [[dot-test_key_vault_init()]] - degree 3, connects to 1 community
- [[dot-__init__()_36]] - degree 2, connects to 1 community
- [[dot-test_wrong_key_fails()_1]] - degree 2, connects to 1 community
