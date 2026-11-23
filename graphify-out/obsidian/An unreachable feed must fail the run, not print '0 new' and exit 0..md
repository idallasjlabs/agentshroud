---
source_file: "gateway/tests/test_sync_cve_registry_ghsa.py"
type: "rationale"
community: "TestFailsLoudly"
location: "L486"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestFailsLoudly
---

# An unreachable feed must fail the run, not print '0 new' and exit 0.

## Connections
- [[dot-test_feed_fetch_failure_is_not_reported_as_zero_new()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestFailsLoudly
