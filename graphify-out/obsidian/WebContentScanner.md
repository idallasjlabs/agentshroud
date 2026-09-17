---
source_file: "gateway/proxy/web_content_scanner.py"
type: "code"
community: "URLAnalyzer"
location: "L176"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/URLAnalyzer
---

# WebContentScanner

## Connections
- [[.__init__()_153]] - `method` [EXTRACTED]
- [[._scan_encoded_payloads()]] - `method` [EXTRACTED]
- [[._scan_hidden_content()]] - `method` [EXTRACTED]
- [[._scan_pii()]] - `method` [EXTRACTED]
- [[._scan_prompt_injection()]] - `method` [EXTRACTED]
- [[._scan_zero_width()]] - `method` [EXTRACTED]
- [[.scan()_3]] - `method` [EXTRACTED]
- [[Any_80]] - `uses` [INFERRED]
- [[DNSFilter]] - `semantically_similar_to` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[Scan web content for prompt injection, PII, and hidden payloads.      All findin]] - `rationale_for` [EXTRACTED]
- [[URLAnalyzer_1]] - `semantically_similar_to` [INFERRED]
- [[URLAnalyzer]] - `uses` [INFERRED]
- [[WebContentScanner_1]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig_1]] - `uses` [INFERRED]
- [[WebProxyResult]] - `uses` [INFERRED]
- [[web_content_scanner.py]] - `contains` [EXTRACTED]
- [[web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/URLAnalyzer