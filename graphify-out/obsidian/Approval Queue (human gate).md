---
source_file: "docs/diagrams/images/diagram-07-data-flow.svg"
type: "concept"
community: "container-net-diag.sh"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/container-net-diagsh
---

# Approval Queue (human gate)

## Connections
- [[PII Sanitizer (Presidio  regex)]] - `shares_data_with` [EXTRACTED]
- [[Telegram API_1]] - `calls` [EXTRACTED]
- [[approval_queue.py]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/container-net-diagsh