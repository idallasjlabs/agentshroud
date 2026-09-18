---
type: community
cohesion: 0.17
members: 16
---

# .validate_docker_compose_config()

**Cohesion:** 0.17 - loosely connected
**Members:** 16 nodes

## Members
- [[._parse_service_network_config()]] - code - gateway/security/network_validator.py
- [[._validate_dns_configuration()]] - code - gateway/security/network_validator.py
- [[._validate_network_modes()]] - code - gateway/security/network_validator.py
- [[._validate_port_exposure()]] - code - gateway/security/network_validator.py
- [[._validate_privileged_containers()]] - code - gateway/security/network_validator.py
- [[._validate_service_network_isolation()]] - code - gateway/security/network_validator.py
- [[.validate_docker_compose_config()]] - code - gateway/security/network_validator.py
- [[Container network configuration.]] - rationale - gateway/security/network_validator.py
- [[NetworkConfiguration]] - code - gateway/security/network_validator.py
- [[Parse network configuration for a service.]] - rationale - gateway/security/network_validator.py
- [[Validate DNS configuration for security.]] - rationale - gateway/security/network_validator.py
- [[Validate docker-compose network configuration.          Args             compos]] - rationale - gateway/security/network_validator.py
- [[Validate network mode configurations.]] - rationale - gateway/security/network_validator.py
- [[Validate port exposure configuration.]] - rationale - gateway/security/network_validator.py
- [[Validate service network isolation.]] - rationale - gateway/security/network_validator.py
- [[Validate that no containers are running in privileged mode.]] - rationale - gateway/security/network_validator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/validate_docker_compose_config
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_lifespan.py]]
- 7 edges to [[_COMMUNITY_NetworkSecurityFinding]]
- 2 edges to [[_COMMUNITY_._validate_network_definitions()]]
- 2 edges to [[_COMMUNITY_validate_network_security()]]

## Top bridge nodes
- [[.validate_docker_compose_config()]] - degree 12, connects to 4 communities
- [[._parse_service_network_config()]] - degree 5, connects to 2 communities
- [[._validate_dns_configuration()]] - degree 5, connects to 2 communities
- [[._validate_network_modes()]] - degree 5, connects to 2 communities
- [[._validate_port_exposure()]] - degree 5, connects to 2 communities