---
type: community
members: 84
---

# TestSSRFDetection

**Members:** 84 nodes

## Members
- [[dot-__init__()_160]] - code - gateway/proxy/url_analyzer.py
- [[dot-_check_base64()]] - code - gateway/proxy/url_analyzer.py
- [[dot-_is_private_ip()_1]] - code - gateway/proxy/url_analyzer.py
- [[dot-_is_ssrf()]] - code - gateway/proxy/url_analyzer.py
- [[dot-_resolve_host()]] - code - gateway/proxy/url_analyzer.py
- [[dot-analyze()]] - code - gateway/proxy/url_analyzer.py
- [[dot-analyze_and_pin()]] - code - gateway/proxy/url_analyzer.py
- [[dot-flagged()_2]] - code - gateway/proxy/url_analyzer.py
- [[dot-test_0_0_0_0_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_10_255_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_10_x_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_127_0_0_1_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_127_x_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_169_254_link_local_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_172_16_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_172_31_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_192_168_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_actual_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_all_lowercase_not_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_api_endpoint_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_base64_in_path_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_base64_in_query_flagged()_1]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_credit_card_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_decimal_ip_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_docs_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_email_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_empty_url()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_github_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_hex_ip_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_https_allowed()_1]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_ip6_localhost_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_ipv4_mapped_ipv6_blocked()_1]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_ipv4_mapped_ipv6_private_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_ipv6_link_local_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_ipv6_loopback_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_ipv6_ula_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_localhost_blocked()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_long_query_string_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_many_params_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_news_site_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_no_scheme()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_non_base64_chars()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_normal_query_not_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_phone_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_public_ip_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_short_base64_not_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_short_string_not_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_ssn_in_url_flagged()_1]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_stackoverflow_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_weird_scheme()]] - code - gateway/tests/test_url_analyzer.py
- [[0x7f000001 = 127.0.0.1 in hex.]] - rationale - gateway/tests/test_url_analyzer.py
- [[2130706433 = 127.0.0.1 in decimal.]] - rationale - gateway/tests/test_url_analyzer.py
- [[A single finding from URL analysis.]] - rationale - gateway/proxy/url_analyzer.py
- [[Analyze URL and pin resolved IP to mitigate DNS rebinding TOCTOU.          When]] - rationale - gateway/proxy/url_analyzer.py
- [[Analyze URLs for SSRF, data exfiltration, and suspicious patterns.]] - rationale - gateway/proxy/url_analyzer.py
- [[Analyze a URL for security issues.          Returns URLAnalysisResult with verdi]] - rationale - gateway/proxy/url_analyzer.py
- [[Args             resolve_dns If True, resolve hostnames to IPs and check those]] - rationale - gateway/proxy/url_analyzer.py
- [[Check for base64-encoded data in URL path and query values.]] - rationale - gateway/proxy/url_analyzer.py
- [[Check if an IP address is privatereservedloopback.]] - rationale - gateway/proxy/url_analyzer.py
- [[Check if hostname is a privatereserved address (SSRF attempt).]] - rationale - gateway/proxy/url_analyzer.py
- [[Data exfiltration patterns in URLs — flagged, not blocked.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Edge cases and malformed URLs.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Ensure normal browsing URLs pass through.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Heuristic does this string look like base64-encoded data]] - rationale - gateway/proxy/url_analyzer.py
- [[PII detection in URLs — flagged, not blocked.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Resolve hostname to IP. Returns None on failure.          NOTE DNS rebinding at]] - rationale - gateway/proxy/url_analyzer.py
- [[Result of analyzing a URL.]] - rationale - gateway/proxy/url_analyzer.py
- [[SSRF blocking — the one hard block.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Short base64 strings are normal (e.g., API tokens in URLs).]] - rationale - gateway/tests/test_url_analyzer.py
- [[Test the _looks_like_base64 helper.]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestBase64Heuristic]] - code - gateway/tests/test_url_analyzer.py
- [[TestDataExfiltration_1]] - code - gateway/tests/test_url_analyzer.py
- [[TestLegitimateURLsAllowed]] - code - gateway/tests/test_url_analyzer.py
- [[TestMalformedURLs]] - code - gateway/tests/test_url_analyzer.py
- [[TestPIIInURLs]] - code - gateway/tests/test_url_analyzer.py
- [[TestSSRFDetection]] - code - gateway/tests/test_url_analyzer.py
- [[URLAnalysisResult]] - code - gateway/proxy/url_analyzer.py
- [[URLAnalyzer_1]] - code - gateway/proxy/url_analyzer.py
- [[URLFinding]] - code - gateway/proxy/url_analyzer.py
- [[URLVerdict]] - code - gateway/proxy/url_analyzer.py
- [[_looks_like_base64()]] - code - gateway/proxy/url_analyzer.py
- [[analyzer()]] - code - gateway/tests/test_url_analyzer.py
- [[test_url_analyzer.py]] - code - gateway/tests/test_url_analyzer.py
- [[url_analyzer.py]] - code - gateway/proxy/url_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSSRFDetection
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_WebContentScanner]]
- 2 edges to [[_COMMUNITY_WebProxyConfig]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig (3)]]

## Top bridge nodes
- [[url_analyzer.py]] - degree 8, connects to 3 communities
- [[URLAnalyzer_1]] - degree 19, connects to 2 communities
- [[TestDataExfiltration_1]] - degree 11, connects to 1 community
- [[URLVerdict]] - degree 10, connects to 1 community
