---
type: community
cohesion: 0.24
members: 10
---

# NetworkSecurityFinding

**Cohesion:** 0.24 - loosely connected
**Members:** 10 nodes

## Members
- [[._validate_container_runtime_config()]] - code - gateway/security/network_validator.py
- [[.detect_configuration_drift()]] - code - gateway/security/network_validator.py
- [[.test_network_security_finding_structure()]] - code - gateway/tests/test_network_validator.py
- [[.validate_runtime_configuration()]] - code - gateway/security/network_validator.py
- [[A network security finding.]] - rationale - gateway/security/network_validator.py
- [[Detect drift between compose file and runtime configuration.]] - rationale - gateway/security/network_validator.py
- [[NetworkSecurityFinding]] - code - gateway/security/network_validator.py
- [[Test NetworkSecurityFinding dataclass structure.]] - rationale - gateway/tests/test_network_validator.py
- [[Validate a single container's runtime network configuration.]] - rationale - gateway/security/network_validator.py
- [[Validate runtime network configuration using Docker API.]] - rationale - gateway/security/network_validator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/NetworkSecurityFinding
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_.validate_docker_compose_config()]]
- 3 edges to [[_COMMUNITY_TestNetworkValidator]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_validate_network_security()]]
- 1 edge to [[_COMMUNITY_._validate_network_definitions()]]

## Top bridge nodes
- [[NetworkSecurityFinding]] - degree 15, connects to 4 communities
- [[.validate_runtime_configuration()]] - degree 6, connects to 2 communities
- [[.detect_configuration_drift()]] - degree 5, connects to 2 communities
- [[._validate_container_runtime_config()]] - degree 4, connects to 1 community
- [[.test_network_security_finding_structure()]] - degree 3, connects to 1 community