---
source_file: "gateway/security/agent_cve_registry.py"
type: "code"
community: "AgentRegistry"
location: "L18521"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentRegistry
---

# list_cve_agents()

## Connections
- [[.test_runs_ingest_records_then_skips_next_iteration()]] - `calls` [EXTRACTED]
- [[Return the list of registered agent bot IDs with CVE coverage.      Returns]] - `rationale_for` [EXTRACTED]
- [[_AGENT_CVE_SOURCES (per-agent CVE pipeline config)]] - `calls` [EXTRACTED]
- [[_resolve_registries()]] - `calls` [EXTRACTED]
- [[agent_cve_registry.py]] - `references` [EXTRACTED]
- [[daily_cve_report.py]] - `imports` [EXTRACTED]
- [[generate-cve-page.py]] - `imports` [EXTRACTED]
- [[run_ghsa_sync()]] - `calls` [EXTRACTED]
- [[run_upstream_cve_check_all_agents()]] - `calls` [EXTRACTED]
- [[sync-cve-registry.py]] - `imports` [EXTRACTED]
- [[test_agent_cve_registry.py]] - `references` [EXTRACTED]
- [[test_all_registered_sources_are_wrapped_agents_plus_security_tools()]] - `calls` [EXTRACTED]
- [[test_daily_cve_report.py]] - `imports` [EXTRACTED]
- [[test_list_cve_agents_is_list_of_str()]] - `calls` [EXTRACTED]
- [[test_list_cve_agents_returns_wrapped_agents_and_security_tools()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AgentRegistry