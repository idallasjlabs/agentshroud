---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "check_upstream_cves"
location: "L512"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/check_upstream_cves
---

# check_upstream_cves()

## Connections
- [[dot-test_raises_on_network_error()]] - `calls` [EXTRACTED]
- [[dot-test_returns_empty_when_all_known()]] - `calls` [EXTRACTED]
- [[dot-test_returns_new_advisory_not_in_registry()]] - `calls` [EXTRACTED]
- [[dot-test_skips_advisory_whose_cve_is_already_tracked()]] - `calls` [EXTRACTED]
- [[dot-test_skips_advisory_without_ghsa_id()]] - `calls` [EXTRACTED]
- [[dot-test_skips_ghsa_already_in_registry()]] - `calls` [EXTRACTED]
- [[dot-test_uses_github_token_in_header()]] - `calls` [EXTRACTED]
- [[Any_67]] - `references` [EXTRACTED]
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't trac]] - `rationale_for` [EXTRACTED]
- [[_AGENT_CVE_REGISTRIES]] - `calls` [EXTRACTED]
- [[daily_cve_report.py]] - `contains` [EXTRACTED]
- [[get_agent_ghsa_repo()]] - `calls` [EXTRACTED]
- [[run_upstream_cve_check()]] - `calls` [EXTRACTED]
- [[test_daily_cve_report.py]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/check_upstream_cves
