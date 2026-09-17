---
source_file: "gateway/security/differential_pii_detector.py"
type: "rationale"
community: "DifferentialPIIDetector"
location: "L139"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/DifferentialPIIDetector
---

# Strip common adversarial encoding tricks, return (normalized, count_removed).

## Connections
- [[_normalize_adversarial()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/DifferentialPIIDetector