---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "check_upstream_cves()"
location: "L270"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/check_upstream_cves
---

# Stub urllib.request.urlopen to return a list of advisories.

## Connections
- [[._patch_urllib()]] - `rationale_for` [EXTRACTED]
- [[._patch_urllib()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/check_upstream_cves