---
type: community
cohesion: 0.25
members: 8
---

# test_hermes_model_resolver.py (2)

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[A2AGovernanceProxy._check_peer]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy._process]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy._sanitize_message]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy.process_inbound]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy.process_outbound]] - code - gateway/security/a2a_governance.py
- [[ToolACLEnforcer._can_use_tool_impl]] - code - gateway/security/tool_acl.py
- [[TrustManager.get_trust]] - code - gateway/security/trust_manager.py
- [[TrustManager.is_tool_allowed]] - code - gateway/security/trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_hermes_model_resolverpy_2
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_record_decision()]]

## Top bridge nodes
- [[ToolACLEnforcer._can_use_tool_impl]] - degree 2, connects to 1 community
