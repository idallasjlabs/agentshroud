---
type: community
members: 15
---

# differential_pii_detector.py

**Members:** 15 nodes

## Members
- [[dot-_redact()]] - code - gateway/security/differential_pii_detector.py
- [[dot-_scan()]] - code - gateway/security/differential_pii_detector.py
- [[dot-scan_prompt()]] - code - gateway/security/differential_pii_detector.py
- [[dot-scan_tool_result()_1]] - code - gateway/security/differential_pii_detector.py
- [[Core scan normalize adversarial patterns, then run PII recognition.]] - rationale - gateway/security/differential_pii_detector.py
- [[Differential PII Detector for Tool Results — Module 28 (v1.2.0) IEC 62443 FR3…]] - rationale - gateway/security/differential_pii_detector.py
- [[Full scan result for a tool result or prompt.]] - rationale - gateway/security/differential_pii_detector.py
- [[Replace detected PII tokens with ENTITY_TYPE placeholders.]] - rationale - gateway/security/differential_pii_detector.py
- [[Scan a prompt with the standard (higher) confidence floor. Args content…]] - rationale - gateway/security/differential_pii_detector.py
- [[Scan a tool result with the lower confidence floor. Args tool_name Name of…]] - rationale - gateway/security/differential_pii_detector.py
- [[Strip common adversarial encoding tricks, return (normalized, count_removed).]] - rationale - gateway/security/differential_pii_detector.py
- [[ToolResultPIIReport]] - code - gateway/security/differential_pii_detector.py
- [[_collapse_spaced()]] - code - gateway/security/differential_pii_detector.py
- [[_normalize_adversarial()]] - code - gateway/security/differential_pii_detector.py
- [[differential_pii_detector.py]] - code - gateway/security/differential_pii_detector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/differential_pii_detectorpy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_DifferentialPIIDetector]]
- 4 edges to [[_COMMUNITY_PIIHit]]
- 2 edges to [[_COMMUNITY_test_differential_pii_detector.py]]

## Top bridge nodes
- [[differential_pii_detector.py]] - degree 8, connects to 3 communities
- [[dot-_scan()]] - degree 8, connects to 2 communities
- [[dot-_redact()]] - degree 4, connects to 2 communities
- [[dot-scan_prompt()]] - degree 4, connects to 1 community
- [[dot-scan_tool_result()_1]] - degree 4, connects to 1 community
