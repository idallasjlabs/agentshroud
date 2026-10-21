---
type: community
members: 4
---

# Required: ≥ 4.5 for text, ≥ 3.0 for UI elements (2)

**Members:** 4 nodes

## Members
- [[Proxy mode — full network isolation + egress control]] - concept - docker-compose.secure.yml
- [[Sidecar mode — optional security scanning]] - concept - docker-compose.sidecar.yml
- [[agentshroud-gateway service (sidecar mode)]] - code - docker-compose.sidecar.yml
- [[openclaw service (exposed, sidecar mode)]] - code - docker-compose.sidecar.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Required__45_for_text__30_for_UI_elements_2
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Required ≥ 4.5 for text, ≥ 3.0 for UI elements]]

## Top bridge nodes
- [[Proxy mode — full network isolation + egress control]] - degree 2, connects to 1 community
