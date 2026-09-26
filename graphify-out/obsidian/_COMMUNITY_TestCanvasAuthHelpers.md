---
type: community
cohesion: 0.18
members: 13
---

# TestCanvasAuthHelpers

**Cohesion:** 0.18 - loosely connected
**Members:** 13 nodes

## Members
- [[._log_event()]] - code - gateway/security/subagent_governance.py
- [[.authorize_spawn()]] - code - gateway/security/subagent_governance.py
- [[.get_governance_events()]] - code - gateway/security/subagent_governance.py
- [[.test_deregister_cleans_up()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_deregister_returns_usage()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_summary()_1]] - code - gateway/tests/test_subagent_governance.py
- [[Action to take when a governance limit is hit.]] - rationale - gateway/security/subagent_governance.py
- [[Authorize a subagent spawn. Returns (allowed, reason).]] - rationale - gateway/security/subagent_governance.py
- [[GovernanceAction]] - code - gateway/security/subagent_governance.py
- [[GovernanceEvent]] - code - gateway/security/subagent_governance.py
- [[GovernanceEventType]] - code - gateway/security/subagent_governance.py
- [[Retrieve governance events with optional filters.]] - rationale - gateway/security/a2a_governance.py
- [[TestLifecycle_1]] - code - gateway/tests/test_subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestCanvasAuthHelpers
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Quick Reference — AgentShroud]]
- 4 edges to [[_COMMUNITY_EncryptedStore]]
- 3 edges to [[_COMMUNITY_Vulcan — Subject Matter Auditor]]
- 3 edges to [[_COMMUNITY_Skill Project Management (PM)]]
- 2 edges to [[_COMMUNITY_Hermes — Reference Verifier]]
- 2 edges to [[_COMMUNITY_Discovery Strategy]]
- 2 edges to [[_COMMUNITY_Mnemosyne — Retention Engineer]]
- 2 edges to [[_COMMUNITY_purge_low_value_events()]]
- 1 edge to [[_COMMUNITY_hermesskillsi-bsREADME]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]

## Top bridge nodes
- [[GovernanceAction]] - degree 12, connects to 7 communities
- [[GovernanceEventType]] - degree 12, connects to 7 communities
- [[._log_event()]] - degree 8, connects to 3 communities
- [[.authorize_spawn()]] - degree 4, connects to 2 communities
- [[TestLifecycle_1]] - degree 9, connects to 1 community