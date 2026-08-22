---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "rationale"
community: "Resource Guard & Local Model Parity"
location: "L382"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Resource_Guard__Local_Model_Parity
---

# If no secondary is configured and primary hits OOM, 503 is returned.

## Connections
- [[test_local_oom_no_secondary_falls_through_to_503()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Resource_Guard__Local_Model_Parity