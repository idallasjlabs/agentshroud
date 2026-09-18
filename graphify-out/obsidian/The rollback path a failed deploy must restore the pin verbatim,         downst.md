---
source_file: "gateway/tests/test_auto_remediate_cves.py"
type: "rationale"
community: "auto_remediate_cves.py"
location: "L195"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/auto_remediate_cvespy
---

# The rollback path: a failed deploy must restore the pin verbatim,         downst

## Connections
- [[.test_pin_revert_restores_the_exact_original_string()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/auto_remediate_cvespy