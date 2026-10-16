---
type: community
cohesion: 0.22
members: 9
---

# ._parse_service_network_config

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-_parse_service_network_config()]] - code - gateway/security/network_validator.py
- [[dot-_validate_network_definitions()]] - code - gateway/security/network_validator.py
- [[dot-export_report()]] - code - gateway/security/network_validator.py
- [[dot-get_security_report()]] - code - gateway/security/network_validator.py
- [[Any_7]] - code - gateway/security/network_validator.py
- [[Export network security report to file.]] - rationale - gateway/security/network_validator.py
- [[Get comprehensive network security report.]] - rationale - gateway/security/network_validator.py
- [[Parse network configuration for a service.]] - rationale - gateway/security/network_validator.py
- [[Validate network definitions in compose file.]] - rationale - gateway/security/network_validator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_parse_service_network_config
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_dot-validate_docker_compose_config]]
- 1 edge to [[_COMMUNITY_NetworkSecurityFinding]]

## Top bridge nodes
- [[dot-_validate_network_definitions()]] - degree 5, connects to 3 communities
- [[dot-_parse_service_network_config()]] - degree 5, connects to 2 communities
- [[dot-get_security_report()]] - degree 4, connects to 1 community
- [[dot-export_report()]] - degree 3, connects to 1 community
