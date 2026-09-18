---
source_file: "gateway/tests/test_us_ssn_regex_tightened.py"
type: "rationale"
community: "test_us_ssn_regex_tightened.py"
location: "L41"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_us_ssn_regex_tightenedpy
---

# Real SSNs (not preceded by uppercase) must still be detected.

## Connections
- [[test_real_ssn_still_flagged()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_us_ssn_regex_tightenedpy