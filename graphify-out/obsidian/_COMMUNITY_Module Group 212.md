---
type: community
cohesion: 0.16
members: 22
---

# Module Group 212

**Cohesion:** 0.16 - loosely connected
**Members:** 22 nodes

## Members
- [[Append new_entries to AGENT_CVE_REGISTRY (OpenClaw).  Returns count appended.]] - rationale - scripts/sync-cve-registry.py
- [[Append new_entries to _HERMES_CVE_REGISTRY.  Returns count appended.      Insert]] - rationale - scripts/sync-cve-registry.py
- [[Parse raw NVD vulnerability records into registry entry dicts.]] - rationale - scripts/sync-cve-registry.py
- [[Print a human-readable breakdown of new entries by severitystatus.]] - rationale - scripts/sync-cve-registry.py
- [[Return (status, mitigation, defense_layers).]] - rationale - scripts/sync-cve-registry.py
- [[Return True if version a = version b.]] - rationale - scripts/sync-cve-registry.py
- [[_classify()]] - code - scripts/sync-cve-registry.py
- [[_entry_to_py()]] - code - scripts/sync-cve-registry.py
- [[_extract_affected_max()]] - code - scripts/sync-cve-registry.py
- [[_extract_fix_version()]] - code - scripts/sync-cve-registry.py
- [[_get_cvss()]] - code - scripts/sync-cve-registry.py
- [[_make_title()]] - code - scripts/sync-cve-registry.py
- [[_parse_ver()]] - code - scripts/sync-cve-registry.py
- [[_print_summary()]] - code - scripts/sync-cve-registry.py
- [[_process_nvd_results()]] - code - scripts/sync-cve-registry.py
- [[_ver_gt()]] - code - scripts/sync-cve-registry.py
- [[_ver_gte()]] - code - scripts/sync-cve-registry.py
- [[append_to_hermes_registry()]] - code - scripts/sync-cve-registry.py
- [[append_to_registry()]] - code - scripts/sync-cve-registry.py
- [[fetch_nvd_cves()]] - code - scripts/sync-cve-registry.py
- [[main()_7]] - code - scripts/sync-cve-registry.py
- [[sync-cve-registry.py]] - code - scripts/sync-cve-registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_212
SORT file.name ASC
```
