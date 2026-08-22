---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "Daily Cve Report"
location: "L456"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Daily_Cve_Report
---

# check_upstream_cves()

## Connections
- [[.test_raises_on_network_error()]] - `calls` [EXTRACTED]
- [[.test_returns_empty_when_all_known()]] - `calls` [EXTRACTED]
- [[.test_returns_new_advisory_not_in_registry()]] - `calls` [EXTRACTED]
- [[.test_skips_advisory_whose_cve_is_already_tracked()]] - `calls` [EXTRACTED]
- [[.test_skips_advisory_without_ghsa_id()]] - `calls` [EXTRACTED]
- [[.test_skips_ghsa_already_in_registry()]] - `calls` [EXTRACTED]
- [[.test_uses_github_token_in_header()]] - `calls` [EXTRACTED]
- [[Any_37]] - `references` [EXTRACTED]
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't trac]] - `rationale_for` [EXTRACTED]
- [[daily_cve_report.py]] - `contains` [EXTRACTED]
- [[get_agent_ghsa_repo()]] - `calls` [EXTRACTED]
- [[run_upstream_cve_check()]] - `calls` [EXTRACTED]
- [[test_daily_cve_report.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Daily_Cve_Report