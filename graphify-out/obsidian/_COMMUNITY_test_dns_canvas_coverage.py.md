---
type: community
members: 40
---

# test_dns_canvas_coverage.py

**Members:** 40 nodes

## Members
- [[dot-__init__()_176]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_all_upstreams_fail_returns_none()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_binds_and_returns_transport()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_compression_pointer()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_dns_blocklist_import_failure_sets_none()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_failover_to_second_upstream()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_first_upstream_succeeds()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_pointer_loop_bounded()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_simple_name()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_truncated_name_breaks()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[AgentShroud DNS Blocklist — Pi-hole-compatible domain blocking for the gateway.…]] - rationale - gateway/proxy/dns_blocklist.py
- [[AgentShroud DNS Forwarder — Lightweight DNS proxy for gateway container. Routes…]] - rationale - gateway/proxy/dns_forwarder.py
- [[Build a fake `socket` module namespace driving forward_query without IO. Each…]] - rationale - gateway/tests/test_dns_canvas_coverage.py
- [[Coverage tests for dns_forwarder, dns_blocklist, and canvas_proxy. Exercises…]] - rationale - gateway/tests/test_dns_canvas_coverage.py
- [[DatagramTransport]] - code
- [[Forward a DNS query to upstream resolvers with failover.]] - rationale - gateway/proxy/dns_forwarder.py
- [[Parse a DNS domain name from wire format, handling compression pointers.]] - rationale - gateway/proxy/dns_forwarder.py
- [[Provision a gateway password file and return the password.]] - rationale - gateway/tests/test_dns_canvas_coverage.py
- [[Start the DNS forwarding server with optional blocklist. Returns the transport…]] - rationale - gateway/proxy/dns_forwarder.py
- [[TestForwardQuery]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestImportFallback]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestParseDomainName]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestStartDNSForwarder]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[_FakeUpstreamResponse]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[__init__()_18]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[close()_2]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dns_blocklist.py]] - code - gateway/proxy/dns_blocklist.py
- [[dns_forwarder.py]] - code - gateway/proxy/dns_forwarder.py
- [[fake_httpx_client()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[fixture_112]] - code
- [[forward_query()]] - code - gateway/proxy/dns_forwarder.py
- [[gateway_password()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[main()_30]] - code - gateway/proxy/dns_forwarder.py
- [[make_fake_socket_module()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[parse_domain_name()]] - code - gateway/proxy/dns_forwarder.py
- [[recv()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[sendto()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[settimeout()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[start_dns_forwarder()]] - code - gateway/proxy/dns_forwarder.py
- [[test_dns_canvas_coverage.py]] - code - gateway/tests/test_dns_canvas_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_dns_canvas_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_DNSBlocklist]]
- 7 edges to [[_COMMUNITY_DNSForwarderProtocol]]
- 6 edges to [[_COMMUNITY__run_asgi]]
- 5 edges to [[_COMMUNITY_parse_query]]
- 4 edges to [[_COMMUNITY_TestCanvasAuthHelpers]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY__FakeAsyncClient]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_ingest_apiconfig.py]]
- 1 edge to [[_COMMUNITY_canvas_proxy.py]]

## Top bridge nodes
- [[test_dns_canvas_coverage.py]] - degree 38, connects to 8 communities
- [[dns_forwarder.py]] - degree 11, connects to 4 communities
- [[start_dns_forwarder()]] - degree 9, connects to 3 communities
- [[dns_blocklist.py]] - degree 6, connects to 2 communities
- [[parse_domain_name()]] - degree 8, connects to 1 community
