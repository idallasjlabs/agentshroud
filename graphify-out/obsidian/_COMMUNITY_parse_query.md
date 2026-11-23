---
type: community
members: 13
---

# parse_query

**Members:** 13 nodes

## Members
- [[dot-_handle_query()]] - code - gateway/proxy/dns_forwarder.py
- [[dot-datagram_received()]] - code - gateway/proxy/dns_forwarder.py
- [[dot-test_malformed_pointer_returns_none()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_too_short()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_truncated_after_name()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_valid_a_query()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_valid_aaaa_query()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_zero_qdcount()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[Extract domain name and query type from a DNS query packet. Returns (domain,…]] - rationale - gateway/proxy/dns_forwarder.py
- [[Handle incoming DNS query.]] - rationale - gateway/proxy/dns_forwarder.py
- [[Process a single DNS query log, forward, respond.]] - rationale - gateway/proxy/dns_forwarder.py
- [[TestParseQuery]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[parse_query()]] - code - gateway/proxy/dns_forwarder.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/parse_query
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_dns_canvas_coverage.py]]
- 4 edges to [[_COMMUNITY_DNSForwarderProtocol]]
- 1 edge to [[_COMMUNITY_make_fake_socket_module]]

## Top bridge nodes
- [[dot-_handle_query()]] - degree 5, connects to 2 communities
- [[parse_query()]] - degree 11, connects to 1 community
- [[TestParseQuery]] - degree 7, connects to 1 community
- [[dot-datagram_received()]] - degree 3, connects to 1 community
- [[dot-test_valid_a_query()]] - degree 3, connects to 1 community
