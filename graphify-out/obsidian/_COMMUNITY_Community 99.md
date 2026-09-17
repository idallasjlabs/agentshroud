---
type: community
cohesion: 0.07
members: 52
---

# Community 99

**Cohesion:** 0.07 - loosely connected
**Members:** 52 nodes

## Members
- [[Any_83]] - code
- [[Append new_entries to AGENT_CVE_REGISTRY (OpenClaw). Returns count appended.]] - rationale - scripts/sync-cve-registry.py
- [[Append new_entries to _HERMES_CVE_REGISTRY. Returns count appended. Inserts…]] - rationale - scripts/sync-cve-registry.py
- [[Append under_review new_entries to agent_id's OWN registry list. Inserts…]] - rationale - scripts/sync-cve-registry.py
- [[Diff advisories against an agent's OWN registry and build under_review…]] - rationale - scripts/sync-cve-registry.py
- [[Extract a numeric CVSS base score from an advisory, else None. GitHub…]] - rationale - scripts/sync-cve-registry.py
- [[Fetch every published GitHub Security Advisory for repo (cursor-paginated).]] - rationale - scripts/migrate-cve-registry-ghsa.py
- [[Namespace_1]] - code
- [[Parse raw NVD vulnerability records into registry entry dicts.]] - rationale - scripts/sync-cve-registry.py
- [[Path_63]] - code
- [[Print a human-readable breakdown of new entries by severitystatus.]] - rationale - scripts/sync-cve-registry.py
- [[Read a vendor version from dockerversions.env — the single source of truth…]] - rationale - scripts/sync-cve-registry.py
- [[Return (status, mitigation, defense_layers).]] - rationale - scripts/sync-cve-registry.py
- [[Return True if version a = version b.]] - rationale - scripts/sync-cve-registry.py
- [[Return the first patched version string across the advisory's vulns, else ''.]] - rationale - scripts/sync-cve-registry.py
- [[Return the next zero-padded ASH id number for an agent's registry list.]] - rationale - scripts/sync-cve-registry.py
- [[Return the resolved GitHub advisory repo slug for bot_id. Honors the per-…]] - rationale - gateway/security/agent_cve_registry.py
- [[Run ONE agent's full, independent GHSA pipeline. Returns count registered.…]] - rationale - scripts/sync-cve-registry.py
- [[Run the GHSA pipeline for EVERY registered agent, each on its OWN path. Returns…]] - rationale - scripts/sync-cve-registry.py
- [[Run the legacy NVD keyword source for OpenClaw + Hermes (unchanged).]] - rationale - scripts/sync-cve-registry.py
- [[Serialize an under_review entry to Python source matching the file schema.]] - rationale - scripts/sync-cve-registry.py
- [[Sync per-agent CVEs into gatewaysecurityagent_cve_registry.py. Two…]] - rationale - scripts/sync-cve-registry.py
- [[_classify()]] - code - scripts/sync-cve-registry.py
- [[_entry_to_py()]] - code - scripts/sync-cve-registry.py
- [[_extract_affected_max()]] - code - scripts/sync-cve-registry.py
- [[_extract_fix_version()]] - code - scripts/sync-cve-registry.py
- [[_get_cvss()]] - code - scripts/sync-cve-registry.py
- [[_ghsa_cvss_score()]] - code - scripts/sync-cve-registry.py
- [[_ghsa_entry_to_py()]] - code - scripts/sync-cve-registry.py
- [[_ghsa_patched_version()]] - code - scripts/sync-cve-registry.py
- [[_make_title()]] - code - scripts/sync-cve-registry.py
- [[_next_ash_number()]] - code - scripts/sync-cve-registry.py
- [[_parse_ver()]] - code - scripts/sync-cve-registry.py
- [[_print_summary()]] - code - scripts/sync-cve-registry.py
- [[_process_nvd_results()]] - code - scripts/sync-cve-registry.py
- [[_read_pinned_version()]] - code - scripts/sync-cve-registry.py
- [[_run_nvd_sync()]] - code - scripts/sync-cve-registry.py
- [[_ver_gt()]] - code - scripts/sync-cve-registry.py
- [[_ver_gte()]] - code - scripts/sync-cve-registry.py
- [[append_ghsa_entries()]] - code - scripts/sync-cve-registry.py
- [[append_to_hermes_registry()]] - code - scripts/sync-cve-registry.py
- [[append_to_registry()]] - code - scripts/sync-cve-registry.py
- [[fetch_ghsa_advisories()]] - code - scripts/sync-cve-registry.py
- [[fetch_nvd_cves()]] - code - scripts/sync-cve-registry.py
- [[get_agent_ghsa_repo]] - code - gateway/security/agent_cve_registry.py
- [[lit()]] - code - scripts/sync-cve-registry.py
- [[main()_5]] - code - scripts/sync-cve-registry.py
- [[process_ghsa_advisories()]] - code - scripts/sync-cve-registry.py
- [[qs()]] - code - scripts/sync-cve-registry.py
- [[run_ghsa_sync()]] - code - scripts/sync-cve-registry.py
- [[sync-cve-registry.py]] - code - scripts/sync-cve-registry.py
- [[sync_agent_ghsa()]] - code - scripts/sync-cve-registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_99
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 124]]
- 4 edges to [[_COMMUNITY_Community 458]]
- 2 edges to [[_COMMUNITY_Community 158]]
- 1 edge to [[_COMMUNITY_Community 832]]
- 1 edge to [[_COMMUNITY_Community 268]]

## Top bridge nodes
- [[sync-cve-registry.py]] - degree 31, connects to 2 communities
- [[process_ghsa_advisories()]] - degree 9, connects to 2 communities
- [[get_agent_ghsa_repo]] - degree 6, connects to 2 communities
- [[sync_agent_ghsa()]] - degree 10, connects to 1 community
- [[_classify()]] - degree 6, connects to 1 community