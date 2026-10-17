---
source_file: "scripts/auto_remediate_cves.py"
type: "code"
community: "plan_remediation"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/plan_remediation
---

# auto_remediate_cves.py

## Connections
- [[RemediationPlan dataclass]] - `contains` [EXTRACTED]
- [[_print_plan()]] - `contains` [EXTRACTED]
- [[_run()_2]] - `contains` [EXTRACTED]
- [[apply_remediation()]] - `contains` [EXTRACTED]
- [[check-vendor-compat.sh]] - `semantically_similar_to` [INFERRED]
- [[discover_upstream_versions.py]] - `semantically_similar_to` [INFERRED]
- [[load_registry()_1]] - `contains` [EXTRACTED]
- [[main()_27]] - `contains` [EXTRACTED]
- [[parse_version()_1]] - `contains` [EXTRACTED]
- [[plan_remediation()]] - `contains` [EXTRACTED]
- [[promptssunday-upgrade.md (Sunday mission procedure)]] - `references` [EXTRACTED]
- [[read_pin()]] - `contains` [EXTRACTED]
- [[sunday-upgrade-apply.sh]] - `conceptually_related_to` [EXTRACTED]
- [[versions.env]] - `references` [EXTRACTED]
- [[write_pin()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/plan_remediation
