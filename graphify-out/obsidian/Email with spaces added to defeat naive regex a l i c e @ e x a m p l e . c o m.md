---
source_file: "gateway/tests/test_differential_pii_detector.py"
type: "rationale"
community: "test_soc_router_coverage.py"
location: "L305"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_soc_router_coveragepy
---

# Email with spaces added to defeat naive regex: a l i c e @ e x a m p l e . c o m

## Connections
- [[.test_spaced_email_caught_in_tool_result()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_soc_router_coveragepy