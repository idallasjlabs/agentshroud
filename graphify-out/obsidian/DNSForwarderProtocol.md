---
source_file: "gateway/proxy/dns_forwarder.py"
type: "code"
community: "Community 573"
location: "L160"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_573
---

# DNSForwarderProtocol

## Connections
- [[dot-__init__()_166]] - `method` [EXTRACTED]
- [[dot-_handle_query()]] - `method` [EXTRACTED]
- [[dot-_make_protocol()]] - `calls` [EXTRACTED]
- [[dot-connection_made()]] - `method` [EXTRACTED]
- [[dot-datagram_received()]] - `method` [EXTRACTED]
- [[dot-error_received()]] - `method` [EXTRACTED]
- [[dot-test_error_received_logs()]] - `calls` [EXTRACTED]
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

#graphify/code #graphify/INFERRED #community/Community_573