---
source_file: "gateway/tests/test_security_fixes.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L394"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# ClientDisconnect mid-body-read must not crash the gateway process.

## Connections
- [[TestTelegramProxyClientDisconnect]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy