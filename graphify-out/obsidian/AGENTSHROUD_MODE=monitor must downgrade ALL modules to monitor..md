---
source_file: "gateway/tests/test_all_modules_enforce.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L124"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# AGENTSHROUD_MODE=monitor must downgrade ALL modules to monitor.

## Connections
- [[.test_global_monitor_override_downgrades_all()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy