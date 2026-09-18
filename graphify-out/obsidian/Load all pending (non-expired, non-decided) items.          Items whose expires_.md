---
source_file: "gateway/approval_queue/store.py"
type: "rationale"
community: "ApprovalRequest"
location: "L99"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ApprovalRequest
---

# Load all pending (non-expired, non-decided) items.          Items whose expires_

## Connections
- [[.load_pending()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ApprovalRequest