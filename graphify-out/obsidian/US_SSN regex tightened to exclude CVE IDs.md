---
source_file: "gateway/tests/test_us_ssn_regex_tightened.py"
type: "rationale"
community: "Community 765"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_765
---

# US_SSN regex tightened to exclude CVE IDs

## Connections
- [[ToolResultSanitizer]] - `conceptually_related_to` [INFERRED]
- [[test_cve_pattern_not_flagged_as_ssn()]] - `rationale_for` [EXTRACTED]
- [[test_real_ssn_still_flagged()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_765