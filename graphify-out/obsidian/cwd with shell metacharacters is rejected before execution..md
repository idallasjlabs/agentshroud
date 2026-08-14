---
source_file: "gateway/tests/test_ssh_endpoints.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L198"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# cwd with shell metacharacters is rejected before execution.

## Connections
- [[.test_ssh_exec_cwd_invalid_rejects_400()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy