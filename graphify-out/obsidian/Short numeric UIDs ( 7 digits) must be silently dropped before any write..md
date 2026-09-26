---
source_file: "gateway/tests/test_collaborator_tracker.py"
type: "rationale"
community: "_wrap_response()"
location: "L401"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# Short numeric UIDs (< 7 digits) must be silently dropped before any write.

## Connections
- [[test_fixture_uid_writes_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response