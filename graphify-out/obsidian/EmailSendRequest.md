---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L329"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# EmailSendRequest

## Connections
- [[.body_not_empty()]] - `method` [EXTRACTED]
- [[.subject_not_empty()]] - `method` [EXTRACTED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Request to send an email through the gateway (P3 channel ownership).      The b]] - `rationale_for` [EXTRACTED]
- [[SSHExecRequest]] - `uses` [INFERRED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[models.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline