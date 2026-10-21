---
source_file: "gateway/tests/test_us_ssn_regex_tightened.py"
type: "rationale"
community: "web_config.py"
location: "L41"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/web_configpy
---

# Real SSNs (not preceded by uppercase) must still be detected.

## Connections
- [[test_real_ssn_still_flagged()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/web_configpy
