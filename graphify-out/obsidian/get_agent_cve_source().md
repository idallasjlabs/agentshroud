---
source_file: "gateway/security/agent_cve_registry.py"
type: "code"
community: "Generate Cve Page (scripts)"
location: "L15435"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Generate_Cve_Page_scripts
---

# get_agent_cve_source()

## Connections
- [[Return the CVE-pipeline config for bot_id (raises KeyError if unknown).      A]] - `rationale_for` [EXTRACTED]
- [[agent_cve_registry.py]] - `contains` [EXTRACTED]
- [[daily_cve_report.py]] - `imports` [EXTRACTED]
- [[run_upstream_cve_check()]] - `calls` [EXTRACTED]
- [[sync-cve-registry.py]] - `imports` [EXTRACTED]
- [[sync_agent_ghsa()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Generate_Cve_Page_scripts