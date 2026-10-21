---
source_file: "gateway/security/clamav_scanner.py"
type: "rationale"
community: "parse_clamscan_output"
location: "L60"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/parse_clamscan_output
---

# Update ClamAV virus database using freshclam. Args: freshclam_bin: Path to…

## Connections
- [[update_virus_db()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/parse_clamscan_output
