---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L128"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# Valid request: SSHProxy.write_file() is invoked with decoded path/content

## Connections
- [[.test_write_file_valid_round_trip()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy