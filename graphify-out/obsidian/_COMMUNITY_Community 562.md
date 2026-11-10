---
type: community
members: 55
---

# Community 562

**Members:** 55 nodes

## Members
- [[.__init__()_42]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_encoded_payloads()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_hidden_content()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_pii()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_prompt_injection()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_xml_dtd()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_zero_width()]] - code - gateway/proxy/web_content_scanner.py
- [[._triage()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.finding_summary()]] - code - gateway/proxy/web_content_scanner.py
- [[.flagged()_1]] - code - gateway/proxy/web_content_scanner.py
- [[.scan()_1]] - code - gateway/proxy/web_content_scanner.py
- [[.setUp()_1]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_billion_laughs_detected()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_case_insensitive()_3]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_detected_in_svg()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_detected_when_mislabelled_as_text()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_doctype_internal_subset_detected()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_entity_declaration_detected()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_external_dtd_reference_detected()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_finding_severity_is_critical()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_json_not_flagged()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_libxml2_dtd_uaf_classifies_as_xxe_not_dos()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_plain_html_not_flagged()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_plain_xml_not_flagged()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_unrelated_classes_unchanged()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_web_proxy_blocks_on_dangerous_xml()]] - code - gateway/tests/test_xml_dtd_control.py
- [[.test_xxe_class_is_covered_by_the_gateway_control()]] - code - gateway/tests/test_xml_dtd_control.py
- [[A document with no DTD is untouched — this must not break feeds.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[A single finding from content scanning.]] - rationale - gateway/proxy/web_content_scanner.py
- [[An attacker controls the Content-Type header, so sniff the body.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[ContentFinding]] - code - gateway/proxy/web_content_scanner.py
- [[Detect DTDentity constructs that drive XML parser memory-safety bugs.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Detect zero-width character sequences (steganographic attacks).]] - rationale - gateway/proxy/web_content_scanner.py
- [[Entity declarations carry both XXE and billion-laughs.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[HTML5's bare !DOCTYPE html has no internal subset and is harmless.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[It calls itself DoS; the generic DOS profile is containment-only.          Left]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[No internal subset, but still pulls a remote DTD.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[Proves enforcement, not just detection.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[Result of scanning web content.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan HTML for hidden instructions in comments, invisible elements, meta tags.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan content for security issues.          Args             content The web co]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for base64-encoded or otherwise obfuscated payloads.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for prompt injection patterns.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan response content for PII.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan web content for prompt injection, PII, and hidden payloads.      All findin]] - rationale - gateway/proxy/web_content_scanner.py
- [[ScanResult]] - code - gateway/proxy/web_content_scanner.py
- [[TestDangerousXMLDetection]] - code - gateway/tests/test_xml_dtd_control.py
- [[TestDangerousXMLIsBlockedNotFlagged]] - code - gateway/tests/test_xml_dtd_control.py
- [[TestTriageClassLevelCoverage]] - code - gateway/tests/test_xml_dtd_control.py
- [[The '' block inside DOCTYPE is what xmlParseInternalSubset parses.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[The distinction this whole control rests on.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[The durable statement is at the CLASS level, not per-CVE.      A register entry]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[The new rule runs first, so prove it does not swallow neighbours.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[WebContentScanner]] - code - gateway/proxy/web_content_scanner.py
- [[test_xml_dtd_control.py]] - code - gateway/tests/test_xml_dtd_control.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_562
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 69]]
- 7 edges to [[_COMMUNITY_Community 8]]
- 4 edges to [[_COMMUNITY_Community 120]]
- 3 edges to [[_COMMUNITY_Community 1000]]
- 1 edge to [[_COMMUNITY_Community 72]]
- 1 edge to [[_COMMUNITY_Community 27]]

## Top bridge nodes
- [[WebContentScanner]] - degree 34, connects to 6 communities
- [[TestDangerousXMLDetection]] - degree 14, connects to 1 community
- [[ScanResult]] - degree 11, connects to 1 community
- [[ContentFinding]] - degree 8, connects to 1 community
- [[TestTriageClassLevelCoverage]] - degree 8, connects to 1 community