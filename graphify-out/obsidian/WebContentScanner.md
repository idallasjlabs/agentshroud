---
source_file: "gateway/proxy/web_content_scanner.py"
type: "code"
community: "WebContentScanner"
location: "L196"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/WebContentScanner
---

# WebContentScanner

## Connections
- [[dot-__init__()_159]] - `references` [EXTRACTED]
- [[dot-__init__()_138]] - `method` [EXTRACTED]
- [[dot-_scan_encoded_payloads()]] - `method` [EXTRACTED]
- [[dot-_scan_hidden_content()]] - `method` [EXTRACTED]
- [[dot-_scan_pii()]] - `method` [EXTRACTED]
- [[dot-_scan_prompt_injection()]] - `method` [EXTRACTED]
- [[dot-_scan_xml_dtd()]] - `method` [EXTRACTED]
- [[dot-_scan_zero_width()]] - `method` [EXTRACTED]
- [[dot-scan()_4]] - `method` [EXTRACTED]
- [[dot-setUp()_1]] - `calls` [EXTRACTED]
- [[dot-test_finding_severity_is_critical()]] - `calls` [EXTRACTED]
- [[Scan web content for prompt injection, PII, and hidden payloads. All findings…]] - `rationale_for` [EXTRACTED]
- [[TestDangerousXMLDetection]] - `uses` [INFERRED]
- [[TestDangerousXMLIsBlockedNotFlagged]] - `uses` [INFERRED]
- [[TestDefenseLayerVocabulary]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[test_triage_cve_mitigations.py]] - `imports` [EXTRACTED]
- [[test_xml_dtd_control.py]] - `imports` [EXTRACTED]
- [[web_content_scanner.py_2]] - `contains` [EXTRACTED]
- [[web_proxy.py_2]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/WebContentScanner
