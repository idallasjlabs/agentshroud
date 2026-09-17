---
type: community
cohesion: 0.24
members: 13
---

# validate_network_security()

**Cohesion:** 0.24 - loosely connected
**Members:** 13 nodes

## Members
- [[.test_clean_compose_yields_zero_critical()]] - code - gateway/tests/test_network_validator_gate.py
- [[.test_get_security_report_shape()]] - code - gateway/tests/test_network_validator_gate.py
- [[.test_privileged_service_is_critical()]] - code - gateway/tests/test_network_validator_gate.py
- [[A privileged container is the textbook escape-the-sandbox finding —         vali]] - rationale - gateway/tests/test_network_validator_gate.py
- [[Convenience function to validate network security.]] - rationale - gateway/security/network_validator.py
- [[Path_34]] - code - gateway/tests/test_network_validator_gate.py
- [[TestGateScope]] - code - gateway/tests/test_network_validator_gate.py
- [[TestValidatorAPI]] - code - gateway/tests/test_network_validator_gate.py
- [[network_validator.py]] - code - gateway/security/network_validator.py
- [[post-deploy-check.sh fails ONLY on critical. These tests pin that contract.]] - rationale - gateway/tests/test_network_validator_gate.py
- [[test_network_validator_gate.py]] - code - gateway/tests/test_network_validator_gate.py
- [[tmp_compose()]] - code - gateway/tests/test_network_validator_gate.py
- [[validate_network_security()]] - code - gateway/security/network_validator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/validate_network_security
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_.validate_docker_compose_config()]]
- 2 edges to [[_COMMUNITY_NetworkSecurityFinding]]

## Top bridge nodes
- [[validate_network_security()]] - degree 9, connects to 3 communities
- [[network_validator.py]] - degree 6, connects to 3 communities
- [[test_network_validator_gate.py]] - degree 7, connects to 1 community
- [[TestGateScope]] - degree 5, connects to 1 community
- [[TestValidatorAPI]] - degree 3, connects to 1 community