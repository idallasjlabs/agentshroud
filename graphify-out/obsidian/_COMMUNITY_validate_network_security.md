---
type: community
cohesion: 0.21
members: 14
---

# validate_network_security

**Cohesion:** 0.21 - loosely connected
**Members:** 14 nodes

## Members
- [[dot-test_clean_compose_yields_zero_critical()]] - code - gateway/tests/test_network_validator_gate.py
- [[dot-test_get_security_report_shape()]] - code - gateway/tests/test_network_validator_gate.py
- [[dot-test_privileged_service_is_critical()]] - code - gateway/tests/test_network_validator_gate.py
- [[dot-test_validator_knows_the_two_real_networks()]] - code - gateway/tests/test_network_validator_gate.py
- [[A privileged container is the textbook escape-the-sandbox finding —         vali]] - rationale - gateway/tests/test_network_validator_gate.py
- [[Convenience function to validate network security.]] - rationale - gateway/security/network_validator.py
- [[Path_49]] - code - gateway/tests/test_network_validator_gate.py
- [[TestExpectedNetworksAllowlist]] - code - gateway/tests/test_network_validator_gate.py
- [[TestGateScope]] - code - gateway/tests/test_network_validator_gate.py
- [[TestValidatorAPI]] - code - gateway/tests/test_network_validator_gate.py
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
- 7 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_dot-validate_docker_compose_config]]
- 1 edge to [[_COMMUNITY_check-vendor-compat.sh]]
- 1 edge to [[_COMMUNITY_NetworkSecurityFinding]]

## Top bridge nodes
- [[validate_network_security()]] - degree 10, connects to 4 communities
- [[test_network_validator_gate.py]] - degree 7, connects to 2 communities
- [[TestGateScope]] - degree 5, connects to 1 community
- [[TestExpectedNetworksAllowlist]] - degree 3, connects to 1 community
- [[TestValidatorAPI]] - degree 3, connects to 1 community
