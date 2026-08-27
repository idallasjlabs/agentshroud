---
source_file: "gateway/proxy/dns_forwarder.py"
type: "code"
community: "Community 560"
location: "L160"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_560
---

# DNSForwarderProtocol

## Connections
- [[.__init__()_21]] - `method` [EXTRACTED]
- [[._handle_query()]] - `method` [EXTRACTED]
- [[._make_protocol()]] - `calls` [EXTRACTED]
- [[.connection_made()]] - `method` [EXTRACTED]
- [[.datagram_received()]] - `method` [EXTRACTED]
- [[.error_received()]] - `method` [EXTRACTED]
- [[.test_error_received_logs()]] - `calls` [EXTRACTED]
- [[DNSBlocklist]] - `uses` [INFERRED]
- [[TestBlocklistDownload]] - `uses` [INFERRED]
- [[TestBlocklistUpdate]] - `uses` [INFERRED]
- [[TestBlocklistWildcardsAndAllowlist]] - `uses` [INFERRED]
- [[TestCanvasAuthHelpers]] - `uses` [INFERRED]
- [[TestCanvasHTTP]] - `uses` [INFERRED]
- [[TestCanvasLifespan]] - `uses` [INFERRED]
- [[TestCanvasWebSocket]] - `uses` [INFERRED]
- [[TestDNSForwarderProtocol]] - `uses` [INFERRED]
- [[TestForwardQuery]] - `uses` [INFERRED]
- [[TestImportFallback]] - `uses` [INFERRED]
- [[TestParseDomainName]] - `uses` [INFERRED]
- [[TestParseQuery]] - `uses` [INFERRED]
- [[TestStartDNSForwarder]] - `uses` [INFERRED]
- [[UDP protocol handler for DNS forwarding with optional blocklist.]] - `rationale_for` [EXTRACTED]
- [[_BlockAll]] - `uses` [INFERRED]
- [[_BlockNone]] - `uses` [INFERRED]
- [[_FakeAsyncClient]] - `uses` [INFERRED]
- [[_FakeUpstreamResponse]] - `uses` [INFERRED]
- [[_FakeUpstreamWS]] - `uses` [INFERRED]
- [[_FakeWSConnect]] - `uses` [INFERRED]
- [[dns_forwarder.py]] - `contains` [EXTRACTED]
- [[start_dns_forwarder()]] - `calls` [EXTRACTED]
- [[test_dns_canvas_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_560