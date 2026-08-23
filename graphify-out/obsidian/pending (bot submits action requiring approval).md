---
source_file: "docs/diagrams/images/diagram-16-state-approval-queue.svg"
type: "concept"
community: "Diagram 16 State Approval (images)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Diagram_16_State_Approval_images
---

# pending (bot submits action requiring approval)

## Connections
- [[approved (action executed, ledger entry written)]] - `calls` [EXTRACTED]
- [[expired (1-hour TTL exceeded, auto-transition on load)]] - `calls` [EXTRACTED]
- [[rejected (action blocked, bot notified)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Diagram_16_State_Approval_images