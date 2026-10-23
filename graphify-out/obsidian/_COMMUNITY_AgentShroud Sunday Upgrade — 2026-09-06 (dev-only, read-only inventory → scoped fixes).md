---
type: community
cohesion: 0.12
members: 23
---

# AgentShroud Sunday Upgrade — 2026-09-06 (dev-only, read-only inventory → scoped fixes)

**Cohesion:** 0.12 - loosely connected
**Members:** 23 nodes

## Members
- [[AgentShroud Infrastructure (own images reported in full)]] - concept - docs/index.html
- [[AgentShroud public site + CVE page]] - document - docs/index.html
- [[Build the H2 heading block for one agent's CVE section.]] - rationale - scripts/generate-cve-page.py
- [[Build the full paginated CVE table block for one agent's section.      Args]] - rationale - scripts/generate-cve-page.py
- [[Commit, auto-PR, merge and prove state change]] - code - .github/workflows/update-cve-page.yml
- [[Daily CVE Sync + Page Update workflow]] - code - .github/workflows/update-cve-page.yml
- [[Hermes CVE table (cves-hermes, paginated)]] - concept - docs/index.html
- [[Mitigation status badges (crithighmedlowokpartial)]] - concept - docs/index.html
- [[OpenClaw CVE table (cves, paginated)]] - concept - docs/index.html
- [[Read pinned vendor versions step]] - code - .github/workflows/update-cve-page.yml
- [[Regenerate all CVE sections in docsindex.html.  Returns True if changed.]] - rationale - scripts/generate-cve-page.py
- [[Registry tests gate the auto-PR]] - code - .github/workflows/update-cve-page.yml
- [[Return a mapping of bot_id → CVE list, using the new API when available.      Fa]] - rationale - scripts/generate-cve-page.py
- [[Return the human-readable display name for a bot_id.]] - rationale - scripts/generate-cve-page.py
- [[_agent_display_name()]] - code - scripts/generate-cve-page.py
- [[_build_heading()]] - code - scripts/generate-cve-page.py
- [[_build_table()]] - code - scripts/generate-cve-page.py
- [[_replace_between()]] - code - scripts/generate-cve-page.py
- [[_resolve_registries()]] - code - scripts/generate-cve-page.py
- [[dockerversions.env]] - code - .github/workflows/update-cve-page.yml
- [[gatewaysecurityagent_cve_registry.py (AGENT_CVE_REGISTRY  HERMES_CVE_REGISTRY)]] - code - .github/workflows/update-cve-page.yml
- [[generate()]] - code - scripts/generate-cve-page.py
- [[generate-cve-page.py]] - code - scripts/generate-cve-page.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Sunday_Upgrade__2026-09-06_dev-only_read-only_inventory__scoped_fixes
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_A2APolicyEngine]]
- 2 edges to [[_COMMUNITY_run-standalone.sh]]
- 2 edges to [[_COMMUNITY_browserscriptsbrowse.py]]
- 1 edge to [[_COMMUNITY__wrap_response() (2)]]
- 1 edge to [[_COMMUNITY_GatewayEmailService]]

## Top bridge nodes
- [[generate-cve-page.py]] - degree 12, connects to 2 communities
- [[AgentShroud public site + CVE page]] - degree 7, connects to 1 community
- [[_resolve_registries()]] - degree 5, connects to 1 community
- [[gatewaysecurityagent_cve_registry.py (AGENT_CVE_REGISTRY  HERMES_CVE_REGISTRY)]] - degree 5, connects to 1 community
- [[Daily CVE Sync + Page Update workflow]] - degree 5, connects to 1 community
