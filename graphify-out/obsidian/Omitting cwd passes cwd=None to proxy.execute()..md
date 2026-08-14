---
source_file: "gateway/tests/test_ssh_endpoints.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L216"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# Omitting cwd passes cwd=None to proxy.execute().

## Connections
- [[.test_ssh_exec_cwd_none_forwards_none()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy