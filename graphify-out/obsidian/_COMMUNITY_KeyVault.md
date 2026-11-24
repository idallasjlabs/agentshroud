---
type: community
members: 15
---

# KeyVault

**Members:** 15 nodes

## Members
- [[dot-_agent_in_scope()]] - code - gateway/security/key_vault.py
- [[dot-_log_audit()]] - code - gateway/security/key_vault.py
- [[dot-check_value_match()]] - code - gateway/security/key_vault.py
- [[dot-delete_key()]] - code - gateway/security/key_vault.py
- [[dot-get_audit_log()]] - code - gateway/security/key_vault.py
- [[dot-get_key()]] - code - gateway/security/key_vault.py
- [[dot-list_keys()]] - code - gateway/security/key_vault.py
- [[dot-redact()]] - code - gateway/security/key_vault.py
- [[dot-rotate_key()]] - code - gateway/security/key_vault.py
- [[dot-store_key()]] - code - gateway/security/key_vault.py
- [[Check if any stored key values appear in text. Returns matching key names.]] - rationale - gateway/security/key_vault.py
- [[KeyAuditEvent]] - code - gateway/security/key_vault.py
- [[KeyEntry]] - code - gateway/security/key_vault.py
- [[KeyVault]] - code - gateway/security/key_vault.py
- [[key_vault.py]] - code - gateway/security/key_vault.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyVault
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_KeyLeakDetector]]
- 4 edges to [[_COMMUNITY_KeyVaultConfig]]
- 3 edges to [[_COMMUNITY_test_key_vault.py]]
- 2 edges to [[_COMMUNITY_TestKeyLeakDetection]]
- 2 edges to [[_COMMUNITY_KeyInjector]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[KeyVault]] - degree 26, connects to 9 communities
- [[key_vault.py]] - degree 8, connects to 4 communities
