---
source_file: "gateway/tests/test_round2_hardening.py"
type: "rationale"
community: "LLM Proxy Resource Guard"
location: "L159"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/LLM_Proxy_Resource_Guard
---

# Proxy endpoint must not crash if upstream returns non-JSON body.

## Connections
- [[.test_v1_endpoint_handles_non_json_upstream_bodies()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/LLM_Proxy_Resource_Guard