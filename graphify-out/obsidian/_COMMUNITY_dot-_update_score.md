---
type: community
cohesion: 0.12
members: 19
---

# ._update_score

**Cohesion:** 0.12 - loosely connected
**Members:** 19 nodes

## Members
- [[dot-_apply_decay()]] - code - gateway/security/trust_manager.py
- [[dot-_promotion_allowed()]] - code - gateway/security/trust_manager.py
- [[dot-_score_to_level()]] - code - gateway/security/trust_manager.py
- [[dot-_update_score()]] - code - gateway/security/trust_manager.py
- [[dot-get_trust()]] - code - gateway/security/trust_manager.py
- [[dot-is_action_allowed()]] - code - gateway/security/trust_manager.py
- [[dot-is_tool_allowed()_1]] - code - gateway/security/trust_manager.py
- [[dot-record_failure()]] - code - gateway/security/trust_manager.py
- [[dot-record_success()]] - code - gateway/security/trust_manager.py
- [[dot-register_agent()]] - code - gateway/security/trust_manager.py
- [[Apply time-based decay to score.]] - rationale - gateway/security/trust_manager.py
- [[Check if an agent's trust level allows a given action.]] - rationale - gateway/security/trust_manager.py
- [[Check the progressive ladder's threshold for promotion to target_level.]] - rationale - gateway/security/trust_manager.py
- [[Convert score to trust level based on thresholds.]] - rationale - gateway/security/trust_manager.py
- [[Get current trust level and score for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Per-level tool gate from the progressive trust ladder.          Tri-state True]] - rationale - gateway/security/trust_manager.py
- [[Record a failedblocked action, decreasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Record a successful action, increasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Register a new agent with initial trust.]] - rationale - gateway/security/trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_update_score
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_PIIConfig]]
- 8 edges to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[dot-_update_score()]] - degree 9, connects to 2 communities
- [[dot-get_trust()]] - degree 7, connects to 2 communities
- [[dot-_score_to_level()]] - degree 6, connects to 2 communities
- [[dot-register_agent()]] - degree 5, connects to 2 communities
- [[dot-_promotion_allowed()]] - degree 4, connects to 2 communities
