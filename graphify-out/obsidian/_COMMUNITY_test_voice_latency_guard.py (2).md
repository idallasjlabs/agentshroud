---
type: community
cohesion: 0.22
members: 9
---

# test_voice_latency_guard.py (2)

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-test_credential_never_in_logs()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_get_status_structure()]] - code - gateway/tests/test_credential_injector.py
- [[Create a temp secrets directory with a test credential.]] - rationale - gateway/tests/test_credential_injector.py
- [[CredentialInjector with a custom mapping pointing at the temp secrets.]] - rationale - gateway/tests/test_credential_injector.py
- [[TestStatus_1]] - code - gateway/tests/test_credential_injector.py
- [[Verify that raw credential values never appear in log output.]] - rationale - gateway/tests/test_credential_injector.py
- [[injector()]] - code - gateway/tests/test_credential_injector.py
- [[secrets_dir()]] - code - gateway/tests/test_credential_injector.py
- [[test_credential_injector.py]] - code - gateway/tests/test_credential_injector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_voice_latency_guardpy_2
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Restart Procedure (3)]]
- 1 edge to [[_COMMUNITY_i-eightd SKILL — 8D Root Cause Analysis]]
- 1 edge to [[_COMMUNITY_AgentShroud System Status Report]]
- 1 edge to [[_COMMUNITY_setup-https-proxy.js]]
- 1 edge to [[_COMMUNITY_multi_host_test.py]]

## Top bridge nodes
- [[test_credential_injector.py]] - degree 7, connects to 4 communities
- [[injector()]] - degree 3, connects to 1 community
