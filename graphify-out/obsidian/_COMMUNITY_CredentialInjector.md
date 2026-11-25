---
type: community
members: 21
---

# CredentialInjector

**Members:** 21 nodes

## Members
- [[dot-__init__()_212]] - code - gateway/security/credential_injector.py
- [[dot-_load_credentials()]] - code - gateway/security/credential_injector.py
- [[dot-_load_default_mappings()]] - code - gateway/security/credential_injector.py
- [[dot-get_all_loaded_values()]] - code - gateway/security/credential_injector.py
- [[dot-get_status()_2]] - code - gateway/security/credential_injector.py
- [[dot-has_credential()]] - code - gateway/security/credential_injector.py
- [[dot-inject_headers()_1]] - code - gateway/security/credential_injector.py
- [[dot-injector()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-injector()_1]] - code - gateway/tests/test_credential_isolation.py
- [[dot-injector_with_secrets()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-scan_for_credential_leak()]] - code - gateway/security/credential_injector.py
- [[Check if we have a loaded credential for a domain.]] - rationale - gateway/security/credential_injector.py
- [[CredentialInjector]] - code - gateway/security/credential_injector.py
- [[Inject credentials into request headers based on destination domain. Args…]] - rationale - gateway/security/credential_injector.py
- [[Injects credentials into outbound requests based on destination domain. The…]] - rationale - gateway/security/credential_injector.py
- [[Load credential values from Docker Secrets directory.]] - rationale - gateway/security/credential_injector.py
- [[Register default domain → credential mappings.]] - rationale - gateway/security/credential_injector.py
- [[Return all loaded credential values for use in outbound scrubbing…]] - rationale - gateway/security/credential_injector.py
- [[Return status for managemodules endpoint.]] - rationale - gateway/security/credential_injector.py
- [[Scan outbound content for credential patterns. Returns description of detected…]] - rationale - gateway/security/credential_injector.py
- [[fixture_130]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CredentialInjector
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_CredentialInjectorConfig]]
- 4 edges to [[_COMMUNITY_TestCredentialInjector]]
- 2 edges to [[_COMMUNITY_TestCredentialLeakDetection]]
- 2 edges to [[_COMMUNITY_TestOAuthInjection]]
- 2 edges to [[_COMMUNITY_test_credential_injector.py]]
- 1 edge to [[_COMMUNITY_load_all_secret_file_values]]
- 1 edge to [[_COMMUNITY_TestLeakDetection]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_test_credential_isolation.py]]

## Top bridge nodes
- [[CredentialInjector]] - degree 28, connects to 11 communities
- [[dot-injector()]] - degree 4, connects to 2 communities
- [[dot-injector_with_secrets()]] - degree 4, connects to 2 communities
- [[dot-injector()_1]] - degree 4, connects to 2 communities
- [[dot-__init__()_212]] - degree 4, connects to 1 community
