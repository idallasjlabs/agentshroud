---
type: community
members: 65
---

# Community 562

**Members:** 65 nodes

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
- [[._scan_xml_dtd()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_zero_width()]] - code - gateway/proxy/web_content_scanner.py
- [[._triage()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.analyze()]] - code - gateway/proxy/url_analyzer.py
- [[.analyze_and_pin()]] - code - gateway/proxy/url_analyzer.py
- [[.finding_summary()]] - code - gateway/proxy/web_content_scanner.py
- [[.flagged()]] - code - gateway/proxy/url_analyzer.py
- [[.flagged()_1]] - code - gateway/proxy/web_content_scanner.py
- [[.get_stats()_10]] - code - gateway/proxy/web_proxy.py
- [[.scan()_1]] - code - gateway/proxy/web_content_scanner.py
- [[.test_finding_severity_is_critical()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_libxml2_dtd_uaf_classifies_as_xxe_not_dos()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_unrelated_classes_unchanged()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_web_proxy_blocks_on_dangerous_xml()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_xxe_class_is_covered_by_the_gateway_control()]] - code - gateway/tests/test_xml_dtd_control.py
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
- [[Detect DTDentity constructs that drive XML parser memory-safety bugs.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Detect zero-width character sequences (steganographic attacks).]] - rationale - gateway/proxy/web_content_scanner.py
- [[Get proxy statistics._1]] - rationale - gateway/proxy/web_proxy.py
- [[It calls itself DoS; the generic DOS profile is containment-only.          Left]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[Proves enforcement, not just detection.]] - rationale - gateway/tests/test_xml_dtd_control.py
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
- [[TestDangerousXMLIsBlockedNotFlagged]] - code - gateway/tests/test_xml_dtd_control.py
- [[TestTriageClassLevelCoverage]] - code - gateway/tests/test_xml_dtd_control.py
- [[The distinction this whole control rests on.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[The durable statement is at the CLASS level, not per-CVE.      A register entry]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[The new rule runs first, so prove it does not swallow neighbours.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[URLAnalysisResult]] - code - gateway/proxy/url_analyzer.py
- [[URLAnalyzer]] - code - gateway/proxy/url_analyzer.py
- [[URLAnalyzer_1]] - code - gateway/proxy/web_proxy.py
- [[URLFinding]] - code - gateway/proxy/url_analyzer.py
- [[WebContentScanner]] - code - gateway/proxy/web_content_scanner.py
- [[WebContentScanner_1]] - code - gateway/proxy/web_proxy.py
- [[WebProxyConfig_1]] - code - gateway/proxy/web_proxy.py
- [[test_xml_dtd_control.py]] - code - gateway/tests/test_xml_dtd_control.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_562
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 8]]
- 9 edges to [[_COMMUNITY_Community 27]]
- 9 edges to [[_COMMUNITY_Community 69]]
- 8 edges to [[_COMMUNITY_Community 1000]]
- 6 edges to [[_COMMUNITY_Community 120]]
- 3 edges to [[_COMMUNITY_Community 1137]]
- 3 edges to [[_COMMUNITY_Community 72]]
- 2 edges to [[_COMMUNITY_Community 431]]
- 1 edge to [[_COMMUNITY_Community 68]]
- 1 edge to [[_COMMUNITY_Community 437]]

## Top bridge nodes
- [[URLAnalyzer]] - degree 27, connects to 7 communities
- [[WebContentScanner]] - degree 34, connects to 6 communities
- [[Any_23]] - degree 6, connects to 2 communities
- [[test_xml_dtd_control.py]] - degree 5, connects to 2 communities
- [[WebProxyConfig_1]] - degree 4, connects to 2 communities