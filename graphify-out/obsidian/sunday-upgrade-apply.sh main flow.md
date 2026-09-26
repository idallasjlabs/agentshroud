---
source_file: "scripts/sunday-upgrade-apply.sh"
type: "code"
community: "DraftEntry"
location: "825"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/DraftEntry
---

# sunday-upgrade-apply.sh main flow

## Connections
- [[check_noop_gate()]] - `calls` [EXTRACTED]
- [[phase_apply()]] - `calls` [EXTRACTED]
- [[phase_baseline()]] - `calls` [EXTRACTED]
- [[phase_discover()]] - `calls` [EXTRACTED]
- [[phase_preflight()]] - `calls` [EXTRACTED]
- [[phase_scan()]] - `calls` [EXTRACTED]
- [[phase_verify()]] - `calls` [EXTRACTED]
- [[sunday-upgrade.sh]] - `references` [EXTRACTED]
- [[write_handoff()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/DraftEntry