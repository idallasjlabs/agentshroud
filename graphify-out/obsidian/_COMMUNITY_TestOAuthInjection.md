---
type: community
members: 16
---

# TestOAuthInjection

**Members:** 16 nodes

## Members
- [[dot-_make_anthropic_injector()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_adds_oauth_beta_header_when_injecting()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_anthropic_version_auto_injected_when_absent()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_existing_anthropic_beta_preserved_and_oauth_appended_no_duplicate()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_existing_anthropic_version_preserved()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_inject_if_absent_skips_when_bearer_already_present()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_x_api_key_stripped_and_bearer_plus_beta_injected()]] - code - gateway/tests/test_credential_injector.py
- [[Caller-supplied anthropic-version (e.g. a newer beta date) must not be…]] - rationale - gateway/tests/test_credential_injector.py
- [[Existing anthropic-beta values are kept; oauth-2025-04-20 is appended once.]] - rationale - gateway/tests/test_credential_injector.py
- [[Path_62]] - code
- [[TestOAuthInjection]] - code - gateway/tests/test_credential_injector.py
- [[Verify gateway-side OAuth-token translation for the Anthropic path. Root cause…]] - rationale - gateway/tests/test_credential_injector.py
- [[anthropic-version is required on every v1messages call; the gateway adds it…]] - rationale - gateway/tests/test_credential_injector.py
- [[inject_headers does NOT overwrite an existing Authorization Bearer token, but…]] - rationale - gateway/tests/test_credential_injector.py
- [[inject_headers sets anthropic-beta oauth-2025-04-20 when Bearer is injected.]] - rationale - gateway/tests/test_credential_injector.py
- [[x-api-key is stripped; Authorization Bearer and anthropic-beta are added.]] - rationale - gateway/tests/test_credential_injector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOAuthInjection
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_CredentialInjectorConfig]]
- 2 edges to [[_COMMUNITY_CredentialInjector]]
- 1 edge to [[_COMMUNITY_test_credential_injector.py]]

## Top bridge nodes
- [[TestOAuthInjection]] - degree 11, connects to 3 communities
- [[dot-_make_anthropic_injector()]] - degree 10, connects to 2 communities
