---
source_file: "docs/diagrams/images/diagram-16-state-approval-queue.svg"
type: "concept"
community: "AgentShroud Phase Review — 2026-02-23 (3)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AgentShroud_Phase_Review__2026-02-23_3
---

# pending (bot submits action requiring approval)

## Connections
- [[approved (action executed, ledger entry written)]] - `calls` [EXTRACTED]
- [[expired (1-hour TTL exceeded, auto-transition on load)]] - `calls` [EXTRACTED]
- [[rejected (action blocked, bot notified)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/AgentShroud_Phase_Review__2026-02-23_3
