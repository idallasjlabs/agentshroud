---
type: community
members: 5
---

# cve_prefetch.py

**Members:** 5 nodes

## Members
- [[Deterministic prefetch for the CVE Triage cron job. Fetches both GitHub…]] - rationale - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[curl_json()]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[cve_prefetch.py]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[known_ghsa_ids()]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[main()_14]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/cve_prefetchpy
SORT file.name ASC
```
