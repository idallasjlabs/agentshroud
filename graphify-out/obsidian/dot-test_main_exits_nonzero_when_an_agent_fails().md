---
source_file: "gateway/tests/test_sync_cve_registry_ghsa.py"
type: "code"
community: "An unreachable feed must fail the run, not print '0 new' and exit 0."
location: "L470"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/An_unreachable_feed_must_fail_the_run_not_print_0_new_and_exit_0
---

# .test_main_exits_nonzero_when_an_agent_fails()

## Connections
- [[TestFailsLoudly]] - `method` [EXTRACTED]
- [[_boom()_1]] - `contains` [EXTRACTED]
- [[_boom()_2]] - `indirect_call` [INFERRED]
- [[_sync()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/An_unreachable_feed_must_fail_the_run_not_print_0_new_and_exit_0
