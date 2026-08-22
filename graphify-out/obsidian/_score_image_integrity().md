---
source_file: "gateway/security/scanner_integration.py"
type: "code"
community: "Scanner Integration (security)"
location: "L927"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Scanner_Integration_security
---

# _score_image_integrity()

## Connections
- [[.test_capped_at_five()]] - `calls` [EXTRACTED]
- [[.test_four_when_sbom_and_clean_trivy()]] - `calls` [EXTRACTED]
- [[.test_one_when_sbom_exists()]] - `calls` [EXTRACTED]
- [[.test_zero_when_no_sbom_no_trivy()]] - `calls` [EXTRACTED]
- [[Any_58]] - `references` [EXTRACTED]
- [[Score domain 1 Image Integrity (0-5).      1=SBOM exists, 2=Trivy ran, 3=zero c]] - `rationale_for` [EXTRACTED]
- [[_is_fresh()]] - `calls` [EXTRACTED]
- [[compute_scorecard()]] - `calls` [EXTRACTED]
- [[scanner_integration.py]] - `contains` [EXTRACTED]
- [[test_scanner_integration.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Scanner_Integration_security