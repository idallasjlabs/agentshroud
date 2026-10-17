---
type: community
members: 10
---

# DifferentialPIIDetector (2)

**Members:** 10 nodes

## Members
- [[dot-_scan()]] - code - gateway/security/differential_pii_detector.py
- [[dot-scan_prompt()]] - code - gateway/security/differential_pii_detector.py
- [[dot-scan_tool_result()_3]] - code - gateway/security/differential_pii_detector.py
- [[Core scan normalize adversarial patterns, then run PII recognition.]] - rationale - gateway/security/differential_pii_detector.py
- [[Full scan result for a tool result or prompt.]] - rationale - gateway/security/differential_pii_detector.py
- [[Scan a prompt with the standard (higher) confidence floor.          Args]] - rationale - gateway/security/differential_pii_detector.py
- [[Scan a tool result with the lower confidence floor.          Args             t]] - rationale - gateway/security/differential_pii_detector.py
- [[Strip common adversarial encoding tricks, return (normalized, count_removed).]] - rationale - gateway/security/differential_pii_detector.py
- [[ToolResultPIIReport]] - code - gateway/security/differential_pii_detector.py
- [[_normalize_adversarial()]] - code - gateway/security/differential_pii_detector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DifferentialPIIDetector_2
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_DifferentialPIIDetector]]

## Top bridge nodes
- [[dot-_scan()]] - degree 8, connects to 1 community
- [[ToolResultPIIReport]] - degree 5, connects to 1 community
- [[dot-scan_prompt()]] - degree 4, connects to 1 community
- [[dot-scan_tool_result()_3]] - degree 4, connects to 1 community
- [[_normalize_adversarial()]] - degree 3, connects to 1 community
