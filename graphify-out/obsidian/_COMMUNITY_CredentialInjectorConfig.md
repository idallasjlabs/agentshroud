---
type: community
members: 17
---

# CredentialInjectorConfig

**Members:** 17 nodes

## Members
- [[dot-test_anthropic_default_strips_x_api_key()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_credential_injected_into_request()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_credential_not_injected_for_unknown_domain()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_has_credential_false_for_missing()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_has_credential_true_for_loaded()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_injection_disabled()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_leak_detection_disabled()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-test_strip_headers_removes_conflicting_header()]] - code - gateway/tests/test_credential_injector.py
- [[Configuration for the credential injector.]] - rationale - gateway/security/credential_injector.py
- [[Credential Injector — transparent credential injection for outbound requests.…]] - rationale - gateway/security/credential_injector.py
- [[CredentialInjectorConfig]] - code - gateway/security/credential_injector.py
- [[CredentialMapping]] - code - gateway/security/credential_injector.py
- [[Default Anthropic mapping must strip x-api-key (regression guard).]] - rationale - gateway/tests/test_credential_injector.py
- [[Maps a destination domain to its credential injection config.]] - rationale - gateway/security/credential_injector.py
- [[TestCredentialInjection]] - code - gateway/tests/test_credential_injector.py
- [[credential_injector.py]] - code - gateway/security/credential_injector.py
- [[strip_headers must remove x-api-key before injecting Authorization Bearer.]] - rationale - gateway/tests/test_credential_injector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CredentialInjectorConfig
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_CredentialInjector]]
- 6 edges to [[_COMMUNITY_test_credential_injector.py]]
- 3 edges to [[_COMMUNITY_load_all_secret_file_values]]
- 2 edges to [[_COMMUNITY_TestLeakDetection]]
- 2 edges to [[_COMMUNITY_TestOAuthInjection]]
- 2 edges to [[_COMMUNITY_TestCredentialInjector]]
- 2 edges to [[_COMMUNITY_TestCredentialLeakDetection]]
- 1 edge to [[_COMMUNITY_test_credential_isolation.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[CredentialInjectorConfig]] - degree 23, connects to 8 communities
- [[credential_injector.py]] - degree 7, connects to 4 communities
- [[TestCredentialInjection]] - degree 11, connects to 2 communities
- [[CredentialMapping]] - degree 8, connects to 2 communities
- [[dot-test_leak_detection_disabled()]] - degree 3, connects to 2 communities
