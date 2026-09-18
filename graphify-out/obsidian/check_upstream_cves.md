---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "check_upstream_cves"
location: "512"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/check_upstream_cves
---

# check_upstream_cves

## Connections
- [[.test_raises_on_network_error()]] - `calls` [EXTRACTED]
- [[.test_returns_empty_when_all_known()]] - `calls` [EXTRACTED]
- [[.test_returns_new_advisory_not_in_registry()]] - `calls` [EXTRACTED]
- [[.test_skips_advisory_whose_cve_is_already_tracked()]] - `calls` [EXTRACTED]
- [[.test_skips_advisory_without_ghsa_id()]] - `calls` [EXTRACTED]
- [[.test_skips_ghsa_already_in_registry()]] - `calls` [EXTRACTED]
- [[.test_uses_github_token_in_header()]] - `calls` [EXTRACTED]
- [[Agent CVE Registry module (_AGENT_CVE_REGISTRIES etc.)]] - `shares_data_with` [EXTRACTED]
- [[Any_15]] - `references` [EXTRACTED]
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't…]] - `rationale_for` [EXTRACTED]
- [[fetch_ghsa_advisories()]] - `references` [EXTRACTED]
- [[gateway.security.daily_cve_report]] - `contains` [EXTRACTED]
- [[get_agent_ghsa_repo]] - `calls` [EXTRACTED]
- [[run_upstream_cve_check]] - `calls` [EXTRACTED]
- [[sunday_resolve_scan_image]] - `references` [EXTRACTED]
- [[test_daily_cve_report.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/check_upstream_cves