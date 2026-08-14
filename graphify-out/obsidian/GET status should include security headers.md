---
source_file: "gateway/tests/test_security_fixes.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L362"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# GET /status should include security headers

## Connections
- [[.test_json_api_has_cache_control()]] - `rationale_for` [EXTRACTED]
- [[.test_status_has_security_headers()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy