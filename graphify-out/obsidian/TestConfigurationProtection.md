---
source_file: "gateway/tests/test_privilege_separation.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L135"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# TestConfigurationProtection

## Connections
- [[.test_docker_compose_write_blocked()]] - `method` [EXTRACTED]
- [[.test_dockerfile_write_blocked()]] - `method` [EXTRACTED]
- [[.test_gateway_config_write_blocked()]] - `method` [EXTRACTED]
- [[Agent cannot modify AgentShroud configuration files.]] - `rationale_for` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[test_privilege_separation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection
