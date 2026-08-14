---
source_file: "gateway/tests/test_security_fixes.py"
type: "code"
community: "scripts/sync-cve-registry.py"
location: "L48"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# TestSSHStrictHostKeyChecking

## Connections
- [[.test_ssh_command_uses_strict_checking()]] - `method` [EXTRACTED]
- [[.test_strict_host_key_checking_in_source()]] - `method` [EXTRACTED]
- [[SSHConfig]] - `uses` [INFERRED]
- [[SSHHostConfig]] - `uses` [INFERRED]
- [[SSHProxy]] - `uses` [INFERRED]
- [[Verify SSH proxy uses StrictHostKeyChecking=yes, not accept-new]] - `rationale_for` [EXTRACTED]
- [[test_security_fixes.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/scripts/sync-cve-registrypy