---
type: community
cohesion: 0.15
members: 15
---

# setup-https-proxy.js

**Cohesion:** 0.15 - loosely connected
**Members:** 15 nodes

## Members
- [[dot-injector()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-injector()_1]] - code - gateway/tests/test_credential_isolation.py
- [[dot-injector_with_secrets()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-test_has_credential()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-test_inject_anthropic_key()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-test_inject_openai_key()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-test_leak_detection_disabled()_1]] - code - gateway/tests/test_credential_isolation.py
- [[dot-test_no_injection_unknown_domain()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-test_no_injection_when_disabled()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-test_no_secrets_loaded_from_empty_dir()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-test_status_report()]] - code - gateway/tests/test_credential_isolation.py
- [[Agent container should have no secrets.]] - rationale - gateway/tests/test_credential_isolation.py
- [[CredentialInjector]] - code - gateway/tests/test_credential_injector.py
- [[Test the CredentialInjector module.]] - rationale - gateway/tests/test_credential_isolation.py
- [[TestCredentialInjector]] - code - gateway/tests/test_credential_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/setup-https-proxyjs
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_multi_host_test.py]]
- 2 edges to [[_COMMUNITY_ModeRequest (3)]]
- 1 edge to [[_COMMUNITY_Restart Procedure (3)]]
- 1 edge to [[_COMMUNITY_i-eightd SKILL — 8D Root Cause Analysis]]
- 1 edge to [[_COMMUNITY_Browser Fetch Skill]]
- 1 edge to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_AgentShroud System Status Report]]
- 1 edge to [[_COMMUNITY_test_voice_latency_guard.py (2)]]

## Top bridge nodes
- [[CredentialInjector]] - degree 13, connects to 6 communities
- [[TestCredentialInjector]] - degree 12, connects to 2 communities
- [[dot-injector()_1]] - degree 2, connects to 1 community
- [[dot-test_leak_detection_disabled()_1]] - degree 2, connects to 1 community
