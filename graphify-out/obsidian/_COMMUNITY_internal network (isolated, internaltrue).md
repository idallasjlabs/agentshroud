---
type: community
members: 3
---

# internal network (isolated, internal:true)

**Members:** 3 nodes

## Members
- [[internal network (isolated, internaltrue)]] - code - docker-compose.secure.yml
- [[openclaw service (proxy mode, internal-only network)]] - code - docker-compose.secure.yml
- [[wazuh service (proxy-mode HIDS sidecar)]] - code - docker-compose.secure.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/internal_network_isolated_internaltrue
SORT file.name ASC
```
