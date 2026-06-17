---
type: community
cohesion: 0.15
members: 18
---

# Module Group 251

**Cohesion:** 0.15 - loosely connected
**Members:** 18 nodes

## Members
- [[Build the H2 heading block for one agent's CVE section.]] - rationale - scripts/generate-cve-page.py
- [[Build the full paginated CVE table block for one agent's section.      Args]] - rationale - scripts/generate-cve-page.py
- [[Regenerate all CVE sections in docsindex.html.  Returns True if changed.]] - rationale - scripts/generate-cve-page.py
- [[Return a mapping of bot_id → CVE list, using the new API when available.      Fa]] - rationale - scripts/generate-cve-page.py
- [[Return the human-readable display name for a bot_id.]] - rationale - scripts/generate-cve-page.py
- [[Return the list of registered agent bot IDs with CVE coverage.      Returns]] - rationale - gateway/security/agent_cve_registry.py
- [[_agent_display_name()]] - code - scripts/generate-cve-page.py
- [[_build_heading()]] - code - scripts/generate-cve-page.py
- [[_build_table()]] - code - scripts/generate-cve-page.py
- [[_replace_between()]] - code - scripts/generate-cve-page.py
- [[_resolve_registries()]] - code - scripts/generate-cve-page.py
- [[agent_cve_registry.py]] - code - gateway/security/agent_cve_registry.py
- [[generate()]] - code - scripts/generate-cve-page.py
- [[generate-cve-page.py]] - code - scripts/generate-cve-page.py
- [[list_cve_agents()]] - code - gateway/security/agent_cve_registry.py
- [[list_cve_agents() must return exactly 'openclaw', 'hermes'.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[test_list_cve_agents_is_list_of_str()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_list_cve_agents_returns_both()]] - code - gateway/tests/test_agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_251
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Module Group 84]]
- 1 edge to [[_COMMUNITY_Module Group 189]]

## Top bridge nodes
- [[generate-cve-page.py]] - degree 8, connects to 1 community
- [[list_cve_agents()]] - degree 7, connects to 1 community
- [[_resolve_registries()]] - degree 5, connects to 1 community
- [[_replace_between()]] - degree 3, connects to 1 community
- [[test_list_cve_agents_returns_both()]] - degree 3, connects to 1 community