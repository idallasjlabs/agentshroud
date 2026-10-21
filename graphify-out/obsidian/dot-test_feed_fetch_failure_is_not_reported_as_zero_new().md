---
source_file: "gateway/tests/test_sync_cve_registry_ghsa.py"
type: "code"
community: "An unreachable feed must fail the run, not print '0 new' and exit 0."
location: "L485"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/An_unreachable_feed_must_fail_the_run_not_print_0_new_and_exit_0
---

# .test_feed_fetch_failure_is_not_reported_as_zero_new()

## Connections
- [[An unreachable feed must fail the run, not print '0 new' and exit 0.]] - `rationale_for` [EXTRACTED]
- [[TestFailsLoudly]] - `method` [EXTRACTED]
- [[_sync()]] - `calls` [EXTRACTED]
- [[_timeout()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/An_unreachable_feed_must_fail_the_run_not_print_0_new_and_exit_0
