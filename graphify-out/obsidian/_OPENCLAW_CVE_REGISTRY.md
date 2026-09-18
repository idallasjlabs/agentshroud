---
source_file: "gateway/security/agent_cve_registry.py"
type: "code"
community: "plan_remediation()"
location: "55"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/plan_remediation
---

# _OPENCLAW_CVE_REGISTRY

## Connections
- [[_AGENT_CVE_REGISTRIES]] - `shares_data_with` [EXTRACTED]
- [[get_agent_cve_summary]] - `shares_data_with` [INFERRED]
- [[test_auto_remediate_cves.py_1]] - `references` [EXTRACTED]
- [[test_no_entry_id_looks_like_a_cve]] - `calls` [EXTRACTED]
- [[test_real_registry_plan_is_internally_consistent]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/plan_remediation