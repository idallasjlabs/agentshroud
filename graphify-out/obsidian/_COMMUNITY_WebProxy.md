---
type: community
cohesion: 0.04
members: 75
---

# WebProxy

**Cohesion:** 0.04 - loosely connected
**Members:** 75 nodes

## Members
- [[dot-__init__()_177]] - code - gateway/security/network_validator.py
- [[dot-_parse_service_network_config()]] - code - gateway/security/network_validator.py
- [[dot-_validate_container_runtime_config()]] - code - gateway/security/network_validator.py
- [[dot-_validate_dns_configuration()]] - code - gateway/security/network_validator.py
- [[dot-_validate_network_definitions()]] - code - gateway/security/network_validator.py
- [[dot-_validate_network_modes()]] - code - gateway/security/network_validator.py
- [[dot-_validate_port_exposure()]] - code - gateway/security/network_validator.py
- [[dot-_validate_privileged_containers()]] - code - gateway/security/network_validator.py
- [[dot-_validate_service_network_isolation()]] - code - gateway/security/network_validator.py
- [[dot-detect_configuration_drift()]] - code - gateway/security/network_validator.py
- [[dot-export_report()]] - code - gateway/security/network_validator.py
- [[dot-get_security_report()]] - code - gateway/security/network_validator.py
- [[dot-setup_method()_33]] - code - gateway/tests/test_network_validator.py
- [[dot-test_clean_compose_yields_zero_critical()]] - code - gateway/tests/test_network_validator_gate.py
- [[dot-test_gateway_network_bridging_validation()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_get_security_report_shape()]] - code - gateway/tests/test_network_validator_gate.py
- [[dot-test_network_security_finding_structure()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_network_validation_comprehensive_rules()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_network_validator_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_privileged_service_is_critical()]] - code - gateway/tests/test_network_validator_gate.py
- [[dot-test_validate_docker_compose_config_empty_config()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_validate_docker_compose_config_host_network_flagged()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_validate_docker_compose_config_invalid_file()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_validate_docker_compose_config_missing_internal_network()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_validate_docker_compose_config_multiple_violations()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_validate_docker_compose_config_openclaw_isolation()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_validate_docker_compose_config_privileged_flagged()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_validate_docker_compose_config_valid_config_passes()]] - code - gateway/tests/test_network_validator.py
- [[dot-test_validator_knows_the_two_real_networks()]] - code - gateway/tests/test_network_validator_gate.py
- [[dot-validate_docker_compose_config()]] - code - gateway/security/network_validator.py
- [[dot-validate_runtime_configuration()]] - code - gateway/security/network_validator.py
- [[A network security finding.]] - rationale - gateway/security/network_validator.py
- [[A privileged container is the textbook escape-the-sandbox finding —         vali]] - rationale - gateway/tests/test_network_validator_gate.py
- [[Any_73]] - code - gateway/security/network_validator.py
- [[Container network configuration.]] - rationale - gateway/security/network_validator.py
- [[Convenience function to validate network security.]] - rationale - gateway/security/network_validator.py
- [[Detect drift between compose file and runtime configuration.]] - rationale - gateway/security/network_validator.py
- [[Export network security report to file.]] - rationale - gateway/security/network_validator.py
- [[Get comprehensive network security report.]] - rationale - gateway/security/network_validator.py
- [[NetworkConfiguration]] - code - gateway/security/network_validator.py
- [[NetworkSecurityFinding]] - code - gateway/security/network_validator.py
- [[NetworkValidator]] - code - gateway/security/network_validator.py
- [[Parse network configuration for a service.]] - rationale - gateway/security/network_validator.py
- [[Path_58]] - code - gateway/tests/test_network_validator_gate.py
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
- [[TestExpectedNetworksAllowlist]] - code - gateway/tests/test_network_validator_gate.py
- [[TestGateScope]] - code - gateway/tests/test_network_validator_gate.py
- [[TestNetworkValidator]] - code - gateway/tests/test_network_validator.py
- [[TestValidatorAPI]] - code - gateway/tests/test_network_validator_gate.py
- [[Validate DNS configuration for security.]] - rationale - gateway/security/network_validator.py
- [[Validate a single container's runtime network configuration.]] - rationale - gateway/security/network_validator.py
- [[Validate container network isolation and security.]] - rationale - gateway/security/network_validator.py
- [[Validate docker-compose network configuration.          Args             compos]] - rationale - gateway/security/network_validator.py
- [[Validate network definitions in compose file.]] - rationale - gateway/security/network_validator.py
- [[Validate network mode configurations.]] - rationale - gateway/security/network_validator.py
- [[Validate port exposure configuration.]] - rationale - gateway/security/network_validator.py
- [[Validate runtime network configuration using Docker API.]] - rationale - gateway/security/network_validator.py
- [[Validate service network isolation.]] - rationale - gateway/security/network_validator.py
- [[Validate that no containers are running in privileged mode.]] - rationale - gateway/security/network_validator.py
- [[network_validator.py]] - code - gateway/security/network_validator.py
- [[post-deploy-check.sh fails ONLY on critical. These tests pin that contract.]] - rationale - gateway/tests/test_network_validator_gate.py
- [[test_network_validator.py]] - code - gateway/tests/test_network_validator.py
- [[test_network_validator_gate.py]] - code - gateway/tests/test_network_validator_gate.py
- [[tmp_compose()]] - code - gateway/tests/test_network_validator_gate.py
- [[validate_network_security()]] - code - gateway/security/network_validator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/WebProxy
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_ContextGuard]]
- 9 edges to [[_COMMUNITY_Any]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_One Shroud Over Every Wire (founding mantra)]]
- 1 edge to [[_COMMUNITY_dot-_make_proxy()]]
- 1 edge to [[_COMMUNITY__wrap_response()]]

## Top bridge nodes
- [[NetworkValidator]] - degree 52, connects to 5 communities
- [[validate_network_security()]] - degree 10, connects to 1 community
- [[dot-test_network_validator_init()]] - degree 2, connects to 1 community
