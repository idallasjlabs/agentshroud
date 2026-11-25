---
type: community
members: 7
---

# .verify_shared_nothing

**Members:** 7 nodes

## Members
- [[dot-verify_network_isolation()]] - code - gateway/security/agent_isolation.py
- [[dot-verify_shared_nothing()]] - code - gateway/security/agent_isolation.py
- [[dot-verify_volume_isolation()]] - code - gateway/security/agent_isolation.py
- [[Full shared-nothing verification network + volume + security settings.]] - rationale - gateway/security/agent_isolation.py
- [[IsolationCheck]] - code - gateway/security/agent_isolation.py
- [[Verify that each agent has its own network namespace.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own volume (no shared filesystems).]] - rationale - gateway/security/agent_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/verify_shared_nothing
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AgentRegistry]]

## Top bridge nodes
- [[dot-verify_shared_nothing()]] - degree 5, connects to 1 community
- [[IsolationCheck]] - degree 4, connects to 1 community
- [[dot-verify_network_isolation()]] - degree 4, connects to 1 community
- [[dot-verify_volume_isolation()]] - degree 4, connects to 1 community
