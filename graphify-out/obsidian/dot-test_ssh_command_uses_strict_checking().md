---
source_file: "gateway/tests/test_security_fixes.py"
type: "code"
community: "GatewayConfig"
location: "L62"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/GatewayConfig
---

# .test_ssh_command_uses_strict_checking()

## Connections
- [[SSH execute builds command with StrictHostKeyChecking=yes]] - `rationale_for` [EXTRACTED]
- [[SSHConfig]] - `calls` [EXTRACTED]
- [[SSHHostConfig]] - `calls` [EXTRACTED]
- [[SSHProxy]] - `calls` [EXTRACTED]
- [[TestSSHStrictHostKeyChecking]] - `method` [EXTRACTED]
- [[asyncio_40]] - `references` [EXTRACTED]
- [[mock_create_subprocess()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/GatewayConfig
