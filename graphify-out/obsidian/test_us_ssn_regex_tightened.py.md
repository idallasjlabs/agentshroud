---
source_file: "gateway/tests/test_us_ssn_regex_tightened.py"
type: "code"
community: "Us Ssn Regex Tightened"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Us_Ssn_Regex_Tightened
---

# test_us_ssn_regex_tightened.py

## Connections
- [[test_cve_dense_report_body_preserved()]] - `contains` [EXTRACTED]
- [[test_cve_pattern_not_flagged_as_ssn()]] - `contains` [EXTRACTED]
- [[test_cve_with_five_digit_suffix_not_flagged()]] - `contains` [EXTRACTED]
- [[test_real_ssn_still_flagged()]] - `contains` [EXTRACTED]
- [[test_ssn_at_start_of_string_still_flagged()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Us_Ssn_Regex_Tightened