---
type: community
members: 55
---

# WebContentScanner

**Members:** 55 nodes

## Members
- [[dot-__init__()]] - code - gateway/proxy/web_content_scanner.py
- [[dot-__init__()_1]] - code - gateway/proxy/web_proxy.py
- [[dot-_scan_encoded_payloads()]] - code - gateway/proxy/web_content_scanner.py
- [[dot-_scan_hidden_content()]] - code - gateway/proxy/web_content_scanner.py
- [[dot-_scan_pii()]] - code - gateway/proxy/web_content_scanner.py
- [[dot-_scan_prompt_injection()]] - code - gateway/proxy/web_content_scanner.py
- [[dot-_scan_xml_dtd()]] - code - gateway/proxy/web_content_scanner.py
- [[dot-_scan_zero_width()]] - code - gateway/proxy/web_content_scanner.py
- [[dot-finding_summary()]] - code - gateway/proxy/web_content_scanner.py
- [[dot-flagged()]] - code - gateway/proxy/web_content_scanner.py
- [[dot-scan()]] - code - gateway/proxy/web_content_scanner.py
- [[dot-setUp()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_billion_laughs_detected()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_case_insensitive()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_detected_in_svg()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_detected_when_mislabelled_as_text()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_doctype_internal_subset_detected()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_entity_declaration_detected()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_external_dtd_reference_detected()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_finding_severity_is_critical()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_json_not_flagged()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_plain_html_not_flagged()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_plain_xml_not_flagged()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_web_proxy_blocks_on_dangerous_xml()]] - code - gateway/tests/test_xml_dtd_control.py
- [[A document with no DTD is untouched — this must not break feeds.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[A single finding from content scanning.]] - rationale - gateway/proxy/web_content_scanner.py
- [[An attacker controls the Content-Type header, so sniff the body.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[ContentFinding]] - code - gateway/proxy/web_content_scanner.py
- [[Detect DTDentity constructs that drive XML parser memory-safety bugs. Flags…]] - rationale - gateway/proxy/web_content_scanner.py
- [[Detect zero-width character sequences (steganographic attacks).]] - rationale - gateway/proxy/web_content_scanner.py
- [[Entity declarations carry both XXE and billion-laughs.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[Enum]] - code
- [[FindingSeverity]] - code - gateway/proxy/web_content_scanner.py
- [[Gateway XML DTDentity control — CLAUDE.md 0.05 arm 2. CVE-2026-6653 is a use-…]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[HTML5's bare !DOCTYPE html has no internal subset and is harmless.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[No internal subset, but still pulls a remote DTD.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[Proves enforcement, not just detection.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[Result of scanning web content.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan HTML for hidden instructions in comments, invisible elements, meta tags.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan content for security issues. Args content The web content to scan.…]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for base64-encoded or otherwise obfuscated payloads.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for prompt injection patterns.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan response content for PII.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan web content for prompt injection, PII, and hidden payloads. All findings…]] - rationale - gateway/proxy/web_content_scanner.py
- [[ScanResult]] - code - gateway/proxy/web_content_scanner.py
- [[TestDangerousXMLDetection]] - code - gateway/tests/test_xml_dtd_control.py
- [[TestDangerousXMLIsBlockedNotFlagged]] - code - gateway/tests/test_xml_dtd_control.py
- [[The '' block inside DOCTYPE is what xmlParseInternalSubset parses.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[The distinction this whole control rests on.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[URLAnalyzer]] - code
- [[WebContentScanner]] - code - gateway/proxy/web_content_scanner.py
- [[WebProxyConfig]] - code
- [[str]] - code
- [[test_xml_dtd_control.py]] - code - gateway/tests/test_xml_dtd_control.py
- [[web_content_scanner.py]] - code - gateway/proxy/web_content_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/WebContentScanner
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TestSSRFDetection]]
- 2 edges to [[_COMMUNITY_ProxyAction]]
- 2 edges to [[_COMMUNITY__t]]
- 2 edges to [[_COMMUNITY_WebProxy]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_WebContentScanner (2)]]
- 1 edge to [[_COMMUNITY_WebProxyConfig]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py]]

## Top bridge nodes
- [[WebContentScanner]] - degree 22, connects to 5 communities
- [[web_content_scanner.py]] - degree 10, connects to 3 communities
- [[dot-__init__()_1]] - degree 5, connects to 2 communities
- [[test_xml_dtd_control.py]] - degree 7, connects to 1 community
