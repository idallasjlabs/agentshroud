---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L484"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# The remote command string must not vary with request content —         proving i

## Connections
- [[.test_write_file_remote_command_is_identical_across_calls()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy