---
type: community
cohesion: 0.07
members: 32
---

# CREDENTIAL-PROTECTION-IMPLEMENTED.md

**Cohesion:** 0.07 - loosely connected
**Members:** 32 nodes

## Members
- [[._validate_container_runtime_config()]] - code - gateway/security/network_validator.py
- [[.detect_configuration_drift()]] - code - gateway/security/network_validator.py
- [[.test_gateway_network_bridging_validation()]] - code - gateway/tests/test_network_validator.py
- [[.test_network_security_finding_structure()]] - code - gateway/tests/test_network_validator.py
- [[.test_network_validation_comprehensive_rules()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_empty_config()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_host_network_flagged()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_invalid_file()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_missing_internal_network()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_multiple_violations()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_openclaw_isolation()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_privileged_flagged()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_valid_config_passes()]] - code - gateway/tests/test_network_validator.py
- [[.validate_runtime_configuration()]] - code - gateway/security/network_validator.py
- [[A network security finding.]] - rationale - gateway/security/network_validator.py
- [[Detect drift between compose file and runtime configuration.]] - rationale - gateway/security/network_validator.py
- [[NetworkSecurityFinding]] - code - gateway/security/network_validator.py
- [[Test NetworkSecurityFinding dataclass structure.]] - rationale - gateway/tests/test_network_validator.py
- [[Test comprehensive network validation rules.]] - rationale - gateway/tests/test_network_validator.py
- [[Test detection of multiple configuration violations.]] - rationale - gateway/tests/test_network_validator.py
- [[Test handling of empty configuration.]] - rationale - gateway/tests/test_network_validator.py
- [[Test handling of invalidnon-existent files.]] - rationale - gateway/tests/test_network_validator.py
- [[Test that OpenClaw container isolation is validated.]] - rationale - gateway/tests/test_network_validator.py
- [[Test that a valid docker-compose configuration passes.]] - rationale - gateway/tests/test_network_validator.py
- [[Test that gateway service network bridging is validated.]] - rationale - gateway/tests/test_network_validator.py
- [[Test that host network mode is flagged.]] - rationale - gateway/tests/test_network_validator.py
- [[Test that missing internal network is flagged.]] - rationale - gateway/tests/test_network_validator.py
- [[Test that privileged containers are flagged.]] - rationale - gateway/tests/test_network_validator.py
- [[TestNetworkValidator]] - code - gateway/tests/test_network_validator.py
- [[Validate a single container's runtime network configuration.]] - rationale - gateway/security/network_validator.py
- [[Validate runtime network configuration using Docker API.]] - rationale - gateway/security/network_validator.py
- [[test_network_validator.py]] - code - gateway/tests/test_network_validator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CREDENTIAL-PROTECTION-IMPLEMENTEDmd
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_AgentShroud Security Value Proposition - REVISED]]
- 1 edge to [[_COMMUNITY_AgentShroud™ Telegram-Reported Issues]]

## Top bridge nodes
- [[.validate_runtime_configuration()]] - degree 6, connects to 2 communities
- [[NetworkSecurityFinding]] - degree 15, connects to 1 community
- [[TestNetworkValidator]] - degree 15, connects to 1 community
- [[.detect_configuration_drift()]] - degree 5, connects to 1 community
- [[._validate_container_runtime_config()]] - degree 4, connects to 1 community