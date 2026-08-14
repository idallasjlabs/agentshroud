---
source_file: "gateway/web/api.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L681"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# Pull latest AgentShroud, test, rebuild, restart. Auto-rollback on failure.

## Connections
- [[upgrade_agentshroud()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy