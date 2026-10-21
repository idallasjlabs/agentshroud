---
source_file: "gateway/security/clamav_scanner.py"
type: "rationale"
community: "cli/main.py"
location: "L53"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/cli/mainpy
---

# clamdscan' when the resident clamd can take the scan, else 'clamscan'.

## Connections
- [[preferred_scan_binary()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/cli/mainpy
