---
type: community
cohesion: 0.15
members: 15
---

# CredentialInjector

**Cohesion:** 0.15 - loosely connected
**Members:** 15 nodes

## Members
- [[.injector()]] - code - gateway/tests/test_credential_isolation.py
- [[.injector()_1]] - code - gateway/tests/test_credential_isolation.py
- [[.injector_with_secrets()]] - code - gateway/tests/test_credential_isolation.py
- [[.test_has_credential()]] - code - gateway/tests/test_credential_isolation.py
- [[.test_inject_anthropic_key()]] - code - gateway/tests/test_credential_isolation.py
- [[.test_inject_openai_key()]] - code - gateway/tests/test_credential_isolation.py
- [[.test_leak_detection_disabled()_1]] - code - gateway/tests/test_credential_isolation.py
- [[.test_no_injection_unknown_domain()]] - code - gateway/tests/test_credential_isolation.py
- [[.test_no_injection_when_disabled()]] - code - gateway/tests/test_credential_isolation.py
- [[.test_no_secrets_loaded_from_empty_dir()]] - code - gateway/tests/test_credential_isolation.py
- [[.test_status_report()]] - code - gateway/tests/test_credential_isolation.py
- [[Agent container should have no secrets.]] - rationale - gateway/tests/test_credential_isolation.py
- [[CredentialInjector_1]] - code - gateway/tests/test_credential_injector.py
- [[Test the CredentialInjector module.]] - rationale - gateway/tests/test_credential_isolation.py
- [[TestCredentialInjector]] - code - gateway/tests/test_credential_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CredentialInjector
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_TestCredentialInjection]]
- 2 edges to [[_COMMUNITY_TestCredentialLeakDetection]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TestLeakDetection]]
- 1 edge to [[_COMMUNITY_TestLoadAllSecretFileValues]]
- 1 edge to [[_COMMUNITY_TestDockerSecretIsolation]]
- 1 edge to [[_COMMUNITY_TestOAuthInjection]]
- 1 edge to [[_COMMUNITY_test_credential_injector.py]]

## Top bridge nodes
- [[CredentialInjector_1]] - degree 13, connects to 6 communities
- [[TestCredentialInjector]] - degree 12, connects to 2 communities
- [[.injector()_1]] - degree 2, connects to 1 community
- [[.test_leak_detection_disabled()_1]] - degree 2, connects to 1 community