---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "_build_image_targets"
location: "175"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_build_image_targets
---

# _build_image_targets

## Connections
- [[.test_always_includes_every_configured_bot_image()]] - `calls` [EXTRACTED]
- [[.test_always_includes_gateway_image()]] - `calls` [EXTRACTED]
- [[.test_deduplication()]] - `calls` [EXTRACTED]
- [[.test_env_var_adds_extra_targets()]] - `calls` [EXTRACTED]
- [[.test_env_var_empty_string_ignored()]] - `calls` [EXTRACTED]
- [[.test_whitespace_stripped_from_env_var()]] - `calls` [EXTRACTED]
- [[Build the list of container image targets for Trivy image scanning.      Prefers]] - `rationale_for` [EXTRACTED]
- [[_running_image]] - `calls` [EXTRACTED]
- [[gateway.security.daily_cve_report]] - `contains` [EXTRACTED]
- [[run_and_send_cve_report]] - `calls` [EXTRACTED]
- [[test_daily_cve_report.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_build_image_targets