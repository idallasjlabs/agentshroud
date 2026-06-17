---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "CLI & Core Gateway Routes"
location: "L236"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/CLI__Core_Gateway_Routes
---

# EmailSendRequest

## Connections
- [[.body_not_empty()]] - `method` [EXTRACTED]
- [[.subject_not_empty()]] - `method` [EXTRACTED]
- [[AuthRequired]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[Exception]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Request]] - `uses` [INFERRED]
- [[Request to send an email through the gateway (P3 channel ownership).      The b]] - `rationale_for` [EXTRACTED]
- [[SSHExecRequest]] - `uses` [INFERRED]
- [[WebSocket_2]] - `uses` [INFERRED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[models.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/CLI__Core_Gateway_Routes