---
source_file: "gateway/tests/test_data_exfil_volume_guard.py"
type: "rationale"
community: "Data Exfil Volume Guard"
location: "L279"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Data_Exfil_Volume_Guard
---

# If the guard raises, non-owner outbound is blocked (fail-closed).

## Connections
- [[test_pipeline_fail_closed_for_non_owner_on_error()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Data_Exfil_Volume_Guard