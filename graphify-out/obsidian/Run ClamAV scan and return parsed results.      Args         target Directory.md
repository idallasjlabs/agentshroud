---
source_file: "gateway/security/clamav_scanner.py"
type: "rationale"
community: "parse_clamscan_output"
location: "L59"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/parse_clamscan_output
---

# Run ClamAV scan and return parsed results.      Args:         target: Directory

## Connections
- [[run_clamscan()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/parse_clamscan_output
