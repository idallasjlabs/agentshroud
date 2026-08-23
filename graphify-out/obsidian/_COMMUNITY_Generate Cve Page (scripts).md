---
type: community
cohesion: 0.13
members: 22
---

# Generate Cve Page (scripts)

**Cohesion:** 0.13 - loosely connected
**Members:** 22 nodes

## Members
- [[Build the H2 heading block for one agent's CVE section.]] - rationale - scripts/generate-cve-page.py
- [[Build the full paginated CVE table block for one agent's section.      Args]] - rationale - scripts/generate-cve-page.py
- [[Regenerate all CVE sections in docsindex.html.  Returns True if changed.]] - rationale - scripts/generate-cve-page.py
- [[Return a mapping of bot_id → CVE list, using the new API when available.      Fa]] - rationale - scripts/generate-cve-page.py
- [[Return the CVE-pipeline config for bot_id (raises KeyError if unknown).      A]] - rationale - gateway/security/agent_cve_registry.py
- [[Return the human-readable display name for a bot_id.]] - rationale - scripts/generate-cve-page.py
- [[Return the list of registered agent bot IDs with CVE coverage.      Returns]] - rationale - gateway/security/agent_cve_registry.py
- [[_agent_display_name()]] - code - scripts/generate-cve-page.py
- [[_build_heading()]] - code - scripts/generate-cve-page.py
- [[_build_table()]] - code - scripts/generate-cve-page.py
- [[_replace_between()]] - code - scripts/generate-cve-page.py
- [[_resolve_registries()]] - code - scripts/generate-cve-page.py
- [[agent_cve_registry.py]] - code - gateway/security/agent_cve_registry.py
- [[gatewaysecurityagent_cve_registry.py (known CVE registry, referenced)]] - code - gateway/security/agent_cve_registry.py
- [[generate()]] - code - scripts/generate-cve-page.py
- [[generate-cve-page.py]] - code - scripts/generate-cve-page.py
- [[get_agent_cve_source()]] - code - gateway/security/agent_cve_registry.py
- [[list_cve_agents()]] - code - gateway/security/agent_cve_registry.py
- [[list_registry_ghsa_ids.py]] - code - scripts/list_registry_ghsa_ids.py
- [[main()_21]] - code - scripts/list_registry_ghsa_ids.py
- [[test_list_cve_agents_is_list_of_str()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_list_cve_agents_returns_both()]] - code - gateway/tests/test_agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Generate_Cve_Page_scripts
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Agent Cve Registry]]
- 6 edges to [[_COMMUNITY_Sync Cve Registry (scripts)]]
- 5 edges to [[_COMMUNITY_Daily Cve Report (security)]]
- 2 edges to [[_COMMUNITY_Daily Cve Report]]
- 2 edges to [[_COMMUNITY_Generate Cve Page]]
- 1 edge to [[_COMMUNITY_Migrate Cve Registry Ghsa (scripts)]]
- 1 edge to [[_COMMUNITY_List Registry Ghsa Ids]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]

## Top bridge nodes
- [[agent_cve_registry.py]] - degree 9, connects to 5 communities
- [[list_cve_agents()]] - degree 13, connects to 4 communities
- [[gatewaysecurityagent_cve_registry.py (known CVE registry, referenced)]] - degree 5, connects to 3 communities
- [[generate-cve-page.py]] - degree 11, connects to 2 communities
- [[get_agent_cve_source()]] - degree 6, connects to 2 communities