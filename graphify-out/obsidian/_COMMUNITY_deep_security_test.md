---
type: community
members: 21
---

# deep_security_test

**Members:** 21 nodes

## Members
- [[Comprehensive security integration test — tests every module with real payloads.]] - rationale - gateway/ingest_api/main.py
- [[_check_mod()]] - code - gateway/ingest_api/main.py
- [[_pii()]] - code - gateway/ingest_api/main.py
- [[atest()]] - code - gateway/ingest_api/main.py
- [[deep_security_test()]] - code - gateway/ingest_api/main.py
- [[t_alert()]] - code - gateway/ingest_api/main.py
- [[t_audit()]] - code - gateway/ingest_api/main.py
- [[t_auth()]] - code - gateway/ingest_api/main.py
- [[t_canary()]] - code - gateway/ingest_api/main.py
- [[t_clamav()]] - code - gateway/ingest_api/main.py
- [[t_context()]] - code - gateway/ingest_api/main.py
- [[t_egress()]] - code - gateway/ingest_api/main.py
- [[t_encrypt()]] - code - gateway/ingest_api/main.py
- [[t_git()]] - code - gateway/ingest_api/main.py
- [[t_hardening()]] - code - gateway/ingest_api/main.py
- [[t_keyvault()]] - code - gateway/ingest_api/main.py
- [[t_op()]] - code - gateway/ingest_api/main.py
- [[t_prompt()]] - code - gateway/ingest_api/main.py
- [[t_trivy()]] - code - gateway/ingest_api/main.py
- [[t_trust()]] - code - gateway/ingest_api/main.py
- [[test()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/deep_security_test
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_FileSandbox]]
- 3 edges to [[_COMMUNITY_ResourceGuard]]
- 3 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_EnvironmentGuard]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_ContainerSnapshot]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_MetadataGuard]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 2 edges to [[_COMMUNITY_TestAuth]]
- 2 edges to [[_COMMUNITY_LogSanitizer]]
- 2 edges to [[_COMMUNITY_TokenValidator]]
- 1 edge to [[_COMMUNITY_test_security_integration.py]]

## Top bridge nodes
- [[deep_security_test()]] - degree 48, connects to 15 communities
- [[t_context()]] - degree 2, connects to 1 community
- [[t_egress()]] - degree 2, connects to 1 community
- [[t_encrypt()]] - degree 2, connects to 1 community
- [[t_git()]] - degree 2, connects to 1 community
