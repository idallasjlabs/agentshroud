---
type: community
cohesion: 0.20
members: 10
---

# A2AGovernanceProxy._process

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[A2AGovernanceProxy._check_peer]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy._process]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy._sanitize_message]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy.process_inbound]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy.process_outbound]] - code - gateway/security/a2a_governance.py
- [[ToolACLEnforcer._can_use_tool_impl]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool_in_group_context]] - code - gateway/security/tool_acl.py
- [[TrustManager.get_trust]] - code - gateway/security/trust_manager.py
- [[TrustManager.is_tool_allowed]] - code - gateway/security/trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AGovernanceProxy_process
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_A2AMethod]]
- 1 edge to [[_COMMUNITY_Role]]

## Top bridge nodes
- [[ToolACLEnforcer.can_use_tool]] - degree 4, connects to 2 communities
