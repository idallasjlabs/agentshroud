---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L249"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# Decoded content exceeding the ~500KB cap is rejected with 413, and         proxy

## Connections
- [[.test_write_file_oversized_content_rejected()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy