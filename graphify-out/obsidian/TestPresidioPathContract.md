---
source_file: "gateway/tests/test_differential_pii_detector.py"
type: "code"
community: "Community 45"
location: "L199"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_45
---

# TestPresidioPathContract

## Connections
- [[._detector_with_fake()]] - `method` [EXTRACTED]
- [[.test_bare_city_name_not_flagged_but_street_address_is()]] - `method` [EXTRACTED]
- [[.test_core_ssn_unioned_when_presidio_misses_it()]] - `method` [EXTRACTED]
- [[.test_presidio_analyze_restricted_to_pii_entities()]] - `method` [EXTRACTED]
- [[.test_presidio_exception_falls_back_to_regex()]] - `method` [EXTRACTED]
- [[.test_presidio_result_becomes_pii_hit()]] - `method` [EXTRACTED]
- [[DifferentialPIIConfig]] - `uses` [INFERRED]
- [[DifferentialPIIDetector]] - `uses` [INFERRED]
- [[Exercise the Presidio detection path with an injected fake analyzer.      The re]] - `rationale_for` [EXTRACTED]
- [[PIIHit]] - `uses` [INFERRED]
- [[PIIHitSeverity]] - `uses` [INFERRED]
- [[test_differential_pii_detector.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_45