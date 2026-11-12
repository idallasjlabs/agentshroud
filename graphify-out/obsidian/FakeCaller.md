---
source_file: "gateway/tests/test_soc_edge.py"
type: "code"
community: "Community 65"
location: "L41"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_65
---

# FakeCaller

## Connections
- [[.__init__()_210]] - `method` [EXTRACTED]
- [[.is_owner()_4]] - `method` [EXTRACTED]
- [[.require()_1]] - `method` [EXTRACTED]
- [[.test_owner_only()]] - `calls` [EXTRACTED]
- [[.test_rbac_denial_is_403()]] - `calls` [EXTRACTED]
- [[.test_requires_manage_and_owner()]] - `calls` [EXTRACTED]
- [[.test_unkill_owner_only()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[EdgeService]] - `uses` [INFERRED]
- [[EventBus]] - `uses` [INFERRED]
- [[LockdownLevel_1]] - `uses` [INFERRED]
- [[ProgressiveLockdown]] - `uses` [INFERRED]
- [[RBAC is recorded, not enforced; owner is switchable.]] - `rationale_for` [EXTRACTED]
- [[Resource_1]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[SOCWebSocketHandler]] - `uses` [INFERRED]
- [[VendorStats]] - `uses` [INFERRED]
- [[holder()]] - `calls` [EXTRACTED]
- [[test_soc_edge.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_65