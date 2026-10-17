---
type: community
members: 12
---

# agent_cve_registry.py

**Members:** 12 nodes

## Members
- [[Build the H2 heading block for one agent's CVE section.]] - rationale - scripts/generate-cve-page.py
- [[Build the full paginated CVE table block for one agent's section.      Args]] - rationale - scripts/generate-cve-page.py
- [[Regenerate all CVE sections in docsindex.html.  Returns True if changed.]] - rationale - scripts/generate-cve-page.py
- [[Return a mapping of bot_id → CVE list, using the new API when available.      Fa]] - rationale - scripts/generate-cve-page.py
- [[Return the human-readable display name for a bot_id.]] - rationale - scripts/generate-cve-page.py
- [[_agent_display_name()]] - code - scripts/generate-cve-page.py
- [[_build_heading()]] - code - scripts/generate-cve-page.py
- [[_build_table()]] - code - scripts/generate-cve-page.py
- [[_replace_between()]] - code - scripts/generate-cve-page.py
- [[_resolve_registries()]] - code - scripts/generate-cve-page.py
- [[generate()]] - code - scripts/generate-cve-page.py
- [[generate-cve-page.py]] - code - scripts/generate-cve-page.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agent_cve_registrypy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY__make_cve]]

## Top bridge nodes
- [[generate-cve-page.py]] - degree 9, connects to 2 communities
- [[_resolve_registries()]] - degree 5, connects to 1 community
