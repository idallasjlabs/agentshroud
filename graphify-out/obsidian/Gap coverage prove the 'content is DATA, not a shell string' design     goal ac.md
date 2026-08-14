---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L592"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# Gap coverage: prove the 'content is DATA, not a shell string' design     goal ac

## Connections
- [[TestSSHWriteFileShellMetacharacterContentRoundTrip]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy