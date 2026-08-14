---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L128"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# Unicode tricks shouldn't bypass PII detection.

## Connections
- [[.test_unicode_normalization_bypass()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy