---
source_file: "gateway/soc/router.py"
type: "code"
community: "_FakeRBAC"
location: "L380"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/_FakeRBAC
---

# EgressApproveRequest

## Connections
- [[AuditLogEntry]] - `uses` [INFERRED]
- [[AuditResult_1]] - `uses` [INFERRED]
- [[BaseModel_2]] - `inherits` [EXTRACTED]
- [[ContributorManager]] - `uses` [INFERRED]
- [[SCLCaller_2]] - `uses` [INFERRED]
- [[SCLConfirmationRequired]] - `uses` [INFERRED]
- [[SCLInterface_1]] - `uses` [INFERRED]
- [[ServiceManager]] - `uses` [INFERRED]
- [[approve_egress()]] - `references` [EXTRACTED]
- [[socrouter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/_FakeRBAC
