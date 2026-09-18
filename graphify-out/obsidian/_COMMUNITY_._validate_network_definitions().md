---
type: community
cohesion: 0.29
members: 7
---

# ._validate_network_definitions()

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[._validate_network_definitions()]] - code - gateway/security/network_validator.py
- [[.export_report()]] - code - gateway/security/network_validator.py
- [[.get_security_report()]] - code - gateway/security/network_validator.py
- [[Any_12]] - code - gateway/security/network_validator.py
- [[Export network security report to file.]] - rationale - gateway/security/network_validator.py
- [[Get comprehensive network security report.]] - rationale - gateway/security/network_validator.py
- [[Validate network definitions in compose file.]] - rationale - gateway/security/network_validator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_validate_network_definitions
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_.validate_docker_compose_config()]]
- 1 edge to [[_COMMUNITY_NetworkSecurityFinding]]

## Top bridge nodes
- [[._validate_network_definitions()]] - degree 5, connects to 3 communities
- [[.get_security_report()]] - degree 4, connects to 1 community
- [[Any_12]] - degree 3, connects to 1 community
- [[.export_report()]] - degree 3, connects to 1 community