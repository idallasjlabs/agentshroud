---
type: community
cohesion: 0.12
members: 31
---

# Migrate Cve Registry Ghsa (scripts)

**Cohesion:** 0.12 - loosely connected
**Members:** 31 nodes

## Members
- [[.__init__()_199]] - code - scripts/migrate-cve-registry-ghsa.py
- [[.confident()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[Any_75]] - code - scripts/migrate-cve-registry-ghsa.py
- [[Compute the per-entry rewrite plan and manual-review buckets.      Returns]] - rationale - scripts/migrate-cve-registry-ghsa.py
- [[Counter]] - code - scripts/migrate-cve-registry-ghsa.py
- [[Fetch every published GitHub Security Advisory for repo (cursor-paginated).]] - rationale - scripts/migrate-cve-registry-ghsa.py
- [[Import the current OpenClaw + Hermes registry lists (in file order).]] - rationale - scripts/migrate-cve-registry-ghsa.py
- [[Lowercase alphanumericunderscore tokens, minus stopwords and short noise.]] - rationale - scripts/migrate-cve-registry-ghsa.py
- [[Match a single registry entry to at most one advisory, honestly.      Returns]] - rationale - scripts/migrate-cve-registry-ghsa.py
- [[MatchResult]] - code - scripts/migrate-cve-registry-ghsa.py
- [[Namespace]] - code - scripts/migrate-cve-registry-ghsa.py
- [[Outcome of matching one registry entry to the advisory feed.]] - rationale - scripts/migrate-cve-registry-ghsa.py
- [[Path_46]] - code - scripts/migrate-cve-registry-ghsa.py
- [[Render the manual-review markdown listing every unmatched entry.]] - rationale - scripts/migrate-cve-registry-ghsa.py
- [[Return per-agent advisory lists from snapshot or live GitHub.]] - rationale - scripts/migrate-cve-registry-ghsa.py
- [[Rewrite every ``id old`` line and set ghsa_idcve_id right after it.]] - rationale - scripts/migrate-cve-registry-ghsa.py
- [[_advisory_patched_versions()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[_advisory_text_tokens()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[_py_literal()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[_tokens()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[build_id_plan()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[compute_stats()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[fetch_advisories()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[gather_advisories()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[load_registry()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[load_snapshot()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[main()_22]] - code - scripts/migrate-cve-registry-ghsa.py
- [[match_entry()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[migrate-cve-registry-ghsa.py]] - code - scripts/migrate-cve-registry-ghsa.py
- [[render_manual_review()]] - code - scripts/migrate-cve-registry-ghsa.py
- [[rewrite_registry_text()]] - code - scripts/migrate-cve-registry-ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Migrate_Cve_Registry_Ghsa_scripts
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Generate Cve Page (scripts)]]
- 1 edge to [[_COMMUNITY_Egress Filter (security)]]
- 1 edge to [[_COMMUNITY_Dashboard]]

## Top bridge nodes
- [[Counter]] - degree 4, connects to 2 communities
- [[migrate-cve-registry-ghsa.py]] - degree 16, connects to 1 community