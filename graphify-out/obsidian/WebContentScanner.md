---
source_file: "gateway/proxy/web_content_scanner.py"
type: "code"
community: "Community 562"
location: "L203"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_562
---

# WebContentScanner

## Connections
- [[.__init__()_42]] - `method` [EXTRACTED]
- [[._scan_encoded_payloads()]] - `method` [EXTRACTED]
- [[._scan_hidden_content()]] - `method` [EXTRACTED]
- [[._scan_pii()]] - `method` [EXTRACTED]
- [[._scan_prompt_injection()]] - `method` [EXTRACTED]
- [[._scan_xml_dtd()]] - `method` [EXTRACTED]
- [[._scan_zero_width()]] - `method` [EXTRACTED]
- [[.scan()_1]] - `method` [EXTRACTED]
- [[.setUp()_1]] - `calls` [EXTRACTED]
- [[.test_finding_severity_is_critical()]] - `calls` [EXTRACTED]
- [[Any_23]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[Scan web content for prompt injection, PII, and hidden payloads.      All findin]] - `rationale_for` [EXTRACTED]
- [[TestClassify_2]] - `uses` [INFERRED]
- [[TestConsumeFieldEdge]] - `uses` [INFERRED]
- [[TestDangerousXMLDetection]] - `uses` [INFERRED]
- [[TestDangerousXMLIsBlockedNotFlagged]] - `uses` [INFERRED]
- [[TestDefenseLayerVocabulary]] - `uses` [INFERRED]
- [[TestDriverIsolation]] - `uses` [INFERRED]
- [[TestMain_1]] - `uses` [INFERRED]
- [[TestRewrite]] - `uses` [INFERRED]
- [[TestTriageClassLevelCoverage]] - `uses` [INFERRED]
- [[TestTriageEntry]] - `uses` [INFERRED]
- [[TestVersion]] - `uses` [INFERRED]
- [[URLAnalyzer_1]] - `uses` [INFERRED]
- [[WebContentScanner_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig_1]] - `uses` [INFERRED]
- [[WebProxyResult]] - `uses` [INFERRED]
- [[test_triage_cve_mitigations.py]] - `imports` [EXTRACTED]
- [[test_xml_dtd_control.py]] - `imports` [EXTRACTED]
- [[web_content_scanner.py]] - `contains` [EXTRACTED]
- [[web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_562