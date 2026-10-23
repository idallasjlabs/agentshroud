---
type: community
cohesion: 0.29
members: 7
---

# Browser Fetch Skill

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-test_compose_agent_no_gateway_secrets()]] - code - gateway/tests/test_credential_isolation.py
- [[dot-test_compose_gateway_has_secrets()]] - code - gateway/tests/test_credential_isolation.py
- [[Agent (agentshroud) service should not have credential secrets.]] - rationale - gateway/tests/test_credential_isolation.py
- [[Gateway service should have secrets configured.]] - rationale - gateway/tests/test_credential_isolation.py
- [[TestDockerSecretIsolation]] - code - gateway/tests/test_credential_isolation.py
- [[Verify Docker Compose configuration isolates secrets correctly.]] - rationale - gateway/tests/test_credential_isolation.py
- [[test_credential_isolation.py]] - code - gateway/tests/test_credential_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Browser_Fetch_Skill
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_setup-https-proxy.js]]
- 1 edge to [[_COMMUNITY_ModeRequest (3)]]

## Top bridge nodes
- [[test_credential_isolation.py]] - degree 3, connects to 2 communities
