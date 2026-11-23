---
type: community
members: 8
---

# TestConfigurationProtection

**Members:** 8 nodes

## Members
- [[dot-test_docker_compose_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_dockerfile_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_gateway_config_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify AgentShroud configuration files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify Docker Compose configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify Dockerfile.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to gateway config directory.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestConfigurationProtection]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestConfigurationProtection
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[TestConfigurationProtection]] - degree 5, connects to 1 community
