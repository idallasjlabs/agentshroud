---
source_file: "scripts/auto_remediate_cves.py"
type: "code"
community: "test_daily_cve_report.py"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# auto_remediate_cves.py

## Connections
- [[RemediationPlan dataclass]] - `contains` [EXTRACTED]
- [[Sunday Upgrade prompt (weekly maintenance run)]] - `references` [EXTRACTED]
- [[_print_plan()]] - `contains` [EXTRACTED]
- [[_run()_3]] - `contains` [EXTRACTED]
- [[apply_remediation()]] - `contains` [EXTRACTED]
- [[check-vendor-compat.sh]] - `semantically_similar_to` [INFERRED]
- [[discover_upstream_versions.py]] - `semantically_similar_to` [INFERRED]
- [[load_registry()]] - `contains` [EXTRACTED]
- [[main()_12]] - `contains` [EXTRACTED]
- [[parse_version()_1]] - `contains` [EXTRACTED]
- [[plan_remediation()]] - `contains` [EXTRACTED]
- [[read_pin()]] - `contains` [EXTRACTED]
- [[sunday-upgrade-apply.sh]] - `conceptually_related_to` [EXTRACTED]
- [[versions.env]] - `references` [EXTRACTED]
- [[write_pin()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_daily_cve_reportpy
