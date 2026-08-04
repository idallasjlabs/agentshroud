---
source_file: "docs/diagrams/images/diagram-14-logic-flow.svg"
type: "image"
community: "Module Group 504"
tags:
  - graphify/image
  - graphify/EXPLICIT
  - community/Module_Group_504
---

# Isaiah Decides (Approve/Reject/Timeout)

## Connections
- [[Add to Approval Queue — Notify Isaiah via Telegram, Wait up to 1 hour]] - `flows_to` [EXPLICIT]
- [[Approved — Execute action via HTTP CONNECT proxy]] - `flows_to` [EXPLICIT]
- [[Expired (1h timeout) — Auto-reject]] - `flows_to` [EXPLICIT]
- [[Rejected — Log + Notify Bot]] - `flows_to` [EXPLICIT]

#graphify/image #graphify/EXPLICIT #community/Module_Group_504
