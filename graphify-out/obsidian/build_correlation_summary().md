---
source_file: "gateway/security/soc_correlation.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L48"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# build_correlation_summary()

## Connections
- [[CorrelationSummary]] - `references` [EXTRACTED]
- [[Counter]] - `calls` [INFERRED]
- [[_build_egress_live_snapshot()]] - `calls` [EXTRACTED]
- [[dashboard.py]] - `imports` [EXTRACTED]
- [[get_risk_score()]] - `calls` [EXTRACTED]
- [[get_risk_summary()]] - `calls` [EXTRACTED]
- [[get_soc_correlation()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[router.py_1]] - `imports` [EXTRACTED]
- [[soc_correlation()]] - `calls` [EXTRACTED]
- [[soc_correlation.py]] - `contains` [EXTRACTED]
- [[soc_report()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline