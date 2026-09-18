---
source_file: "gateway/tests/test_auto_remediate_cves.py"
type: "rationale"
community: "auto_remediate_cves.py"
location: "L199"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/auto_remediate_cvespy
---

# The rollback path: a failed deploy must restore the pin verbatim, downstream…

## Connections
- [[.test_pin_revert_restores_the_exact_original_string()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/auto_remediate_cvespy