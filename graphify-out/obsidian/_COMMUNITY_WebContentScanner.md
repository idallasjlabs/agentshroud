---
type: community
members: 32
---

# WebContentScanner

**Members:** 32 nodes

## Members
- [[dot-__init__()_150]] - code - gateway/proxy/web_content_scanner.py
- [[dot-setUp()_1]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_billion_laughs_detected()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_case_insensitive()_1]] - code - gateway/tests/test_xml_dtd_control.py
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
- [[An attacker controls the Content-Type header, so sniff the body.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[Entity declarations carry both XXE and billion-laughs.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[Enum_34]] - code
- [[FindingSeverity]] - code - gateway/proxy/web_content_scanner.py
- [[Gateway XML DTDentity control — CLAUDE.md 0.05 arm 2. CVE-2026-6653 is a use-…]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[HTML5's bare !DOCTYPE html has no internal subset and is harmless.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[No internal subset, but still pulls a remote DTD.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[Proves enforcement, not just detection.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[Scan web content for prompt injection, PII, and hidden payloads. All findings…]] - rationale - gateway/proxy/web_content_scanner.py
- [[TestDangerousXMLDetection]] - code - gateway/tests/test_xml_dtd_control.py
- [[TestDangerousXMLIsBlockedNotFlagged]] - code - gateway/tests/test_xml_dtd_control.py
- [[The '' block inside DOCTYPE is what xmlParseInternalSubset parses.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[The distinction this whole control rests on.]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[WebContentScanner]] - code - gateway/proxy/web_content_scanner.py
- [[str_18]] - code
- [[test_xml_dtd_control.py]] - code - gateway/tests/test_xml_dtd_control.py
- [[web_content_scanner.py_2]] - code - gateway/proxy/web_content_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/WebContentScanner
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_ScanResult]]
- 3 edges to [[_COMMUNITY_WebProxy]]
- 1 edge to [[_COMMUNITY_TestTriageClassLevelCoverage]]
- 1 edge to [[_COMMUNITY_TestDefenseLayerVocabulary]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY__t]]

## Top bridge nodes
- [[WebContentScanner]] - degree 20, connects to 5 communities
- [[web_content_scanner.py_2]] - degree 7, connects to 2 communities
- [[test_xml_dtd_control.py]] - degree 7, connects to 1 community
