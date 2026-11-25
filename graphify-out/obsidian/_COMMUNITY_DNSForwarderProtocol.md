---
type: community
members: 24
---

# DNSForwarderProtocol

**Members:** 24 nodes

## Members
- [[dot-__init__()_193]] - code - gateway/proxy/dns_forwarder.py
- [[dot-_make_protocol()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-connection_made()]] - code - gateway/proxy/dns_forwarder.py
- [[dot-error_received()]] - code - gateway/proxy/dns_forwarder.py
- [[dot-is_blocked()_1]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-is_blocked()_2]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_all_upstreams_fail_sends_servfail()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_blocked_a_query_returns_zero_ip()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_blocked_aaaa_query_returns_null_ipv6()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_blocked_other_qtype_returns_nxdomain()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_datagram_received_schedules_handler()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_error_received_logs()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_forwarded_query_relays_upstream_response()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_short_upstream_response_still_relayed()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_unparseable_short_query_no_servfail_sent()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[Blocklist stub that blocks every domain.]] - rationale - gateway/tests/test_dns_canvas_coverage.py
- [[Blocklist stub that blocks nothing.]] - rationale - gateway/tests/test_dns_canvas_coverage.py
- [[Build a minimal DNS query packet in wire format.]] - rationale - gateway/tests/test_dns_canvas_coverage.py
- [[DNSForwarderProtocol]] - code - gateway/proxy/dns_forwarder.py
- [[TestDNSForwarderProtocol]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[UDP protocol handler for DNS forwarding with optional blocklist.]] - rationale - gateway/proxy/dns_forwarder.py
- [[_BlockAll]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[_BlockNone]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[build_dns_query()]] - code - gateway/tests/test_dns_canvas_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DNSForwarderProtocol
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_dns_canvas_coverage.py]]
- 4 edges to [[_COMMUNITY_AsyncMock]]
- 4 edges to [[_COMMUNITY_parse_query]]

## Top bridge nodes
- [[DNSForwarderProtocol]] - degree 12, connects to 2 communities
- [[build_dns_query()]] - degree 11, connects to 2 communities
- [[TestDNSForwarderProtocol]] - degree 12, connects to 1 community
- [[_BlockAll]] - degree 7, connects to 1 community
- [[dot-test_forwarded_query_relays_upstream_response()]] - degree 5, connects to 1 community
