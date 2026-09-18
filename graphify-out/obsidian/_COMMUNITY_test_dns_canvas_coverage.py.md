---
type: community
cohesion: 0.12
members: 21
---

# test_dns_canvas_coverage.py

**Cohesion:** 0.12 - loosely connected
**Members:** 21 nodes

## Members
- [[.__aenter__()_2]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.__aexit__()_2]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.__init__()_145]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.__init__()_146]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.request()_2]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_compression_pointer()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_dns_blocklist_import_failure_sets_none()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_pointer_loop_bounded()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_simple_name()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_truncated_name_breaks()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[Parse a DNS domain name from wire format, handling compression pointers.]] - rationale - gateway/proxy/dns_forwarder.py
- [[Provision a gateway password file and return the password.]] - rationale - gateway/tests/test_dns_canvas_coverage.py
- [[Stands in for httpx.AsyncClient; records request kwargs.]] - rationale - gateway/tests/test_dns_canvas_coverage.py
- [[TestImportFallback]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestParseDomainName]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[_FakeAsyncClient]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[_FakeUpstreamResponse]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[fake_httpx_client()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[gateway_password()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[parse_domain_name()]] - code - gateway/proxy/dns_forwarder.py
- [[test_dns_canvas_coverage.py]] - code - gateway/tests/test_dns_canvas_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_dns_canvas_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_DNSBlocklist]]
- 8 edges to [[_COMMUNITY__FakeUpstreamWS]]
- 8 edges to [[_COMMUNITY_DNSForwarderProtocol]]
- 3 edges to [[_COMMUNITY_forward_query()]]
- 3 edges to [[_COMMUNITY_parse_query()]]
- 3 edges to [[_COMMUNITY_TestDNSForwarderProtocol]]
- 2 edges to [[_COMMUNITY_TestCanvasAuthHelpers]]
- 1 edge to [[_COMMUNITY_canvas_proxy_app()]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]

## Top bridge nodes
- [[test_dns_canvas_coverage.py]] - degree 35, connects to 9 communities
- [[parse_domain_name()]] - degree 8, connects to 2 communities
- [[_FakeAsyncClient]] - degree 8, connects to 2 communities
- [[TestParseDomainName]] - degree 7, connects to 2 communities
- [[_FakeUpstreamResponse]] - degree 5, connects to 2 communities