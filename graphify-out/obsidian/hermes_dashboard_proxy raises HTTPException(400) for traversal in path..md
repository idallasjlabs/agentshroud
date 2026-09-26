---
source_file: "gateway/tests/test_main_endpoints.py"
type: "rationale"
community: "InjectionSeverity"
location: "L401"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/InjectionSeverity
---

# hermes_dashboard_proxy raises HTTPException(400) for traversal in path.

## Connections
- [[.test_proxy_returns_400_on_traversal()]] - `rationale_for` [EXTRACTED]
- [[.test_proxy_returns_400_on_traversal_in_query()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/InjectionSeverity