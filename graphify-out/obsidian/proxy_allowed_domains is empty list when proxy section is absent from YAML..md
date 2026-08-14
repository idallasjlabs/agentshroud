---
source_file: "gateway/tests/test_mcp_result_endpoint.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L341"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# proxy_allowed_domains is empty list when proxy section is absent from YAML.

## Connections
- [[.test_proxy_allowed_domains_defaults_to_empty_when_absent()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy