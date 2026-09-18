---
source_file: "gateway/approval_queue/enhanced_queue.py"
type: "code"
community: "ApprovalRequest"
location: "L215"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ApprovalRequest
---

# ApprovalQueueItem

## Connections
- [[._notify_telegram()]] - `references` [EXTRACTED]
- [[.decide()]] - `references` [EXTRACTED]
- [[.get_item()_1]] - `references` [EXTRACTED]
- [[.get_pending()]] - `references` [EXTRACTED]
- [[.submit()]] - `references` [EXTRACTED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalQueueItem_2]] - `uses` [INFERRED]
- [[ApprovalRequest_2]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[MFAGuard_2]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/ApprovalRequest