---
source_file: "gateway/ssh_proxy/proxy.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L283"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# Write file content to a remote host via structured (non-shell-string) transport.

## Connections
- [[.write_file()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy