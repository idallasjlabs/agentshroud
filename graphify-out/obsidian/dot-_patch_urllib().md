---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "Community 124"
location: "L269"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_124
---

# ._patch_urllib()

## Connections
- [[dot-test_returns_empty_when_all_known()]] - `calls` [EXTRACTED]
- [[dot-test_returns_new_advisory_not_in_registry()]] - `calls` [EXTRACTED]
- [[dot-test_skips_advisory_whose_cve_is_already_tracked()]] - `calls` [EXTRACTED]
- [[dot-test_skips_advisory_without_ghsa_id()]] - `calls` [EXTRACTED]
- [[dot-test_skips_ghsa_already_in_registry()]] - `calls` [EXTRACTED]
- [[Stub urllib.request.urlopen to return a list of advisories.]] - `rationale_for` [EXTRACTED]
- [[TestCheckUpstreamCves]] - `method` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_124