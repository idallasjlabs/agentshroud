---
type: community
cohesion: 0.09
members: 23
---

# TestNetworkValidator

**Cohesion:** 0.09 - loosely connected
**Members:** 23 nodes

## Members
- [[.setup_method()_32]] - code - gateway/tests/test_network_validator.py
- [[.test_gateway_network_bridging_validation()]] - code - gateway/tests/test_network_validator.py
- [[.test_network_validation_comprehensive_rules()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_empty_config()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_host_network_flagged()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_invalid_file()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_missing_internal_network()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_multiple_violations()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_openclaw_isolation()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_privileged_flagged()]] - code - gateway/tests/test_network_validator.py
- [[.test_validate_docker_compose_config_valid_config_passes()]] - code - gateway/tests/test_network_validator.py
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
- [[test_network_validator.py]] - code - gateway/tests/test_network_validator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestNetworkValidator
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_NetworkSecurityFinding]]
- 3 edges to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[TestNetworkValidator]] - degree 15, connects to 2 communities
- [[test_network_validator.py]] - degree 3, connects to 2 communities
- [[.setup_method()_32]] - degree 2, connects to 1 community