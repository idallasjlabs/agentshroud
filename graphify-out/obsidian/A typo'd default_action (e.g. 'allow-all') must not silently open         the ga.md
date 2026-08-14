---
source_file: "gateway/tests/test_a2a_policy_default_failclosed.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L55"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# A typo'd default_action (e.g. 'allow-all') must not silently open         the ga

## Connections
- [[.test_invalid_default_action_string_falls_back_to_deny()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite