---
type: community
cohesion: 0.22
members: 20
---

# Quick Reference — AgentShroud

**Cohesion:** 0.22 - loosely connected
**Members:** 20 nodes

## Members
- [[.__init__()_119]] - code - gateway/security/subagent_governance.py
- [[.test_api_calls_exceed()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_no_tracking_returns_ok()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_tokens_exceed_budget()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_tokens_within_budget()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_tool_calls_budget_blocks_authorize_tool()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_warning_at_80_percent()]] - code - gateway/tests/test_subagent_governance.py
- [[Default governance instance in enforce mode.]] - rationale - gateway/tests/test_subagent_governance.py
- [[Governance in monitor mode (log but don't block).]] - rationale - gateway/tests/test_subagent_governance.py
- [[GovernanceConfig]] - code - gateway/security/subagent_governance.py
- [[Per-subagent resource limits.]] - rationale - gateway/security/subagent_governance.py
- [[ResourceBudget]] - code - gateway/security/subagent_governance.py
- [[SubagentGovernance]] - code - gateway/security/subagent_governance.py
- [[TestResourceBudgets]] - code - gateway/tests/test_subagent_governance.py
- [[Top-level governance configuration.]] - rationale - gateway/security/subagent_governance.py
- [[Unified governance layer for subagent lifecycle.      Wraps SubagentMonitor with]] - rationale - gateway/security/subagent_governance.py
- [[disabled_gov()]] - code - gateway/tests/test_subagent_governance.py
- [[gov()]] - code - gateway/tests/test_subagent_governance.py
- [[monitor_gov()]] - code - gateway/tests/test_subagent_governance.py
- [[test_subagent_governance.py]] - code - gateway/tests/test_subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Quick_Reference__AgentShroud
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_TestCanvasAuthHelpers]]
- 8 edges to [[_COMMUNITY_Skill Project Management (PM)]]
- 6 edges to [[_COMMUNITY_purge_low_value_events()]]
- 4 edges to [[_COMMUNITY_Hermes — Reference Verifier]]
- 4 edges to [[_COMMUNITY_Discovery Strategy]]
- 4 edges to [[_COMMUNITY_Mnemosyne — Retention Engineer]]
- 3 edges to [[_COMMUNITY_Vulcan — Subject Matter Auditor]]
- 3 edges to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]

## Top bridge nodes
- [[SubagentGovernance]] - degree 30, connects to 8 communities
- [[GovernanceConfig]] - degree 17, connects to 6 communities
- [[ResourceBudget]] - degree 13, connects to 6 communities
- [[test_subagent_governance.py]] - degree 17, connects to 5 communities
- [[TestResourceBudgets]] - degree 12, connects to 1 community