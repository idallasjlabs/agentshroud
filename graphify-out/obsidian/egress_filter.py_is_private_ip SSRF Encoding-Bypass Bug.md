---
source_file: "gateway/security/egress_filter.py"
type: "rationale"
community: "RovoBlast Attack (Atlassian Rovo AI)"
location: "lines 459-480"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/RovoBlast_Attack_Atlassian_Rovo_AI
---

# egress_filter.py::_is_private_ip SSRF Encoding-Bypass Bug

## Connections
- [[EgressFilter.check()]] - `shares_data_with` [INFERRED]
- [[a2a_policy.py]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/RovoBlast_Attack_Atlassian_Rovo_AI