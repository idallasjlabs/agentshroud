---
type: community
cohesion: 0.13
members: 24
---

# Module Group 199

**Cohesion:** 0.13 - loosely connected
**Members:** 24 nodes

## Members
- [[.__init__()_33]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_encoded_payloads()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_hidden_content()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_pii()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_prompt_injection()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_zero_width()]] - code - gateway/proxy/web_content_scanner.py
- [[.finding_summary()]] - code - gateway/proxy/web_content_scanner.py
- [[.flagged()_1]] - code - gateway/proxy/web_content_scanner.py
- [[.scan()_1]] - code - gateway/proxy/web_content_scanner.py
- [[A single finding from content scanning.]] - rationale - gateway/proxy/web_content_scanner.py
- [[ContentFinding]] - code - gateway/proxy/web_content_scanner.py
- [[Detect zero-width character sequences (steganographic attacks).]] - rationale - gateway/proxy/web_content_scanner.py
- [[Result of scanning web content.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan HTML for hidden instructions in comments, invisible elements, meta tags.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan content for security issues.          Args             content The web co]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for base64-encoded or otherwise obfuscated payloads.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for prompt injection patterns.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan response content for PII.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan web content for prompt injection, PII, and hidden payloads.      All findin]] - rationale - gateway/proxy/web_content_scanner.py
- [[ScanResult]] - code - gateway/proxy/web_content_scanner.py
- [[URLAnalyzer_1]] - code - gateway/proxy/web_proxy.py
- [[WebContentScanner]] - code - gateway/proxy/web_content_scanner.py
- [[WebContentScanner_1]] - code - gateway/proxy/web_proxy.py
- [[WebProxyConfig_1]] - code - gateway/proxy/web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_199
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_HTTP CONNECT Proxy & Egress]]
- 4 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 3 edges to [[_COMMUNITY_Module Group 62]]
- 3 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 2 edges to [[_COMMUNITY_Module Group 77]]

## Top bridge nodes
- [[WebContentScanner]] - degree 18, connects to 4 communities
- [[URLAnalyzer_1]] - degree 4, connects to 3 communities
- [[WebContentScanner_1]] - degree 4, connects to 3 communities
- [[WebProxyConfig_1]] - degree 4, connects to 3 communities
- [[ScanResult]] - degree 10, connects to 1 community
