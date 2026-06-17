---
type: community
cohesion: 0.20
members: 10
---

# Module Group 383

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_anthropic_default_strips_x_api_key()]] - code - gateway/tests/test_credential_injector.py
- [[.test_credential_injected_into_request()]] - code - gateway/tests/test_credential_injector.py
- [[.test_credential_not_injected_for_unknown_domain()]] - code - gateway/tests/test_credential_injector.py
- [[.test_has_credential_false_for_missing()]] - code - gateway/tests/test_credential_injector.py
- [[.test_has_credential_true_for_loaded()]] - code - gateway/tests/test_credential_injector.py
- [[.test_injection_disabled()]] - code - gateway/tests/test_credential_injector.py
- [[.test_strip_headers_removes_conflicting_header()]] - code - gateway/tests/test_credential_injector.py
- [[Default Anthropic mapping must strip x-api-key (regression guard).]] - rationale - gateway/tests/test_credential_injector.py
- [[TestCredentialInjection]] - code - gateway/tests/test_credential_injector.py
- [[strip_headers must remove x-api-key before injecting Authorization Bearer.]] - rationale - gateway/tests/test_credential_injector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_383
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Module Group 288]]
- 1 edge to [[_COMMUNITY_Module Group 409]]

## Top bridge nodes
- [[TestCredentialInjection]] - degree 8, connects to 1 community
- [[.test_anthropic_default_strips_x_api_key()]] - degree 3, connects to 1 community
- [[.test_strip_headers_removes_conflicting_header()]] - degree 3, connects to 1 community
- [[.test_injection_disabled()]] - degree 2, connects to 1 community