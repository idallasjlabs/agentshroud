---
source_file: "docs/diagrams/images/diagram-17-state-bot-session.png"
type: "image"
community: "Approval Queue (human-in-the-loop)"
tags:
  - graphify/image
  - graphify/AMBIGUOUS
  - community/Approval_Queue_human-in-the-loop
---

# Bot Session State Diagram (fresh → active → idle/compacting → reset)

## Connections
- [[OpenClaw auto-compaction (reserveTokensFloor=4000; triggers at ~196K of 200K tokens; hard overflow 200K after 3 failed retries → session reset)]] - `conceptually_related_to` [EXTRACTED]
- [[flowsREADME]] - `conceptually_related_to` [AMBIGUOUS]

#graphify/image #graphify/AMBIGUOUS #community/Approval_Queue_human-in-the-loop