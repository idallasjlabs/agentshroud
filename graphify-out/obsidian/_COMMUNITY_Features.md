---
type: community
cohesion: 0.15
members: 15
---

# Features

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
- [[CredentialInjector]] - code - gateway/tests/test_credential_injector.py
- [[Test the CredentialInjector module.]] - rationale - gateway/tests/test_credential_isolation.py
- [[TestCredentialInjector]] - code - gateway/tests/test_credential_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Features
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_tailscale-check.sh]]
- 2 edges to [[_COMMUNITY__script()]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_ssh_proxy.py]]
- 1 edge to [[_COMMUNITY_Skill OpenClaw Dev Workflow (ODEV)]]
- 1 edge to [[_COMMUNITY_AgentShroud System Status Report]]
- 1 edge to [[_COMMUNITY_Trivy action immutable SHA pin (CI supply chain)]]
- 1 edge to [[_COMMUNITY_Marvin Dev Overlay (port and subnet offsets from]]

## Top bridge nodes
- [[CredentialInjector]] - degree 13, connects to 6 communities
- [[TestCredentialInjector]] - degree 12, connects to 2 communities
- [[.injector()_1]] - degree 2, connects to 1 community
- [[.test_leak_detection_disabled()_1]] - degree 2, connects to 1 community