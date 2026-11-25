---
type: community
members: 61
---

# test_url_analyzer.py

**Members:** 61 nodes

## Members
- [[dot-_check_base64()]] - code - gateway/proxy/url_analyzer.py
- [[dot-_is_private_ip()]] - code - gateway/proxy/url_analyzer.py
- [[dot-_is_ssrf()]] - code - gateway/proxy/url_analyzer.py
- [[dot-_resolve_host()]] - code - gateway/proxy/url_analyzer.py
- [[dot-analyze()]] - code - gateway/proxy/url_analyzer.py
- [[dot-flagged()]] - code - gateway/proxy/url_analyzer.py
- [[dot-test_actual_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_all_lowercase_not_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_api_endpoint_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_base64_in_path_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_base64_in_query_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_credit_card_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_docs_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_email_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_empty_url()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_github_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_https_allowed()]] - code - gateway/tests/test_url_analyzer.py
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
- [[dot-test_ssn_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_stackoverflow_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_weird_scheme()]] - code - gateway/tests/test_url_analyzer.py
- [[A single finding from URL analysis.]] - rationale - gateway/proxy/url_analyzer.py
- [[Analyze a URL for security issues. Returns URLAnalysisResult with verdict and…]] - rationale - gateway/proxy/url_analyzer.py
- [[Check for base64-encoded data in URL path and query values.]] - rationale - gateway/proxy/url_analyzer.py
- [[Check if an IP address is privatereservedloopback.]] - rationale - gateway/proxy/url_analyzer.py
- [[Check if hostname is a privatereserved address (SSRF attempt).]] - rationale - gateway/proxy/url_analyzer.py
- [[Data exfiltration patterns in URLs — flagged, not blocked.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Edge cases and malformed URLs.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Ensure normal browsing URLs pass through.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Enum_8]] - code
- [[Heuristic does this string look like base64-encoded data]] - rationale - gateway/proxy/url_analyzer.py
- [[PII detection in URLs — flagged, not blocked.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Resolve hostname to IP. Returns None on failure. NOTE DNS rebinding attacks…]] - rationale - gateway/proxy/url_analyzer.py
- [[Result of analyzing a URL.]] - rationale - gateway/proxy/url_analyzer.py
- [[Short base64 strings are normal (e.g., API tokens in URLs).]] - rationale - gateway/tests/test_url_analyzer.py
- [[Test the _looks_like_base64 helper.]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestBase64Heuristic]] - code - gateway/tests/test_url_analyzer.py
- [[TestDataExfiltration]] - code - gateway/tests/test_url_analyzer.py
- [[TestLegitimateURLsAllowed]] - code - gateway/tests/test_url_analyzer.py
- [[TestMalformedURLs]] - code - gateway/tests/test_url_analyzer.py
- [[TestPIIInURLs]] - code - gateway/tests/test_url_analyzer.py
- [[Tests for URL Analyzer — SSRF detection, PII in URLs, data exfiltration.]] - rationale - gateway/tests/test_url_analyzer.py
- [[URL Analyzer — detect SSRF, data exfiltration, and suspicious URL patterns.…]] - rationale - gateway/proxy/url_analyzer.py
- [[URLAnalysisResult]] - code - gateway/proxy/url_analyzer.py
- [[URLFinding]] - code - gateway/proxy/url_analyzer.py
- [[URLVerdict]] - code - gateway/proxy/url_analyzer.py
- [[_looks_like_base64()]] - code - gateway/proxy/url_analyzer.py
- [[analyzer()]] - code - gateway/tests/test_url_analyzer.py
- [[fixture_19]] - code
- [[str_5]] - code
- [[test_url_analyzer.py]] - code - gateway/tests/test_url_analyzer.py
- [[url_analyzer.py_2]] - code - gateway/proxy/url_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_url_analyzerpy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TestSSRFDetection]]

## Top bridge nodes
- [[test_url_analyzer.py]] - degree 12, connects to 2 communities
- [[url_analyzer.py_2]] - degree 9, connects to 1 community
- [[URLVerdict]] - degree 8, connects to 1 community
- [[dot-analyze()]] - degree 8, connects to 1 community
- [[dot-_check_base64()]] - degree 6, connects to 1 community
