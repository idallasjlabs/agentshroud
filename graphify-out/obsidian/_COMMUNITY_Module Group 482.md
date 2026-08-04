---
type: community
cohesion: 0.33
members: 6
---

# Module Group 482

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[._is_private_ip()_1]] - code - gateway/security/dns_filter.py
- [[.check_rebinding()]] - code - gateway/security/dns_filter.py
- [[.resolve_and_cache()]] - code - gateway/security/dns_filter.py
- [[Resolve domain to an IP and cache it for 5 minutes.]] - rationale - gateway/security/dns_filter.py
- [[Return True if a DNS rebinding attack is detected.          Re-resolves the doma]] - rationale - gateway/security/dns_filter.py
- [[Return True if the IP address is in a private  loopback range.]] - rationale - gateway/security/dns_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_482
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]

## Top bridge nodes
- [[.check_rebinding()]] - degree 4, connects to 1 community
- [[._is_private_ip()_1]] - degree 3, connects to 1 community
- [[.resolve_and_cache()]] - degree 3, connects to 1 community
