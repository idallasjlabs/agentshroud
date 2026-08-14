---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L362"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# EmailSendResponse

## Connections
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Response from POST emailsend.]] - `rationale_for` [EXTRACTED]
- [[SSHExecRequest]] - `uses` [INFERRED]
- [[email_send()]] - `calls` [EXTRACTED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[models.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline