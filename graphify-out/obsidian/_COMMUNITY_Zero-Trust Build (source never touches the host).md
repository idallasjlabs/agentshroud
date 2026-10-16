---
type: community
cohesion: 1.00
members: 2
---

# Zero-Trust Build (source never touches the host)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[Secure Multi-Stage Docker Build (builder discarded)]] - rationale - docs/archive/SECURITY.md
- [[Zero-Trust Build (source never touches the host)]] - rationale - docs/archive/SECURITY-AUDIT.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Zero-Trust_Build_source_never_touches_the_host
SORT file.name ASC
```
