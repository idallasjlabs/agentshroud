---
type: community
cohesion: 0.14
members: 14
---

# Module Group 302

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[.__init__()_12]] - code - gateway/proxy/dns_blocklist.py
- [[._periodic_update_loop()]] - code - gateway/proxy/dns_blocklist.py
- [[.download_blocklist()]] - code - gateway/proxy/dns_blocklist.py
- [[.load_from_text()]] - code - gateway/proxy/dns_blocklist.py
- [[.parse_hosts_line()]] - code - gateway/proxy/dns_blocklist.py
- [[.start_periodic_updates()]] - code - gateway/proxy/dns_blocklist.py
- [[.update()]] - code - gateway/proxy/dns_blocklist.py
- [[Background loop update blocklists every UPDATE_INTERVAL_SECONDS.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Download a blocklist URL. Uses the gateway's own HTTP client.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Download all blocklists and rebuild the blocked domains set.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Parse a single line from a hosts-format or domain-only blocklist.          Suppo]] - rationale - gateway/proxy/dns_blocklist.py
- [[Parse blocklist text and add domains. Returns count of new domains.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Path_3]] - code - gateway/proxy/dns_blocklist.py
- [[Start background task for periodic blocklist updates.]] - rationale - gateway/proxy/dns_blocklist.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_302
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Module Group 100]]

## Top bridge nodes
- [[.update()]] - degree 6, connects to 1 community
- [[.parse_hosts_line()]] - degree 4, connects to 1 community
- [[._periodic_update_loop()]] - degree 4, connects to 1 community
- [[.download_blocklist()]] - degree 3, connects to 1 community
- [[.__init__()_12]] - degree 3, connects to 1 community
