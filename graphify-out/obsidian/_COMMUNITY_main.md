---
type: community
cohesion: 0.43
members: 7
---

# main

**Cohesion:** 0.43 - moderately connected
**Members:** 7 nodes

## Members
- [[Cron Daily CVE Triage & Remediation Scan]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[curl_json()]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[cve_prefetch.py]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[gatewaysecurityagent_cve_registry.py GHSA registry]] - concept - docker/config/openclaw/cron/scripts/prefetch-ghsa-registry.sh
- [[known_ghsa_ids()]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[main()_30]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[prefetch-ghsa-registry.sh (known-GHSA-ID cache prefetch)]] - code - docker/config/openclaw/cron/scripts/prefetch-ghsa-registry.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/main
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_sunday-upgrade-apply.sh]]

## Top bridge nodes
- [[gatewaysecurityagent_cve_registry.py GHSA registry]] - degree 3, connects to 1 community
