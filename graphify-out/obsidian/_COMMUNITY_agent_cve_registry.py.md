---
type: community
cohesion: 0.11
members: 26
---

# agent_cve_registry.py

**Cohesion:** 0.11 - loosely connected
**Members:** 26 nodes

## Members
- [[Build the H2 heading block for one agent's CVE section.]] - rationale - scripts/generate-cve-page.py
- [[Build the full paginated CVE table block for one agent's section.      Args]] - rationale - scripts/generate-cve-page.py
- [[Regenerate all CVE sections in docsindex.html.  Returns True if changed.]] - rationale - scripts/generate-cve-page.py
- [[Return a mapping of bot_id → CVE list, using the new API when available.      Fa]] - rationale - scripts/generate-cve-page.py
- [[Return the CVE-pipeline config for bot_id (raises KeyError if unknown).      A]] - rationale - gateway/security/agent_cve_registry.py
- [[Return the human-readable display name for a bot_id.]] - rationale - scripts/generate-cve-page.py
- [[Return the list of registered agent bot IDs with CVE coverage.      Returns]] - rationale - gateway/security/agent_cve_registry.py
- [[Return the resolved GitHub advisory repo slug for bot_id.      Honors the per-]] - rationale - gateway/security/agent_cve_registry.py
- [[_AGENT_CVE_SOURCES]] - code - gateway/security/agent_cve_registry.py
- [[_AGENT_CVE_SOURCES (per-agent CVE pipeline config)]] - code - gateway/security/agent_cve_registry.py
- [[_HERMES_CVE_REGISTRY (HERMES_CVE_REGISTRY alias)]] - code - gateway/security/agent_cve_registry.py
- [[_OPENCLAW_CVE_REGISTRY (AGENT_CVE_REGISTRY alias)]] - code - gateway/security/agent_cve_registry.py
- [[_agent_display_name()]] - code - scripts/generate-cve-page.py
- [[_build_heading()]] - code - scripts/generate-cve-page.py
- [[_build_table()]] - code - scripts/generate-cve-page.py
- [[_replace_between()]] - code - scripts/generate-cve-page.py
- [[_resolve_registries()]] - code - scripts/generate-cve-page.py
- [[agent_cve_registry.py]] - code - gateway/security/agent_cve_registry.py
- [[generate()]] - code - scripts/generate-cve-page.py
- [[generate-cve-page.py]] - code - scripts/generate-cve-page.py
- [[get_agent_cve_source()]] - code - gateway/security/agent_cve_registry.py
- [[get_agent_ghsa_repo()]] - code - gateway/security/agent_cve_registry.py
- [[list_cve_agents()]] - code - gateway/security/agent_cve_registry.py
- [[test_all_registered_sources_are_wrapped_agents_plus_security_tools()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_list_cve_agents_is_list_of_str()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_list_cve_agents_returns_wrapped_agents_and_security_tools()]] - code - gateway/tests/test_agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agent_cve_registrypy
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 7 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 7 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 2 edges to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_triage-cve-mitigations.py]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY__make_cve]]
- 1 edge to [[_COMMUNITY_agentshroud-ssh-exec.sh]]
- 1 edge to [[_COMMUNITY_test_soc_realtime_coverage.py_1]]
- 1 edge to [[_COMMUNITY_check_upstream_cves]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py_1]]

## Top bridge nodes
- [[agent_cve_registry.py]] - degree 17, connects to 9 communities
- [[list_cve_agents()]] - degree 15, connects to 4 communities
- [[get_agent_cve_source()]] - degree 9, connects to 3 communities
- [[get_agent_ghsa_repo()]] - degree 8, connects to 3 communities
- [[generate-cve-page.py]] - degree 9, connects to 2 communities
