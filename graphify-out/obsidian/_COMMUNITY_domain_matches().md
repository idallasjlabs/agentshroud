---
type: community
cohesion: 0.50
members: 4
---

# domain_matches()

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-matches_allowlist()]] - code - gateway/security/egress_config.py
- [[Public does domain match any pattern in the effective default allowlist…]] - rationale - gateway/security/egress_config.py
- [[Return True if domain matches any pattern (exact or ``.`` wildcard). Single…]] - rationale - gateway/security/egress_config.py
- [[domain_matches()]] - code - gateway/security/egress_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/domain_matches
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 1 edge to [[_COMMUNITY_MCPPolicyEngine (2)]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor (3)]]

## Top bridge nodes
- [[domain_matches()]] - degree 7, connects to 3 communities
- [[dot-matches_allowlist()]] - degree 3, connects to 1 community
