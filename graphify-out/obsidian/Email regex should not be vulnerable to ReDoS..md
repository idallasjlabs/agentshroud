---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L310"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# Email regex should not be vulnerable to ReDoS.

## Connections
- [[.test_regex_redos_email()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy