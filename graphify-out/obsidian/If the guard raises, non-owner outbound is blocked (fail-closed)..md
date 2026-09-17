---
source_file: "gateway/tests/test_data_exfil_volume_guard.py"
type: "rationale"
community: "DataExfilVolumeGuard"
location: "L279"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/DataExfilVolumeGuard
---

# If the guard raises, non-owner outbound is blocked (fail-closed).

## Connections
- [[test_pipeline_fail_closed_for_non_owner_on_error()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/DataExfilVolumeGuard