---
source_file: "gateway/tests/test_auto_remediate_cves.py"
type: "rationale"
community: "auto_remediate_cves.py"
location: "L182"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/auto_remediate_cvespy
---

# Silently appending a new key could create a pin nothing consumes.

## Connections
- [[.test_write_pin_refuses_an_absent_key()]] - `rationale_for` [EXTRACTED]
- [[.test_write_pin_refuses_an_absent_key()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/auto_remediate_cvespy