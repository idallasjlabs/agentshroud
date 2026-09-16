---
type: community
cohesion: 0.40
members: 6
---

# Community 1130

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Members
- [[Cron Daily CVE Triage & Remediation Scan]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[curl_json]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[gatewaysecurityagent_cve_registry.py GHSA registry]] - concept - docker/config/openclaw/cron/scripts/prefetch-ghsa-registry.sh
- [[known_ghsa_ids]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[main (cve_prefetch.py)]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[prefetch-ghsa-registry.sh (known-GHSA-ID cache prefetch)]] - code - docker/config/openclaw/cron/scripts/prefetch-ghsa-registry.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1130
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 832]]

## Top bridge nodes
- [[gatewaysecurityagent_cve_registry.py GHSA registry]] - degree 3, connects to 1 community