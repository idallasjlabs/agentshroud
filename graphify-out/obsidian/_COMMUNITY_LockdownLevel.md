---
type: community
members: 25
---

# LockdownLevel

**Members:** 25 nodes

## Members
- [[dot-_action()]] - code - gateway/security/progressive_lockdown.py
- [[dot-_claim_notify()]] - code - gateway/security/progressive_lockdown.py
- [[dot-_effective_level()]] - code - gateway/security/progressive_lockdown.py
- [[dot-_get_state()]] - code - gateway/security/progressive_lockdown.py
- [[dot-_refresh()]] - code - gateway/security/progressive_lockdown.py
- [[dot-escalate_to()]] - code - gateway/security/progressive_lockdown.py
- [[dot-is_suspended()]] - code - gateway/security/progressive_lockdown.py
- [[dot-level_of()]] - code - gateway/security/progressive_lockdown.py
- [[dot-record_block()]] - code - gateway/security/progressive_lockdown.py
- [[Apply decay (if enabled) and recompute the principal's level.]] - rationale - gateway/security/progressive_lockdown.py
- [[Enum_39]] - code
- [[Jump a principal directly to `level` (never lowers its current level). The…]] - rationale - gateway/security/progressive_lockdown.py
- [[LockdownAction]] - code - gateway/security/progressive_lockdown.py
- [[LockdownLevel]] - code - gateway/security/progressive_lockdown.py
- [[Progressive Lockdown — per-principal cumulative risk scoring and escalation.…]] - rationale - gateway/security/progressive_lockdown.py
- [[Record one blocked request for a principal and return the resulting action.…]] - rationale - gateway/security/progressive_lockdown.py
- [[Return True if the principal's session is currently suspended.]] - rationale - gateway/security/progressive_lockdown.py
- [[Return True the first time `level` is reached; mark it as notified.]] - rationale - gateway/security/progressive_lockdown.py
- [[Return the principal's current level (decay applied); NORMAL if unknown.]] - rationale - gateway/security/progressive_lockdown.py
- [[UserLockdownState]] - code - gateway/security/progressive_lockdown.py
- [[What the caller should do in response to this block.]] - rationale - gateway/security/progressive_lockdown.py
- [[_level_for_count()]] - code - gateway/security/progressive_lockdown.py
- [[_max_level()]] - code - gateway/security/progressive_lockdown.py
- [[progressive_lockdown.py]] - code - gateway/security/progressive_lockdown.py
- [[str_22]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LockdownLevel
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 7 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 2 edges to [[_COMMUNITY__token]]
- 2 edges to [[_COMMUNITY_test_progressive_lockdown.py]]
- 2 edges to [[_COMMUNITY_test_soc_edge.py]]
- 1 edge to [[_COMMUNITY_FakeClock]]
- 1 edge to [[_COMMUNITY_TestAgentsRegistry]]
- 1 edge to [[_COMMUNITY_ContributorManager]]

## Top bridge nodes
- [[LockdownLevel]] - degree 23, connects to 7 communities
- [[progressive_lockdown.py]] - degree 14, connects to 5 communities
- [[dot-escalate_to()]] - degree 10, connects to 1 community
- [[dot-record_block()]] - degree 9, connects to 1 community
- [[dot-_refresh()]] - degree 8, connects to 1 community
