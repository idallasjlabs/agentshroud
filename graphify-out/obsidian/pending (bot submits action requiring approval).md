---
source_file: "docs/diagrams/images/diagram-16-state-approval-queue.svg"
type: "concept"
community: "browser-extension/README.md"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/browser-extension/READMEmd
---

# pending (bot submits action requiring approval)

## Connections
- [[approved (action executed, ledger entry written)]] - `calls` [EXTRACTED]
- [[expired (1-hour TTL exceeded, auto-transition on load)]] - `calls` [EXTRACTED]
- [[rejected (action blocked, bot notified)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/browser-extension/READMEmd