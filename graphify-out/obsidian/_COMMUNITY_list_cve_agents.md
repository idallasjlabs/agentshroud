---
type: community
members: 18
---

# list_cve_agents

**Members:** 18 nodes

## Members
- [[Build the H2 heading block for one agent's CVE section.]] - rationale - scripts/generate-cve-page.py
- [[Build the full paginated CVE table block for one agent's section. Args cves…]] - rationale - scripts/generate-cve-page.py
- [[Regenerate all CVE sections in docsindex.html. Returns True if changed.]] - rationale - scripts/generate-cve-page.py
- [[Regenerate the CVE sections of docsindex.html from…]] - rationale - scripts/generate-cve-page.py
- [[Return a mapping of bot_id → CVE list, using the new API when available. Falls…]] - rationale - scripts/generate-cve-page.py
- [[Return the human-readable display name for a bot_id.]] - rationale - scripts/generate-cve-page.py
- [[Return the list of registered agent bot IDs with CVE coverage. Returns List of…]] - rationale - gateway/security/agent_cve_registry.py
- [[_agent_display_name()]] - code - scripts/generate-cve-page.py
- [[_build_heading()]] - code - scripts/generate-cve-page.py
- [[_build_table()]] - code - scripts/generate-cve-page.py
- [[_replace_between()]] - code - scripts/generate-cve-page.py
- [[_resolve_registries()]] - code - scripts/generate-cve-page.py
- [[generate()]] - code - scripts/generate-cve-page.py
- [[generate-cve-page.py]] - code - scripts/generate-cve-page.py
- [[list_cve_agents()]] - code - gateway/security/agent_cve_registry.py
- [[test_all_registered_sources_are_wrapped_agents_plus_security_tools()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_list_cve_agents_is_list_of_str()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_list_cve_agents_returns_wrapped_agents_and_security_tools()]] - code - gateway/tests/test_agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/list_cve_agents
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 4 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 2 edges to [[_COMMUNITY_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY__sleep]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]

## Top bridge nodes
- [[list_cve_agents()]] - degree 14, connects to 5 communities
- [[generate-cve-page.py]] - degree 10, connects to 2 communities
- [[_resolve_registries()]] - degree 5, connects to 1 community
- [[test_all_registered_sources_are_wrapped_agents_plus_security_tools()]] - degree 2, connects to 1 community
- [[test_list_cve_agents_is_list_of_str()]] - degree 2, connects to 1 community
