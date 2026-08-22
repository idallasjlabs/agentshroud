---
source_file: "gateway/tests/test_data_exfil_volume_guard.py"
type: "rationale"
community: "Data Exfil Volume Guard"
location: "L192"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Data_Exfil_Volume_Guard
---

# The rolling baseline deque is trimmed to adaptive_window; old samples drop.

## Connections
- [[test_adaptive_window_bounds_baseline_memory()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Data_Exfil_Volume_Guard