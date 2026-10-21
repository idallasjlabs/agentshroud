---
source_file: "gateway/security/scanner_integration.py"
type: "rationale"
community: "parse_clamscan_output"
location: "L928"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/parse_clamscan_output
---

# Score domain 1: Image Integrity (0-5).      1=SBOM exists, 2=Trivy ran, 3=zero c

## Connections
- [[_score_image_integrity()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/parse_clamscan_output
