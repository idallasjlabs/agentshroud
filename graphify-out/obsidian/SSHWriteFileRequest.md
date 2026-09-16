---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "Ingest API & RBAC Core"
location: "L261"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Ingest_API__RBAC_Core
---

# SSHWriteFileRequest

## Connections
- [[dot-path_not_empty()]] - `method` [EXTRACTED]
- [[dot-validate_base64()]] - `method` [EXTRACTED]
- [[AuthRequired]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[Exception]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Request]] - `uses` [INFERRED]
- [[Request to write file content to an allowlisted SSH host.      Unlike SSHExecReq]] - `rationale_for` [EXTRACTED]
- [[SSHExecRequest_1]] - `uses` [INFERRED]
- [[SSHWriteFileRequest_1]] - `uses` [INFERRED]
- [[WebSocket]] - `uses` [INFERRED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[ingest_apimodels.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Ingest_API__RBAC_Core