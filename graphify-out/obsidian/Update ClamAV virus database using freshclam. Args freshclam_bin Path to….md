---
source_file: "gateway/security/clamav_scanner.py"
type: "rationale"
community: "run_trivy_scan"
location: "L60"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/run_trivy_scan
---

# Update ClamAV virus database using freshclam. Args: freshclam_bin: Path to…

## Connections
- [[update_virus_db()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/run_trivy_scan
