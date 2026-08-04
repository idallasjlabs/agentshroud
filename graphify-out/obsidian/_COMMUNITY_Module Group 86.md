---
type: community
cohesion: 0.06
members: 46
---

# Module Group 86

**Cohesion:** 0.06 - loosely connected
**Members:** 46 nodes

## Members
- [[._parse_service_network_config()]] - code - gateway/security/network_validator.py
- [[._validate_container_runtime_config()]] - code - gateway/security/network_validator.py
- [[._validate_dns_configuration()]] - code - gateway/security/network_validator.py
- [[._validate_network_definitions()]] - code - gateway/security/network_validator.py
- [[._validate_network_modes()]] - code - gateway/security/network_validator.py
- [[._validate_port_exposure()]] - code - gateway/security/network_validator.py
- [[._validate_privileged_containers()]] - code - gateway/security/network_validator.py
- [[._validate_service_network_isolation()]] - code - gateway/security/network_validator.py
- [[.detect_configuration_drift()]] - code - gateway/security/network_validator.py
- [[.export_report()]] - code - gateway/security/network_validator.py
- [[.get_security_report()]] - code - gateway/security/network_validator.py
- [[.test_clean_compose_yields_zero_critical()]] - code - gateway/tests/test_network_validator_gate.py
- [[.test_get_security_report_shape()]] - code - gateway/tests/test_network_validator_gate.py
- [[.test_privileged_service_is_critical()]] - code - gateway/tests/test_network_validator_gate.py
- [[.test_validator_knows_the_two_real_networks()]] - code - gateway/tests/test_network_validator_gate.py
- [[.validate_docker_compose_config()]] - code - gateway/security/network_validator.py
- [[.validate_runtime_configuration()]] - code - gateway/security/network_validator.py
- [[A network security finding.]] - rationale - gateway/security/network_validator.py
- [[A privileged container is the textbook escape-the-sandbox finding —         vali]] - rationale - gateway/tests/test_network_validator_gate.py
- [[Any_45]] - code - gateway/security/network_validator.py
- [[Container network configuration.]] - rationale - gateway/security/network_validator.py
- [[Convenience function to validate network security.]] - rationale - gateway/security/network_validator.py
- [[Detect drift between compose file and runtime configuration.]] - rationale - gateway/security/network_validator.py
- [[Export network security report to file.]] - rationale - gateway/security/network_validator.py
- [[Get comprehensive network security report.]] - rationale - gateway/security/network_validator.py
- [[NetworkConfiguration]] - code - gateway/security/network_validator.py
- [[NetworkSecurityFinding]] - code - gateway/security/network_validator.py
- [[Parse network configuration for a service.]] - rationale - gateway/security/network_validator.py
- [[Path_26]] - code - gateway/tests/test_network_validator_gate.py
- [[TestExpectedNetworksAllowlist]] - code - gateway/tests/test_network_validator_gate.py
- [[TestGateScope]] - code - gateway/tests/test_network_validator_gate.py
- [[TestValidatorAPI]] - code - gateway/tests/test_network_validator_gate.py
- [[Validate DNS configuration for security.]] - rationale - gateway/security/network_validator.py
- [[Validate a single container's runtime network configuration.]] - rationale - gateway/security/network_validator.py
- [[Validate docker-compose network configuration.          Args             compos]] - rationale - gateway/security/network_validator.py
- [[Validate network definitions in compose file.]] - rationale - gateway/security/network_validator.py
- [[Validate network mode configurations.]] - rationale - gateway/security/network_validator.py
- [[Validate port exposure configuration.]] - rationale - gateway/security/network_validator.py
- [[Validate runtime network configuration using Docker API.]] - rationale - gateway/security/network_validator.py
- [[Validate service network isolation.]] - rationale - gateway/security/network_validator.py
- [[Validate that no containers are running in privileged mode.]] - rationale - gateway/security/network_validator.py
- [[post-deploy-check.sh fails ONLY on critical. These tests pin that contract.]] - rationale - gateway/tests/test_network_validator_gate.py
- [[test_network_validator.py]] - code - gateway/tests/test_network_validator.py
- [[test_network_validator_gate.py]] - code - gateway/tests/test_network_validator_gate.py
- [[tmp_compose()]] - code - gateway/tests/test_network_validator_gate.py
- [[validate_network_security()]] - code - gateway/security/network_validator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_86
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 3 edges to [[_COMMUNITY_Module Group 201]]

## Top bridge nodes
- [[NetworkSecurityFinding]] - degree 15, connects to 2 communities
- [[test_network_validator.py]] - degree 3, connects to 2 communities
- [[.validate_docker_compose_config()]] - degree 12, connects to 1 community
- [[validate_network_security()]] - degree 9, connects to 1 community
- [[NetworkConfiguration]] - degree 8, connects to 1 community
