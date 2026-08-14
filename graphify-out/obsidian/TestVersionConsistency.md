---
source_file: "gateway/tests/test_security_fixes.py"
type: "code"
community: "scripts/sync-cve-registry.py"
location: "L379"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/scripts/sync-cve-registrypy
---

# TestVersionConsistency

## Connections
- [[.test_status_returns_current_version()]] - `method` [EXTRACTED]
- [[SSHConfig]] - `uses` [INFERRED]
- [[SSHHostConfig]] - `uses` [INFERRED]
- [[SSHProxy]] - `uses` [INFERRED]
- [[Version strings should be consistent across the codebase.]] - `rationale_for` [EXTRACTED]
- [[test_security_fixes.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/scripts/sync-cve-registrypy