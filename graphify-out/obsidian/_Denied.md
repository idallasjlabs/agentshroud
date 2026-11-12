---
source_file: "gateway/inbound_edge/call_pipeline.py"
type: "code"
community: "Community 25"
location: "L107"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_25
---

# _Denied

## Connections
- [[.__init__()_10]] - `method` [EXTRACTED]
- [[._authenticate()]] - `calls` [EXTRACTED]
- [[._check_limits()]] - `calls` [EXTRACTED]
- [[.call_tool()]] - `calls` [EXTRACTED]
- [[ApprovalContext]] - `uses` [INFERRED]
- [[ApprovalDenied]] - `uses` [INFERRED]
- [[ApprovalPending]] - `uses` [INFERRED]
- [[EdgeApprovals]] - `uses` [INFERRED]
- [[EdgePrincipal_1]] - `uses` [INFERRED]
- [[Exception]] - `inherits` [EXTRACTED]
- [[LockdownLevel_1]] - `uses` [INFERRED]
- [[TokenRejected]] - `uses` [INFERRED]
- [[TokenService]] - `uses` [INFERRED]
- [[VendorProfile_2]] - `uses` [INFERRED]
- [[call_pipeline.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_25