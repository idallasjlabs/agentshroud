---
type: community
members: 49
---

# Community 5

**Members:** 49 nodes

## Members
- [[.__init__()_41]] - code - gateway/proxy/url_analyzer.py
- [[.__init__()_42]] - code - gateway/proxy/web_content_scanner.py
- [[._check_base64()]] - code - gateway/proxy/url_analyzer.py
- [[._is_private_ip()]] - code - gateway/proxy/url_analyzer.py
- [[._is_ssrf()]] - code - gateway/proxy/url_analyzer.py
- [[._resolve_host()]] - code - gateway/proxy/url_analyzer.py
- [[._scan_encoded_payloads()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_hidden_content()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_pii()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_prompt_injection()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_zero_width()]] - code - gateway/proxy/web_content_scanner.py
- [[.analyze()]] - code - gateway/proxy/url_analyzer.py
- [[.analyze_and_pin()]] - code - gateway/proxy/url_analyzer.py
- [[.finding_summary()]] - code - gateway/proxy/web_content_scanner.py
- [[.flagged()]] - code - gateway/proxy/url_analyzer.py
- [[.flagged()_1]] - code - gateway/proxy/web_content_scanner.py
- [[.get_stats()_10]] - code - gateway/proxy/web_proxy.py
- [[.scan()_1]] - code - gateway/proxy/web_content_scanner.py
- [[.to_dict()_2]] - code - gateway/proxy/web_proxy.py
- [[A single finding from URL analysis.]] - rationale - gateway/proxy/url_analyzer.py
- [[A single finding from content scanning.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Analyze URL and pin resolved IP to mitigate DNS rebinding TOCTOU.          When]] - rationale - gateway/proxy/url_analyzer.py
- [[Analyze URLs for SSRF, data exfiltration, and suspicious patterns.]] - rationale - gateway/proxy/url_analyzer.py
- [[Analyze a URL for security issues.          Returns URLAnalysisResult with verdi]] - rationale - gateway/proxy/url_analyzer.py
- [[Any_23]] - code - gateway/proxy/web_proxy.py
- [[Args             resolve_dns If True, resolve hostnames to IPs and check those]] - rationale - gateway/proxy/url_analyzer.py
- [[Check for base64-encoded data in URL path and query values.]] - rationale - gateway/proxy/url_analyzer.py
- [[Check if an IP address is privatereservedloopback.]] - rationale - gateway/proxy/url_analyzer.py
- [[Check if hostname is a privatereserved address (SSRF attempt).]] - rationale - gateway/proxy/url_analyzer.py
- [[ContentFinding]] - code - gateway/proxy/web_content_scanner.py
- [[Detect zero-width character sequences (steganographic attacks).]] - rationale - gateway/proxy/web_content_scanner.py
- [[Get proxy statistics._1]] - rationale - gateway/proxy/web_proxy.py
- [[Resolve hostname to IP. Returns None on failure.          NOTE DNS rebinding at]] - rationale - gateway/proxy/url_analyzer.py
- [[Result of analyzing a URL.]] - rationale - gateway/proxy/url_analyzer.py
- [[Result of scanning web content.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan HTML for hidden instructions in comments, invisible elements, meta tags.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan content for security issues.          Args             content The web co]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for base64-encoded or otherwise obfuscated payloads.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for prompt injection patterns.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan response content for PII.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan web content for prompt injection, PII, and hidden payloads.      All findin]] - rationale - gateway/proxy/web_content_scanner.py
- [[ScanResult]] - code - gateway/proxy/web_content_scanner.py
- [[URLAnalysisResult]] - code - gateway/proxy/url_analyzer.py
- [[URLAnalyzer]] - code - gateway/proxy/url_analyzer.py
- [[URLAnalyzer_1]] - code - gateway/proxy/web_proxy.py
- [[URLFinding]] - code - gateway/proxy/url_analyzer.py
- [[WebContentScanner]] - code - gateway/proxy/web_content_scanner.py
- [[WebContentScanner_1]] - code - gateway/proxy/web_proxy.py
- [[WebProxyConfig_1]] - code - gateway/proxy/web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_5
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 30]]
- 8 edges to [[_COMMUNITY_Community 1129]]
- 6 edges to [[_COMMUNITY_Community 78]]
- 6 edges to [[_COMMUNITY_Community 119]]
- 5 edges to [[_COMMUNITY_Community 6]]
- 1 edge to [[_COMMUNITY_Community 282]]
- 1 edge to [[_COMMUNITY_Community 406]]
- 1 edge to [[_COMMUNITY_Community 46]]

## Top bridge nodes
- [[URLAnalyzer]] - degree 28, connects to 7 communities
- [[WebContentScanner]] - degree 20, connects to 5 communities
- [[Any_23]] - degree 6, connects to 2 communities
- [[WebProxyConfig_1]] - degree 4, connects to 2 communities
- [[URLAnalyzer_1]] - degree 4, connects to 2 communities