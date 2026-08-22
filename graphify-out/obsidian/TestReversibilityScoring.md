---
source_file: "gateway/tests/test_tool_chain_analyzer.py"
type: "code"
community: "Tool Chain & CVE Triage"
location: "L525"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Tool_Chain__CVE_Triage
---

# TestReversibilityScoring

## Connections
- [[.analyzer()_1]] - `method` [EXTRACTED]
- [[.test_delete_file_mostly_irreversible()]] - `method` [EXTRACTED]
- [[.test_read_file_fully_reversible()]] - `method` [EXTRACTED]
- [[.test_reversibility_below_threshold_has_reasoning()]] - `method` [EXTRACTED]
- [[.test_unknown_tool_defaults_low()]] - `method` [EXTRACTED]
- [[ChainAction]] - `uses` [INFERRED]
- [[ChainMatch]] - `uses` [INFERRED]
- [[ParamScanResult]] - `uses` [INFERRED]
- [[ReversibilityScore]] - `uses` [INFERRED]
- [[RiskLevel_4]] - `uses` [INFERRED]
- [[ToolChainAnalyzer]] - `uses` [INFERRED]
- [[test_tool_chain_analyzer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Tool_Chain__CVE_Triage