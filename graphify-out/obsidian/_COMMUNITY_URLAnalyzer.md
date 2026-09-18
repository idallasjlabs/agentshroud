---
type: community
cohesion: 0.04
members: 79
---

# URLAnalyzer

**Cohesion:** 0.04 - loosely connected
**Members:** 79 nodes

## Members
- [[.__init__()_157]] - code - gateway/proxy/url_analyzer.py
- [[.__init__()_153]] - code - gateway/proxy/web_content_scanner.py
- [[._check_base64()]] - code - gateway/proxy/url_analyzer.py
- [[._is_private_ip()_1]] - code - gateway/proxy/url_analyzer.py
- [[._is_ssrf()]] - code - gateway/proxy/url_analyzer.py
- [[._resolve_host()]] - code - gateway/proxy/url_analyzer.py
- [[._scan_encoded_payloads()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_hidden_content()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_pii()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_prompt_injection()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_zero_width()]] - code - gateway/proxy/web_content_scanner.py
- [[.analyze()_1]] - code - gateway/proxy/url_analyzer.py
- [[.analyze_and_pin()]] - code - gateway/proxy/url_analyzer.py
- [[.finding_summary()]] - code - gateway/proxy/web_content_scanner.py
- [[.flagged()_1]] - code - gateway/proxy/url_analyzer.py
- [[.flagged()]] - code - gateway/proxy/web_content_scanner.py
- [[.get_stats()_19]] - code - gateway/proxy/web_proxy.py
- [[.scan()_3]] - code - gateway/proxy/web_content_scanner.py
- [[.test_actual_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_all_lowercase_not_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_api_endpoint_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_credit_card_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_docs_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_email_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_empty_url()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_github_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_https_allowed()_1]] - code - gateway/tests/test_url_analyzer.py
- [[.test_news_site_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_no_scheme()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_non_base64_chars()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_phone_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_public_ip_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_short_string_not_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_ssn_in_url_flagged()_1]] - code - gateway/tests/test_url_analyzer.py
- [[.test_stackoverflow_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_weird_scheme()]] - code - gateway/tests/test_url_analyzer.py
- [[.to_dict()_17]] - code - gateway/proxy/web_proxy.py
- [[A single finding from URL analysis.]] - rationale - gateway/proxy/url_analyzer.py
- [[A single finding from content scanning.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Analyze URL and pin resolved IP to mitigate DNS rebinding TOCTOU.          When]] - rationale - gateway/proxy/url_analyzer.py
- [[Analyze URLs for SSRF, data exfiltration, and suspicious patterns.]] - rationale - gateway/proxy/url_analyzer.py
- [[Analyze a URL for security issues.          Returns URLAnalysisResult with verdi]] - rationale - gateway/proxy/url_analyzer.py
- [[Any_80]] - code - gateway/proxy/web_proxy.py
- [[Args             resolve_dns If True, resolve hostnames to IPs and check those]] - rationale - gateway/proxy/url_analyzer.py
- [[Check for base64-encoded data in URL path and query values.]] - rationale - gateway/proxy/url_analyzer.py
- [[Check if an IP address is privatereservedloopback.]] - rationale - gateway/proxy/url_analyzer.py
- [[Check if hostname is a privatereserved address (SSRF attempt).]] - rationale - gateway/proxy/url_analyzer.py
- [[ContentFinding]] - code - gateway/proxy/web_content_scanner.py
- [[Detect zero-width character sequences (steganographic attacks).]] - rationale - gateway/proxy/web_content_scanner.py
- [[Edge cases and malformed URLs.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Ensure normal browsing URLs pass through.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Get proxy statistics._1]] - rationale - gateway/proxy/web_proxy.py
- [[Heuristic does this string look like base64-encoded data]] - rationale - gateway/proxy/url_analyzer.py
- [[PII detection in URLs — flagged, not blocked.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Resolve hostname to IP. Returns None on failure.          NOTE DNS rebinding at]] - rationale - gateway/proxy/url_analyzer.py
- [[Result of analyzing a URL.]] - rationale - gateway/proxy/url_analyzer.py
- [[Result of scanning web content.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan HTML for hidden instructions in comments, invisible elements, meta tags.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan content for security issues.          Args             content The web co]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for base64-encoded or otherwise obfuscated payloads.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for prompt injection patterns.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan response content for PII.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan web content for prompt injection, PII, and hidden payloads.      All findin]] - rationale - gateway/proxy/web_content_scanner.py
- [[ScanResult_4]] - code - gateway/proxy/web_content_scanner.py
- [[Test the _looks_like_base64 helper.]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestBase64Heuristic]] - code - gateway/tests/test_url_analyzer.py
- [[TestLegitimateURLsAllowed]] - code - gateway/tests/test_url_analyzer.py
- [[TestMalformedURLs]] - code - gateway/tests/test_url_analyzer.py
- [[TestPIIInURLs]] - code - gateway/tests/test_url_analyzer.py
- [[URLAnalysisResult_1]] - code - gateway/proxy/url_analyzer.py
- [[URLAnalyzer_1]] - code - gateway/proxy/url_analyzer.py
- [[URLAnalyzer]] - code - gateway/proxy/web_proxy.py
- [[URLFinding]] - code - gateway/proxy/url_analyzer.py
- [[WebContentScanner]] - code - gateway/proxy/web_content_scanner.py
- [[WebContentScanner_1]] - code - gateway/proxy/web_proxy.py
- [[WebProxyConfig_1]] - code - gateway/proxy/web_proxy.py
- [[_looks_like_base64()]] - code - gateway/proxy/url_analyzer.py
- [[analyzer()]] - code - gateway/tests/test_url_analyzer.py
- [[test_url_analyzer.py]] - code - gateway/tests/test_url_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/URLAnalyzer
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Enum]]
- 9 edges to [[_COMMUNITY_WebProxy]]
- 6 edges to [[_COMMUNITY_WebProxyConfig]]
- 4 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TestDataExfiltration]]
- 2 edges to [[_COMMUNITY_TestSSRFDetection]]
- 1 edge to [[_COMMUNITY_EgressFilter]]

## Top bridge nodes
- [[URLAnalyzer_1]] - degree 28, connects to 7 communities
- [[WebContentScanner]] - degree 20, connects to 5 communities
- [[test_url_analyzer.py]] - degree 10, connects to 3 communities
- [[Any_80]] - degree 6, connects to 2 communities
- [[URLAnalyzer]] - degree 4, connects to 2 communities