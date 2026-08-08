---
source_file: "docs/diagrams/images/diagram-16-state-approval-queue.svg"
type: "concept"
community: "docs/diagrams"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/docs/diagrams
---

# pending (bot submits action requiring approval)

## Connections
- [[approved (action executed, ledger entry written)]] - `calls` [EXTRACTED]
- [[expired (1-hour TTL exceeded, auto-transition on load)]] - `calls` [EXTRACTED]
- [[rejected (action blocked, bot notified)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/docs/diagrams