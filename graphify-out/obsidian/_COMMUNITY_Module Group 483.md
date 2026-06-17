---
type: community
cohesion: 0.33
members: 6
---

# Module Group 483

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[._matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[.get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[.is_denylisted()]] - code - gateway/security/egress_config.py
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_483
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Egress Filter & Approval]]

## Top bridge nodes
- [[._matches_any_pattern()]] - degree 4, connects to 1 community
- [[.get_effective_allowlist()]] - degree 3, connects to 1 community
- [[.is_denylisted()]] - degree 3, connects to 1 community