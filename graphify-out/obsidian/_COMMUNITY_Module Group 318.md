---
type: community
cohesion: 0.22
members: 13
---

# Module Group 318

**Cohesion:** 0.22 - loosely connected
**Members:** 13 nodes

## Members
- [[._handle_query()]] - code - gateway/proxy/dns_forwarder.py
- [[.datagram_received()]] - code - gateway/proxy/dns_forwarder.py
- [[.test_malformed_pointer_returns_none()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_too_short()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_truncated_after_name()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_valid_a_query()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_valid_aaaa_query()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_zero_qdcount()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[Extract domain name and query type from a DNS query packet.      Returns (domai]] - rationale - gateway/proxy/dns_forwarder.py
- [[Handle incoming DNS query.]] - rationale - gateway/proxy/dns_forwarder.py
- [[Process a single DNS query log, forward, respond.]] - rationale - gateway/proxy/dns_forwarder.py
- [[TestParseQuery]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[parse_query()]] - code - gateway/proxy/dns_forwarder.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_318
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 275]]
- 3 edges to [[_COMMUNITY_Module Group 265]]
- 2 edges to [[_COMMUNITY_Module Group 291]]
- 1 edge to [[_COMMUNITY_Module Group 100]]
- 1 edge to [[_COMMUNITY_Module Group 430]]

## Top bridge nodes
- [[TestParseQuery]] - degree 9, connects to 3 communities
- [[parse_query()]] - degree 11, connects to 2 communities
- [[._handle_query()]] - degree 5, connects to 2 communities
- [[.datagram_received()]] - degree 3, connects to 1 community
- [[.test_valid_a_query()]] - degree 3, connects to 1 community