---
source_file: "gateway/tests/test_us_ssn_regex_tightened.py"
type: "rationale"
community: "Us Ssn Regex Tightened"
location: "L41"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Us_Ssn_Regex_Tightened
---

# Real SSNs (not preceded by uppercase) must still be detected.

## Connections
- [[test_real_ssn_still_flagged()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Us_Ssn_Regex_Tightened