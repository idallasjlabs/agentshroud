---
source_file: "gateway/tests/test_adversarial_injection.py"
type: "rationale"
community: "_any_detector_fires()"
location: "L235"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_any_detector_fires
---

# Return True if InputNormalizer changes the text (encoding detected).

## Connections
- [[_normalizer_transforms()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_any_detector_fires