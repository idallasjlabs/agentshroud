---
source_file: "docs/diagrams/images/diagram-14-logic-flow.svg"
type: "image"
community: "Module Group 509"
tags:
  - graphify/image
  - graphify/EXPLICIT
  - community/Module_Group_509
---

# Action Requires Approval? (email_sending, file_deletion, external_api_calls, skill_installation)

## Connections
- [[Add to Approval Queue — Notify Isaiah via Telegram, Wait up to 1 hour]] - `flows_to` [EXPLICIT]
- [[Approved — Execute action via HTTP CONNECT proxy]] - `flows_to` [EXPLICIT]
- [[MEDIUM — Allow + Audit Flag]] - `flows_to` [EXPLICIT]
- [[NONELOW — Allow + Log]] - `flows_to` [EXPLICIT]

#graphify/image #graphify/EXPLICIT #community/Module_Group_509
