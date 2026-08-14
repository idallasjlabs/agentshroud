---
source_file: "gateway/tests/test_dns_filter.py"
type: "rationale"
community: "Egress & RBAC Security Core"
location: "L238"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress__RBAC_Security_Core
---

# Resolving a domain that fails should return empty string gracefully.

## Connections
- [[.test_resolve_and_cache_empty_domain_graceful()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress__RBAC_Security_Core