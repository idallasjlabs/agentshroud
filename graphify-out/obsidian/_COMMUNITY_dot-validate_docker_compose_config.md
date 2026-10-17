---
type: community
members: 15
---

# .validate_docker_compose_config

**Members:** 15 nodes

## Members
- [[dot-_validate_dns_configuration()]] - code - gateway/security/network_validator.py
- [[dot-_validate_network_modes()]] - code - gateway/security/network_validator.py
- [[dot-_validate_port_exposure()]] - code - gateway/security/network_validator.py
- [[dot-_validate_privileged_containers()]] - code - gateway/security/network_validator.py
- [[dot-_validate_service_network_isolation()]] - code - gateway/security/network_validator.py
- [[dot-validate_docker_compose_config()]] - code - gateway/security/network_validator.py
- [[Container network configuration.]] - rationale - gateway/security/network_validator.py
- [[NetworkConfiguration]] - code - gateway/security/network_validator.py
- [[Validate DNS configuration for security.]] - rationale - gateway/security/network_validator.py
- [[Validate docker-compose network configuration.          Args             compos]] - rationale - gateway/security/network_validator.py
- [[Validate network mode configurations.]] - rationale - gateway/security/network_validator.py
- [[Validate port exposure configuration.]] - rationale - gateway/security/network_validator.py
- [[Validate service network isolation.]] - rationale - gateway/security/network_validator.py
- [[Validate that no containers are running in privileged mode.]] - rationale - gateway/security/network_validator.py
- [[network_validator.py]] - code - gateway/security/network_validator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/validate_docker_compose_config
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_NetworkSecurityFinding]]
- 7 edges to [[_COMMUNITY_AlertDispatcher]]
- 3 edges to [[_COMMUNITY_dot-_parse_service_network_config]]
- 3 edges to [[_COMMUNITY_validate_network_security]]

## Top bridge nodes
- [[dot-validate_docker_compose_config()]] - degree 12, connects to 4 communities
- [[network_validator.py]] - degree 5, connects to 3 communities
- [[dot-_validate_dns_configuration()]] - degree 5, connects to 2 communities
- [[dot-_validate_network_modes()]] - degree 5, connects to 2 communities
- [[dot-_validate_port_exposure()]] - degree 5, connects to 2 communities
