---
source_file: "gateway/tests/test_sync_cve_registry_ghsa.py"
type: "code"
community: "An unreachable feed must fail the run, not print '0 new' and exit 0."
location: "L450"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/An_unreachable_feed_must_fail_the_run_not_print_0_new_and_exit_0
---

# _boom()

## Connections
- [[dot-test_main_exits_nonzero_when_an_agent_fails()]] - `indirect_call` [INFERRED]
- [[dot-test_nvd_layout_failure_exits_nonzero()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/INFERRED #community/An_unreachable_feed_must_fail_the_run_not_print_0_new_and_exit_0
