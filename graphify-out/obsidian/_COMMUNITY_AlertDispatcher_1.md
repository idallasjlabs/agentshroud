---
type: community
cohesion: 0.11
members: 19
---

# AlertDispatcher

**Cohesion:** 0.11 - loosely connected
**Members:** 19 nodes

## Members
- [[dot-setup_method()_34]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_b64_roundtrip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_custom_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_different_encryptions_differ()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_bytes()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_dict()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_string()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_env_var_secret()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_file_secret()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_blob_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_invalid_blob_too_short()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_invalid_blob_version()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation_auto_increment()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_large_data()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_secret_raises()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wrong_key_fails()_1]] - code - gateway/tests/test_security_hardening.py
- [[Same plaintext should produce different blobs (random saltnonce).]] - rationale - gateway/tests/test_security_hardening.py
- [[TestEncryptedStore]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AlertDispatcher
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_AlertDispatcher]]
- 6 edges to [[_COMMUNITY_EgressFilterConfig]]
- 3 edges to [[_COMMUNITY_PIIConfig]]
- 3 edges to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[TestEncryptedStore]] - degree 35, connects to 6 communities
- [[dot-setup_method()_34]] - degree 2, connects to 1 community
- [[dot-test_custom_key_id()]] - degree 2, connects to 1 community
- [[dot-test_env_var_secret()]] - degree 2, connects to 1 community
- [[dot-test_file_secret()]] - degree 2, connects to 1 community
