---
type: community
members: 9
---

# KeyLeakDetector

**Members:** 9 nodes

## Members
- [[dot-__init__()_76]] - code - gateway/security/key_vault.py
- [[dot-scan_outbound()]] - code - gateway/security/key_vault.py
- [[dot-test_detect_api_key_patterns()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_detect_key_in_outbound()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_leak_detection_logged()]] - code - gateway/tests/test_key_vault.py
- [[dot-test_no_leak_clean_message()]] - code - gateway/tests/test_key_vault.py
- [[KeyLeakDetector]] - code - gateway/security/key_vault.py
- [[LeakScanResult]] - code - gateway/security/key_vault.py
- [[TestKeyLeakDetection]] - code - gateway/tests/test_key_vault.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyLeakDetector
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_KeyVault]]
- 2 edges to [[_COMMUNITY_KeyVaultConfig]]
- 2 edges to [[_COMMUNITY_TestKeyLeakDetection]]
- 2 edges to [[_COMMUNITY_test_key_vault.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_run]]

## Top bridge nodes
- [[KeyLeakDetector]] - degree 14, connects to 6 communities
- [[TestKeyLeakDetection]] - degree 8, connects to 3 communities
- [[dot-test_detect_api_key_patterns()]] - degree 4, connects to 2 communities
- [[dot-scan_outbound()]] - degree 3, connects to 1 community
- [[LeakScanResult]] - degree 2, connects to 1 community
