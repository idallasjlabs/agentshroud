---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L100"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# ApprovalDecision

## Connections
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[SSHExecRequest]] - `uses` [INFERRED]
- [[User's decision on a pending approval request]] - `rationale_for` [EXTRACTED]
- [[approval.py]] - `imports` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[models.py]] - `contains` [EXTRACTED]
- [[test_approval_decision_valid()]] - `calls` [EXTRACTED]
- [[test_main_simple.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline