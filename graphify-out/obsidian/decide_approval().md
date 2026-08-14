---
source_file: "gateway/ingest_api/routes/approval.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L67"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# decide_approval()

## Connections
- [[ApprovalDecision_1]] - `references` [EXTRACTED]
- [[Approve or reject a pending action      Authentication required.]] - `rationale_for` [EXTRACTED]
- [[AuthRequired_1]] - `references` [EXTRACTED]
- [[Request_2]] - `references` [EXTRACTED]
- [[approval.py]] - `contains` [EXTRACTED]
- [[make_event()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline