---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L261"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer_Pipeline
---

# SSHWriteFileRequest

## Connections
- [[.path_not_empty()]] - `method` [EXTRACTED]
- [[.validate_base64()]] - `method` [EXTRACTED]
- [[AuthRequired]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[Exception]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Request_1]] - `uses` [INFERRED]
- [[Request to write file content to an allowlisted SSH host.      Unlike SSHExecReq]] - `rationale_for` [EXTRACTED]
- [[SSHExecRequest]] - `uses` [INFERRED]
- [[SSHWriteFileRequest]] - `uses` [INFERRED]
- [[WebSocket_2]] - `uses` [INFERRED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[models.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer_Pipeline