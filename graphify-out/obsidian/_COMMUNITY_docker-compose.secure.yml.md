---
type: community
cohesion: 0.40
members: 5
---

# docker-compose.secure.yml

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[Dual Network Topology external + internal (isolated)]] - rationale - docker-compose.secure.yml
- [[OpenClaw Container Isolation No Port Mapping, DNS via Gateway]] - code - docker-compose.secure.yml
- [[Sidecar Mode Warning Does Not Guarantee All Traffic Scanned]] - rationale - docker-compose.sidecar.yml
- [[docker-compose.secure.yml Full Network Isolation Proxy Mode]] - code - docker-compose.secure.yml
- [[docker-compose.sidecar.yml Optional Sidecar Scanning Mode]] - code - docker-compose.sidecar.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/docker-composesecureyml
SORT file.name ASC
```
