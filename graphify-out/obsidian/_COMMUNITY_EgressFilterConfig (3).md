---
type: community
members: 4
---

# EgressFilterConfig (3)

**Members:** 4 nodes

## Members
- [[dot-matches_allowlist()]] - code - gateway/security/egress_config.py
- [[Public does domain match any pattern in the effective default allowlist…]] - rationale - gateway/security/egress_config.py
- [[Return True if domain matches any pattern (exact or ``.`` wildcard). Single…]] - rationale - gateway/security/egress_config.py
- [[domain_matches()]] - code - gateway/security/egress_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig_3
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_api.py (2)]]
- 1 edge to [[_COMMUNITY_CompetitiveIntelReport]]

## Top bridge nodes
- [[domain_matches()]] - degree 7, connects to 3 communities
- [[dot-matches_allowlist()]] - degree 3, connects to 1 community
