---
type: community
cohesion: 0.23
members: 22
---

# A2AGovernanceProxy

**Cohesion:** 0.23 - loosely connected
**Members:** 22 nodes

## Members
- [[.__init__()_205]] - code - gateway/security/a2a_governance.py
- [[._check_message_size()_1]] - code - gateway/security/a2a_governance.py
- [[._check_peer()_1]] - code - gateway/security/a2a_governance.py
- [[._check_rate_limit()_1]] - code - gateway/security/a2a_governance.py
- [[._check_task_concurrency()_1]] - code - gateway/security/a2a_governance.py
- [[._finalize()_1]] - code - gateway/security/a2a_governance.py
- [[._process()_1]] - code - gateway/security/a2a_governance.py
- [[._sanitize_message()_1]] - code - gateway/security/a2a_governance.py
- [[.fingerprint()]] - code - gateway/security/a2a_governance.py
- [[.fingerprint()_1]] - code - gateway/security/a2a_governance.py
- [[.get_events()_3]] - code - gateway/security/a2a_governance.py
- [[.process_inbound()_11]] - code - gateway/security/a2a_governance.py
- [[.process_outbound()_8]] - code - gateway/security/a2a_governance.py
- [[A2ADecision_1]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceConfig_1]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceEvent_1]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy_1]] - code - gateway/security/a2a_governance.py
- [[A2AMessage_1]] - code - gateway/security/a2a_governance.py
- [[Configuration for the A2A governance proxy.]] - rationale - gateway/security/a2a_governance.py
- [[Content hash for deduplication and audit.]] - rationale - gateway/security/a2a_governance.py
- [[Governance proxy for Agent-to-Agent communication.      Sits between local agent]] - rationale - gateway/security/a2a_governance.py
- [[a2a_governance.py_1]] - code - gateway/security/a2a_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AGovernanceProxy
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_A2AMessage]]
- 6 edges to [[_COMMUNITY_A2APeer]]
- 4 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY_check_upstream_cves()]]
- 1 edge to [[_COMMUNITY_.complete_task()]]
- 1 edge to [[_COMMUNITY_.update_peer_trust()]]
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]

## Top bridge nodes
- [[A2AGovernanceProxy_1]] - degree 25, connects to 4 communities
- [[A2ADecision_1]] - degree 15, connects to 3 communities
- [[a2a_governance.py_1]] - degree 8, connects to 2 communities
- [[A2AMessage_1]] - degree 13, connects to 1 community
- [[._process()_1]] - degree 12, connects to 1 community