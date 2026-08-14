---
source_file: "gateway/tests/test_security_fixes.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L215"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# SSH exec requiring approval sanitizes PII in command before storing

## Connections
- [[.test_ssh_approval_sanitizes_command_pii()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy