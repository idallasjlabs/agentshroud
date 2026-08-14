---
source_file: "gateway/tests/test_security_fixes.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L49"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# Verify SSH proxy uses StrictHostKeyChecking=yes, not accept-new

## Connections
- [[TestSSHStrictHostKeyChecking]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy