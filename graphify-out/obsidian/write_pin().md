---
source_file: "scripts/auto_remediate_cves.py"
type: "code"
community: "auto_remediate_cves.py"
location: "L105"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/auto_remediate_cvespy
---

# write_pin()

## Connections
- [[.test_pin_revert_restores_the_exact_original_string()]] - `calls` [INFERRED]
- [[.test_pin_revert_restores_the_exact_original_string()_1]] - `calls` [INFERRED]
- [[.test_write_pin_is_idempotent()]] - `calls` [INFERRED]
- [[.test_write_pin_is_idempotent()_1]] - `calls` [INFERRED]
- [[.test_write_pin_refuses_an_absent_key()]] - `calls` [INFERRED]
- [[.test_write_pin_refuses_an_absent_key()_1]] - `calls` [INFERRED]
- [[.test_write_pin_replaces_only_the_target_line()]] - `calls` [INFERRED]
- [[.test_write_pin_replaces_only_the_target_line()_1]] - `calls` [INFERRED]
- [[.test_write_pin_round_trips_through_read_pin()]] - `calls` [INFERRED]
- [[.test_write_pin_round_trips_through_read_pin()_1]] - `calls` [INFERRED]
- [[Path_12]] - `references` [EXTRACTED]
- [[Rewrite one pin in place, preserving every other line byte for byte. Raises…]] - `rationale_for` [EXTRACTED]
- [[apply_remediation()]] - `calls` [EXTRACTED]
- [[auto_remediate_cves.py]] - `contains` [EXTRACTED]
- [[test_pin_revert_restores_the_exact_original_string]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/auto_remediate_cvespy