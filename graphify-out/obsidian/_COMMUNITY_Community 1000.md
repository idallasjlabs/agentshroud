---
type: community
members: 62
---

# Community 1000

**Members:** 62 nodes

## Members
- [[.__init__()_41]] - code - gateway/proxy/url_analyzer.py
- [[._check_base64()]] - code - gateway/proxy/url_analyzer.py
- [[._is_private_ip()]] - code - gateway/proxy/url_analyzer.py
- [[._is_ssrf()]] - code - gateway/proxy/url_analyzer.py
- [[._resolve_host()]] - code - gateway/proxy/url_analyzer.py
- [[.analyze()]] - code - gateway/proxy/url_analyzer.py
- [[.analyze_and_pin()]] - code - gateway/proxy/url_analyzer.py
- [[.flagged()]] - code - gateway/proxy/url_analyzer.py
- [[.test_actual_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_all_lowercase_not_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_api_endpoint_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_base64_in_path_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_base64_in_query_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_credit_card_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_docs_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_email_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_empty_url()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_github_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_https_allowed()_1]] - code - gateway/tests/test_url_analyzer.py
- [[.test_long_query_string_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_many_params_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_news_site_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_no_scheme()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_non_base64_chars()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_normal_query_not_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_phone_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_public_ip_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_short_base64_not_flagged()_1]] - code - gateway/tests/test_url_analyzer.py
- [[.test_short_string_not_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_ssn_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_stackoverflow_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_weird_scheme()]] - code - gateway/tests/test_url_analyzer.py
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
- [[Short base64 strings are normal (e.g., API tokens in URLs).]] - rationale - gateway/tests/test_url_analyzer.py
- [[Test the _looks_like_base64 helper.]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestBase64Heuristic]] - code - gateway/tests/test_url_analyzer.py
- [[TestDataExfiltration]] - code - gateway/tests/test_url_analyzer.py
- [[TestLegitimateURLsAllowed]] - code - gateway/tests/test_url_analyzer.py
- [[TestMalformedURLs]] - code - gateway/tests/test_url_analyzer.py
- [[TestPIIInURLs]] - code - gateway/tests/test_url_analyzer.py
- [[URLAnalysisResult]] - code - gateway/proxy/url_analyzer.py
- [[URLAnalyzer]] - code - gateway/proxy/url_analyzer.py
- [[URLFinding]] - code - gateway/proxy/url_analyzer.py
- [[_looks_like_base64()]] - code - gateway/proxy/url_analyzer.py
- [[analyzer()]] - code - gateway/tests/test_url_analyzer.py
- [[test_url_analyzer.py]] - code - gateway/tests/test_url_analyzer.py
- [[url_analyzer.py]] - code - gateway/proxy/url_analyzer.py
- [[web_config.py]] - code - gateway/proxy/web_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1000
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 8]]
- 6 edges to [[_COMMUNITY_Community 431]]
- 5 edges to [[_COMMUNITY_Community 27]]
- 3 edges to [[_COMMUNITY_Community 120]]
- 2 edges to [[_COMMUNITY_Community 437]]
- 1 edge to [[_COMMUNITY_Community 104]]
- 1 edge to [[_COMMUNITY_Community 162]]
- 1 edge to [[_COMMUNITY_Community 17]]

## Top bridge nodes
- [[URLAnalyzer]] - degree 27, connects to 5 communities
- [[web_config.py]] - degree 6, connects to 4 communities
- [[TestDataExfiltration]] - degree 11, connects to 2 communities
- [[test_url_analyzer.py]] - degree 10, connects to 2 communities
- [[url_analyzer.py]] - degree 8, connects to 2 communities