---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "CI test job (matrix ubuntu/macos x py3.11/3.13)"
location: "L4538"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/CI_test_job_matrix_ubuntu/macos_x_py311/313
---

# First sendMessage returns 400 'can't parse entities'; retry with plain text succ

## Connections
- [[.test_400_retry_succeeds_when_text_strippable()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/CI_test_job_matrix_ubuntu/macos_x_py311/313