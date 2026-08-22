---
source_file: "gateway/security/agent_cve_registry.py"
type: "code"
community: "Generate Cve Page (scripts)"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Generate_Cve_Page_scripts
---

# agent_cve_registry.py

## Connections
- [[generate-cve-page.py]] - `shares_data_with` [EXTRACTED]
- [[get_agent_cve_source()]] - `contains` [EXTRACTED]
- [[get_agent_cve_summary()]] - `contains` [EXTRACTED]
- [[get_agent_ghsa_repo()]] - `contains` [EXTRACTED]
- [[list_cve_agents()]] - `contains` [EXTRACTED]
- [[list_registry_ghsa_ids.py]] - `shares_data_with` [EXTRACTED]
- [[migrate-cve-registry-ghsa.py]] - `shares_data_with` [EXTRACTED]
- [[test_daily_cve_report.py]] - `imports_from` [EXTRACTED]
- [[test_generate_cve_page.py]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Generate_Cve_Page_scripts