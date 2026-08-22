---
source_file: "gateway/tests/test_us_ssn_regex_tightened.py"
type: "rationale"
community: "Us Ssn Regex Tightened"
location: "L32"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Us_Ssn_Regex_Tightened
---

# CVE IDs with 5-digit suffix must also be excluded.

## Connections
- [[test_cve_with_five_digit_suffix_not_flagged()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Us_Ssn_Regex_Tightened